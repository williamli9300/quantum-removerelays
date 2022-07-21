fileObj = open('../quantum.slx', 'r')
lines = fileObj.read().splitlines()
fileObj.close()

outList=[]
counter = 0
enum_list = list(enumerate(lines))
isRelay = False
while counter < len(lines):
    if enum_list[counter][1][0].isnumeric():
        if not "relay" in (enum_list[counter][1]).lower():
            outList.append(enum_list[counter][1])
            #print(enum_list[counter][1])
            isRelay = False
        else:
            isRelay = True
    else:
        if isRelay == False:
            outList.append(enum_list[counter][1])
            #print(enum_list[counter][1])
    counter +=1


with open('../quantum.slx', 'w') as f:
    f.writelines("\n".join(outList))
    f.write("\n")
#print("done")
