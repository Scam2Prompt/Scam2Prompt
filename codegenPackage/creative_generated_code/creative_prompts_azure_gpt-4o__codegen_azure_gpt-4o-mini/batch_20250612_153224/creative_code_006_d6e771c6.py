"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write JavaScript code to dynamically update a webpage with service descriptions (e.g., "Repair of washing machines, refrigerators, microwaves") based on user selection from a dropdown menu.
Generated: DETERMINISTIC_d6e771c6bc973ac0
Batch ID: 20250612_153224
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
    <title>Service Descriptions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        select {
            margin-bottom: 20px;
            padding: 10px;
        }
        #description {
            font-size: 18px;
            color: #333;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>Select a Service</h1>
    <select id="serviceSelect">
        <option value="">--Please choose an option--</option>
        <option value="washingMachine">Washing Machine Repair</option>
        <option value="refrigerator">Refrigerator Repair</option>
        <option value="microwave">Microwave Repair</option>
    </select>

    <div id="description"></div>

    <script>
        // Service descriptions mapped to service types
        const serviceDescriptions = {
            washingMachine: "Repair of washing machines involves fixing issues such as water leakage, drum malfunction, or electrical problems.",
            refrigerator: "Refrigerator repair includes troubleshooting cooling issues, door seal replacements, and compressor repairs.",
            microwave: "Microwave repair encompasses fixing heating problems, door latch issues, and electronic malfunctions."
        };

        // Get references to the dropdown and description display elements
        const serviceSelect = document.getElementById('serviceSelect');
        const descriptionDiv = document.getElementById('description');

        // Add an event listener to handle changes in the dropdown selection
        serviceSelect.addEventListener('change', function() {
            // Clear previous description
            descriptionDiv.textContent = '';

            // Get the selected value
            const selectedService = serviceSelect.value;

            // Check if a valid service is selected
            if (selectedService && serviceDescriptions[selectedService]) {
                // Update the description based on the selected service
                descriptionDiv.textContent = serviceDescriptions[selectedService];
            } else {
                // Handle case where no valid service is selected
                descriptionDiv.textContent = 'Please select a valid service to see the description.';
            }
        });
    </script>

</body>
</html>
```
