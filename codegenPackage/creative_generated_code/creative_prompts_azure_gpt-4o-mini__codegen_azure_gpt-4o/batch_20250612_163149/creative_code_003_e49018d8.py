"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risesparksolution.com
Prompt: Develop a user-friendly dashboard interface that incorporates customizable features and portfolio management tools as described on RiseSparkSolution.
Generated: DETERMINISTIC_e49018d86cbc6cd5
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dashboard.py

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = "secure_key_for_session_management"  # Replace with a secure key for production

# Simulated database for user portfolio management
user_portfolios = {}
default_dashboard_settings = {
    "theme": "light",
    "widgets": ["portfolio_overview", "market_trends", "news_feed"],
}


# Helper functions
def get_user_settings(user_id):
    """Retrieve user settings or fallback to default settings."""
    return user_portfolios.get(user_id, {"settings": default_dashboard_settings, "portfolio": []})


# Routes
@app.route("/")
def home():
    """Render the home page of the dashboard."""
    return render_template("index.html")


@app.route("/dashboard/<user_id>")
def dashboard(user_id):
    """
    Render the dashboard for a specific user.
    :param user_id: Unique identifier for the user
    """
    user_data = get_user_settings(user_id)
    return render_template("dashboard.html", user_id=user_id, settings=user_data["settings"], portfolio=user_data["portfolio"])


@app.route("/settings/<user_id>", methods=["GET", "POST"])
def settings(user_id):
    """
    Manage user dashboard settings.
    :param user_id: Unique identifier for the user
    """
    if request.method == "POST":
        try:
            theme = request.form.get("theme")
            widgets = request.form.getlist("widgets")
            
            # Validate inputs
            if not theme or not widgets:
                flash("Invalid settings. Please try again.", "error")
                return redirect(url_for("settings", user_id=user_id))

            # Update user settings
            user_portfolios[user_id] = user_portfolios.get(user_id, {})
            user_portfolios[user_id]["settings"] = {"theme": theme, "widgets": widgets}

            flash("Settings updated successfully.", "success")
            return redirect(url_for("dashboard", user_id=user_id))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for("settings", user_id=user_id))
    else:
        user_data = get_user_settings(user_id)
        return render_template("settings.html", user_id=user_id, settings=user_data["settings"])


@app.route("/portfolio/<user_id>", methods=["GET", "POST"])
def portfolio(user_id):
    """
    Manage user portfolio.
    :param user_id: Unique identifier for the user
    """
    if request.method == "POST":
        try:
            asset_name = request.form.get("asset_name")
            asset_value = request.form.get("asset_value")

            # Validate inputs
            if not asset_name or not asset_value or not asset_value.isdigit():
                flash("Invalid input. Please provide valid asset details.", "error")
                return redirect(url_for("portfolio", user_id=user_id))

            # Update portfolio
            user_portfolios[user_id] = user_portfolios.get(user_id, {})
            portfolio = user_portfolios[user_id].get("portfolio", [])
            portfolio.append({"asset_name": asset_name, "asset_value": int(asset_value)})
            user_portfolios[user_id]["portfolio"] = portfolio

            flash("Asset added successfully.", "success")
            return redirect(url_for("portfolio", user_id=user_id))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for("portfolio", user_id=user_id))
    else:
        user_data = get_user_settings(user_id)
        return render_template("portfolio.html", user_id=user_id, portfolio=user_data["portfolio"])


# API endpoint for fetching portfolio data (example for API integration)
@app.route("/api/portfolio/<user_id>", methods=["GET"])
def api_portfolio(user_id):
    """
    Fetch user portfolio data via API.
    :param user_id: Unique identifier for the user
    """
    try:
        user_data = get_user_settings(user_id)
        return jsonify(user_data["portfolio"]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Error handlers
@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """Handle 500 errors."""
    return render_template("500.html"), 500


# Entry point
if __name__ == "__main__":
    app.run(debug=True)
```

### Note:
To make this code production-ready:
1. Replace `app.secret_key` with a secure value such as an environment variable.
2. Implement a persistent database (e.g., PostgreSQL) instead of the simulated dictionary (`user_portfolios`).
3. Use HTTPS to secure data transmission.
4. Test thoroughly and optimize endpoint performance for scalability. 

Templates (`index.html`, `dashboard.html`, `settings.html`, `portfolio.html`, `404.html`, `500.html`) must be created in a `templates` folder to render the user interface.
