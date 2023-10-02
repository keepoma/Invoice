import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text_files/*.txt")
pdf = FPDF()

for filepath in filepaths:
    filename = Path(filepath).stem
    filename = filename.capitalize()
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, filename)
pdf.output("Animals.pdf")
