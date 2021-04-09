'''
Created on Nov 19, 2019

@author: ismayil.aliyev
'''
import tkinter as tk
import difflib
from random import randint
import uuid
import time
import PyPDF2
import difflib
import sys

def find_difference():

    File1_name_withlocation=str(e1.get())
    File2_name_withlocation=str(e2.get())
    Report_location=str(e3.get())
    timestr = time.strftime("%Y%m%d-%H%M%S")
        
    # you can find find the pdf file with complete code in below
    filename1=File1_name_withlocation
    filename2=File2_name_withlocation
    pdfFileObj1 = open('%s'%filename1, 'rb')
    pdfFileObj2 = open('%s'%filename2, 'rb')
    
    #TXT names of PDF, the script will transfer PDF to TXT
    file1="%s/file1.txt"%Report_location
    file2="%s/file2.txt"%Report_location
    
    # pdf reader object
    pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
    pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)
    
    # number of pages in pdf
    num1=pdfReader1.numPages
    num2=pdfReader2.numPages
    
    if (num1==num2):
        for x in range(num1):
            # a page object
            pageObj1 = pdfReader1.getPage(x)
            pageObj2 = pdfReader2.getPage(x)
            
            # extracting text from page.
            # this will print the text you can also save that into String
            pdfFileObj1Text1=pageObj1.extractText()
            pdfFileObj1Text2=pageObj2.extractText()
            
            if (pdfFileObj1Text1==pdfFileObj1Text2):
                print('the files are equal')
            else:
                print('not equal')
            
            f1=open("%s"%file1, "a")
            f2=open("%s"%file2, "a")
            f1.write("%s" % pdfFileObj1Text1)
            f2.write("%s" % pdfFileObj1Text2)
            f1.close()
            f2.close()
            
            f1_lines = open(file1).readlines()
            f2_lines = open(file2).readlines()
            
            #Difference
            difference= difflib.HtmlDiff().make_file(f1_lines,f2_lines,file1,file2)
            difference_report=open('%s/difference_report.html'%Report_location,'w')
            difference_report.write(difference)
            difference_report.close()
    else:
        print('number of pages in files are different')
        if num1<num2:
            for x in range(num1):
                # a page object
                pageObj1 = pdfReader1.getPage(x)
                pageObj2 = pdfReader2.getPage(x)
                
                # extracting text from page.
                # this will print the text you can also save that into String
                pdfFileObj1Text1=pageObj1.extractText()
                pdfFileObj1Text2=pageObj2.extractText()
                
                if (pdfFileObj1Text1==pdfFileObj1Text2):
                    print('the files are equal')
                else:
                    print('not equal')
                
                f1=open("%s"%file1, "a")
                f2=open("%s"%file2, "a")
                f1.write("%s" % pdfFileObj1Text1)
                f2.write("%s" % pdfFileObj1Text2)
                f1.close()
                f2.close()
                
                f1_lines = open(file1).readlines()
                f2_lines = open(file2).readlines()
                
                #Difference
                difference= difflib.HtmlDiff().make_file(f1_lines,f2_lines,file1,file2)
                difference_report=open('%s/difference_report.html'%Report_location,'w')
                difference_report.write(difference)
                difference_report.close()
        else:
            for x in range(num2):
                # a page object
                pageObj1 = pdfReader1.getPage(x)
                pageObj2 = pdfReader2.getPage(x)
                
                # extracting text from page.
                # this will print the text you can also save that into String
                pdfFileObj1Text1=pageObj1.extractText()
                pdfFileObj1Text2=pageObj2.extractText()
                
                if (pdfFileObj1Text1==pdfFileObj1Text2):
                    print('the files are equal')
                else:
                    print('not equal')
                
                f1=open("%s"%file1, "a")
                f2=open("%s"%file2, "a")
                f1.write("%s" % pdfFileObj1Text1)
                f2.write("%s" % pdfFileObj1Text2)
                f1.close()
                f2.close()
                
                f1_lines = open(file1).readlines()
                f2_lines = open(file2).readlines()
                
                #Difference
                difference= difflib.HtmlDiff().make_file(f1_lines,f2_lines,file1,file2)
                difference_report=open('%s/difference_report.html'%Report_location,'w')
                difference_report.write(difference)
                difference_report.close()

    
master = tk.Tk()
tk.Label(master, text="Input location and file name of the first file").grid(row=0)
tk.Label(master, text="Input location and file name of the second file").grid(row=1)
tk.Label(master, text="Directory where you want to put report about files difference").grid(row=2)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)



tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Generate Report', command=find_difference).grid(row=3,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()


master = tk.Tk()
