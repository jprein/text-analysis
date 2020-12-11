import sys 
from io import StringIO
import os
from os import path
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import numpy as np 

def convert_pdf_to_txt(path):
    print(path)
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
    text = text + "\n" + 'The ENd of Document.'

    fp.close()
    device.close()
    retstr.close()
    
    direc,filename = os.path.split(path)
    filename,ext = os.path.splitext(filename)
    new_file = filename + '.txt'
    direc = '/Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/txts'
    new_file = os.path.join(direc,new_file)
    textfile = open(new_file, 'w')
    textfile.write(text)
    textfile.close()
    
    return

# x = convert_pdf_to_txt('/Users/julia_prein/Work/experiments/soc_cog_textanalysis/raw-data/testpdfs/')
