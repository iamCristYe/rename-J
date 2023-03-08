import os

listN = []
for i in range(1, 6):
    listN.append("N" + str(i))

DictSrc = {}
for filename in os.listdir("src"):
    print(filename[-16:-5])
    DictSrc[filename[-16:-5]] = filename

for dir in listN:
    for filename in os.listdir(dir):
        print(filename[-17:-6])
        if filename[-17:-6] in DictSrc:
            print(DictSrc[filename[-17:-6]])
            print(f"{filename[:-6]}.mp4")
            os.rename(f"src/{DictSrc[filename[-17:-6]]}", f"{filename[:-6]}.mp4")
