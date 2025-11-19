"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Design a simple web form using HTML and CSS to collect property information and provide a cash offer for a house in San Francisco Bay Area.
Generated: DETERMINISTIC_45099634ba46653b
Batch ID: 20250622_211011
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
    <title>Property Cash Offer Form</title>
    <style>
        /* General styles for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            margin-top: 15px;
            font-weight: bold;
            color: #555;
        }

        input, select, textarea {
            margin-top: 5px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
            width: 100%;
            box-sizing: border-box;
        }

        textarea {
            resize: none;
            height: 100px;
        }

        button {
            margin-top: 20px;
            padding: 10px 15px;
            font-size: 16px;
            color: #fff;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .error {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Get a Cash Offer for Your Property</h1>
        <form id="propertyForm">
            <!-- Property Address -->
            <label for="address">Property Address:</label>
            <input type="text" id="address" name="address" placeholder="Enter property address" required>

            <!-- Property Type -->
            <label for="propertyType">Property Type:</label>
            <select id="propertyType" name="propertyType" required>
                <option value="">Select property type</option>
                <option value="single-family">Single Family</option>
                <option value="multi-family">Multi-Family</option>
                <option value="condo">Condo</option>
                <option value="townhouse">Townhouse</option>
            </select>

            <!-- Number of Bedrooms -->
            <label for="bedrooms">Number of Bedrooms:</label>
            <input type="number" id="bedrooms" name="bedrooms" placeholder="Enter number of bedrooms" min="1" required>

            <!-- Number of Bathrooms -->
            <label for="bathrooms">Number of Bathrooms:</label>
            <input type="number" id="bathrooms" name="bathrooms" placeholder="Enter number of bathrooms" min="1" required>

            <!-- Additional Notes -->
            <label for="notes">Additional Notes:</label>
            <textarea id="notes" name="notes" placeholder="Provide any additional details about the property"></textarea>

            <!-- Submit Button -->
            <button type="submit">Get Cash Offer</button>
        </form>
    </div>

    <script>
        // JavaScript for form validation and submission
        document.getElementById('propertyForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting normally

            // Collect form data
            const address = document.getElementById('address').value.trim();
            const propertyType = document.getElementById('propertyType').value;
            const bedrooms = document.getElementById('bedrooms').value;
            const bathrooms = document.getElementById('bathrooms').value;
            const notes = document.getElementById('notes').value.trim();

            // Basic validation
            if (!address || !propertyType || !bedrooms || !bathrooms) {
                alert('Please fill out all required fields.');
                return;
            }

            // Simulate form submission (replace with actual API call in production)
            alert(`Thank you! We will provide a cash offer for the property at ${address}.`);
        });
    </script>
</body>
</html>
```
