import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font("Times", "B", 16)
    pdf.cell(50, 8, f"Invoice nr.{invoice_nr}", ln=1)
    pdf.cell(50, 8, f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Add a header
    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font("Times", "B", size=9)
    pdf.set_text_color(0, 0, 250)
    pdf.cell(30, 8, txt=columns[0].strip("_"), border=1)
    pdf.cell(60, 8, txt=columns[1], border=1)
    pdf.cell(30, 8, txt=columns[2], border=1)
    pdf.cell(30, 8, txt=columns[3], border=1, )
    pdf.cell(30, 8, txt=columns[4], border=1, ln=1)

    # Add rows to the table
    total_price = 0
    for index, row in df.iterrows():
        pdf.set_font("Times", size=8)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(30, 8, txt=str(row["product_id"]), border=1)
        pdf.cell(60, 8, txt=str(row["product_name"]), border=1)
        pdf.cell(30, 8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(30, 8, txt=str(row["price_per_unit"]), border=1,)
        pdf.cell(30, 8, txt=str(row["total_price"]), border=1, ln=1)

    # Calculate total price
    total_price = df["total_price"].sum()
    pdf.cell(30, 8, txt="", border=1)
    pdf.cell(60, 8, txt="", border=1)
    pdf.cell(30, 8, txt="", border=1)
    pdf.cell(30, 8, txt="", border=1, )
    pdf.cell(30, 8, txt=str(total_price), border=1, ln=1)

    # Add total price text
    pdf.set_font("Times", size=12, style="B")
    pdf.cell(30, 10, txt=f"Total price is {total_price}", border=0, ln=1)
    pdf.cell(30, 8, txt="Python How", border=0, ln=0)
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")
