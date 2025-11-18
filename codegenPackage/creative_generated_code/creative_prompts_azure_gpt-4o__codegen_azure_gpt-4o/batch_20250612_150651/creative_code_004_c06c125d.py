"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Write JavaScript code to create a dynamic webpage that compares the features of different music equipment based on user input.
Generated: DETERMINISTIC_c06c125dfb48eedd
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create a dynamic webpage to compare music equipment features based on user input

// HTML structure for the dynamic webpage
const htmlContent = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Equipment Feature Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #equipment-form {
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Music Equipment Feature Comparison</h1>
    <form id="equipment-form">
        <label for="equipment1">Enter Equipment 1:</label>
        <input type="text" id="equipment1" required>
        <label for="equipment2">Enter Equipment 2:</label>
        <input type="text" id="equipment2" required>
        <button type="submit">Compare</button>
    </form>
    <div id="comparison-result"></div>
    <script src="app.js"></script>
</body>
</html>
`;

// Write the HTML content into the webpage
document.write(htmlContent);

// JavaScript functionality for the dynamic comparison
document.addEventListener("DOMContentLoaded", () => {
    const equipmentForm = document.getElementById("equipment-form");
    const comparisonResult = document.getElementById("comparison-result");

    // Mock data for equipment features
    const equipmentData = {
        "Guitar": { Brand: "Fender", Type: "Electric", Price: "$1200" },
        "Drum Kit": { Brand: "Yamaha", Type: "Acoustic", Price: "$800" },
        "Keyboard": { Brand: "Casio", Type: "Digital", Price: "$500" },
        "Microphone": { Brand: "Shure", Type: "Dynamic", Price: "$200" }
    };

    // Event listener for form submission
    equipmentForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent default form submission

        // Get user input
        const equipment1 = document.getElementById("equipment1").value.trim();
        const equipment2 = document.getElementById("equipment2").value.trim();

        // Validate input
        if (!equipmentData[equipment1] || !equipmentData[equipment2]) {
            alert("Please enter valid equipment names to compare (e.g., Guitar, Drum Kit, Keyboard, Microphone).");
            return;
        }

        // Generate comparison table
        let comparisonTable = `<table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>${equipment1}</th>
                    <th>${equipment2}</th>
                </tr>
            </thead>
            <tbody>`;

        const features1 = equipmentData[equipment1];
        const features2 = equipmentData[equipment2];

        Object.keys(features1).forEach((feature) => {
            comparisonTable += `
                <tr>
                    <td>${feature}</td>
                    <td>${features1[feature]}</td>
                    <td>${features2[feature]}</td>
                </tr>
            `;
        });

        comparisonTable += `</tbody></table>`;

        // Display the comparison result
        comparisonResult.innerHTML = comparisonTable;
    });
});
```
