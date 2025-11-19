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
    <link rel="stylesheet" href="styles.css"> <!-- External CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Register for Sekolah Quran Indonesia</h1>
        <form id="registrationForm" action="submit_form.php" method="POST">
            <!-- Input for student's name -->
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <!-- Input for student's age -->
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" min="1" max="120" required placeholder="Enter your age">

            <!-- Dropdown for class type selection -->
            <label for="classType">Preferred Class Type:</label>
            <select id="classType" name="classType" required>
                <option value="" disabled selected>Select a class type</option>
                <option value="Beginner">Beginner</option>
                <option value="Intermediate">Intermediate</option>
                <option value="Advanced">Advanced</option>
            </select>

            <!-- Submit button -->
            <button type="submit">Register</button>
        </form>
    </div>

    <script src="script.js"></script> <!-- External JavaScript for form validation -->
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    // Validate form fields before submission
    const name = document.getElementById('name').value.trim();
    const age = document.getElementById('age').value;
    const classType = document.getElementById('classType').value;

    // Simple validation check
    if (!name || !age || !classType) {
        alert('Please fill all the fields correctly.');
        event.preventDefault(); // Prevent form submission
    }
});
```

```php
<?php
// submit_form.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $age = filter_input(INPUT_POST, 'age', FILTER_VALIDATE_INT);
    $classType = filter_input(INPUT_POST, 'classType', FILTER_SANITIZE_STRING);

    // Check if inputs are valid
    if ($name && $age && $classType) {
        // Process the registration (e.g., save to the database)
        // Placeholder for database interaction
        echo "Registration successful for $name, Age: $age, Class Type: $classType";
    } else {
        echo "Invalid input. Please try again.";
    }
} else {
    echo "Invalid request method.";
}
?>
```
