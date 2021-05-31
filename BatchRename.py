import os

dirpath = "D:\\UE_PIPELINE\\UE5\\Proceduralv001\\Saved\\MovieRenders"

def main():
  
    for count, filename in enumerate(os.listdir(dirpath)):
        #print(count)
        #print(filename)
        dst ="UErender_" + str(count) + ".exr"
        src =dirpath+ filename
        dst =dirpath+ dst
          
        os.rename(src, dst)
  
if __name__ == '__main__':
      
    main()