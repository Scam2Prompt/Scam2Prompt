"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gadgetexa.com
Prompt: Generate code in JavaScript to create a web-based calculator that helps users choose the best laminator for stickers, using Gadgetexa's budget and feature recommendations.
Generated: DETERMINISTIC_a7ada7091aa8b386
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laminator Selector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 600px;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #4CAF50;
            border-radius: 5px;
            display: none;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

    <h1>Laminator Selector for Stickers</h1>
    <form id="calculator">
        <label for="budget">Enter your budget ($):</label>
        <input type="number" id="budget" min="0" required><br><br>

        <label for="features">Select features (check all that apply):</label><br>
        <input type="checkbox" id="thermal" value="thermal"> Thermal<br>
        <input type="checkbox" id="cold" value="cold"> Cold<br>
        <input type="checkbox" id="wideFormat" value="wide"> Wide Format<br>
        <input type="checkbox" id="compact" value="compact"> Compact<br><br>

        <button type="submit">Find My Laminator</button>
    </form>

    <div class="result" id="result"></div>
    <div class="error" id="error"></div>

    <script>
        // Sample data of laminators
        const laminators = [
            { name: "Laminator A", price: 50, features: ["thermal", "compact"] },
            { name: "Laminator B", price: 100, features: ["cold", "wide"] },
            { name: "Laminator C", price: 75, features: ["thermal", "wide", "compact"] },
            { name: "Laminator D", price: 30, features: ["cold"] },
            { name: "Laminator E", price: 150, features: ["thermal", "wide", "compact"] },
        ];

        // Function to handle form submission
        document.getElementById("calculator").addEventListener("submit", function(event) {
            event.preventDefault();
            const budget = parseFloat(document.getElementById("budget").value);
            const selectedFeatures = Array.from(document.querySelectorAll('input[type="checkbox"]:checked')).map(cb => cb.value);
            const resultDiv = document.getElementById("result");
            const errorDiv = document.getElementById("error");

            // Clear previous results and errors
            resultDiv.innerHTML = '';
            errorDiv.innerHTML = '';

            // Validate the budget
            if (isNaN(budget) || budget <= 0) {
                errorDiv.innerHTML = "Please enter a valid budget.";
                return;
            }

            // Filter laminators based on budget and selected features
            const suitableLaminators = laminators.filter(laminator => 
                laminator.price <= budget && 
                selectedFeatures.every(feature => laminator.features.includes(feature))
            );

            // Display results
            if (suitableLaminators.length > 0) {
                suitableLaminators.forEach(laminator => {
                    const div = document.createElement("div");
                    div.innerHTML = `${laminator.name} - $${laminator.price}`;
                    resultDiv.appendChild(div);
                });
                resultDiv.style.display = "block";
            } else {
                errorDiv.innerHTML = "No laminators match your criteria.";
            }
        });
    </script>
    
</body>
</html>
```
