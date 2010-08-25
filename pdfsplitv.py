#!/usr/bin/python
import sys
from pyPdf import PdfFileReader, PdfFileWriter

if len(sys.argv) != 3:
    sys.exit("Splits verticaly PDF pages\nUsage: pdfsplitv in.pdf out.pdf")
input1 = PdfFileReader(file(sys.argv[1],"rb"))
input2 = PdfFileReader(file(sys.argv[1],"rb"))
output = PdfFileWriter()

for br in range(0,input2.getNumPages()):
    page1 = input1.getPage(br)
    page2 = input2.getPage(br)
    page1.mediaBox.upperRight = (
            page1.mediaBox.getUpperRight_x()/2,
            page2.mediaBox.getUpperRight_y()
        )
    page2.mediaBox.upperLeft = (
            page2.mediaBox.getUpperRight_x()/2,
            page2.mediaBox.getUpperLeft_y()
        )
    output.addPage(page1)
    output.addPage(page2)
outStream = file(sys.argv[2],"wb")
output.write(outStream)
outStream.close()

