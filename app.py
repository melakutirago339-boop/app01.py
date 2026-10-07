
```python
from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "hospital-system-secret-key"
)


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Demo admin account
        if username == "admin" and password == "admin123":
            session["username"] = username
            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hospital Management System</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
            }}

            .header {{
                background: #1769aa;
                color: white;
                padding: 25px;
                text-align: center;
            }}

            .container {{
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}

            .menu {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 15px;
                margin-top: 20px;
            }}

            .menu-item {{
                background: #eaf3fb;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
            }}

            .button {{
                display: inline-block;
                padding: 12px 20px;
                background: #1769aa;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                margin-top: 20px;
            }}

            .logout {{
                background: #d32f2f;
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Hospital Management System</h1>
            <p>Admin Dashboard</p>
        </div>

        <div class="container">
            <div class="card">

                <h2>Welcome, {session["username"]}!</h2>

                <p>You have successfully logged in.</p>

                <div class="menu">
                    <div class="menu-item">
                        <h3>👤 Patient Registration</h3>
                    </div>

                    <div class="menu-item">
                        <h3>📋 Patient Records</h3>
                    </div>

                    <div class="menu-item">
                        <h3>👨‍⚕️ Doctors</h3>
                    </div>

                    <div class="menu-item">
                        <h3>📅 Appointments</h3>
                    </div>

                    <div class="menu-item">
                        <h3>📊 Reports</h3>
                    </div>
                </div>

                <a class="button logout" href="/logout">
                    Logout
                </a>

            </div>
        </div>

    </body>
    </html>
    """


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
