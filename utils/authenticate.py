def getUsers():
    data = open("data/users.csv","r")
    #fText = f.read()
    array = data.readlines()#split("\n")
    userslist = {}
    print array
    for item in range(len(array)):
        array[item] = array[item].strip("\n").split(",")
        userslist[array[item][0]] = array[item][1]
    data.close()
    return userslist

def addUser(user,pin):
    data = open("data/users.csv","a")
    data.write(str(user)+","+str(pin)+"\n")
    data.close()
    return str(user)+", "+str(pin)+"\n"
