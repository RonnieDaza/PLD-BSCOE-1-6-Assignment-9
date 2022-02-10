# Assignment 9
# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format.
# All personal details are stored in a JSON file.
# Your program should read the JSON file and write the details in the PDF.
# The output should be: LASTNAME_FIRSTNAME.pdf

# Steps
# 1. Import the module json and FPDF.
import json
from fpdf import FPDF

# 2. Open the JSON file.
openJsonFile = open("My Resume.json")
# 3. Read the JSON file and convert the JSON String document into the Python dictionary.
readJsonFile = json.loads(openJsonFile.read())

# 4. Create the FPDF object.
pdf = FPDF()
# 5. Add a page.
pdf.add_page()
# 6. Specify the font family and size.
pdf.set_font("Helvetica", size = 15)