print("情书生成器v1.1，LazyToNameOvO作品，中文版")
mn = input("请告诉我您的名字是什么（如果语言是英文请输入英文）：")
n = input("请告诉我您的对象的名字是什么（如果语言是英文请输入英文）：")
bg = int(input("请告诉我您的对象是男(0)是女(1)："))
l = int(input("请告诉我您的情书的语言（仅限中文(0)与英文(1)）："))
if bg == 0:
    if l == 0:
        print("至我亲爱的",n)
        print("我爱你，我的",n,",我爱着你❤，我可以不惜一切代价喜欢你，你是我生命中最耀眼的阳光，让我迫不及待地望着你😊。",n,"，你知道没有你，我的日子是怎么过的吗？正如一滩烂泥，什么也没用，失去了动力。虽然我是女的，说着这么肉麻的话，但我珍惜和你在一起的时光。我只需要你😊。尽管你冷漠着瞥我一眼，我也会在心中默念:我爱你。因为，爱情的种子在我心中发了芽❤！")
        print("你亲爱的",mn)
    elif l == 1:
        print("To my dear",n)
        print("My dear",n,",I love you so much❤,I can do any thing you want to do.You are the bright sunshine of my life😊!So I always watching you anywhere,anytime.",n,",Do you know my life without you?I like a USELESS TEDDYBEAR!I can't do anything,lost the power!Don't think im a girl,but who says girl can't write love letter!I just need someone stay with me.But I'll always watching you,because the love have a root in my heart❤!")
        print("You dear",mn)
if bg == 1:
    if l == 0:
        print("至我亲爱的",n)
        print("我爱你，我的",n,",我爱着你❤，我可以不惜一切代价吹捧你你，你是我生命中最耀眼的阳光，让我深情地望着你😊。",n,"，你知道没有你，我的日子是怎么过的吗？正如一滩烂泥，软趴趴的，失去了动力。你可以想象一个男的没了动力有多么可怕吗？但我珍惜和你在一起的时光。我只需要你😊。尽管你冷漠着瞥我一眼，我也会在心中默念:我爱你",n,"。因为，爱情的种子在我心中早已生根发芽❤！")
        print("你的好友",mn)
    elif l == 1:
        print("To my dear",n)
        print("My dear",n,",I love you so much❤,I can do any thing you want to do.You are the bright sunshine of my life😊!So I always watching you anywhere,anytime.",n,",Do you know my life without you?I like a USELESS TEDDYBEAR!I can't do anything,I lost the power!Don't think im sick,but I really love you!I just need someone stay with me.But I'll always watching you,because the love have a root in my heart❤!")
        print("You dear",mn)
print("请记得复制粘贴哦！")
#程序作者LazyToNameOvO
#请记得关注我哦！
#编辑语言：python3