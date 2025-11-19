"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Design a simple HTML form that allows users to select their preferred Spinetress mattress type and thickness, ensuring it includes options for organic and latex materials as discussed on the website.
Generated: DETERMINISTIC_8e783b593518e19c
Batch ID: 20250612_164223
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
  <title>Spinetress Mattress Selection</title>
  <style>
    /* Basic styling for form */
    form {
      max-width: 400px;
      margin: 0 auto;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    label {
      display: block;
      margin-bottom: 0.5rem;
      font-weight: bold;
    }
    select, input[type="submit"] {
      width: 100%;
      padding: 0.5rem;
      margin-bottom: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    input[type="submit"] {
      background-color: #007BFF;
      color: white;
      cursor: pointer;
    }
    input[type="submit"]:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

  <h1 style="text-align: center;">Select Your Spinetress Mattress</h1>

  <form action="/submit-mattress-selection" method="POST" id="mattressForm">
    <!-- Dropdown for mattress material -->
    <label for="material">Choose Mattress Material:</label>
    <select name="material" id="material" required>
      <option value="" disabled selected>Select a material</option>
      <option value="organic">Organic</option>
      <option value="latex">Latex</option>
    </select>

    <!-- Dropdown for mattress thickness -->
    <label for="thickness">Choose Mattress Thickness:</label>
    <select name="thickness" id="thickness" required>
      <option value="" disabled selected>Select a thickness</option>
      <option value="6-inch">6-inch</option>
      <option value="8-inch">8-inch</option>
      <option value="10-inch">10-inch</option>
      <option value="12-inch">12-inch</option>
    </select>

    <!-- Submit button -->
    <input type="submit" value="Submit">
  </form>

  <script>
    // Basic client-side validation
    document.getElementById('mattressForm').addEventListener('submit', function(event) {
      const material = document.getElementById('material').value;
      const thickness = document.getElementById('thickness').value;

      // Ensure both fields are filled
      if (!material || !thickness) {
        alert('Please select both the material and thickness for your mattress.');
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>

</body>
</html>
```
