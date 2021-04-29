# coding: utf-8
# 导入依赖
import os
import cv2
import time
from PIL import Image, ImageDraw, ImageFont

text = "极乐世界"                                   # 所转文字
src_video_path = 'Elysion.mp4'                    # 视频路径
video_frame_dir = 'pics'                          # 提成图片的保存路径
gen_img_dir = 'img'                               # 生成图片的保存路径
font_path = './simkai.ttf'                        # 字体路径（行楷）

vidcap = cv2.VideoCapture(src_video_path)         # 读取源视频
count = 0
flag = True
while flag:
    flag, frame = vidcap.read()                   # 读取图像信息，读取失败，即视频读取完成，返回False和空图像
    if not flag:
        break
    else:
        cv2.imwrite(os.path.join(video_frame_dir, "frame_%04d.jpg" % count), frame)     # 保存读取的图片
        count += 1
        if count % 100 == 0:
            print('processing', count)

print("total image count", count)
print("end")

# 创造全黑的背景图，

img = cv2.imread('pics/frame_0001.jpg')                 # 读取原图
size = 9                                                # 文字大小
font = ImageFont.truetype(font_path, size=size)         # 读取字体


def draw(pic):                                          # 图片转字符画
    img = cv2.imread(video_frame_dir + '/' + pic)       # 读取图片
    blank = Image.new("RGB", [img.shape[1], img.shape[0]], "white")     # 新建空白图片
    drawObj = ImageDraw.Draw(blank)                     # 绘制图片

    n = 7                                               # 读取像素的间隔
    m = 9                                               # 文字大小

    font = ImageFont.truetype(font_path, size=m)        # 读取字体以及大小

    t1 = time.time()
    for i in range(0, img.shape[0], n):
        for j in range(0, img.shape[1], n):
            drawObj.text([j, i], text[int(j / n) % len(text)],
                         fill=(img[i][j][2], img[i][j][1], img[i][j][0]),
                         font=font)                     # 按文字的顺序填充文字
    print('cost time %.3f s' % (time.time() - t1))

    blank.save(gen_img_dir + '/' + pic)                 # 保存生成的图片


filelist = os.listdir(video_frame_dir)                  # 读取视频中提取的所有帧图片

n = 1
for file in filelist[:500]:                             # 读取20s视频的图片，即前500张
    try:
        draw(file)
        print('finish %d/%d'%(n, len(filelist)))
    except Exception as e:
        print('error %d'%n, e)
    n += 1


def covert_img2video(img_dir):                          # 将转化的字符画绘制成视频
    filelist = os.listdir(img_dir)
    filelist.sort()                                     # 将图片名按照从小到大的顺序进行排序
    img = cv2.imread(os.path.join(img_dir, filelist[1]))

    fps = 25                                             # 视频帧率
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # MP4的编码格式
    size = (img.shape[1], img.shape[0])
    video = cv2.VideoWriter("out.mp4", fourcc, fps, size)  # size是保存视频的分辨率

    for file_name in filelist:
        if file_name.endswith('.jpg'):
            img = cv2.imread(os.path.join(img_dir, file_name))
            video.write(img)                             # 利用图片制作视频

    video.release()                                      # 生成视频
    print('convert done!')


covert_img2video(gen_img_dir)
