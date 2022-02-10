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
openJsonFile = open("My Resume in JSON File.json")
# 3. Read the JSON file and convert the JSON String document into the Python dictionary.
readJsonFile = json.loads(openJsonFile.read())

# 4. Create the FPDF object.
pdf = FPDF()
# 5. Add a page.
pdf.add_page()
# 6. Specify the font family and size.
pdf.set_font("Helvetica", size = 15)

# 7. Specify the width and height, add every text, indicate the Python dictionary keyword, and move down the next line after the cell is complete.
# myInfo
pdf.multi_cell(190, 7, txt = readJsonFile["myInfo"]["myName"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInfo"]["myPosition"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInfo"]["myBio"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInfo"]["myEmail"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInfo"]["myLocation"], ln = True)

# myAcademicBackground
pdf.multi_cell(190, 7, txt = readJsonFile["myAcademicBackground"]["blankTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myAcademicBackground"]["sectionTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myAcademicBackground"]["myUniversity"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myAcademicBackground"]["myDegree"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myAcademicBackground"]["theYears"], ln = True)

# myFirstReference
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstReference"]["blankThree"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstReference"]["sectionThree"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstReference"]["statementOne"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstReference"]["personOne"], ln = True)

# mySecondReference
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondReference"]["blankFour"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondReference"]["statementTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondReference"]["personTwo"], ln = True)

# myFirstWorkExperience
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["blankFive"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["sectionFour"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["companyOne"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["positionOne"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["startDateOne"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myFirstWorkExperience"]["endDateOne"], ln = True)

# mySecondWorkExperience
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondWorkExperience"]["blankSix"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondWorkExperience"]["companyTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondWorkExperience"]["positionTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondWorkExperience"]["startDateTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["mySecondWorkExperience"]["endDateTwo"], ln = True)

# myInterests
pdf.multi_cell(190, 7, txt = readJsonFile["myInterests"]["blankSeven"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInterests"]["sectionFive"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInterests"]["interestOne"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInterests"]["interestTwo"], ln = True)
pdf.multi_cell(190, 7, txt = readJsonFile["myInterests"]["interestThree"], ln = True)

# 8. Create the PDF file.
pdf.output("DAZA_RONNIE.pdf")