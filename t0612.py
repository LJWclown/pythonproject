a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)

#优先级
z=a=5
print(z)
z=a==5
print(z)
print(a)

# #if语句
# while True:
#     a = int(input('请输入分数:'))
#     if (a<60):
#         print('不及格')
#     elif (a<80):
#         print('及格')
#     elif(a<90):
#         print('良好')
#     else:
#         print('优秀')

while True:
    deposit=int(input('请输入我的存款(万）：'))
    if deposit==0:
        break
    if (deposit>500):
        print('我买路虎')
    elif (deposit>100):
        print('我买宝马')
    elif (deposit>50):
        print('我买迈腾')
    elif (deposit>10):
        print('我买福特')
    else:
        print('我买比亚迪')