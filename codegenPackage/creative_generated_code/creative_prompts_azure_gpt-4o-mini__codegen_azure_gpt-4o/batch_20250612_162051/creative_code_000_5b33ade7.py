"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Generate a code snippet for an e-commerce website that includes features for user login, product display, and a shopping cart, similar to the functionalities described on the Mambo Wood site.
Generated: DETERMINISTIC_5b33ade72507dcdd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce.py

from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
app.permanent_session_lifetime = timedelta(days=5)

# Mock database (replace with proper database integrations in production)
users_db = {}  # {username: hashed_password}
products_db = [
    {"id": 1, "name": "Wooden Chair", "price": 75.00},
    {"id": 2, "name": "Wooden Table", "price": 150.00},
    {"id": 3, "name": "Wooden Shelf", "price": 120.00},
]

@app.route("/")
def home():
    """Render the homepage."""
    return render_template("home.html", products=products_db)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in users_db and check_password_hash(users_db[username], password):
            session.permanent = True
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    """Handle user logout."""
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in users_db:
            flash("Username already exists. Please choose another.", "error")
            return redirect(url_for("register"))
        
        hashed_password = generate_password_hash(password, method="sha256")
        users_db[username] = hashed_password
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/cart", methods=["GET", "POST"])
def cart():
    """Handle shopping cart."""
    if "cart" not in session:
        session["cart"] = []  # Initialize an empty cart
    
    if request.method == "POST":
        product_id = int(request.form["product_id"])
        product = next((p for p in products_db if p["id"] == product_id), None)
        
        if product:
            session["cart"].append(product)
            flash(f"{product['name']} added to cart!", "success")
        else:
            flash("Product not found.", "error")
    
    return render_template("cart.html", cart=session["cart"])

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    """Remove an item from the cart."""
    product_id = int(request.form["product_id"])
    session["cart"] = [p for p in session["cart"] if p["id"] != product_id]
    flash("Item removed from cart.", "info")
    return redirect(url_for("cart"))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template("404.html"), 404

if __name__ == "__main__":
    # To run in production, use a production server (e.g., Gunicorn or uWSGI)
    app.run(debug=True)
```

### Note:
- HTML templates (`home.html`, `login.html`, `register.html`, `cart.html`, `404.html`) are required for rendering views. Ensure they are properly created and styled according to your requirements.
- Replace the mock database with a real database (e.g., MySQL, PostgreSQL) in production environments.
- Use environment variables for sensitive values (e.g., secret keys).
