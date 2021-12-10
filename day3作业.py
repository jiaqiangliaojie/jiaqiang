# a=0
# d=0
# B=10
# LIST=[]
# while True:
#     C=int(input("请输入"+str(B)+"个数字"))
#     LIST.append(C)
#     B=B-1
#     a=a+C
#     W=a/10
#     if B == d:
#         print(a)
#         print(max(LIST))
#         print(W)
#         break

#随机生成数字
# import random
# w=random.randint(50,150)
# print(w)


# b+c>a
# while True:
#     a=int(input("三角形a边"))
#     b=int(input("三角形b边"))
#     c=int(input("三角形c边"))
#     if a+b>c and a+c>b and b+c>a:
#         print("构成三角形")
#     if  a==b or a==c or b==c :
#         print("构成等腰三角形")
#     if a==b==c :
#         print("构成等边三角形")
#     Q=(a*a)
#     W=(b*b)
#     E=(c*c)
#     if Q==W+E or W==Q+E or E==Q+W:
#         print("构成直角三角形")


# print("A=56,B=78")
# A=int (input("A="))
# B=int (input("B="))
# C=A
# A=B                   #   A,B=B,A
# B=C
# print("实现效果")
# print("A=%d"% A)      #调换  print("A变化后为：%d"%A)
# print("B=%d"% B)
#方法二
# print("请输入两个整数：")
# W=int (input("W="))
# X=int (input("X="))
# W,X=X,W
# print("转化后:")
# print("W=%d"%W)
# print("X=%d"%X)


# A="root"
# B="admin"
# for i in range(0,3):
#     name=input("用户名:")
#     passwd=input("密码:")
#     if name==A and passwd==B:
#         break
#     elif A !=" root" or B != "admin" :
#         if i< 2:
#             print("输入错误，请重新输入")
#         else:
#             print("三次机会已用完锁定")



# lines=int(input("需要打印的行数:"))
# for i in range(lines):
#     for j in range(0,lines-i):     #print是默认结尾并且自动换行
#         print(end=" ")              #end="" 是结尾不换行，加个空格键
#     for k in range(1*i+1):
#         print("*",end=" ")
#     print()


#正序打印99乘法表
# A=1
# B=1
# while A<10:
#     while B<(A+1):
#         print("%d*%d=%d"%(B,A,A*B),end="\t")
#         B=B+1
#     print()
#     A=A+1
#     B=1
#方法二
# for A in range(1,10):
#     for B in range(1,A+1):
#         print("%d*%d=%-2d"%(A,B,A*B),end="\t")
#     print()
# 倒序打印99乘法表
# for A in range(9,0,-1):
#     for B in range(A,0,-1):
#         print("%d*%d=%-2d"%(A,B,A*B),end="\t")
#     print()





# #青蛙爬井
# a=0
# for i in range(0,100):
#     a+=3
#     if a>20:
#         print("第",i,"天爬出来")
#         break
#     a-=2




