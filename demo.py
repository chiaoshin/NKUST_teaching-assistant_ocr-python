# OCR
from PIL import Image, ImageGrab
import pytesseract

# shift+win+s 截圖自動產圖
im = ImageGrab.grabclipboard()
im.save('savefile.png', 'png')
# im.show()

# img_name = './001.en-us.png'
# img2_name = './002.zh-cht.png'
# img_name = './F/hw.png'
img_name = './savefile.png'
img = Image.open(img_name)
text = pytesseract.image_to_string(img, lang='eng')
print(text)
# 計算十位數函式


def sum_of_all_number(text):
    num = 0
    sum = 0
    for i in text:
        if i.isdigit():
            num = num*10+int(i)
        else:
            sum += num
            num = 0
    return sum-3
# 剪掉圖片判斷的Screen1跟F2C，裡面的數字會被抓出來，所以總和-3


print(sum_of_all_number(text))

# 切換檔案、執行指令
# cd C:\Users\User\Downloads\ocr
# python .\demo.py

# 中文判斷有誤
# img4_name = './mhw3.png'
# mimg = Image.open(img4_name)
# mtext = pytesseract.image_to_string(mimg, lang='chi_tra+eng')
# print(mtext)
