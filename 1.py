import os
form PIL import Image

path = 'C:/Users/HS/Desktop/사진/'
resultPath = 'C:/Users/HS/Desktop/사진_크기변경/'

if not os.path.exists(resultPath):
  os.mkdir(resultPath)
  
list = os.listdir(path)

list.sort()

for filename in list:
