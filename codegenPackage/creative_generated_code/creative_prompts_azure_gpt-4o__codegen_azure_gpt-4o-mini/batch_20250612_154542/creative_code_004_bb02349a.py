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
    <title>Egatur Course Selection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Select a Course from Egatur</h1>
    <form id="courseForm" onsubmit="return validateForm()">
        <label for="course">Choose a course:</label>
        <select id="course" name="course">
            <option value="">--Please choose an option--</option>
            <option value="Barismo">Barismo</option>
            <option value="Gestión de Hotelería y Turismo">Gestión de Hotelería y Turismo</option>
            <option value="Pastelería y Panificación">Pastelería y Panificación</option>
        </select>
        <span id="error-message" class="error"></span>
        <br><br>
        <button type="submit">Submit</button>
    </form>

    <script>
        /**
         * Validates the form input.
         * @returns {boolean} - Returns true if valid, false otherwise.
         */
        function validateForm() {
            // Clear previous error message
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = '';

            // Get the selected course value
            const selectedCourse = document.getElementById('course').value;

            // Validate that a course has been selected
            if (selectedCourse === '') {
                errorMessage.textContent = 'Please select a course.';
                return false; // Prevent form submission
            }

            // Form is valid
            alert(`You have selected: ${selectedCourse}`);
            return true; // Allow form submission
        }
    </script>
</body>
</html>
```
