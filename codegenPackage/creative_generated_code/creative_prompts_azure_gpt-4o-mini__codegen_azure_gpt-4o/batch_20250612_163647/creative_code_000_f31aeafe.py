"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centralseedandchem.co.nz
Prompt: Generate a code snippet for a web form that allows users to request seed and chemical supply information specific to Otago and Southland.
Generated: DETERMINISTIC_f31aeafe9250c09d
Batch ID: 20250612_163647
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
  <title>Seed and Chemical Supply Request</title>
  <style>
    /* Simple styling for clean UI */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f5f5f5;
    }
    form {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input, select, textarea, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 16px;
    }
    button {
      background-color: #007bff;
      color: #fff;
      border: none;
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
  <form id="supplyRequestForm">
    <h2>Seed and Chemical Supply Request</h2>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Enter your name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>

    <label for="region">Region:</label>
    <select id="region" name="region" required>
      <option value="" disabled selected>Select your region</option>
      <option value="Otago">Otago</option>
      <option value="Southland">Southland</option>
    </select>

    <label for="requestDetails">Request Details:</label>
    <textarea id="requestDetails" name="requestDetails" rows="4" placeholder="Provide details about your seed and chemical supply needs" required></textarea>

    <button type="submit">Submit Request</button>
    <p id="formError" class="error" style="display: none;"></p>
  </form>

  <script>
    // Attach event listener to handle form submission
    document.getElementById('supplyRequestForm').addEventListener('submit', async function (event) {
      event.preventDefault(); // Prevent default form submission
      
      // Retrieve form data
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const region = document.getElementById('region').value;
      const requestDetails = document.getElementById('requestDetails').value.trim();
      const errorElement = document.getElementById('formError');

      // Clear previous error message
      errorElement.style.display = 'none';

      try {
        // Basic validation
        if (!name || !email || !region || !requestDetails) {
          throw new Error('All fields are required.');
        }

        if (!/\S+@\S+\.\S+/.test(email)) {
          throw new Error('Please enter a valid email address.');
        }

        // Simulate sending data to the server (replace with actual API call)
        const response = await fetch('/submitRequest', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name, email, region, requestDetails }),
        });

        if (!response.ok) {
          throw new Error('Failed to submit the request. Please try again later.');
        }

        // Inform user of successful submission
        alert('Your request has been submitted successfully!');
        document.getElementById('supplyRequestForm').reset(); // Reset form fields
      } catch (error) {
        // Display error message
        errorElement.textContent = error.message;
        errorElement.style.display = 'block';
      }
    });
  </script>
</body>
</html>
```
