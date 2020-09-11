#Install Libraries
# pip install PyPDF2


# import libraries
import os
import pandas as pd
import PyPDF2

#Working directory
print("Current Working Directory " , os.getcwd())
myPath=os.chdir("D:/BITS MTech/4-sem/Project/Dupe check/Data sets/Resume&Job_Description/dupe-check/dataset")

#Count number of PDFs in the directory
import glob
pdfCounter = len(glob.glob1(myPath,"*.pdf"))
#Count number of Word documents in the directory
docCounter = len(glob.glob1(myPath,"*.doc"))
docxCounter = len(glob.glob1(myPath,"*.docx"))

#Read the file names with specific extension in the directory and store as a list
def filebrowser(ext=""):
    "Returns files with an extension"
    return [f for f in glob.glob(f"*{ext}")]

files = filebrowser(".pdf")

df = pd.DataFrame()
df2 = pd.DataFrame()
#open the PDF as an object and read it into PyPDF2
for filenum in range(pdfCounter):
    pdfFileObj = open(files[filenum], 'rb')
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
    pdfFileObj.close() #close the pdf file object
    df = pd.DataFrame(data = {"DocID":[files[filenum]],"Resume":[text2]})
    df2 = df2.append(df)
print(df2)
type(df2)
df2.size
df2.info()
pdfCounter


df2.to_excel('pdf resumes.xls',index=False,header=True)

first_column_pdf_extracted = df2. iloc[:, 0]
type(first_column_pdf_extracted)
pdf_ext_list = first_column_pdf_extracted.values.tolist()

files_not_in_pdf_ext_list = set(files).difference(pdf_ext_list)
files_not_in_pdf_ext_list

with open("file.txt", 'w') as output:
    for row in files_not_in_pdf_ext_list:
        output.write(str(row) + '\n')






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