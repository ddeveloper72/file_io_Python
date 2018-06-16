f = open('files/relative_data.txt', 'r') #relative file path (relative to this file that were using)


"""an absolute path starts at the very top of the file system.  
Use "pwd" to print working directory.ArithmeticError.
Use readlink -f relative_data.txt to find the absolute path to relative_data.txt.
"""
x = open('/home/ubuntu/workspace/files/relative_data.txt', 'r')

relativeLines = f.read()
f.close()
print(relativeLines)

absoluteLines = x.read()
x.close()
print(absoluteLines)
