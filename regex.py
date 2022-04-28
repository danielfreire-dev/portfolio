import os, fnmatch

# Find and replace in files in a directory
ogText = "<img \s id=\"profile-photo\"\s src=\"/img/photo.svg \"\s/>"

newText = "<a href=\"/index.html\"><img id=\"profile-photo\" src=\"/img/photo.svg\" alt=\"profile picture\"/></a>"


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
findReplace("/home/zany/Documents/portfolio/", ogText, newText, "*.html")