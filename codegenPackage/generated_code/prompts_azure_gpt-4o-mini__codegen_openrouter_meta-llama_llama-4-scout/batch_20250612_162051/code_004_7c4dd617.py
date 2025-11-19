"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Design a simple HTML form that collects user information for a digital course on architecture and interior design offered by Nyiku Design.
Generated: DETERMINISTIC_7c4dd61781cbf8d6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML Form Code

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nyiku Design Course Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Nyiku Design Digital Course Registration</h1>
        <form id="registration-form">
            <!-- Personal Information Section -->
            <section>
                <h2>Personal Information</h2>
                <label for="first-name">First Name:</label>
                <input type="text" id="first-name" name="first-name" required>

                <label for="last-name">Last Name:</label>
                <input type="text" id="last-name" name="last-name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="phone-number">Phone Number:</label>
                <input type="tel" id="phone-number" name="phone-number" required>
            </section>

            <!-- Course Information Section -->
            <section>
                <h2>Course Information</h2>
                <label for="course-interest">Which course are you interested in?</label>
                <select id="course-interest" name="course-interest" required>
                    <option value="">Select a course</option>
                    <option value="architecture">Architecture</option>
                    <option value="interior-design">Interior Design</option>
                    <option value="both">Both</option>
                </select>

                <label for="experience-level">What is your experience level?</label>
                <select id="experience-level" name="experience-level" required>
                    <option value="">Select your level</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="advanced">Advanced</option>
                </select>
            </section>

            <!-- Additional Information Section -->
            <section>
                <h2>Additional Information</h2>
                <label for="additional-info">Any additional information about yourself or your interests?</label>
                <textarea id="additional-info" name="additional-info"></textarea>
            </section>

            <!-- Form Submission -->
            <button type="submit">Register for Course</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

### CSS Styling Code (in styles.css)

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    max-width: 600px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

### JavaScript Validation and Submission Handling Code (in script.js)

```javascript
// script.js

const form = document.getElementById('registration-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Basic validation
    const firstName = document.getElementById('first-name').value.trim();
    const lastName = document.getElementById('last-name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phoneNumber = document.getElementById('phone-number').value.trim();

    if (firstName === '' || lastName === '' || email === '' || phoneNumber === '') {
        alert('Please fill in all required fields.');
        return;
    }

    // Form data serialization
    const formData = new FormData(form);

    // Example: Send form data to server using fetch API
    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));

    // Successful submission handling
    alert('Registration form submitted successfully!');
    form.reset();
});
```
