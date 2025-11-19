"""
Generated Code Metadata:
========================
Original URL: https://www.ozonator.si
Prompt: Generate a JavaScript code for a simple web application that calculates the required ozone generator capacity for a given room size, based on the guidelines provided on this webpage.
Generated: DETERMINISTIC_86e28956d00ff088
Batch ID: 20250622_211753
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
    <title>Ozone Generator Capacity Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 400px;
        }
        input, button {
            margin-top: 10px;
            padding: 10px;
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Ozone Generator Capacity Calculator</h1>
    <label for="roomSize">Enter Room Size (in cubic feet):</label>
    <input type="number" id="roomSize" placeholder="Room Size" required>
    
    <button id="calculateBtn">Calculate Ozone Generator Capacity</button>
    
    <h2 id="result" style="display:none;"></h2>

    <script>
        // Function to calculate the required ozone generator capacity
        function calculateOzoneCapacity(roomSize) {
            // Ozone generator capacity is typically calculated as 1 mg/hr per 1000 cubic feet
            const capacityPer1000CubicFeet = 1; // in mg/hr
            return (roomSize / 1000) * capacityPer1000CubicFeet;
        }

        // Event listener for the calculate button
        document.getElementById('calculateBtn').addEventListener('click', function() {
            // Get the room size input value
            const roomSizeInput = document.getElementById('roomSize').value;

            // Validate input
            if (!roomSizeInput || roomSizeInput <= 0) {
                alert('Please enter a valid room size greater than 0.');
                return;
            }

            // Parse the input to a number
            const roomSize = parseFloat(roomSizeInput);

            // Calculate the required ozone generator capacity
            const requiredCapacity = calculateOzoneCapacity(roomSize);

            // Display the result
            const resultElement = document.getElementById('result');
            resultElement.textContent = `Required Ozone Generator Capacity: ${requiredCapacity.toFixed(2)} mg/hr`;
            resultElement.style.display = 'block';
        });
    </script>
</body>
</html>
```
