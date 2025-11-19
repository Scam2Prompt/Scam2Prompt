"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Develop a simple HTML form for prospective students to register for Sekolah Quran Indonesia, including fields for name, age, and preferred class type.
Generated: DETERMINISTIC_770cb3abbd09a8e0
Batch ID: 20250612_160703
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
    <title>Registration Form - Sekolah Quran Indonesia</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"], input[type="number"], select {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <!-- Registration Form -->
    <form id="registrationForm">
        <h2>Student Registration</h2>

        <!-- Field for Name -->
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
        <div class="error-message" id="nameError"></div>

        <!-- Field for Age -->
        <label for="age">Age</label>
        <input type="number" id="age" name="age" placeholder="Enter your age" min="5" max="100" required>
        <div class="error-message" id="ageError"></div>

        <!-- Field for Preferred Class Type -->
        <label for="classType">Preferred Class Type</label>
        <select id="classType" name="classType" required>
            <option value="">Select a class type</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
        </select>
        <div class="error-message" id="classTypeError"></div>

        <!-- Submit Button -->
        <input type="submit" value="Register">

    </form>

    <!-- JavaScript for basic form validation -->
    <script>
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            let isValid = true;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('ageError').textContent = '';
            document.getElementById('classTypeError').textContent = '';

            // Validate name field
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }

            // Validate age field
            const age = document.getElementById('age').value;
            if (!age || age < 5 || age > 100) {
                document.getElementById('ageError').textContent = 'Age must be between 5 and 100.';
                isValid = false;
            }

            // Validate class type field
            const classType = document.getElementById('classType').value;
            if (!classType) {
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
