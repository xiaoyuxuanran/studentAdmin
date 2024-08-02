'''
  @author:xiaoyuxuanran
  @date:2024/08/02 10:19
  @location:China Shandong Liaocheng Linqing LEGO robot activity center
'''


import tkinter
import tkinter.messagebox
from tkinter import simpledialog
from tkinter import StringVar
import time
class student:
    def __init__(self,tel,name,num,grade,point):
        self.tel=tel
        self.name=name
        self.num=num
        self.grade=grade
        self.point=point
class demo:
    def __init__(self,tel,pwd):
        self.tel=tel
        self.pwd=pwd
s1=student(1,"张三","12345","12",98)
s2=student(2,"李四","23345","13",92)
students=[s1,s2]
# def test02():
#     def demo04():
#         print("序号\t姓名\t\t学号\t\t班级\t分数")
#         for i in range(len(students)):
#             print(f"{students[i].tel}.\t{students[i].name}\t\t{students[i].num}\t\t{students[i].grade}\t{students[i].point}")
#     def demo01():
#         n1=input("请输入要添加学生的学号")
#         n2=input("请输入要添加学生的班级")
#         n3=input("请输入要添加学生的姓名")
#         n4=input("请输入要添加学生的分数")
#         s2=student(students[-1].tel+1,n3,n1,n2,int(n4))
#         students.append(s2)
#         print("添加成功")
#     def demo02():
#         demo04()
#         n=int(input("请输入要删除的学生信息的序号:"))
#         for i in range(len(students)):
#             if students[i].tel==n:
#                 del students[i]
#         print("删除成功!")
#     def demo03():
#         demo04()
#         n=int(input("请输入要修改的学生信息的序号:"))
#         for i in range(len(students)):
#              if students[i].tel==n:
#                 students[i].num=input("请输入新的学号")
#                 students[i].grade=input("请输入新的班级:")
#                 students[i].name=input("请输入新的姓名:")
#                 students[i].point=int(input("请输入新的分数:"))
#         print("输入成功")  
#     while True:
#         print("\t\t欢迎使用学生信息管理系统")
#         print("\t\t\t1.增加学生信息")
#         print("\t\t\t2.删除指定学生信息")
#         print("\t\t\t3.修改指定学生信息")
#         print("\t\t\t4.查询所有学生信息")
#         print("\t\t\t5.退出系统")
#         cho=input("请选择功能前的数字以使用该功能：")
#         if cho=="1":
#             demo01()
#         elif cho=="2":
#             demo02()
#         elif cho=="3":
#             demo03()
#         elif cho=="4":
#             demo04()
#         elif cho=="5":
#             break
#         else:
#             print("输入错误，请重新输入")
def ui2():
    def displaymeau():
        for i in range(len(students)):
            telLable2=tkinter.Label(mainUi, text=students[i].tel,font=("黑体",20),bg="#00ff00")
            telLable2.place(x=105,y=50+51*(i+1),width=150,height=50)
            nameLable2=tkinter.Label(mainUi, text=students[i].name,font=("黑体",20),bg="#00fff0")
            nameLable2.place(x=255,y=50+51*(i+1),width=150,height=50)
            numLable2=tkinter.Label(mainUi, text=students[i].num,font=("黑体",20),bg="#ffff00")
            numLable2.place(x=405,y=50+51*(i+1),width=150,height=50)
            gradeLable2=tkinter.Label(mainUi, text=students[i].grade,font=("黑体",20),bg="#ff00ff")
            gradeLable2.place(x=555,y=50+51*(i+1),width=150,height=50)
            pointLable2=tkinter.Label(mainUi, text=students[i].point,font=("黑体",20),bg="#aa00ff")
            pointLable2.place(x=705,y=50+51*(i+1),width=150,height=50)
    def add():
        n1 = simpledialog.askstring("添加信息", "请输入要添加学生的学号：")
        n2 = simpledialog.askstring("添加信息", "请输入要添加学生的班级：")
        n3 = simpledialog.askstring("添加信息", "请输入要添加学生的姓名：")
        n4 = simpledialog.askstring("添加信息", "请输入要添加学生的分数：")
        s2=student(int(students[-1].tel+1),n3,n1,n2,int(n4))
        students.append(s2)
        tkinter.messagebox.askquestion("提示", "添加成功")
        displaymeau()
    def delinfo():
        n=simpledialog.askstring("删除信息", "请输入要删除学生的学号")
        for i in range(len(students)):
            if students[i].num==n:
                del students[i]
                break
        tkinter.messagebox.askquestion("提示", "删除成功")
        displaymeau()
    def chinfo():
        n=int(simpledialog.askstring("修改信息", "请输入修改学生信息的序号："))
        for i in range(len(students)):
             if students[i].tel==n:
                students[i].num=simpledialog.askstring("修改信息", "请输入新的学号：")
                students[i].grade=simpledialog.askstring("修改信息", "请输入新的班级：")
                students[i].name=simpledialog.askstring("修改信息", "请输入新的姓名：")
                students[i].point=int(simpledialog.askstring("修改信息", "请输入新的成绩："))
                break
        else:
            tkinter.messagebox.askquestion("提示", "没有相应序号的学生")
        tkinter.messagebox.askquestion("提示", "修改成功")
        displaymeau()
    def quitUi():
        mainUi.destroy()
        
    mainUi=tkinter.Tk()
    mainUi.title("学生信息管理系统")
    mainUi.geometry('960x540')
    telLable=tkinter.Label(mainUi, text="序号",font=("黑体",20),bg="#00ff00")
    telLable.place(x=105,y=50,width=150,height=50)
    nameLable=tkinter.Label(mainUi, text="姓名",font=("黑体",20),bg="#00fff0")
    nameLable.place(x=255,y=50,width=150,height=50)
    numLable=tkinter.Label(mainUi, text="学号",font=("黑体",20),bg="#ffff00")
    numLable.place(x=405,y=50,width=150,height=50)
    gradeLable=tkinter.Label(mainUi, text="班级",font=("黑体",20),bg="#ff00ff")
    gradeLable.place(x=555,y=50,width=150,height=50)
    pointLable=tkinter.Label(mainUi, text="成绩",font=("黑体",20),bg="#aa00ff")
    pointLable.place(x=705,y=50,width=150,height=50)
    displaymeau()
    addBtu=tkinter.Button(mainUi,text="增加信息",command=add,font=("黑体",30),bg="#00ff00")
    addBtu.place(x=100,y=450)
    delBtu=tkinter.Button(mainUi,text="删除信息",command=delinfo,font=("黑体",30),bg="#00ff00")
    delBtu.place(x=300,y=450)
    delBtu=tkinter.Button(mainUi,text="修改信息",command=chinfo,font=("黑体",30),bg="#00ff00")
    delBtu.place(x=500,y=450)
    delBtu=tkinter.Button(mainUi,text="退出系统",command=quitUi,font=("黑体",30),bg="#00ff00")
    delBtu.place(x=700,y=450)
    mainUi.mainloop() 
