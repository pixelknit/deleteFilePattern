import os
import glob

dirpath = 'E:\\MOV\\Becoming_an_Unreal_Automation_Expert\\Becoming an Unreal Automation Expert\\'
text_files = []
for x in os.walk(dirpath):
    for y in glob.glob(os.path.join(x[0], '*.srt')):
        text_files.append(y)

#print(text_files)
def fileDelete(filelist):
	
	for file in filelist:
		if os.path.exists(file):
  			os.remove(file)
		else:
  			print("The file does not exist")


fileDelete(text_files)