import firebase_admin
from firebase_admin import credentials, firestore, auth as firebase_auth
import pyrebase


# Configuration pour Pyrebase (authentification uniquement)
firebase_config = {
    "apiKey": "AIzaSyBkt3AmdkaKfiM5SUFrKeQLUwosJq-Xupo",
    "authDomain": "steps-into-space.firebaseapp.com",
    "databaseURL": "https://steps-into-space.firebaseio.com",  # <-- Ajoute cette ligne
    "projectId": "steps-into-space",
    "storageBucket": "steps-into-space.appspot.com",  # <-- Corrige ici (ajoute .com)
    "messagingSenderId": "554363529046",
    "appId": "1:554363529046:web:a3f6e550c44746d20498f7"
}

# Initialiser Pyrebase pour l'authentification
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Initialiser Firebase Admin pour Firestore
cred = credentials.Certificate("steps-into-space-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'projectId': 'steps-into-space',
})
db = firestore.client()