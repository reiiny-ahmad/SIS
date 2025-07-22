import pyrebase

firebase_config = {
    "apiKey": "AIzaSyBkt3AmdkaKfiM5SUFrKeQLUwosJq-Xupo",
    "authDomain": "steps-into-space.firebaseapp.com",
    "databaseURL": "https://steps-into-space.firebaseio.com",
    "projectId": "steps-into-space",
    "storageBucket": "steps-into-space.appspot.com",
    "messagingSenderId": "554363529046",
    "appId": "1:554363529046:web:a3f6e550c44746d20498f7"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
