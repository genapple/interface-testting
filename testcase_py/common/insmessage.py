from Minstance import datacel
from game_pb2 import  *
filepath=r"D:\project\automator-testting\testcase\socket.xls"
all_case=datacel(filepath)
print ("all_case:" , format(all_case))

def test_message():
    cmd = all_case[0]["cmd"]
    object1=eval(all_case[0]["name1"])
    print(all_case[0]["name1"])
    for key in eval(all_case[0]['parameters1']).keys():
        values=eval(all_case[0]["parameters1"])[key]

        setattr(object1, key, values)
        s=getattr(object1, key)
        print(s)
        # object1.ss=eval(all_case[0]["parameters1"])[key]
    return cmd, object1

test_message()

def read_message():
    object2=eval(all_case[0]['name2'])
    names=[]
    names=(all_case[0]['parameters2'])
    print(all_case[0]['parameters2'])
    for key in names:
        # values = eval(all_case[0]["parameters2"])[key]

        # setattr(object1, key, values)
        s = getattr(object2, key)
        print(s)
        # object1.ss=eval(all_case[0]["paramete

read_message()