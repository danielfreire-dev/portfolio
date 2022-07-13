import os, fnmatch

# Find and replace in files in a directory
ogText = "https://fonts.googleapis.com/css2?family=Kolker+Brush&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Roboto:wght@100;300;400;500;700&display=swap"

newText = "https://fonts.googleapis.com/css2?family=Kolker+Brush&family=Roboto:wght@100;300;400;500;700&display=swap">


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
findReplace("/home/zany/Documents/portfolio/", ogText, newText, "*.map")