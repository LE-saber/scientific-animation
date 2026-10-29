#!/usr/bin/env python3
"""Build two independent, verified ChatGPT Skill ZIPs (no third-party dependencies)."""
from pathlib import Path
import hashlib,zipfile
ROOT=Path(__file__).resolve().parent.parent
def pack(name,output):
    src=ROOT/"skills"/name
    assert (src/"SKILL.md").is_file()
    assert (src/"agents"/"openai.yaml").is_file()
    output.mkdir(parents=True,exist_ok=True)
    target=output/"skill.zip"
    files=[p for p in sorted(src.rglob("*")) if p.is_file() and not any(x.startswith(".") for x in p.relative_to(src).parts)]
    with zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED) as z:
        for p in files:z.write(p,p.relative_to(src.parent))
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        assert sum(x.endswith("/SKILL.md") for x in z.namelist())==1
    assert target.stat().st_size<=25*1024*1024
    print(f"{name}: {len(files)} files; {target}; sha256={hashlib.sha256(target.read_bytes()).hexdigest()}")
for mode,path in [("scientific-animation-autopilot","autopilot"),("scientific-animation-dialogue","dialogue")]:
    pack(mode,ROOT/"dist"/path)
