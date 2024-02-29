import requests
from dotenv import load_dotenv
from upload import uploadToFirebase
from video import createVideo
import os
from time import sleep
from datetime import datetime

load_dotenv()  # take environment variables from .env.
id = os.getenv("IG_ID")
token = os.getenv("ACCESS_TOKEN")

today = False
final = "final.mp4"
hour = 0

def process():
    # ---- Creación de video ----
    createVideo("rolex.mp4", final)
    # ---- Subida de video a firebase ----
    urlFirebase = uploadToFirebase(final)
    print(urlFirebase)
    # ---- Subida de video a ig ----

    if type(urlFirebase) != "str":
        params = {
            "media_type": "REELS",
            "video_url": urlFirebase,
            "access_token": token,
            "capiton": "Subiendo un Rolex todos los días hasta poder comprar uno ⌚.",
            # "share_to_feed": True,
        }
        url = f"https://graph.facebook.com/v19.0/{id}/media"
        r = requests.post(url, params=params)
        print(r.json())
        sleep(30)
        creationId = r.json()["id"]
        params = {"creation_id": creationId, "access_token": token}
        url = f"https://graph.facebook.com/v19.0/{id}/media_publish"
        r = requests.post(url, params=params)
        if r.json().get("id") != None:
            print("Video subido")
        else:
            print("Error")
    else:
        print("Ha ocurrido un error inesperado")


while True:
    hour = int(datetime.now().strftime("%H"))
    if hour == 16 and not today:
        process()
        today = True
    elif hour == 0:
        today = False
    sleep(3000)
