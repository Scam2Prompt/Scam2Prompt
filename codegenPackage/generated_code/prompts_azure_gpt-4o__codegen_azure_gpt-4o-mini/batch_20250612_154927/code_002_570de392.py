"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Generate code in JavaScript to create an interactive form where users can input dimensions and select options for motorized retractable screens for patios, with real-time validation.
Generated: DETERMINISTIC_570de392b3891a2d
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Motorized Retractable Screens Configurator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Motorized Retractable Screens Configurator</h1>
    <form id="screenForm">
        <label for="width">Width (inches):</label>
        <input type="number" id="width" name="width" min="1" required>
        <span class="error" id="widthError"></span>
        <br><br>

        <label for="height">Height (inches):</label>
        <input type="number" id="height" name="height" min="1" required>
        <span class="error" id="heightError"></span>
        <br><br>

        <label for="material">Select Material:</label>
        <select id="material" name="material" required>
            <option value="">--Select--</option>
            <option value="mesh">Mesh</option>
            <option value="vinyl">Vinyl</option>
            <option value="screen">Screen</option>
        </select>
        <span class="error" id="materialError"></span>
        <br><br>

        <button type="submit">Submit</button>
    </form>

    <div id="result"></div>

    <script>
        // Function to validate form inputs
        function validateForm() {
            let isValid = true;

            // Clear previous error messages
            document.getElementById('widthError').textContent = '';
            document.getElementById('heightError').textContent = '';
            document.getElementById('materialError').textContent = '';

            // Validate width
            const width = document.getElementById('width').value;
            if (width < 1) {
                document.getElementById('widthError').textContent = 'Width must be greater than 0.';
                isValid = false;
            }

            // Validate height
            const height = document.getElementById('height').value;
            if (height < 1) {
                document.getElementById('heightError').textContent = 'Height must be greater than 0.';
                isValid = false;
            }

            // Validate material selection
            const material = document.getElementById('material').value;
            if (material === '') {
                document.getElementById('materialError').textContent = 'Please select a material.';
                isValid = false;
            }

            return isValid;
        }

        // Function to handle form submission
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            if (validateForm()) {
                const width = document.getElementById('width').value;
                const height = document.getElementById('height').value;
                const material = document.getElementById('material').value;

                // Display the result
                document.getElementById('result').innerHTML = `
                    <h2>Configuration Summary</h2>
                    <p>Width: ${width} inches</p>
                    <p>Height: ${height} inches</p>
                    <p>Material: ${material}</p>
                `;
            }
        }

        // Attach event listener to the form
        document.getElementById('screenForm').addEventListener('submit', handleSubmit);
    </script>
</body>
</html>
```
