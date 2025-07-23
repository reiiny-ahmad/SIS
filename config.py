# config.py
import os
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase
from dotenv import load_dotenv

load_dotenv()  # Pour le développement local

# Configuration Pyrebase
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "steps-into-space.firebaseapp.com",
    "projectId": "steps-into-space",
    "storageBucket": "steps-into-space.appspot.com",
    "messagingSenderId": "554363529046",
    "appId": "1:554363529046:web:a3f6e550c44746d20498f7",
    "databaseURL": "https://steps-into-space.firebaseio.com"  # Add this line
}

# Initialisation Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Configuration Admin SDK à partir des variables d'environnement
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "steps-into-space",
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": "firebase-adminsdk-fbsvc@steps-into-space.iam.gserviceaccount.com",
    "token_uri": "https://oauth2.googleapis.com/token"
})

firebase_admin.initialize_app(cred)
db = firestore.client()
