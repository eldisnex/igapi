from upload import getMoney
import ffmpeg
import os


def createVideo(videoIn, videoOut):
    w = 1080
    text = f"{getMoney()}/11.000"

    if os.path.exists(videoOut):
        os.remove(videoOut)

    ffmpeg.input(videoIn).output(
        videoOut, vf=f"drawtext=text='{text}':x={w/3}:y=300:fontsize=80:fontcolor=white"
    ).run()
    return True
