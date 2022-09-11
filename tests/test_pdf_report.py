from main import PdfReport

def test_pdf_report_init():
    report = PdfReport(filename = 'prueba')

    assert report.filename == 'prueba'