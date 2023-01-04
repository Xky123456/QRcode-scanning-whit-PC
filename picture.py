import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image



while True:

    file = input("请将图片拖入并按下回车")

    decocdeQR = decode(Image.open(file))

    url = decocdeQR[0].data.decode("ascii")
    print(url)


    #打开浏览器并搜索需要改进
    webbrowser.open_new(url)

    print("===================================================")
