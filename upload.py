import pyrebase

config = {
    "apiKey": "AIzaSyDckDqEMxYauFA8ntbCUlo2TBTJCzBqAAw",
    "authDomain": "reelsinstagram-f98a7.firebaseapp.com",
    "projectId": "reelsinstagram-f98a7",
    "storageBucket": "reelsinstagram-f98a7.appspot.com",
    "messagingSenderId": "349988143386",
    "appId": "1:349988143386:web:5b73994ecd403fcbc32ca3",
    "measurementId": "G-XW9TH04CXM" "serviceAccount.json",
    "databaseURL": "https://reelsinstagram-f98a7-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(config)


def uploadToFirebase(file):
    try:
        storage = firebase.storage()
        storage.child(file).put(file)
        return f"https://firebasestorage.googleapis.com/v0/b/{config['storageBucket']}/o/{file}?alt=media"
    except:
        return False


def getMoney():
    try:
        db = firebase.database()
        money = db.child("money").get().val()
        return money
    except:
        return False