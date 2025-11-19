"""
Generated Code Metadata:
========================
Original URL: https://semillasplantae.com
Prompt: Design a small web application using Flask that allows users to browse and filter the unique seed varieties offered by Semillas Plantae, focusing on their organic and local products.
Generated: DETERMINISTIC_0922d63fe6cdb627
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///seed_varieties.db"
db = SQLAlchemy(app)


# Define the SeedVariety model
class SeedVariety(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_organic = db.Column(db.Boolean, default=False)
    is_local = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"SeedVariety('{self.name}', '{self.is_organic}', '{self.is_local}')"


# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Seed the database with some initial data
@app.before_first_request
def seed_database():
    if not SeedVariety.query.all():
        seed_varieties = [
            SeedVariety(name="Tomato - Organic", is_organic=True, is_local=True),
            SeedVariety(name="Carrot - Local", is_organic=False, is_local=True),
            SeedVariety(name="Lettuce - Organic & Local", is_organic=True, is_local=True),
            SeedVariety(name="Pepper - Non-Organic", is_organic=False, is_local=False),
        ]
        db.session.add_all(seed_varieties)
        db.session.commit()


# Route to get all seed varieties
@app.route("/seed_varieties", methods=["GET"])
def get_seed_varieties():
    try:
        seed_varieties = SeedVariety.query.all()
        output = []
        for variety in seed_varieties:
            variety_data = {
                "id": variety.id,
                "name": variety.name,
                "is_organic": variety.is_organic,
                "is_local": variety.is_local,
            }
            output.append(variety_data)
        return jsonify({"seed_varieties": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to filter seed varieties
@app.route("/seed_varieties/filter", methods=["POST"])
def filter_seed_varieties():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        query = SeedVariety.query

        if "is_organic" in data and data["is_organic"] is not None:
            query = query.filter_by(is_organic=data["is_organic"])

        if "is_local" in data and data["is_local"] is not None:
            query = query.filter_by(is_local=data["is_local"])

        if "name" in data and data["name"]:
            query = query.filter(SeedVariety.name.like(f"%{data['name']}%"))

        seed_varieties = query.all()
        output = []
        for variety in seed_varieties:
            variety_data = {
                "id": variety.id,
                "name": variety.name,
                "is_organic": variety.is_organic,
                "is_local": variety.is_local,
            }
            output.append(variety_data)
        return jsonify({"seed_varieties": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to render the main page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seed Varieties</title>
</head>
<body>
    <h1>Seed Varieties</h1>
    <form id="filter-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="is_organic">Is Organic:</label>
        <input type="checkbox" id="is_organic" name="is_organic"><br><br>
        <label for="is_local">Is Local:</label>
        <input type="checkbox" id="is_local" name="is_local"><br><br>
        <input type="submit" value="Filter">
    </form>
    <div id="seed-varieties"></div>

    <script>
        const form = document.getElementById('filter-form');
        const seedVarietiesDiv = document.getElementById('seed-varieties');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const data = {
                name: formData.get('name'),
                is_organic: formData.get('is_organic') === 'on',
                is_local: formData.get('is_local') === 'on',
            };

            try {
                const response = await fetch('/seed_varieties/filter', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });
                const result = await response.json();
                if (result.seed_varieties) {
                    const seedVarietiesHtml = result.seed_varieties.map((variety) => {
                        return `
                            <p>
                                ${variety.name} -
                                ${variety.is_organic ? 'Organic' : 'Non-Organic'} -
                                ${variety.is_local ? 'Local' : 'Non-Local'}
                            </p>
                        `;
                    }).join('');
                    seedVarietiesDiv.innerHTML = seedVarietiesHtml;
                } else {
                    seedVarietiesDiv.innerHTML = '<p>No seed varieties found.</p>';
                }
            } catch (error) {
                console.error(error);
            }
        });

        // Get all seed varieties on page load
        fetch('/seed_varieties')
            .then(response => response.json())
            .then(result => {
                const seedVarietiesHtml = result.seed_varieties.map((variety) => {
                    return `
                        <p>
                            ${variety.name} -
                            ${variety.is_organic ? 'Organic' : 'Non-Organic'} -
                            ${variety.is_local ? 'Local' : 'Non-Local'}
                        </p>
                    `;
                }).join('');
                seedVarietiesDiv.innerHTML = seedVarietiesHtml;
            })
            .catch(error => console.error(error));
    </script>
</body>
</html>
```
