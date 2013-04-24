#!/usr/bin/env python

import Image
import sys
import fnmatch
import os

the_path = sys.argv[1]

files = []
for root, dirnames, filenames in os.walk(the_path):
  for filename in fnmatch.filter(filenames, '*.png'):
      files.append(os.path.join(root, filename))

htmlPrefix = '''<html>
                <head>
                  <style type="text/css">
                    body { background-color:#e4e8e9; }
                    table {
                      border:none;
                      border-collapse: collapse;
                    }

                    table td {
                      border-bottom: 1px solid #000;
                      padding: 10px
                    }

                    table td:first-child {
                      border-left: none;
                    }

                    table td:last-child {
                     border-right: none;
                    }
                    td { font-family:"Tahoma"; }
                    img { max-width:300px;
                               height:auto
                     }
                  </style>
                </head>
                <body>'''
htmlSuffix = '''</body>
                </html>'''

body = ""
body+= "<table>"

for file in files:
    img = Image.open(file)
    path,filename = os.path.split(file)
    width,height = img.size
    body+= r'<tr><td>'+'<a href="'+file+'"><img src='+file+'></a>'+'</td><td>'+ filename + ", " + str(width)+ " x " +str(height) +r'</td></tr>'

body+= "</table>"

f = open('index.html', 'w')
f.write(htmlPrefix+body+htmlSuffix)