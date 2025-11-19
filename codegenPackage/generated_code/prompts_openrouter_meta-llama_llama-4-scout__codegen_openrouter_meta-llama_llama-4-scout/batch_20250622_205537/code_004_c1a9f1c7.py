"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocats.com
Prompt: Generate a sample intake form for a family law client, including fields for personal and case information, using HTML and CSS, inspired by the layout and content of the Majeli Avocat website.
Generated: DETERMINISTIC_c1a9f1c7f2e4295f
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Family Law Intake Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Family Law Intake Form</h1>
        <form id="intake-form">
            <!-- Personal Information -->
            <section>
                <h2>Personal Information</h2>
                <div class="form-group">
                    <label for="first-name">First Name:</label>
                    <input type="text" id="first-name" name="first-name" required>
                </div>
                <div class="form-group">
                    <label for="last-name">Last Name:</label>
                    <input type="text" id="last-name" name="last-name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone:</label>
                    <input type="tel" id="phone" name="phone" required>
                </div>
            </section>

            <!-- Case Information -->
            <section>
                <h2>Case Information</h2>
                <div class="form-group">
                    <label for="case-type">Case Type:</label>
                    <select id="case-type" name="case-type" required>
                        <option value="">Select an option</option>
                        <option value="divorce">Divorce</option>
                        <option value="child-custody">Child Custody</option>
                        <option value="child-support">Child Support</option>
                        <option value="spousal-support">Spousal Support</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="case-description">Case Description:</label>
                    <textarea id="case-description" name="case-description" required></textarea>
                </div>
                <div class="form-group">
                    <label for="file-upload">Upload Files (optional):</label>
                    <input type="file" id="file-upload" name="file-upload" multiple>
                </div>
            </section>

            <!-- Submission -->
            <button type="submit">Submit</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #337ab7;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select, textarea {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

textarea {
    height: 100px;
    resize: vertical;
}

button[type="submit"] {
    background-color: #337ab7;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #23527c;
}
```

```javascript
// script.js

const form = document.getElementById('intake-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(form);

    // Validate form data
    if (!formData.get('first-name') || !formData.get('last-name')) {
        alert('Please fill out all required fields.');
        return;
    }

    // Send form data to server
    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```
