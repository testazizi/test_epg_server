'''
iframe.py - ffmpeg i-frame extraction
'''

import sys, getopt, os
import subprocess
from pathlib import Path
import glob
import time
import os.path
#from moviepy.editor import VideoFileClip

segment = str(sys.argv[1])

if os.path.isfile("2m_hls/"+segment) and ".ts" in segment:

    print("segment => "+segment)
    # clip = VideoFileClip("2m_hls/"+segment)
    # duration = int(clip.duration)
    duration = 6
    ts = time.time()
    ts = "."+str(ts).split('.')[0]
    now = str(segment).split('.')[0]

    home = os.path.expanduser("~")
    ffmpeg = 'ffmpeg'
    cwd = os.getcwd()

    # video = 25 frame par second

    cmd = "ffmpeg -y -i 2m_hls/"+segment+" -vf 'select=gt(scene\,0.10)' -vsync vfr -frame_pts true iframes_live/"+now+str(ts)+"_%d_"+str(duration)+".png"
    # cmd = "ffmpeg -y -i 2m_hls/"+segment+" -vf \"select='eq(pict_type,PICT_TYPE_I)'\" -vsync vfr -frame_pts true iframes_live/"+now+str(ts)+"_%d_"+str(duration)+".png"
    print(cmd)
    # python3 iframe_scanner.py $file
    os.system(cmd)
    # os.system("rm 2m_hls/"+segment)
    #
    # print("python3 iframe_scanner2.py "+now+"_dfsd")
    # os.system("python3 iframe_scanner2.py "+now+"_sdfsd > /dev/null 2>&1 & ")
