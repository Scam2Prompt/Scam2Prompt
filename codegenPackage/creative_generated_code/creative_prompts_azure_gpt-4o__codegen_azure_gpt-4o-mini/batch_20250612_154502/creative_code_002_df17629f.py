"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Generate code to create a dropdown menu for selecting travel classes (Economy, Premium Economy, Business, First) in a flight booking interface.
Generated: DETERMINISTIC_df17629fce547ca9
Batch ID: 20250612_154502
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
    <title>Flight Booking Interface</title>
    <style>
        /* Basic styles for the dropdown */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        select {
            padding: 8px;
            font-size: 16px;
            width: 200px;
        }
    </style>
</head>
<body>

    <h1>Select Your Travel Class</h1>

    <!-- Dropdown menu for selecting travel class -->
    <label for="travelClass">Choose a travel class:</label>
    <select id="travelClass" name="travelClass" required>
        <option value="" disabled selected>Select a class</option>
        <option value="economy">Economy</option>
        <option value="premium-economy">Premium Economy</option>
        <option value="business">Business</option>
        <option value="first">First</option>
    </select>

    <button id="submitBtn">Submit</button>

    <script>
        // Function to handle form submission
        function handleSubmit() {
            const travelClass = document.getElementById('travelClass').value;

            // Check if a travel class is selected
            if (!travelClass) {
                alert('Please select a travel class.');
                return;
            }

            // Simulate submission of the selected travel class
            console.log(`Selected travel class: ${travelClass}`);
            alert(`You have selected: ${travelClass}`);
        }

        // Event listener for the submit button
        document.getElementById('submitBtn').addEventListener('click', handleSubmit);
    </script>

</body>
</html>
```
