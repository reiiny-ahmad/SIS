import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

# Configuration Pyrebase
firebase_config = {
    "apiKey": "AIzaSyBkt3AmdkaKfiM5SUFrKeQLUwosJq-Xupo",
    "authDomain": "steps-into-space.firebaseapp.com",
    "databaseURL": "https://steps-into-space.firebaseio.com",
    "projectId": "steps-into-space",
    "storageBucket": "steps-into-space.appspot.com",
    "messagingSenderId": "554363529046",
    "appId": "1:554363529046:web:a3f6e550c44746d20498f7"
}

# Initialisation Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialisation Admin SDK (pour Firestore uniquement)
cred = credentials.Certificate("steps-into-space-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # Ceci rend 'db' disponible pour l'importation
