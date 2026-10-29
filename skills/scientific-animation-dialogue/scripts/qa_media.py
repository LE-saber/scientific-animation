#!/usr/bin/env python3
"""Verify a finished video with ffprobe/ffmpeg and SHA-256. Standard library only."""
import argparse, hashlib, json, pathlib, shutil, subprocess, sys
def run(args):
    return subprocess.run(args, capture_output=True, text=True)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("video", type=pathlib.Path)
    p.add_argument("--out", type=pathlib.Path)
    p.add_argument("--duration", type=float)
    p.add_argument("--fps", type=float)
    p.add_argument("--width", type=int)
    p.add_argument("--height", type=int)
    p.add_argument("--require-audio", action="store_true")
    p.add_argument("--quick", action="store_true",help="Draft-only inspection, not final validation")
    a=p.parse_args()
    errors=[]; report={"status":"FAIL","video":str(a.video)}
    if not a.video.is_file() or a.video.stat().st_size==0:errors.append("Missing or empty video")
    if not shutil.which("ffprobe") or not shutil.which("ffmpeg"):errors.append("FFmpeg and ffprobe required")
    if not errors:
        cmd=run(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(a.video)])
        if cmd.returncode:errors.append(cmd.stderr)
        else:
            info=json.loads(cmd.stdout)
            vs=[x for x in info["streams"] if x["codec_type"]=="video"]
            au=[x for x in info["streams"] if x["codec_type"]=="audio"]
            if not vs: errors.append("Missing video stream")
            if a.require_audio and not au: errors.append("Missing audio")
            if vs:
                v=vs[0]
                n,d=map(int,v.get("avg_frame_rate","0/1").split("/"))
                fps=n/d if d else 0
                duration=float(info["format"].get("duration",0))
                if a.width and int(v["width"])!=a.width: errors.append("Wrong width")
                if a.height and int(v["height"])!=a.height: errors.append("Wrong height")
                if a.fps and abs(fps-a.fps)>.05: errors.append("Wrong FPS")
                if a.duration and abs(duration-a.duration)>.5: errors.append("Wrong duration")
                if int(info["format"]["size"])!=a.video.stat().st_size:errors.append("File size mismatch")
                h=hashlib.sha256()
                with a.video.open("rb") as f:
                    for data in iter(lambda:f.read(1048576),b""):h.update(data)
                report.update({"duration":duration,"width":v["width"],"height":v["height"],"fps":fps,"sha256":h.hexdigest(),"bytes":a.video.stat().st_size})
        if not errors and not a.quick:
            dec=run(["ffmpeg","-v","error","-xerror","-i",str(a.video),"-f","null","-"])
            if dec.returncode:errors.append("Full decode failed: "+dec.stderr[-500:])
            report["full_decode"]="PASS" if dec.returncode==0 else "FAIL"
        elif a.quick:report["full_decode"]="SKIPPED"
    report["errors"]=errors
    report["status"]="FAIL" if errors else ("DRAFT_ONLY" if a.quick else "PASS")
    out=a.out or a.video.parent/"qa"
    out.mkdir(parents=True,exist_ok=True)
    (out/"qa_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False))
    return 2 if errors else 0
if __name__=="__main__":sys.exit(main())
