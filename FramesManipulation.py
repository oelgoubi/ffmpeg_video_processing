
# Import core package to run processes
import subprocess


# Get all the Codecs
def get_codecs():
    cmd = "ffmpeg -codecs"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)


# Get All the Formats available in ffmpeg (mp4...)
def get_formats():
    cmd = "ffmpeg -formats"
    x = subprocess.check_output(cmd, shell=True)
    x = x.split(b'\n')
    for e in x:
        print(e)

# Convert sequence of images in images folder to Video with the .mp4 format
def convert_seq_to_vid():
    input = r"C:\Users\Othmane\myDevProjects\python_tuto\Frames_wrapper\images\tiger_scene_v001.%03d.png"
    output = r"C:\Users\Othmane\myDevProjects\python_tuto\Frames_wrapper\output.mp4"
    frame_rate = 30        # by default FPS=25
    cmd = f'ffmpeg -framerate {frame_rate} -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)   # run the command



# Convert Video to Sequences
def convert_vid_to_seq():
    # Add the absolute Path
    input = r"C:\Users\Othmane\myDevProjects\python_tuto\Frames_wrapper\motivational_video.mp4"
    output = r"C:\Users\Othmane\myDevProjects\python_tuto\Frames_wrapper\images\tiger_scene_v001.%03d.png"

    cmd = f'ffmpeg  -i "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)


# Grab one Image from the Video and use it as a Preview for example
def get_thumbnail():
    input = r"C:\Users\HP\Desktop\FFMPEG\comp.mov"
    output = r"C:\Users\HP\Desktop\FFMPEG\thumb.png"
    cmd = f'ffmpeg -i "{input}" -ss 00:00:01.000 -vframes 1  -s 640x360  "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell=True)


# Calling the function
convert_seq_to_vid()





""" 
    Recommandations :
    
       install ffmpeg from the offical website 
       and Add the bin folder to the variable Path of the environment Variables 

    Useful Ressoureces :

    https://stackoverflow.com/questions/5585872/python-image-frames-to-video

    https://stackoverflow.com/questions/4580576/python-library-for-splitting-video

 """