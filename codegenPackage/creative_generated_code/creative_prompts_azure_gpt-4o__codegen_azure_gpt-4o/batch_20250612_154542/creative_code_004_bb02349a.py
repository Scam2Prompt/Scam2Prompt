"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Create an HTML form with dropdown options for Egatur's courses, such as "Barismo," "Gestión de Hotelería y Turismo," and "Pastelería y Panificación," and validate the input using JavaScript.
Generated: DETERMINISTIC_bb02349a10243276
Batch ID: 20250612_154542
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
  <title>Egatur Courses Form</title>
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
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f9f9f9;
    }
    label {
      display: block;
      margin-bottom: 10px;
      font-weight: bold;
    }
    select, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 3px;
    }
    button:hover {
      background-color: #45a049;
    }
    .error {
      color: red;
      font-size: 0.9em;
    }
  </style>
</head>
<body>

  <!-- HTML Form -->
  <form id="courseForm">
    <label for="courses">Select a course:</label>
    <select id="courses" name="courses">
      <option value="">--Please choose an option--</option>
      <option value="Barismo">Barismo</option>
      <option value="Gestión de Hotelería y Turismo">Gestión de Hotelería y Turismo</option>
      <option value="Pastelería y Panificación">Pastelería y Panificación</option>
    </select>
    <span id="errorMessage" class="error"></span>
    <button type="submit">Submit</button>
  </form>

  <!-- JavaScript for form validation -->
  <script>
    // Add event listener for form submission
    document.getElementById('courseForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission

      const courseSelect = document.getElementById('courses');
      const errorMessage = document.getElementById('errorMessage');

      // Validate the dropdown selection
      if (courseSelect.value === '') {
        errorMessage.textContent = 'Please select a course before submitting.';
      } else {
        errorMessage.textContent = ''; // Clear any previous error messages
        alert(`You have selected the course: ${courseSelect.value}`);
        // Proceed with form submission or other logic here
      }
    });
  </script>

</body>
</html>
```
