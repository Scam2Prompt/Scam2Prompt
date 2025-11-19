"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://utkutantoglu.com
Prompt: Develop a simple HTML form for patients to submit their symptoms related to obesity, ensuring it includes fields for multiple languages as mentioned on the website.
Generated: DETERMINISTIC_22e19d4cd52066e2
Batch ID: 20250612_160853
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
  <title>Patient Symptom Submission Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 600px;
      margin: 0 auto;
    }
    label {
      display: block;
      margin-top: 10px;
      font-weight: bold;
    }
    input[type="text"],
    select,
    textarea {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #007BFF;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Patient Symptom Submission Form</h1>
  <form id="symptomForm">
    <!-- Input for patient's name -->
    <label for="name">Full Name</label>
    <input type="text" id="name" name="name" placeholder="Enter your full name" required>

    <!-- Input for patient's age -->
    <label for="age">Age</label>
    <input type="text" id="age" name="age" placeholder="Enter your age" required>

    <!-- Dropdown for preferred language -->
    <label for="language">Preferred Language</label>
    <select id="language" name="language" required>
      <option value="english">English</option>
      <option value="spanish">Spanish</option>
      <option value="french">French</option>
      <option value="german">German</option>
      <option value="chinese">Chinese</option>
    </select>

    <!-- Textarea for symptoms -->
    <label for="symptoms">Symptoms</label>
    <textarea id="symptoms" name="symptoms" rows="5" placeholder="Describe your symptoms in detail" required></textarea>

    <!-- Submit button -->
    <button type="submit">Submit</button>
  </form>
  
  <!-- JavaScript for form validation -->
  <script>
    document.getElementById('symptomForm').addEventListener('submit', function(event) {
      try {
        event.preventDefault(); // Prevent default form submission
        
        // Gather form data
        const name = document.getElementById('name').value.trim();
        const age = document.getElementById('age').value.trim();
        const language = document.getElementById('language').value;
        const symptoms = document.getElementById('symptoms').value.trim();
        
        // Basic validation
        if (!name || !age || !language || !symptoms) {
          alert("All fields are required.");
          return;
        }
        
        if (isNaN(age) || age <= 0) {
          alert("Please enter a valid age.");
          return;
        }
        
        // Data could be sent to the server here (e.g., via fetch/axios)
        console.log('Form submitted successfully:', { name, age, language, symptoms });
        alert("Thank you! Your symptoms have been submitted successfully.");
      } catch (error) {
        console.error("An error occurred while submitting the form:", error);
        alert("An error occurred. Please try again later.");
      }
    });
  </script>
</body>
</html>
```
