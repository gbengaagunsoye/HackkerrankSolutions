def checkConnection(lights):
    # result = True
    TotalLight  = [0]
    for light in lights:
        for index in range(len(light)):
            TotalLight.append(light[index])
            if(index == len(light)-1):
                # TotalLight.append(light[index])
                result = True
            else:
                if(light[index] in TotalLight and light[index+1] not in TotalLight):
                    # TotalLight.append(light[index])
                    result = True
                if(light[index] not in TotalLight and light[index+1] in TotalLight):
                    # TotalLight.append(light[index])
                    result = True
                if (light[index] in TotalLight and light[index+1] in TotalLight):
                    # break
                    result = False

    print(TotalLight)
    print("here")
    return result

a = [[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]
b = [[1,4],[0,2],[1,3],[2,4],[0,3]]

print(checkConnection(a))
print(checkConnection(b))