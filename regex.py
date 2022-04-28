import os, fnmatch

# Find and replace in files in a directory
ogText = "flex-shrink: 0;"

newText = "flex-shrink: 0;\nflex-grow: 0;"


#The Function
def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

#The Order
findReplace("/home/zany/Documents/portfolio/", ogText, newText, "*.css")