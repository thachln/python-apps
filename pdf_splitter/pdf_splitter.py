# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:13:27 2020

@author: ThachLN

Install libraries:
    pip install pypdf2
Refer:
    http://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs-with-python/
"""

import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_splitter(path, outFolder):
    fname = os.path.splitext(os.path.basename(path))[0]
    
    print("path=", path, ";fname=", fname)
    
    pdf = PdfFileReader(path)
    
    # page start with 0
    for page in range(pdf.getNumPages()):
        print('Created: {}'.format(page))
        pdfWritter = PdfFileWriter()
        pdfWritter.addPage(pdf.getPage(page))

        outputFilename = '{}/{}_page_{}.pdf'.format(outFolder, fname, page + 1)
        
        with open(outputFilename, 'wb') as out:
            pdfWritter.write(out)
            
#        print('Created: {}'.format(outputFilename))
        
if __name__ == '__main__':
    lenArgs = len(sys.argv)
    
    # The first argument is the called programm
    # Syntax of command: pdf_splitter <file-path> <out-foldder>
    if (lenArgs < 3):
        print('Usage: pdfsplitter <file-path> <out-folder>')
    else:
        filePath = sys.argv[1]
        outFolder = sys.argv[2]
        print('filePath: ', filePath)
        print('outFolder: ', outFolder)
        
        pdf_splitter(filePath, outFolder)