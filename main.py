
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
import cv2
import numpy
import pdf2image
# image width should be 1500px
# may be multiple pages
# def get_ffields():

def detect_lines():
    '''
    @param img string of image path
    @return coordinates?
    '''
    img = "adolescentinpatientunitInterhospital-Transfer-form-1.png"
    myimg = cv2.imread(img) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
    min_line_length = 100
    max_line_gap = 10
    lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 100, min_line_length, max_line_gap)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(img, (x1, y1), (x2,y2), (0, 255, 0), 2)
    cv2.imwrite('houghlines-test1.png', img)


if __name__ == "__main__":
   # print("running")
    # print(len(sys.argv))
    # want to be like python3 pdftohtml.py path/to/mypdf.pdf 2
    # if len(sys.argv) <= 1: # additional params were given
    #    sys.exit("Please provide a path to the PDF and the number of pages")
    # else:
    #    pdf2image(sys.argv[1], size=(1500, None)) # get PDF file path
        # optional number of pages 
    # print("number of pages: " + len(sys.argv)-1)
#    images = convert_from_path('/home/belval/example.pdf')
    detect_lines()
