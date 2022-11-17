import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image



back = "y"

if back == "y" or "Y":

    name = input("选择文件名Select File Name")
    file = input("选择图片格式Choose a picture format")

    decocdeQR = decode(Image.open("image/" + name + "." + file))

    url = decocdeQR[0].data.decode("ascii")
    print(url)


    #打开浏览器并搜索需要改进
    webbrowser.open_new(url)
    # print(webbrowser.get())

    back = input("继续？continue?y/n")


elif back == "n" or "N":
    print("===================================================")
    # print("弹窗将在1秒后关闭")
    # time.sleep(1)
    # break









# houzhui = ["png","jpg","jpeg","bmp"]
   # for i in houzhui:
   #     if file == i:
   #         val, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread("image/" + name + '.' + file))
   #         print('QR码的内容是:',val)
   #
   #         sys.path.append("libs")
   #         url = val
   #         webbrowser.open(url)
   #         print(webbrowser.get())
   #
   #         if val == " ":
   #             print("NO HAVE")
   #         else:
   #             break
   #
   #         break
   #     else:
   #         print("不支持该格式")
   #         break
