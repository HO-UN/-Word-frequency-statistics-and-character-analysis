import jieba
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import wordcloud
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
text = open("水浒传.txt", "r", encoding="UTF-8").read()     #  读取文本文件数据
stopwords = [line.strip() for line in open("stopwords.txt", 'r', encoding="UTF-8").readlines()]
# 获取词频

words = jieba.lcut(text.strip())
counts = {}

for word in words:
    if len(word) == 1:  # 删除长度为1的字符
        continue
    elif word not in stopwords:
        if word == "凤姐儿":
            word = "凤姐"
        elif word == "林黛玉" or word == "林妹妹" or word == "黛玉笑":
            word = "黛玉"
        elif word == "宝二爷":
            word = "宝玉"
        elif word == "袭道人":
            word = "袭人"
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)  # 获得词频
with open("水浒传_词频.txt", "w") as f:
    for i in range(200):
        word, count = items[i]
        f.writelines("{}\t{}\n".format(word, count))
f.close()
#   画人物出场频率图
name = open("水浒传_词频.txt", "r").readlines()
dic={}
for item in name:
    item = item.split("\t")
    dic[item[0]] = int(item[1])
x = []  # 用来存储人物名称
y = []  # 用来存储出场次数
for item in dic:
    x.append(item)
    y.append(dic[item])
#  用pandas库画图
dic1 = {}
dic1["名字"] = x
dic1["次数"] = y
df = pd.DataFrame(dic1)
df = df.set_index("名字")
df.plot(kind='bar', title="水浒传人物出场频率图", figsize=(15, 15))
plt.savefig("水浒传人物出场频率图.jpg")
plt.show()
#  开始画词云
text = open("水浒传_词频.txt", "r").read()
wcloud = wordcloud.WordCloud(background_color="white", width=1000, max_words=200,
                             font_path=r"C:\Windows\Fonts\simhei.ttf",
                             height=850, margin=2).generate(text)
wcloud.to_file("水浒传cloud.png")
plt.imshow(wcloud)
plt.axis('off')
plt.show()