import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 0, f"Invoice nr.{invoice_nr}", ln=1)
    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 14, f"Date: {date}", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
