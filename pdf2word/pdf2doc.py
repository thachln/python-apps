import os
from pdf2docx import Converter

def convert_pdf_to_word(pdf_file, docx_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    # Convert the PDF to a DOCX file
    cv.convert(docx_file, start=0, end=None)
    # Close the Converter object
    cv.close()

def convertFolder(folder_input : str, folder_output : str):
    # Create output folder
    if not os.path.exists(folder_output):
        os.makedirs(folder_output)
    for path, folders, files in os.walk(folder_input):
        for f in files:
            fpath_pdf_file = os.path.join(path, f)
            opath = fpath_pdf_file.replace('.pdf', '.docx')
            opath_docx_file = opath.replace(folder_input, folder_output)

            print('Writing to {}', opath)
            opath = os.path.dirname(opath_docx_file)
            if not os.path.exists(opath):
                os.makedirs(opath)
            convert_pdf_to_word(fpath_pdf_file, opath_docx_file)

# Example usage
folder_input = r''
folder_output = r''
convertFolder(folder_input, folder_output)
