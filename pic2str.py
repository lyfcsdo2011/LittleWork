import cv2
import time


def draw(path, string, size):                   # path为图片路径，string为所转字符串,size为字符尺寸
    length = len(string)                        # 字符长度
    img = cv2.imread(path)                      # 获取图片
    rows, cols, _ = img.shape                   # 获取图片的长宽
    blank = img * 0 + 255                       # 建立一个白图
    count = 0                                   # 计数用于循环显示字符串
    t1 = time.time()                            # 记录开始时所对应的时间点
    for i in range(0, rows, 6):                 # 行
        for j in range(0, cols, 6):             # 列
            blue, green, red = img[i, j]        # 获取图片RGB的三原色
            text = string[count]                # 取字符串中的一位
            count = (count + 1) % length        # 循环计数
            cv2.putText(blank,                  # 调用cv库里的putText在白图blank上绘制
                        text,
                        (j, i),
                        cv2.FONT_HERSHEY_COMPLEX,
                        size,
                        (int(blue),
                         int(green),
                         int(red)),
                        True)
    print('cost time %.3f s' % (time.time() - t1))
    return blank


cv2.imwrite('out.jpg', draw('1.jpg', "LOVE", 0.2))               # 输出图片
