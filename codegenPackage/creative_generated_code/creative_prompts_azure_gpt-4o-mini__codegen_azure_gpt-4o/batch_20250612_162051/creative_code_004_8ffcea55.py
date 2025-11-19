"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.autocuyo.com.ar
Prompt: Create a sample HTML form for submitting a car listing to Autocuyo's classifieds section.
Generated: DETERMINISTIC_8ffcea55ba295ac5
Batch ID: 20250612_162051
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
    <meta name="author" content="Autocuyo">
    <meta name="description" content="Submit your car listing to Autocuyo's classifieds section">
    <title>Submit Car Listing | Autocuyo</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
            font-size: 16px;
        }

        button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: #fff;
            background-color: #5cb85c;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>
    <h1>Submit Your Car Listing</h1>
    <form id="car-listing-form" action="/submit-car-listing" method="POST">
        <!-- Form group for car make -->
        <div class="form-group">
            <label for="car-make">Car Make</label>
            <input type="text" id="car-make" name="car_make" required placeholder="E.g., Toyota">
        </div>

        <!-- Form group for car model -->
        <div class="form-group">
            <label for="car-model">Car Model</label>
            <input type="text" id="car-model" name="car_model" required placeholder="E.g., Corolla">
        </div>

        <!-- Form group for year -->
        <div class="form-group">
            <label for="car-year">Year</label>
            <input type="number" id="car-year" name="car_year" required min="1886" max="2023" placeholder="E.g., 2020">
        </div>

        <!-- Form group for price -->
        <div class="form-group">
            <label for="car-price">Price ($)</label>
            <input type="number" id="car-price" name="car_price" required min="0" step="0.01" placeholder="E.g., 15000">
        </div>

        <!-- Form group for mileage -->
        <div class="form-group">
            <label for="car-mileage">Mileage (km)</label>
            <input type="number" id="car-mileage" name="car_mileage" required min="0" placeholder="E.g., 50000">
        </div>

        <!-- Form group for fuel type -->
        <div class="form-group">
            <label for="fuel-type">Fuel Type</label>
            <select id="fuel-type" name="fuel_type" required>
                <option value="">Select fuel type</option>
                <option value="petrol">Petrol</option>
                <option value="diesel">Diesel</option>
                <option value="electric">Electric</option>
                <option value="hybrid">Hybrid</option>
            </select>
        </div>

        <!-- Form group for description -->
        <div class="form-group">
            <label for="description">Description</label>
            <textarea id="description" name="description" rows="5" required placeholder="Write a brief description of your car"></textarea>
        </div>

        <!-- Form group for image upload -->
        <div class="form-group">
            <label for="car-image">Upload Image</label>
            <input type="file" id="car-image" name="car_image" accept="image/*" required>
        </div>

        <!-- Submit button -->
        <button type="submit">Submit Listing</button>
    </form>
</body>
</html>
```
