from moviepy.editor import *

video = VideoFileClip('#.mp4')

video = video.subclip(0,17)

audio = AudioFileClip('title0.wav')
audiocom = AudioFileClip('response00.wav')
audio2 = AudioFileClip('title1.wav')
audiocom2 = AudioFileClip('response10.wav')
finaudio = concatenate_audioclips([audio,audiocom,audio2,audiocom2])

video.audio = finaudio

video.write_videofile("Test2.mp4")
