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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Equipment Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

    <h1>Music Equipment Comparison Tool</h1>
    
    <div>
        <label for="equipment1">Enter Equipment 1:</label>
        <input type="text" id="equipment1" placeholder="e.g., Guitar">
        
        <label for="equipment2">Enter Equipment 2:</label>
        <input type="text" id="equipment2" placeholder="e.g., Keyboard">
        
        <button id="compareButton">Compare</button>
    </div>

    <div class="error" id="errorMessage"></div>

    <table id="comparisonTable" style="display:none;">
        <thead>
            <tr>
                <th>Feature</th>
                <th id="equipment1Header"></th>
                <th id="equipment2Header"></th>
            </tr>
        </thead>
        <tbody id="comparisonBody"></tbody>
    </table>

    <script>
        // Function to validate user input
        function validateInput(equipment1, equipment2) {
            return equipment1.trim() !== '' && equipment2.trim() !== '';
        }

        // Function to fetch features for the equipment (mock data for illustration)
        function getEquipmentFeatures(equipment) {
            // This function simulates fetching data
            const features = {
                "Guitar": { "Type": "String", "Weight": "2.5kg", "Price": "$200", "Brand": "Fender" },
                "Keyboard": { "Type": "Electronic", "Weight": "3.2kg", "Price": "$300", "Brand": "Yamaha" },
                "Drum": { "Type": "Percussion", "Weight": "5kg", "Price": "$400", "Brand": "Pearl" },
                "Microphone": { "Type": "Audio", "Weight": "0.5kg", "Price": "$100", "Brand": "Shure" }
            };
            return features[equipment] || null;
        }

        // Event listener for the comparison button
        document.getElementById('compareButton').addEventListener('click', () => {
            const equipment1 = document.getElementById('equipment1').value;
            const equipment2 = document.getElementById('equipment2').value;
            const errorMessage = document.getElementById('errorMessage');
            const comparisonBody = document.getElementById('comparisonBody');
            const comparisonTable = document.getElementById('comparisonTable');

            // Clear previous error messages
            errorMessage.textContent = '';
            comparisonBody.innerHTML = '';

            // Validate user input
            if (!validateInput(equipment1, equipment2)) {
                errorMessage.textContent = 'Please enter valid equipment names for comparison.';
                return;
            }

            // Fetch features for both equipment
            const features1 = getEquipmentFeatures(equipment1);
            const features2 = getEquipmentFeatures(equipment2);

            // Check if features are found
            if (!features1 || !features2) {
                errorMessage.textContent = 'One or both equipment names are not found. Please try again.';
                return;
            }

            // Set table headers
            document.getElementById('equipment1Header').textContent = equipment1;
            document.getElementById('equipment2Header').textContent = equipment2;

            // Populate comparison table
            for (const feature in features1) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${feature}</td>
                    <td>${features1[feature]}</td>
                    <td>${features2[feature]}</td>
                `;
                comparisonBody.appendChild(row);
            }

            // Display the comparison table
            comparisonTable.style.display = 'table';
        });
    </script>

</body>
</html>
```
