import time
import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image


back = "y"
if back == "y" or "Y":
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

    back = input("是否继续?(y/n)")
else:
    pass



