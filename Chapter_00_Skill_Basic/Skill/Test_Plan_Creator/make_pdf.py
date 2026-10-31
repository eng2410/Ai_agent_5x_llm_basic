# owner: Pranali Pawar
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

src = Path(r"D:\AI_Agent_Class\Chapter_00_Skill_Basic\Skill\Test_Plan_Creator\Netting_Hub_Test_Plan.md")
out = src.with_suffix(".pdf")

text = src.read_text(encoding="utf-8")
lines = text.splitlines()

c = canvas.Canvas(str(out), pagesize=A4)
width, height = A4
margin = 50
x = margin
y = height - margin

c.setTitle("Netting Hub Test Plan")
c.setAuthor("AI Agent")


def new_page():
    global y
    c.showPage()
    y = height - margin

for line in lines:
    s = line.strip()
    if not s:
        y -= 12
        continue
    if y < 50:
        new_page()

    if s.startswith("# "):
        c.setFont("Helvetica-Bold", 18)
        c.drawString(x, y, s[2:])
        y -= 28
    elif s.startswith("## "):
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y, s[3:])
        y -= 22
    elif s.startswith("### "):
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, s[4:])
        y -= 18
    elif s.startswith("- "):
        c.setFont("Helvetica", 10)
        part = s[2:]
        words = part.split()
        current = ""
        for w in words:
            if len(current) + len(w) + 1 <= 100:
                current = current + (" " if current else "") + w
            else:
                c.drawString(x + 12, y, current)
                y -= 14
                if y < 50:
                    new_page()
                current = w
        if current:
            c.drawString(x + 12, y, current)
            y -= 14
    elif s.startswith("|"):
        c.setFont("Helvetica", 9)
        c.drawString(x, y, s)
        y -= 12
    else:
        c.setFont("Helvetica", 10)
        words = s.split()
        current = ""
        for w in words:
            if len(current) + len(w) + 1 <= 100:
                current = current + (" " if current else "") + w
            else:
                c.drawString(x, y, current)
                y -= 14
                if y < 50:
                    new_page()
                current = w
        if current:
            c.drawString(x, y, current)
            y -= 14

c.save()
print(f"Created PDF: {out}")
