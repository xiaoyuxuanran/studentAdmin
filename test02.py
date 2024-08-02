nums=["123456"]
grade=["02"]
names=["张三"]
point=[79]
def test02():
    def demo04():
        print("序号\t姓名\t\t学号\t\t班级\t分数")
        for i in range(len(nums)):
            print(f"{i}.\t{names[i]}\t\t{nums[i]}\t\t{grade[i]}\t{point[i]}")
    def demo01():
        n1=input("请输入要添加学生的学号")
        n2=input("请输入要添加学生的班级")
        n3=input("请输入要添加学生的姓名")
        n4=input("请输入要添加学生的分数")
        nums.append(n1)
        grade.append(n2)
        names.append(n3)
        point.append(int(n4))
        print("添加成功")
    def demo02():
        demo04()
        n=int(input("请输入要删除的学生信息的序号:"))
        del nums[n]
        del grade[n]
        del names[n]
        del point[n]
        print("删除成功!")
    def demo03():
        demo04()
        n=int(input("请输入要修改的学生信息的序号:"))
        nums[n]=input("请输入新的学号")
        grade[n]=input("请输入新的班级:")
        names[n]=input("请输入新的姓名:")
        point[n]=int(input("请输入新的分数:"))
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
def my_homework():
    while True:
        tel=input("请输入账号:")
        pwd=input("请输入密码:")
        if tel=="admin" and pwd == "123456789":
            print("账号密码正确，请稍等...")
            print("***********************************")
            test02()
            break
        if tel !="admin" or pwd != "123456789":
            print("账号密码输入错误，请重新输入")
            print("***********************************")
my_homework()