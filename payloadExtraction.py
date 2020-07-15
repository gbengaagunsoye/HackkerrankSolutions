#Challenge
# Many file formats have information that extends beyond the main payload. For example, an image file may contain extensive metadata that is not
# part of the visually-rendered graphic.
#(C) Gbenga S. Agunsoye
#Write a program that will seek a blob of information for header and footer, extracting the payload in between them

import os.path
import sys

selected_file = open("payloadtext.txt", 'r')

#Starting from the beginning of the file
selected_file.seek(0)

payloadtext = selected_file.readlines()
# print(payloadtext)

# for lines in payloadtext:
#     print(lines)

def extractPayLoad(info):
    leftOvers = ""
    info = leftOvers.join(info)
    info = info.upper()
    metaData = info.split('\n')[0]
    header,footer = metaData.split('|')
    leftOvers = leftOvers.join(info.split('\n')[1:])
    startOfPayload = leftOvers.split(header)[1].lstrip(" ")
    payload = startOfPayload.split(footer)[0].rstrip(" ")
    print(payload)

#Call the extractPayLoad() function on the input information. That should do the job.

extractPayLoad(payloadtext)

def checkConnection(lights):
    result = True
    TotalLight  = [0]
    for light in lights:
        for index in range(len(light)):
            if(index == len(light -1)):
                TotalLight.append(light[index])
                result = True
            if (light[index] in TotalLight and light[index+1] in TotalLight):
                break
                result = False
            if(light[index] in TotalLight and light[index+1] not in TotalLight):
                TotalLight.append(light[index])
                result = True
            if(light[index] not in TotalLight and light[index+1] in TotalLight):
                TotalLight.append(light[index])
                result = True
    return result

a = [[1,5],[0,2],[1,3],[2,4],[3,5],[0,0]]

checkConnection(a)


