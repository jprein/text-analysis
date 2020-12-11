# https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from os import path

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    print(type(text))

    return text

# /Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/pdfs/adrián2007mothers.pdf
# /Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/pdfs/bosacki2015children.pdf
# /Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/pdfs/bowman2017action.pdf

x = convert_pdf_to_txt('/Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/pdfs/abc.pdf')
print(x)

# COMMENT MAIN IF YOU WANT TO USE THE convert_pdf_to_txt FUNCTION IN R WITH RETICULATE
# if __name__ == '__main__':
#     from sys import argv
#     # print(convert_pdf_to_txt(argv[1]))
#     text_file = open("test.txt", "w")
#     n = text_file.write(convert_pdf_to_txt(argv[1]))
#     text_file.close()


# TODO: durch directory gehen, alle PDFs listen, einlesen in LIste. 

# import glob, os und io funktionieren nicht. 
# import glob
# glob.glob("*.pdf")

# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)
