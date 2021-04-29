from moviepy.editor import VideoFileClip, AudioFileClip         # 利用moviepy库对音频视频文件进行操作


def Video2mp3(video_path, audio_out_path):                      # 提取原视频中的音频
    video = VideoFileClip(video_path)                           # 读取视频
    audio = video.audio.subclip(0, 20)                          # 提取视频中的音频，因为视频只有20s，所以只提取前20s的音频
    audio.write_audiofile(audio_out_path)                       # 输出纯音频文件


def Video_add_Audio(video_path, audio_path, final_out_path):    # 给视频添加音频
    video = VideoFileClip(video_path)                           # 读取视频
    audio = AudioFileClip(audio_path)                           # 读取纯音频
    video_out = video.set_audio(audio)                          # 给视频添加音频
    video_out.write_videofile(final_out_path)                   # 输出最终视频


Video2mp3("Elysion.mp4", "audio/Elysion.mp3")
Video_add_Audio("out.mp4", "audio/Elysion.mp3", "final_out.mp4")