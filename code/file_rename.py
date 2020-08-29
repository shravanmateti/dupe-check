import os

#Working directory
print("Current Working Directory " , os.getcwd())
myPath=os.chdir("D:/BITS MTech/4-sem/temp/pdf")
# Function to rename multiple files
def main():
   i = 0
   path="D:/BITS MTech/4-sem/temp/pdf"
   for filename in os.listdir(path):
      my_dest ="A" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()