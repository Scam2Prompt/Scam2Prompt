"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwereplicabelts.com
Prompt: Create a sample HTML form that allows users to submit a custom championship belt request, inspired by the features on wwereplicabelts.com.
Generated: DETERMINISTIC_d598036546d1aa8c
Batch ID: 20250612_163848
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
    <title>Custom Championship Belt Request</title>
    <style>
        /* Basic styling for form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
        }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        input,
        textarea,
        select,
        button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <div class="form-container">
        <h1>Custom Championship Belt Request</h1>
        <form action="/submit-belt-request" method="POST">
            <!-- Customer Name -->
            <label for="name">Your Name</label>
            <input type="text" id="name" name="name" placeholder="Enter your full name" required>

            <!-- Customer Email -->
            <label for="email">Your Email</label>
            <input type="email" id="email" name="email" placeholder="Enter your email address" required>

            <!-- Belt Name -->
            <label for="belt-name">Belt Name/Title</label>
            <input type="text" id="belt-name" name="belt_name" placeholder="Enter the championship belt name" required>

            <!-- Belt Design -->
            <label for="belt-design">Select a Belt Design</label>
            <select id="belt-design" name="belt_design" required>
                <option value="" disabled selected>Choose a design</option>
                <option value="classic">Classic Design</option>
                <option value="modern">Modern Design</option>
                <option value="custom">Custom Design</option>
            </select>

            <!-- Belt Color -->
            <label for="belt-color">Preferred Belt Color</label>
            <input type="text" id="belt-color" name="belt_color" placeholder="e.g., Black, Red, Gold" required>

            <!-- Custom Logo Upload -->
            <label for="custom-logo">Upload a Custom Logo</label>
            <input type="file" id="custom-logo" name="custom_logo" accept="image/png, image/jpeg">

            <!-- Additional Notes -->
            <label for="notes">Additional Notes/Requests</label>
            <textarea id="notes" name="notes" placeholder="Describe any special requests..." rows="4"></textarea>

            <!-- Submit Button -->
            <button type="submit">Submit Request</button>
        </form>
    </div>
</body>

</html>
```
