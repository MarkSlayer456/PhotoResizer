import os
from PIL import Image
import sys
 
# Opens a image in RGB mode
directory = ""
new_width = 100
new_height = 100
has_dir = true
if(len(sys.argv) >= 4):
	directory = sys.argv[3]
	try:
		os.mkdir(directory + "/Resized")
	except:
		print("Resized already exists, overwriting data")
else:
	if(os == "darwin"):
		user = os.getlogin()
		directory = "/Users/" + str(user) + "/Desktop/"
		try:
			os.mkdir("/Users/" + str(user) + "/Desktop/Resized")
		except:
			print("Resized already exists, overwriting data")
	else:
		has_dir = false
		print("Please provide a directory!")

if(len(sys.argv) >= 2):
	new_width = int(sys.argv[1])

if(len(sys.argv) >= 3):
	new_height = int(sys.argv[2])

if(has_dir):
	print("----------")
	count = 1
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		if os.path.isfile(f):

			end4 = f[-4:]
			end3 = f[-3:]
			if(end4 == "jpeg"):
				print("Number: " + str(count))
				count+=1
				print("resizing:", f)

				im = Image.open(f)

				width, height = im.size

				newsize = (new_width, new_height)
				im = im.resize(newsize, Image.Resampling.LANCZOS)
				tmpstart = os.path.join(directory, "Resized/")
				start = os.path.join(tmpstart, filename[:-5])
				im.save(start + "-new.jpeg")
				print("new file: " + start + "-new.jpeg" + " created!")
				print("----------")
			elif(end3 == "jpg"):
				print("Number: " + str(count))
				print("resizing:", f)
				im = Image.open(f)

				width, height = im.size

				newsize = (new_width, new_height)
				print(newsize)
				im = im.resize(newsize)
				tmpstart = os.path.join(directory, "Resized/")
				start = os.path.join(tmpstart, filename[:-4])
				im.save(start + "-new.jpg")
				print("new file: " + start + "-new.jpg" + " created!")
				print("----------")
			elif(end3 == "png"):
				print("Number: " + str(count))
				print("resizing:", f)
				im = Image.open(f)

				width, height = im.size

				newsize = (new_width, new_height)
				im = im.resize(newsize, Image.Resampling.LANCZOS)
				tmpstart = os.path.join(directory, "Resized/")
				start = os.path.join(tmpstart, filename[:-4])
				im.save(start + "-new.jpeg")
				print("new file: " + start + "-new.png" + " created!")
				print("----------")
