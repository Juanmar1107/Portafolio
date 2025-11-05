# Import
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    button_discord = False
    button_python = False
    button_html = False
    button_db = False  
    if request.method == "POST":
        # Verifica si es un comentario
        email = request.form.get("email")
        text = request.form.get("text")
        
        if email and text:
            with open("comentarios.txt", "a", encoding="utf-8") as f:
                f.write(f"Email: {email}\nComentario: {text}\n{'-'*40}\n")
    # ...otros botones si los necesitas...
    if request.method == "POST":
        if "button_discord" in request.form:
            button_discord = True
        if "button_python" in request.form:
            button_python = True
        if "button_html" in request.form:
            button_html = True
        if "button_db" in request.form:
            button_db = True
        # ...otros botones...
    return render_template(
        "index.html",
        button_discord=button_discord,
        button_python=button_python,
        button_html=button_html,
        button_db=button_db,
        # ...otros botones...
    )
if __name__ == "__main__":
    app.run(debug=True)