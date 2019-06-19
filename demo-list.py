#使用list函数将字符串（后面还有其他的数据结构）变为列表
# str='hello'
# liststr=list(str)
# print(liststr)
# liststr.append(3)
# print(liststr)
# x=[1,2,3,4]

#extend

#del删除列表或者删除列表中指定位置的元素


#pop()默认删除最后一个元素pop（0）删除第一个元素

# x.pop()
# print(x)

#remove（）删除指定关素在列表出现的第一个数
# x.remove(2)
# print(x)

#clear()清空列表
# x.clear()
# print(x)

#count计数
x=[1,2,3,4,5]
print(x.count(3))

#index索引:显示要找的元素在列表中的位置
print(x.index(3))

#in：测试列表中是否存在某元素
a=5 in x     #实际使用通常作为if或者while的条件
print(a)

#sort：排序

