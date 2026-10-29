#!/usr/bin/env python3
"""Package editable animation sources with SHA-256 manifest; exclude secrets/fonts."""
import argparse,hashlib,json,pathlib,zipfile,sys,os
EXCLUDE={".git","node_modules","__pycache__",".venv","venv","tmp"}
SUFFIXES={".ttf",".ttc",".otf",".woff",".woff2",".pem",".key",".p12"}
def sha(data):return hashlib.sha256(data).hexdigest()
def main():
    a=argparse.ArgumentParser()
    a.add_argument("folder",type=pathlib.Path)
    a.add_argument("--out",type=pathlib.Path,required=True)
    x=a.parse_args();root=x.folder.resolve();target=x.out.resolve()
    if not root.is_dir():a.error("Invalid project source folder")
    target.parent.mkdir(parents=True,exist_ok=True)
    files=[];manifest=[]
    for f in sorted(root.rglob("*")):
        if not f.is_file() or f.is_symlink() or f.resolve()==target:continue
        parts=f.relative_to(root).parts
        if any(y in EXCLUDE or y.startswith(".") for y in parts[:-1]):continue
        if f.name.startswith((".env","secrets.","credentials.")) or f.suffix.lower() in SUFFIXES:continue
        files.append(f)
    if not files:a.error("No source files")
    temp=target.with_suffix(".tmp.zip")
    try:
        with zipfile.ZipFile(temp,"w",zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for f in files:
                b=f.read_bytes();p=f.relative_to(root).as_posix()
                manifest.append({"path":p,"bytes":len(b),"sha256":sha(b)})
                z.writestr(p,b)
            z.writestr("manifest_sha256.json",json.dumps({"files":manifest},indent=2))
        with zipfile.ZipFile(temp) as z:
            assert z.testzip() is None
            for f in manifest:
                b=z.read(f["path"]);assert len(b)==f["bytes"] and sha(b)==f["sha256"]
        os.replace(temp,target)
    finally:
        if temp.exists():temp.unlink()
    print(json.dumps({"status":"PASS","file":str(target),"files":len(files),"sha256":sha(target.read_bytes())}))
if __name__=="__main__":sys.exit(main())
