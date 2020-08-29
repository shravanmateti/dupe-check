#Install Libraries
# pip install PyPDF2


# import libraries
import os
import pandas as pd
import PyPDF2

#Working directory
print("Current Working Directory " , os.getcwd())
myPath=os.chdir("D:/BITS MTech/4-sem/Project/Dupe check/Data sets/Resume&Job_Description/Original_Resumes")

#Count number of PDFs in the directory
import glob
pdfCounter = len(glob.glob1(myPath,"*.pdf"))
print(pdfCounter)
#Count number of Word documents in the directory
docCounter = len(glob.glob1(myPath,"*.doc"))
print(docCounter)
docxCounter = len(glob.glob1(myPath,"*.docx"))
print(docxCounter)

#Read the PDF file names in the directory and store as a list
def filebrowser(ext=""):
    "Returns files with an extension"
    return [f for f in glob.glob(f"*{ext}")]

files = filebrowser(".pdf")
print(files)
files[1]
#Pass each file name from the above "files" list to below code to read the PDF files and convert to a "text" and store in a dataframe-2
#open the PDF as an object and read it into PyPDF2
pdfFileObj = open(files[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
npages=pdfReader.numPages
text2 = ""
# create page object and extract text from all pages based on pages count n "npages"
for pageNum in range(npages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    text = text.replace('\n \n','').replace('\n','')
    text2 = text2 +","+ text
print(text2)
pdfFileObj.close() #close the pdf file object
print(files[1])
# create an Empty DataFrame object 
df = pd.DataFrame() 
df.iloc[1]=pd.DataFrame({"DocID":[files[1]],"Resume":[text2]})  
# append columns to an empty DataFrame 



df1.append(df2) 

#Pass each *.doc and *.docx throuth below code and create a dataframe-3
import docx2txt

# read in word file
result = docx2txt.process("zen_of_python.docx")


#merge dataframe-2 and dataframe-3 to a dataframe df



####----------------------------#####


# insert commas to separate variables and then remove excess strings
text = text.replace('\n \n','').replace('\n','')
text
print(text)

# Create dataframe
dbn_df = pd.DataFrame([sub.split(",") for sub in page1])
dbn_df.head()


######################to start code form ehere
# intialise data of lists.
data = {'File_Name':['Tom', 'nick', 'krish', 'jack'],
        'Profile':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)

######################
# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
print(df) 
# using isnull() function  
df.isnull()