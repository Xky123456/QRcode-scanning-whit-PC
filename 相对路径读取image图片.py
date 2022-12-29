import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image

def QR():
    name = input("选择文件名")
    file = input("选择图片格式")
    #循环报错语句
    try:
        decocdeQR = decode(Image.open("image/" + name + "." + file))
        url = decocdeQR[0].data.decode("ascii")
        print(url)

        # 打开浏览器并搜索
        webbrowser.open_new(url)
        # print(webbrowser.get())

    except:
        print("!!该文件不存在!!")

in_content = "y"
QR()

while(True):
    in_content = input("是否继续？(y/n)：")
    if in_content == "Y" or in_content == "y":
        QR()
    elif in_content == "N" or in_content == "n":
        print("你已退出了该程序！")
        exit(0)
    else:
        print("你输入的内容有误，请重输入！")