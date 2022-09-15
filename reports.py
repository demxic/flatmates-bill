import webbrowser

from fpdf import FPDF

from flat import FlatMate, Bill


class PdfReport:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate(self, flatmate1: FlatMate, flatmate2: FlatMate, bill: Bill):
        """Draw and output a pdf file with the split amount of each flatmate"""
        flatmate1_pays = flatmate1.pays(bill, flatmate2)
        flatmate2_pays = flatmate2.pays(bill, flatmate1)

        # Initialize the pdf file
        file = FPDF(orientation='P', unit='pt', format='letter')
        file.add_page()

        # Insert the image
        file.image('files\\house.png', w=30, h=30)

        # Set the Font and title
        file.set_font(family='Times', style='B', size=24)
        file.cell(w=0, h=70, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Set the "period" label with its corresponding value
        file.set_font(family='Times', style='B', size=20)
        file.cell(w=80, h=40, txt='Period:', border=0, align='')
        file.cell(w=120, h=40, txt=bill.period, border=0, align='', ln=1)

        # Set the first flatmate and its amount due
        file.set_font(family='Times', style='', size=16)
        file.cell(w=80, h=25, txt=flatmate1.name, border=0, align='')
        file.cell(w=100, h=25, txt=f'$ {flatmate1_pays}', border=0, align='R', ln=1)

        # Set the second flatmate and its amount due
        file.cell(w=80, h=25, txt=flatmate2.name, border=0, align='')
        file.cell(w=100, h=25, txt=f'$ {flatmate2_pays}', border=0, align='R', ln=1)

        file.output(name=self.filename)

        webbrowser.open(self.filename)
