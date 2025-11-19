"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Generate a simple web page using HTML and JavaScript that displays the contact information of Colegio Panamericano e Instituto Libertadores, including phone numbers for different educational levels.
Generated: DETERMINISTIC_ad433d05e8e5997d
Batch ID: 20250622_205254
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
    <title>Colegio Panamericano e Instituto Libertadores Contact Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .contact-info {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Colegio Panamericano e Instituto Libertadores Contact Information</h1>
    <div class="contact-info">
        <h2>General Information</h2>
        <p>Address: [Insert Address]</p>
        <p>Email: [Insert Email]</p>
    </div>
    <div class="contact-info">
        <h2>Phone Numbers</h2>
        <p>Preschool: <span id="preschool-phone"></span></p>
        <p>Elementary School: <span id="elementary-phone"></span></p>
        <p>High School: <span id="high-school-phone"></span></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**script.js**
```javascript
// Data for contact information
const contactInfo = {
    preschoolPhone: '123-456-7890',
    elementaryPhone: '987-654-3210',
    highSchoolPhone: '555-123-4567',
};

// Function to display contact information
function displayContactInfo() {
    try {
        document.getElementById('preschool-phone').textContent = contactInfo.preschoolPhone;
        document.getElementById('elementary-phone').textContent = contactInfo.elementaryPhone;
        document.getElementById('high-school-phone').textContent = contactInfo.highSchoolPhone;
    } catch (error) {
        console.error('Error displaying contact information:', error);
    }
}

// Call function to display contact information on page load
document.addEventListener('DOMContentLoaded', displayContactInfo);
```

**Error Handling Note**: 
In a production environment, consider adding more robust error handling and possibly integrating with a backend service for dynamic data retrieval. 

To run the code, save both files (`index.html` and `script.js`) in the same directory and open `index.html` in a web browser. Replace `[Insert Address]` and `[Insert Email]` with the actual address and email of Colegio Panamericano e Instituto Libertadores.
