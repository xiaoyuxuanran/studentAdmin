'''
  @author:xiaoyuxuanran
  @date:2024/08/02 10:19
  @location:China Shandong Liaocheng Linqing LEGO robot activity center
'''
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
students=[s1]
def test02():
    def demo04():
        print("序号\t姓名\t\t学号\t\t班级\t分数")
        for i in range(len(students)):
            print(f"{students[i].tel}.\t{students[i].name}\t\t{students[i].num}\t\t{students[i].grade}\t{students[i].point}")
    def demo01():
        n1=input("请输入要添加学生的学号")
        n2=input("请输入要添加学生的班级")
        n3=input("请输入要添加学生的姓名")
        n4=input("请输入要添加学生的分数")
        s2=student(students[-1].tel+1,n3,n1,n2,int(n4))
        students.append(s2)
        print("添加成功")
    def demo02():
        demo04()
        n=int(input("请输入要删除的学生信息的序号:"))
        for i in range(len(students)):
            if students[i].tel==n:
                del students[i]
        print("删除成功!")
    def demo03():
        demo04()
        n=int(input("请输入要修改的学生信息的序号:"))
        for i in range(len(students)):
             if students[i].tel==n:
                students[i].num=input("请输入新的学号")
                students[i].grade=input("请输入新的班级:")
                students[i].name=input("请输入新的姓名:")
                students[i].point=int(input("请输入新的分数:"))
        print("输入成功")  
    while True:
        print("\t\t欢迎使用学生信息管理系统")
        print("\t\t\t1.增加学生信息")
        print("\t\t\t2.删除指定学生信息")
        print("\t\t\t3.修改指定学生信息")
        print("\t\t\t4.查询所有学生信息")
        print("\t\t\t5.退出系统")
        cho=input("请选择功能前的数字以使用该功能：")
        if cho=="1":
            demo01()
        elif cho=="2":
            demo02()
        elif cho=="3":
            demo03()
        elif cho=="4":
            demo04()
        elif cho=="5":
            break
        else:
            print("输入错误，请重新输入")
admin=demo("admin","123456")
users=[admin]
running=True
while running:
    print("欢迎使用学生信息管理系统")
    print("1.登录")
    print("2.注册")
    print("3.退出")
    ch=input("请选择功能:")
    if ch=='1' or ch=="登录":
        tel=input("请输入账号:")
        pwd=input("请输入密码:")
        for i in range(len(users)):
            if tel==users[i].tel and pwd==users[i].pwd:
                print("登录成功，请稍等")
                '''主要功能入口'''
                test02()
                running=False
                break
        else:
            print("账号密码错误")
    elif ch=='2' or ch=="注册":
        a=input("请输入账号:")
        b=input("请输入密码:")
        usr=demo(a,b)
        users.append(usr)
    elif ch=="3" or ch=="退出":
        break
    else:
        print("请重新输入:")




