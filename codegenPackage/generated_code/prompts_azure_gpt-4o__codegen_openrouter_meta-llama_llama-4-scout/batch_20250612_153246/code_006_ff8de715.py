"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a web form using HTML and JavaScript to allow users to upload custom designs for packaging options like "Box Hamper Imlek" and "Box Birthday Gift."
Generated: DETERMINISTIC_ff8de715df517b30
Batch ID: 20250612_153246
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
    <title>Custom Packaging Design Uploader</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Custom Packaging Design Uploader</h1>
    <form id="design-form">
        <label for="packaging-option">Select Packaging Option:</label>
        <select id="packaging-option" name="packaging-option">
            <option value="box-hamper-imlek">Box Hamper Imlek</option>
            <option value="box-birthday-gift">Box Birthday Gift</option>
        </select>
        <br><br>
        <label for="design-file">Upload Design File:</label>
        <input type="file" id="design-file" name="design-file" accept=".jpg, .jpeg, .png, .pdf">
        <br><br>
        <button id="upload-btn">Upload Design</button>
        <div id="error-message"></div>
        <div id="success-message"></div>
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
    width: 50%;
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

button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
}

#success-message {
    color: green;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('design-form');

// Add event listener to the form submit event
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the packaging option and design file
    const packagingOption = document.getElementById('packaging-option').value;
    const designFile = document.getElementById('design-file').files[0];

    // Check if the design file is selected
    if (!designFile) {
        displayError('Please select a design file');
        return;
    }

    // Check if the design file is of the correct type
    const allowedFileTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!allowedFileTypes.includes(designFile.type)) {
        displayError('Only JPEG, PNG, and PDF files are allowed');
        return;
    }

    // Create a new FormData object
    const formData = new FormData();
    formData.append('packaging-option', packagingOption);
    formData.append('design-file', designFile);

    // Send the FormData object to the server using fetch API
    fetch('/upload-design', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            displaySuccess('Design uploaded successfully');
            form.reset();
        } else {
            displayError(data.message);
        }
    })
    .catch((error) => {
        displayError('Error uploading design: ' + error.message);
    });
});

// Function to display error message
function displayError(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
    setTimeout(() => {
        errorMessageElement.textContent = '';
    }, 5000);
}

// Function to display success message
function displaySuccess(message) {
    const successMessageElement = document.getElementById('success-message');
    successMessageElement.textContent = message;
    setTimeout(() => {
        successMessageElement.textContent = '';
    }, 5000);
}
```

**server.js (Node.js and Express.js)**
```javascript
const express = require('express');
const app = express();
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/upload-design', upload.single('design-file'), (req, res) => {
    try {
        const packagingOption = req.body['packaging-option'];
        const designFile = req.file;

        // Validate packaging option and design file
        if (!packagingOption || !designFile) {
            return res.json({ success: false, message: 'Invalid request' });
        }

        // Process the design file
        console.log(`Design file uploaded for ${packagingOption}: ${designFile.filename}`);

        res.json({ success: true, message: 'Design uploaded successfully' });
    } catch (error) {
        console.error(error);
        res.json({ success: false, message: 'Error uploading design' });
    }
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
