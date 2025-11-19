"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Develop a simple HTML form for prospective students to register for Sekolah Quran Indonesia, including fields for name, age, and preferred class type.
Generated: DETERMINISTIC_770cb3abbd09a8e0
Batch ID: 20250612_160703
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
    <title>Registration Form - Sekolah Quran Indonesia</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            max-width: 500px;
            margin: 50px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #28a745;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            border: none;
        }

        button:hover {
            background-color: #218838;
        }

        .error-message {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Registration Form</h1>
        <form id="registrationForm">
            <!-- Name field -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" placeholder="Enter your full name" required>
            <span class="error-message" id="nameError"></span>

            <!-- Age field -->
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" placeholder="Enter your age" min="1" required>
            <span class="error-message" id="ageError"></span>

            <!-- Preferred class type field -->
            <label for="classType">Preferred Class Type:</label>
            <select id="classType" name="classType" required>
                <option value="" disabled selected>Select a class type</option>
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
            </select>
            <span class="error-message" id="classTypeError"></span>

            <!-- Submit button -->
            <button type="submit">Register</button>
        </form>
    </div>

    <script>
        // JavaScript for form validation
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('ageError').textContent = '';
            document.getElementById('classTypeError').textContent = '';

            // Validate name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }

            // Validate age
            const age = document.getElementById('age').value.trim();
            if (age === '' || isNaN(age) || age <= 0) {
                document.getElementById('ageError').textContent = 'Please enter a valid age.';
                isValid = false;
            }

            // Validate class type
            const classType = document.getElementById('classType').value;
            if (classType === '') {
                document.getElementById('classTypeError').textContent = 'Please select a class type.';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
