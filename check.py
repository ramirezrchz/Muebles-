#!/usr/bin/env python3
"""Revisa index.html: sintaxis del script, ids repetidos y un solo three.js."""
import re, subprocess, sys, tempfile, os

s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), encoding="utf8").read()
ok = True

ids = re.findall(r'id="([^"]+)"', s)
dup = sorted({i for i in ids if ids.count(i) > 1})
if dup:
    ok = False
    print("Ids repetidos:", dup)

n3 = len(re.findall(r'<script[^>]+src="[^"]*three[^"]*"', s))
if n3 != 1:
    ok = False
    print("Debe haber exactamente una carga de three.js; hay", n3)

m = re.search(r"<script>(.*)</script>", s, re.S)
if not m:
    ok = False
    print("No se encontró el script principal")
else:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf8") as f:
        f.write(m.group(1))
    try:
        r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
        if r.returncode:
            ok = False
            print("Error de sintaxis:\n" + r.stderr)
    except FileNotFoundError:
        print("Node.js no está instalado; se omitió la revisión de sintaxis.")
    os.unlink(f.name)

print("Todo bien" if ok else "Hay problemas por corregir")
sys.exit(0 if ok else 1)
