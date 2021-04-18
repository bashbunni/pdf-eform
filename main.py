
# NOTES:
# https://pdf2image.readthedocs.io/en/latest/reference.html
# 

# STEPS:
# 1. Convert PDF to image (will be used as BG for the html)
# 2. Scan the document for horizontal lines
#   a) if there's a horizontal line with vertical lines then only include the bottom line

# TODO: 
# Get PDF to PNG + resize as needed
# Create overlay PNG 
# 
# QUESTIONS:
# Do I want to figure out the # of pages in a PDF or have as an arg (MVP it's easier to have as arg)
#

import sys
# image width should be 1500px
# may be multiple pages
# def get_ffields():


if __name__ == "__main__":
    print("running")
    print(len(sys.argv))
    # want to be like python3 pdftohtml.py path/to/mypdf.pdf 2
    if len(sys.argv) <= 1: # additional params were given
        sys.exit("Please provide a path to the PDF and the number of pages")
    else:
        pdf2image(sys.argv[1], size=(1500, None)) # get PDF file path
        # optional number of pages 
    print("number of pages: " + len(sys.argv)-1)
#    images = convert_from_path('/home/belval/example.pdf')
