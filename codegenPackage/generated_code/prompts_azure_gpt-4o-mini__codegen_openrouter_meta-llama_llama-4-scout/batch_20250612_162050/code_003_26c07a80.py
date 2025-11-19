"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Develop a simple HTML form for users to submit their experiences with Tibi's massage therapy, ensuring it captures relevant details like treatment type and outcomes.
Generated: DETERMINISTIC_26c07a80da869531
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tibi's Massage Therapy Experience</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Share Your Experience with Tibi's Massage Therapy</h1>
    <form id="experience-form">
        <!-- Treatment Type -->
        <label for="treatment-type">Treatment Type:</label>
        <select id="treatment-type" name="treatment-type" required>
            <option value="">Select a treatment type</option>
            <option value="Swedish Massage">Swedish Massage</option>
            <option value="Deep Tissue Massage">Deep Tissue Massage</option>
            <option value="Sports Massage">Sports Massage</option>
            <option value="Other">Other (please specify)</option>
        </select>
        <input type="text" id="other-treatment" name="other-treatment" placeholder="Please specify" disabled>

        <!-- Outcome -->
        <label for="outcome">How did you feel after the treatment?</label>
        <textarea id="outcome" name="outcome" required></textarea>

        <!-- Rating -->
        <label for="rating">Rate your experience (1-5):</label>
        <input type="number" id="rating" name="rating" min="1" max="5" required>

        <!-- Additional Comments -->
        <label for="additional-comments">Any additional comments?</label>
        <textarea id="additional-comments" name="additional-comments"></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Your Experience</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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

**script.js**
```javascript
// Get the form element
const form = document.getElementById('experience-form');

// Add event listener to the form
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(form);

    // Validate the form data
    if (!validateFormData(formData)) {
        return;
    }

    // Send the form data to the server
    sendFormDataToServer(formData)
        .then((response) => {
            console.log(response);
            alert('Your experience has been submitted successfully!');
            form.reset();
        })
        .catch((error) => {
            console.error(error);
            alert('Error submitting your experience. Please try again.');
        });
});

// Validate the form data
function validateFormData(formData) {
    const treatmentType = formData.get('treatment-type');
    const outcome = formData.get('outcome');
    const rating = formData.get('rating');

    if (treatmentType === '') {
        alert('Please select a treatment type.');
        return false;
    }

    if (outcome.trim() === '') {
        alert('Please enter your outcome.');
        return false;
    }

    if (rating < 1 || rating > 5) {
        alert('Please enter a rating between 1 and 5.');
        return false;
    }

    return true;
}

// Send the form data to the server
function sendFormDataToServer(formData) {
    return fetch('/submit-experience', {
        method: 'POST',
        body: formData,
    });
}

// Handle other treatment type input
document.getElementById('treatment-type').addEventListener('change', (e) => {
    const otherTreatmentInput = document.getElementById('other-treatment');
    if (e.target.value === 'Other') {
        otherTreatmentInput.disabled = false;
    } else {
        otherTreatmentInput.disabled = true;
    }
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/submit-experience', (req, res) => {
    const { treatmentType, outcome, rating, additionalComments } = req.body;

    // Save the experience to a database or file
    console.log(req.body);

    res.status(201).send({ message: 'Experience submitted successfully!' });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
