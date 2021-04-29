import os

''''
def webm_to_wav(webm_path, wav_path, sampling_rate, channel):
    """
    webm 转 wav
    :param webm_path: 输入 webm 路劲
    :param wav_path: 输出 wav 路径
    :param sampling_rate: 采样率
    :param channel: 通道数
    :return: wav文件
    """
    # 如果存在wav_path文件，先删除。
    if os.path.exists(wav_path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(wav_path)
    # 终端命令
    command = "ffmpeg -loglevel quiet -i {} -ac {} -ar {} {}".format(webm_path, channel, sampling_rate, wav_path)
    # print('命令是：',command)
    # 执行终端命令
    os.system(command)

if __name__ == '__main__':
    path = "F:/characters"
    for subpath in os.listdir(path):
        subsubpath = os.listdir(path +"/" + subpath)
        for i in subsubpath:
            if '.webm' in i:
                print(path + "/"+ subpath + "/" +i)     # 完整路径,subpath为name
            if '.' not in i:
                finalpath = os.listdir(path + "/"+ subpath + "/" +i)
                for file in


    webm_path = "record_audio.webm"
    wav_path = "record_audio.wav"
    sampling_rate = 16000
    channel = 1
    webm_to_wav(webm_path, wav_path, sampling_rate, channel)
'''


'''
def rename(dirpath, oldext, newext):
    for roots, dirs, files in os.walk(dirpath):        
        for name in files:
            if name.endswith(oldext):      
                curdir = os.getcwd()            
                os.chdir(roots)             
                os.rename(name, os.path.splitext(name)[0] + newext)                
                os.chdir(curdir)

rename('/Users/black3y/Desktop/1/','.txt','.py')
'''
'''
    该方法能修改任意指定的后缀名
'''
path = r"F:\video"
def filerename(filepath,srctype,destype):
    for path,dirlist,filelist in os.walk(filepath):
        for file in filelist:

            #防止文件名中包含.
            fullist = file.split('.')
            namelist = fullist[0:-1]
            filename = ''
            for i in namelist:
                filename = filename + i + '.'
            # print (filename)

            curndir = os.getcwd()    #获取当前路径
            # print (curndir)

            os.chdir(path)            #设置当前路径为目标目录
            newdir = os.getcwd()    #验证当前目录
            # print (newdir)

            filetype = file.split('.')[-1]    #获取目标文件格式

            if filetype == srctype:    #修改目标目录下指定后缀的文件（包含子目录）
                os.rename(file,filename+destype)

            '''
            if srctype == '*':        #修改目标目录下所有文件后缀（包含子目录）
                os.rename(file,filename+destype)

            if srctype == 'null':    #修改目标目录下所有无后缀文件（包含子目录）
                if len(fullist) == 1:
                    os.rename(file,file+'.'+destype)
            '''
            os.chdir(curndir)    #回到之前的路径

filerename(path ,'webm','mp4')
