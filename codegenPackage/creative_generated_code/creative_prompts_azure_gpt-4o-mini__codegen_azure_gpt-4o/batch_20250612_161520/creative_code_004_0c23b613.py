"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spedition-steinhuebl.de
Prompt: Construct a sample HTML form for users to input their package details for shipping, reflecting the user experience on the Spedition Steinhübl website.
Generated: DETERMINISTIC_0c23b6134531d217
Batch ID: 20250612_161520
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
    <title>Shipping Package Details</title>
    <style>
        /* Styling for a clean and user-friendly experience */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            max-width: 600px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        .form-container h2 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }

        .form-group input, 
        .form-group select, 
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }

        .form-group textarea {
            resize: vertical;
            height: 100px;
        }

        .form-actions {
            text-align: center;
        }

        .form-actions button {
            background-color: #007BFF;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }

        .form-actions button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Shipping Package Details</h2>
        <form id="shippingForm" action="/submit-package-details" method="POST">
            <!-- Full Name -->
            <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" required 
                    placeholder="Enter your full name">
            </div>

            <!-- Email Address -->
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required 
                    placeholder="Enter your email address">
            </div>

            <!-- Package Description -->
            <div class="form-group">
                <label for="description">Package Description</label>
                <textarea id="description" name="description" required 
                    placeholder="Provide a short description of the package"></textarea>
            </div>

            <!-- Package Weight -->
            <div class="form-group">
                <label for="weight">Package Weight (kg)</label>
                <input type="number" id="weight" name="weight" required 
                    min="0.1" step="0.1" placeholder="Enter the weight of the package">
            </div>

            <!-- Dimensions -->
            <div class="form-group">
                <label for="dimensions">Dimensions (L×W×H in cm)</label>
                <input type="text" id="dimensions" name="dimensions" required 
                    placeholder="e.g., 50×30×20">
            </div>

            <!-- Shipping Priority -->
            <div class="form-group">
                <label for="priority">Shipping Priority</label>
                <select id="priority" name="priority" required>
                    <option value="" disabled selected>Select priority</option>
                    <option value="standard">Standard</option>
                    <option value="express">Express</option>
                    <option value="overnight">Overnight</option>
                </select>
            </div>

            <!-- Submit Button -->
            <div class="form-actions">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>

    <script>
        // Basic client-side validation
        document.getElementById('shippingForm').addEventListener('submit', function(event) {
            // Ensure dimensions follow format
            const dimensions = document.getElementById('dimensions').value;
            const dimensionsRegex = /^\d+×\d+×\d+$/;

            if (!dimensionsRegex.test(dimensions)) {
                alert('Please enter dimensions in the format L×W×H (e.g., 50×30×20).');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
