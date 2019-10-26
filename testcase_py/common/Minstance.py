# import pb  文件
import xlrd
import  os
#打开文件


'''读取Excel'''
def datacel(filepath):
    all_case=[]
    casefile = xlrd.open_workbook(filepath, "r")
    test = casefile.sheet_by_index(0)
    nrows=test.nrows
    for i in range(1,nrows):
        all_case.append({"cmd":test.cell(i,0).value,"name1":test.cell(i,1).value,
                         "parameters1":test.cell(i,2).value,"name2":test.cell(i,3).value,
                         "parameters2":test.cell(i,4)})
        # print(all_case)
    return all_case



# print (data1)
#先作为测试，先这么写着试试
#读取协议号
# cmd=worksheet.col_values(1,0)
# #读取协议名称
# interfaceName=worksheet.col_values(1,1)
# #读取协议属性
# attrs=[]
# len_attrs=worksheet.col_values(1,4)
#
#
# #多个属性怎么定义
# names=locals()
#
# for i in range(len_attrs):
#     attname= worksheet.col_values(1, 6+i).split(",")[i]
#     names["x%s" %i]=attname
# def instance_messge():
#     instance=interfaceName()
#     instance.names["x1"]=
#获取到对应的协议号，属性
#进行实例化
#调用模块，封装
#发送
#解析