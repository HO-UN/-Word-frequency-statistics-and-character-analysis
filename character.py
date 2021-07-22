import random
import tkinter
def win():
    win = tkinter.Tk()
    text = tkinter.Text(win)  # 文本编辑器(用于展示数据)
    text.insert(tkinter.INSERT, "人物：{}".format(name))
    text.insert(tkinter.INSERT, "\r\n")  # 换行
    text.insert(tkinter.INSERT, "好汉值:{}".format(count))
    text.insert(tkinter.INSERT, "\r\n")
    text.insert(tkinter.INSERT, "好汉值:{}".format(price))
    text.insert(tkinter.INSERT, "\r\n")
    text.insert(tkinter.INSERT, "性格：")
    text.insert(tkinter.INSERT, " ".join(set(weight)))  # 一个个加入集合值
    text.pack()
    win.title('人物性格分析')
    win.mainloop()

book = open("水浒传.txt","r",encoding='utf-8')
#人物名
names=["宋江", "李逵", "吴用", "公孙胜", "关胜", "林冲", "秦明", "呼延", "花荣", "柴进",
                          "燕青", "朱仝", "鲁智深", "武松", "董平", "秦明", "李俊", "卢俊义", "晁盖", "戴宗"]
#读取引用词
justice=open("indexwords.txt","r",encoding='utf-8').read()
maxcount = 1000
baoyi = [line.strip() for line in open("baowords.txt", 'r', encoding="UTF-8").readlines()] #导入褒义词库
for name in names:  #名字循环
    count = 0
    for line in book: #文章一行行读取
        if name in line:
            for just in justice:
                if just in line:
                     count=count+1   #如果名字和关键词都在同一行就count+1
    book.seek(0)
    if count>maxcount:
        maxcount=count       #计算最大好汉值
    price=count*3/maxcount    #计算好汉值百分比
    print("人物：{}，好汉值:{}".format(name,count))
    print("好汉值：{}".format(price))
    if price > 0.7:
        weight=random.choices(baoyi,k=4,weights=[6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5
            , 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1])
        print("性格：{}".format(set(weight)))
        win()  #调用窗口
    elif 0.3 < price < 0.7:
        weight=random.choices(baoyi, k=4, weights=[4, 4, 4, 4, 4, 4, 3, 3,
    3, 3, 3, 3, 5, 5, 5, 5, 5, 5,6, 6, 6, 6, 6, 6,2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1])
        print("性格：{}".format(set(weight)))
        win()  #调用窗口
    else:
        weight=random.choices(baoyi, k=4, weights=[1, 1, 1, 1, 1, 1,2, 2, 2, 2, 2, 2,3, 3, 3, 3, 3, 3
            , 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6])
        print("性格：{}".format(set(weight)))
        win()  #调用窗口