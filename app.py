from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import auth, db
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Page de connexion
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["username"]
        password = request.form["password"]
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session["user"] = user['localId']  # Stocker l'UID de l'utilisateur
            return redirect(url_for("home"))
        except Exception as e:
            flash(f"Identifiants incorrects: {str(e)}")
            return redirect(url_for("login"))
    return render_template("login.html")

# Page d'accueil avec tableau des membres
@app.route("/home", methods=["GET", "POST"])
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    
    # Récupérer tous les membres
    members_ref = db.collection("members")
    members = members_ref.stream()
    members_list = [{"id": doc.id, **doc.to_dict()} for doc in members]
    
    # Récupérer les paramètres de filtre
    year = request.args.get("year", "").strip()
    month = request.args.get("month", "").strip()
    city = request.args.get("city", "").strip().lower()
    print(f"Filters: year={year}, month={month}, city={city}")  # Debug
    
    # Appliquer les filtres
    filtered_members = members_list.copy()
    
    if year:
        try:
            filtered_members = [m for m in filtered_members if datetime.fromisoformat(m.get("join_date", "")).year == int(year)]
        except (ValueError, TypeError):
            flash("Année invalide. Utilisez un format numérique (ex: 2025).")
    
    if month:
        try:
            filtered_members = [m for m in filtered_members if datetime.fromisoformat(m.get("join_date", "")).month == int(month)]
        except (ValueError, TypeError):
            flash("Mois invalide. Utilisez un numéro de 1 à 12.")
    
    if city:
        filtered_members = [m for m in filtered_members if city in m.get("city", "").lower()]
    
    if not filtered_members and (year or month or city):
        flash("Aucun membre trouvé avec les filtres appliqués.")
    
    print(f"Filtered members count: {len(filtered_members)}")  # Debug
    return render_template("home.html", members=filtered_members, year=year, month=month, city=city)

# Ajouter un membre
@app.route("/add_member", methods=["POST"])
def add_member():
    if "user" not in session:
        return redirect(url_for("login"))
    
    data = {
        "full_name": request.form["full_name"],
        "birth_date": request.form["birth_date"],
        "city": request.form["city"],
        "join_date": request.form["join_date"],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    db.collection("members").add(data)
    flash("Membre ajouté avec succès")
    return redirect(url_for("home"))

# Modifier un membre
@app.route("/update_member/<id>", methods=["POST"])
def update_member(id):
    if "user" not in session:
        return redirect(url_for("login"))
    
    data = {
        "full_name": request.form["full_name"],
        "birth_date": request.form["birth_date"],
        "city": request.form["city"],
        "join_date": request.form["join_date"],
        "updated_at": datetime.now().isoformat()
    }
    db.collection("members").document(id).set(data, merge=True)  # Utilise merge pour ne pas écraser created_at
    flash("Membre modifié avec succès")
    return redirect(url_for("home"))

# Supprimer un membre
@app.route("/delete_member/<id>")
def delete_member(id):
    if "user" not in session:
        return redirect(url_for("login"))
    
    db.collection("members").document(id).delete()
    flash("Membre supprimé avec succès")
    return redirect(url_for("home"))

# Déconnexion
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)