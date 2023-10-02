import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text_files/*.txt")
pdf = FPDF()

for filepath in filepaths:
    filename = Path(filepath).stem
    filename = filename.capitalize()
    pdf.add_page()

    # Add title
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(102, 178, 255)
    pdf.cell(0, 12, filename, ln=1)

    # Add paragraph
    with open(filepath, "r") as file:
        text = file.read()
    pdf.set_font("Times", "", 10)
    pdf.set_text_color(153, 204, 255)
    pdf.multi_cell(0, 6, text)

pdf.output("Animals.pdf")
