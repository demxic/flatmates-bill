from flat import Bill, FlatMate
from reports import PdfReport

the_bill = Bill(amount=120, period='march 2022')
xico = FlatMate(name='Xico', days_in_house=20)
mary = FlatMate(name='Mary', days_in_house=25)

pdf = PdfReport('the_bill.pdf')
pdf.generate(xico, mary, the_bill)
