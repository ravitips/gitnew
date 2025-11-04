from fpdf import FPDF

    # Create an instance of the FPDF class
pdf = FPDF()

    # Add a page
pdf.add_page()

    # Set the font
pdf.set_font("Arial", size=12)

    # Add a cell with text
pdf.cell(200, 10, txt="Hello, this is a PDF generated using fpdf2!", ln=True, align='C')

    # Add another line of text
pdf.cell(200, 10, txt="This is a second line of text.", ln=True, align='L')

    # Save the PDF
pdf.output("output_fpdf2.pdf")

print("PDF generated successfully using fpdf2!")
