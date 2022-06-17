import os
form PIL import Image

path = 'C:/Users/HS/Desktop/사진/'
resultPath = 'C:/Users/HS/Desktop/사진크기변경/'

if not os.path.exists(resultPath):
  os.mkdir(resultPath)
  
list = os.listdir(path)

list.sort()

for filename in list:
  
  file = path + filename
  
  img = Image.open(file)
  img.save(os.path.join(resultPate, filename), 'JPEG', quality=85)

  from PIL import Image
  
  image1 = Image.open('A.PNG')
  image1.show()
  
  print(image1.size)
  
  croppedImage=image1.crop((10,10,100,100))
  
  croppedImage.show()
  
  print("잘려진 사진 크기:",croppedImage.size)
  
  crroppedImage.save('croppedImage.PNG')
  
