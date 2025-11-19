"""
Generated Code Metadata:
========================
Original URL: https://rhonybarros.com.br
Prompt: Design a simple HTML form for users to input their details for scheduling a medical exam, including options for pediatric services at Rhony Kids.
Generated: DETERMINISTIC_bab6d1b6f3e8dcca
Batch ID: 20250612_161616
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
    <title>Schedule Medical Exam</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Schedule Medical Exam</h1>
    <form id="exam-form">
        <label for="first-name">First Name:</label>
        <input type="text" id="first-name" name="first-name" required>

        <label for="last-name">Last Name:</label>
        <input type="text" id="last-name" name="last-name" required>

        <label for="date-of-birth">Date of Birth:</label>
        <input type="date" id="date-of-birth" name="date-of-birth" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone-number">Phone Number:</label>
        <input type="tel" id="phone-number" name="phone-number" required>

        <label for="exam-type">Exam Type:</label>
        <select id="exam-type" name="exam-type">
            <option value="">Select Exam Type</option>
            <option value="general">General Medical Exam</option>
            <option value="pediatric">Pediatric Services at Rhony Kids</option>
        </select>

        <div id="pediatric-services" style="display: none;">
            <label for="child-age">Child's Age:</label>
            <input type="number" id="child-age" name="child-age">

            <label for="pediatric-service-type">Pediatric Service Type:</label>
            <select id="pediatric-service-type" name="pediatric-service-type">
                <option value="">Select Service Type</option>
                <option value="check-up">Check-up</option>
                <option value="vaccination">Vaccination</option>
                <option value="consultation">Consultation</option>
            </select>
        </div>

        <button type="submit">Schedule Exam</button>
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

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#pediatric-services {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('exam-form');

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
    sendFormDataToServer(formData);
});

// Function to validate the form data
function validateFormData(formData) {
    const firstName = formData.get('first-name').trim();
    const lastName = formData.get('last-name').trim();
    const dateOfBirth = formData.get('date-of-birth');
    const email = formData.get('email').trim();
    const phoneNumber = formData.get('phone-number').trim();
    const examType = formData.get('exam-type');

    if (firstName === '' || lastName === '' || dateOfBirth === '' || email === '' || phoneNumber === '' || examType === '') {
        alert('Please fill in all required fields.');
        return false;
    }

    if (examType === 'pediatric') {
        const childAge = formData.get('child-age');
        const pediatricServiceType = formData.get('pediatric-service-type');

        if (childAge === '' || pediatricServiceType === '') {
            alert('Please fill in all required fields for pediatric services.');
            return false;
        }
    }

    return true;
}

// Function to send the form data to the server
function sendFormDataToServer(formData) {
    fetch('/schedule-exam', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            alert('Exam scheduled successfully!');
            form.reset();
        } else {
            alert('Error scheduling exam: ' + data.message);
        }
    })
    .catch((error) => {
        alert('Error scheduling exam: ' + error.message);
    });
}

// Add event listener to the exam type select element
const examTypeSelect = document.getElementById('exam-type');
examTypeSelect.addEventListener('change', (e) => {
    const pediatricServicesDiv = document.getElementById('pediatric-services');

    if (e.target.value === 'pediatric') {
        pediatricServicesDiv.style.display = 'block';
    } else {
        pediatricServicesDiv.style.display = 'none';
    }
});
```

**server.js (example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post('/schedule-exam', (req, res) => {
    const { firstName, lastName, dateOfBirth, email, phoneNumber, examType, childAge, pediatricServiceType } = req.body;

    // Validate the request data
    if (!firstName || !lastName || !dateOfBirth || !email || !phoneNumber || !examType) {
        res.json({ success: false, message: 'Please fill in all required fields.' });
        return;
    }

    if (examType === 'pediatric' && (!childAge || !pediatricServiceType)) {
        res.json({ success: false, message: 'Please fill in all required fields for pediatric services.' });
        return;
    }

    // Schedule the exam
    try {
        // TO DO: implement exam scheduling logic here
        res.json({ success: true, message: 'Exam scheduled successfully!' });
    } catch (error) {
        res.json({ success: false, message: error.message });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
