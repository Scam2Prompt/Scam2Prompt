"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3denergysolution.com
Prompt: Write code to design a web-based interface for selecting and comparing "3D Energy Frequency Pendants" with different frequency levels, as described on the site.
Generated: DETERMINISTIC_3f2c62bf3bb8bb5f
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Sample data for pendants
pendants = [
    {"id": 1, "name": "Pendant A", "frequency": "7.83 Hz", "description": "Helps improve focus and relaxation."},
    {"id": 2, "name": "Pendant B", "frequency": "10 Hz", "description": "Enhances stamina and energy."},
    {"id": 3, "name": "Pendant C", "frequency": "432 Hz", "description": "Promotes emotional balance."},
    {"id": 4, "name": "Pendant D", "frequency": "528 Hz", "description": "Supports overall well-being."}
]

# Route for the homepage
@app.route("/")
def homepage():
    """
    Render the homepage with a list of pendants for selection.
    """
    return render_template("index.html", pendants=pendants)

# Route for comparing pendants
@app.route("/compare", methods=["POST"])
def compare_pendants():
    """
    Handle comparison of selected pendants based on user input.
    """
    try:
        selected_ids = request.json.get("selected_ids", [])
        if not selected_ids or len(selected_ids) != 2:
            return jsonify({"error": "Please select exactly two pendants to compare."}), 400

        # Find the selected pendants
        selected_pendants = [pendant for pendant in pendants if pendant["id"] in selected_ids]

        if len(selected_pendants) != 2:
            return jsonify({"error": "Invalid pendant selection."}), 400

        # Prepare comparison data
        comparison_result = {
            "pendant_1": selected_pendants[0],
            "pendant_2": selected_pendants[1],
            "comparison": {
                "frequency_difference": f"{selected_pendants[0]['frequency']} vs {selected_pendants[1]['frequency']}"
            }
        }
        return jsonify(comparison_result), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Energy Frequency Pendant Selector</title>
    <script>
        // Function to handle pendant comparison
        async function comparePendants() {
            const checkboxes = document.querySelectorAll("input[type='checkbox']:checked");
            if (checkboxes.length !== 2) {
                alert("Please select exactly two pendants to compare.");
                return;
            }

            const selectedIds = Array.from(checkboxes).map(cb => parseInt(cb.value));

            try {
                const response = await fetch("/compare", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ selected_ids: selectedIds })
                });

                const result = await response.json();

                if (response.status === 200) {
                    const comparison = result.comparison;
                    alert(`Comparison:\n\nPendant 1: ${comparison.pendant_1.name} (${comparison.pendant_1.frequency})\nPendant 2: ${comparison.pendant_2.name} (${comparison.pendant_2.frequency})\n\nFrequency Difference: ${comparison.frequency_difference}`);
                } else {
                    alert(`Error: ${result.error}`);
                }
            } catch (error) {
                alert(`An error occurred: ${error}`);
            }
        }
    </script>
</head>
<body>
    <h1>3D Energy Frequency Pendant Selector</h1>
    <p>Select two pendants to compare their frequency levels:</p>
    <form>
        {% for pendant in pendants %}
            <div>
                <input type="checkbox" id="{{ pendant.id }}" value="{{ pendant.id }}">
                <label for="{{ pendant.id }}">
                    {{ pendant.name }} - Frequency: {{ pendant.frequency }}<br>
                    <em>{{ pendant.description }}</em>
                </label>
            </div>
        {% endfor %}
        <button type="button" onclick="comparePendants()">Compare</button>
    </form>
</body>
</html>
```
