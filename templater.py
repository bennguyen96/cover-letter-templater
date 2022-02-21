import csv
import os
from docxtpl import DocxTemplate

def template_cover_letter() -> None:
    with open('tech_companies.csv') as tech_companies:
        csv_reader = csv.reader(tech_companies, delimiter=",")
        company_list = next(csv_reader)
        for company in company_list:
            template_company(company)
    
    

def template_company(company: str) -> None:
    doc = DocxTemplate("Cover Letter Template.docx")
    context = { 'company' : company }
    doc.render(context)
    folder_exists = os.path.exists('./Cover Letters')
    if not folder_exists:
        os.makedirs('./Cover Letters')
    doc.save(f"Cover Letters/Ben Nguyen - {context['company']} Cover Letter.docx")



if __name__ == "__main__":
    template_company('Test')