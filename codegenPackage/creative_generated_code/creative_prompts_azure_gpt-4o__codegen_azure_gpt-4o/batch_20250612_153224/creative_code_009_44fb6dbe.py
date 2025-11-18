"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdiscount.pages.dev
Prompt: Develop a dashboard for businesses to track their profits and manage discount offers, inspired by the features described on the "claimdiscount.pages.dev" website.
Generated: DETERMINISTIC_44fb6dbe69687e2d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the code implementing a simple dashboard for businesses to track profits and manage discount offers. The code is built using Python with Flask for the backend and a basic HTML/JavaScript frontend.

### `app.py` (Backend)
```python
from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Mock data for demonstration purposes
business_data = {
    "profits": [],
    "discounts": []
}

@app.route("/")
def dashboard():
    """
    Render the main dashboard page.
    """
    return render_template("dashboard.html", data=business_data)


@app.route("/add-profit", methods=["POST"])
def add_profit():
    """
    Endpoint to add a profit entry.
    """
    try:
        profit_data = request.json
        amount = float(profit_data.get("amount", 0))

        # Validate input
        if amount <= 0:
            return jsonify({"error": "Profit amount must be greater than zero"}), 400

        business_data["profits"].append(amount)
        logging.info(f"Added profit: {amount}")
        return jsonify({"message": "Profit added successfully", "profits": business_data["profits"]}), 200
    except Exception as e:
        logging.error(f"Error in adding profit: {str(e)}")
        return jsonify({"error": "An error occurred while adding profit"}), 500


@app.route("/add-discount", methods=["POST"])
def add_discount():
    """
    Endpoint to add a discount offer.
    """
    try:
        discount_data = request.json
        title = discount_data.get("title", "").strip()
        discount_percentage = int(discount_data.get("percentage", 0))

        # Validate input
        if not title or discount_percentage <= 0 or discount_percentage > 100:
            return jsonify({"error": "Invalid discount data"}), 400

        business_data["discounts"].append({
            "title": title,
            "percentage": discount_percentage
        })
        logging.info(f"Added discount: {title}, {discount_percentage}%")
        return jsonify({"message": "Discount offer added successfully", "discounts": business_data["discounts"]}), 200
    except Exception as e:
        logging.error(f"Error in adding discount: {str(e)}")
        return jsonify({"error": "An error occurred while adding discount"}), 500


if __name__ == "__main__":
    # Running the application
    app.run(debug=True)
```

### `templates/dashboard.html` (Frontend)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Business Dashboard</h1>

        <!-- Profit Management Section -->
        <section>
            <h2>Track Profits</h2>
            <form id="profit-form">
                <div class="form-group">
                    <label for="profit-amount">Profit Amount ($):</label>
                    <input type="number" id="profit-amount" name="amount" required>
                </div>
                <button type="submit">Add Profit</button>
            </form>
            <h3>Profit History</h3>
            <table id="profits-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Amount ($)</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Dynamic rows will be added here -->
                </tbody>
            </table>
        </section>

        <!-- Discount Management Section -->
        <section>
            <h2>Manage Discount Offers</h2>
            <form id="discount-form">
                <div class="form-group">
                    <label for="discount-title">Discount Title:</label>
                    <input type="text" id="discount-title" name="title" required>
                </div>
                <div class="form-group">
                    <label for="discount-percentage">Discount Percentage (%):</label>
                    <input type="number" id="discount-percentage" name="percentage" required>
                </div>
                <button type="submit">Add Discount</button>
            </form>
            <h3>Discount Offers</h3>
            <table id="discounts-table">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Title</th>
                        <th>Percentage (%)</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Dynamic rows will be added here -->
                </tbody>
            </table>
        </section>
    </div>

    <script>
        // Populate tables dynamically
        function updateTables(data) {
            const profitsTable = document.querySelector("#profits-table tbody");
            const discountsTable = document.querySelector("#discounts-table tbody");

            // Clear existing rows
            profitsTable.innerHTML = "";
            discountsTable.innerHTML = "";

            // Populate profits
            data.profits.forEach((profit, index) => {
                const row = `<tr>
                    <td>${index + 1}</td>
                    <td>${profit.toFixed(2)}</td>
                </tr>`;
                profitsTable.innerHTML += row;
            });

            // Populate discounts
            data.discounts.forEach((discount, index) => {
                const row = `<tr>
                    <td>${index + 1}</td>
                    <td>${discount.title}</td>
                    <td>${discount.percentage}%</td>
                </tr>`;
                discountsTable.innerHTML += row;
            });
        }

        // Handle profit form submission
        document.getElementById("profit-form").addEventListener("submit", async (e) => {
            e.preventDefault();
            const amount = document.getElementById("profit-amount").value;

            const response = await fetch("/add-profit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ amount: amount })
            });
            const data = await response.json();
            if (response.ok) {
                updateTables(data);
            } else {
                alert(data.error || "Failed to add profit.");
            }
        });

        // Handle discount form submission
        document.getElementById("discount-form").addEventListener("submit", async (e) => {
            e.preventDefault();
            const title = document.getElementById("discount-title").value;
            const percentage = document.getElementById("discount-percentage").value;

            const response = await fetch("/add-discount", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title: title, percentage: percentage })
            });
            const data = await response.json();
            if (response.ok) {
                updateTables(data);
            } else {
                alert(data.error || "Failed to add discount.");
            }
        });

        // Initial fetch to populate tables
        async function fetchData() {
            const response = await fetch("/");
            const text = await response.text();
            const parser = new DOMParser();
            const htmlDoc = parser.parseFromString(text, "text/html");

            const scripts = htmlDoc.querySelectorAll("script");
            scripts.forEach(s => eval(s.textContent));
        }
        document.addEventListener('DOMContent-loaded ,`script starts tracking init`).
