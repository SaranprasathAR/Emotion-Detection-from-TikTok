import moviepy.editor as mp
video_clip = mp.VideoFileClip("/content/siya_kakkar-6830670901227441410.mp4") #change path
video_clip.audio.write_audiofile(r"audio_file.mp3")