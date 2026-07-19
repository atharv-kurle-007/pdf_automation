from pathlib import Path
import pymupdf

# pdf file path
pdf_folder = Path.home() / "Documents/PDF"

all_pdf = []

# store names & pages in the list
for pdf in pdf_folder.iterdir():
    if pdf.suffix == ".pdf":
        reader = pymupdf.open(pdf)
        pdf_info = {
            "name": pdf.name,
            "pages": len(reader)
        }
        all_pdf.append(pdf_info)

# store the list data into the csv file
file = open("pdf_summary.csv", "w")
file.write("File name,pages\n")

for pdf in all_pdf:
    file.write(pdf["name"] + "," + str(pdf["pages"]) + "\n")

file.close()
