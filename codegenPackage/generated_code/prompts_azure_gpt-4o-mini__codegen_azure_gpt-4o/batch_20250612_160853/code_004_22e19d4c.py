"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Develop a simple HTML form for patients to submit their symptoms related to obesity, ensuring it includes fields for multiple languages as mentioned on the website.
Generated: DETERMINISTIC_22e19d4cd52066e2
Batch ID: 20250612_160853
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
  <title>Patient Symptom Submission Form</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .form-container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .form-container h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .form-group label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    .form-group input, .form-group textarea, .form-group select {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .form-group textarea {
      resize: vertical;
    }
    .form-group button {
      display: block;
      width: 100%;
      padding: 10px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .form-group button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Patient Symptom Submission</h1>
    <form id="symptomForm" action="/submit-symptoms" method="POST">
      <!-- Patient Name -->
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" placeholder="Enter your name" required>
      </div>

      <!-- Patient Age -->
      <div class="form-group">
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" placeholder="Enter your age" required>
      </div>

      <!-- Language Selection -->
      <div class="form-group">
        <label for="language">Preferred Language:</label>
        <select id="language" name="language" required>
          <option value="en">English</option>
          <option value="es">Spanish</option>
          <option value="fr">French</option>
          <option value="de">German</option>
          <option value="zh">Chinese</option>
        </select>
      </div>

      <!-- Symptoms Description -->
      <div class="form-group">
        <label for="symptoms">Describe Your Symptoms:</label>
        <textarea id="symptoms" name="symptoms" rows="5" placeholder="Provide details about your symptoms" required></textarea>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>

  <script>
    // Basic client-side validation and error handling
    document.getElementById('symptomForm').addEventListener('submit', function(event) {
      try {
        const name = document.getElementById('name').value.trim();
        const age = document.getElementById('age').value.trim();
        const symptoms = document.getElementById('symptoms').value.trim();

        if (!name || !age || !symptoms) {
          alert('Please fill out all required fields.');
          event.preventDefault(); // Prevent form submission
        }
      } catch (error) {
        console.error('Error during form submission:', error);
        alert('An unexpected error occurred. Please try again.');
        event.preventDefault(); // Prevent form submission
      }
    });
  </script>
</body>
</html>
```
