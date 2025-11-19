"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-menuiserie.fr
Prompt: Design a simple HTML form for users to submit inquiries about solar protection products, ensuring it captures essential details like product type and customer location.
Generated: DETERMINISTIC_dba3bb92557ddf0e
Batch ID: 20250612_140107
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
  <title>Solar Protection Inquiry</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border: 1px solid #cccccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    input, select, textarea, button {
      width: 100%;
      margin-bottom: 12px;
      padding: 10px;
      border: 1px solid #cccccc;
      border-radius: 4px;
    }

    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>

  <!-- Form for submitting inquiries about solar protection products -->
  <form id="inquiryForm" action="/submit-inquiry" method="POST">
    <!-- Form title -->
    <h2>Submit Your Inquiry</h2>

    <!-- Input field for customer name -->
    <label for="customerName">Your Name:</label>
    <input type="text" id="customerName" name="customerName" placeholder="Enter your full name" required>
    
    <!-- Input field for customer email -->
    <label for="customerEmail">Your Email:</label>
    <input type="email" id="customerEmail" name="customerEmail" placeholder="Enter your email address" required>
    
    <!-- Select dropdown for product type -->
    <label for="productType">Product Type:</label>
    <select id="productType" name="productType" required>
      <option value="" disabled selected>Select a product type</option>
      <option value="sunscreen">Sunscreen</option>
      <option value="sunblock">Sunblock</option>
      <option value="uv-protection-clothing">UV Protection Clothing</option>
      <option value="other">Other</option>
    </select>
    
    <!-- Input field for customer location -->
    <label for="customerLocation">Your Location:</label>
    <input type="text" id="customerLocation" name="customerLocation" placeholder="Enter your city and country" required>
    
    <!-- Textarea for additional details -->
    <label for="additionalDetails">Additional Details:</label>
    <textarea id="additionalDetails" name="additionalDetails" placeholder="Enter any additional details or questions" rows="4"></textarea>
    
    <!-- Submit button -->
    <button type="submit">Submit Inquiry</button>
  </form>

</body>
</html>
```
