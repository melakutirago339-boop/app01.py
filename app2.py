```python
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "hospital-system-secret-key"


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

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
        <title>Hospital System Dashboard</title>
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
                padding: 20px;
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

            .button {{
                display: inline-block;
                padding: 12px 20px;
                background: #1769aa;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                margin-top: 15px;
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

                <h3>System Menu</h3>

                <ul>
                    <li>Patient Registration</li>
                    <li>Patient Records</li>
                    <li>Doctors</li>
                    <li>Appointments</li>
                    <li>Reports</li>
                </ul>

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
    app.run(host="0.0.0.0", port=5000)
```
