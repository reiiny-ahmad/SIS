import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Configuration Pyrebase
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID")
}

# Initialisation Pyrebase
firebase = pyrebase.initialize_app(firebase_config)
auth_pyrebase = firebase.auth()  # Renommé pour éviter conflit

# Initialisation Admin SDK
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token"
})
firebase_admin.initialize_app(cred)
db = firestore.client()