admin=demo("admin","123456")
users=[admin]
def ui():
    def log1():
        a=telEnter.get()
        b=pwdEnter.get()
        for i in range(len(users)):
            if a==users[i].tel and b==users[i].pwd:
                helpLable.config(text="登陆状态:登录成功")
                tkinter.messagebox.askquestion("提示", "登录成功")
                time.sleep(1)
                logUi.destroy()
                ui2()
                break
        else:
            helpLable.config(text="登陆状态:登录失败")
    def re1():
        tel1 = simpledialog.askstring("注册", "请输入账号：")
        pwd1 = simpledialog.askstring("注册", "请输入密码：")
        usr=demo(tel1,pwd1)
        users.append(usr)
        tkinter.messagebox.askquestion("提示", "注册成功")
    logUi=tkinter.Tk()
    logUi.title("学生信息管理系统")
    logUi.geometry('960x540')
    mainTitle = tkinter.Label(logUi, text="学生信息管理系统",font=("楷体",30))
    mainTitle.place(x=350,y=1)
    telLable=tkinter.Label(logUi, text="账号:",font=("黑体",30))
    telLable.place(x=200,y=100)
    pwdLable=tkinter.Label(logUi, text="密码:",font=("黑体",30))
    pwdLable.place(x=200,y=200)
    telEnter=tkinter.Entry(logUi,font=("黑体",30))
    telEnter.place(x=320,y=100)
    pwdEnter=tkinter.Entry(logUi,font=("黑体",30))
    pwdEnter.place(x=320,y=200)
    helpLable=tkinter.Label(logUi, text="登录状态:未登录",font=("黑体",30))
    helpLable.place(x=350,y=300)
    logBtu=tkinter.Button(logUi,text="登录",command=log1,font=("黑体",30),bg="#00ffff")
    logBtu.place(x=300,y=400)
    reBtu=tkinter.Button(logUi,text="注册",command=re1,font=("黑体",30),bg="#00ffff")
    reBtu.place(x=600,y=400)
    logUi.mainloop()    
ui()
# running=True
# while running:
#     print("欢迎使用学生信息管理系统")
#     print("1.登录")
#     print("2.注册")
#     print("3.退出")
#     ch=input("请选择功能:")
#     if ch=='1' or ch=="登录":
#         tel=input("请输入账号:")
#         pwd=input("请输入密码:")
#         for i in range(len(users)):
#             if tel==users[i].tel and pwd==users[i].pwd:
#                 print("登录成功，请稍等")
#                 '''主要功能入口'''
#                 test02()
#                 running=False
#                 break
#         else:
#             print("账号密码错误")
#     elif ch=='2' or ch=="注册":
#         a=input("请输入账号:")
#         b=input("请输入密码:")
#         usr=demo(a,b)
#         users.append(usr)
#     elif ch=="3" or ch=="退出":
#         break
#     else:
#         print("请重新输入:")




