import firebase_admin
from firebase_admin import credentials, firestore

# Configuration Firebase Admin uniquement
cred = credentials.Certificate("steps-into-space-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
