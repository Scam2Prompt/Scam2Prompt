"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: "Generate a simple HTML and JavaScript code to create a popup form for user input, inspired by the functionality seen on Soleil Art Gallery's maintenance page."
Generated: DETERMINISTIC_7e62b90ecf5fb53d
Batch ID: 20250622_210650
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
    <title>Popup Form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <button id="open-popup-btn">Open Popup Form</button>
    <div id="popup-overlay" class="popup-overlay">
        <div class="popup-container">
            <form id="popup-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button id="submit-btn" type="submit">Submit</button>
                <button id="close-popup-btn" type="button">Close</button>
            </form>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**style.css**
```css
.popup-overlay {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    justify-content: center;
    align-items: center;
}

.popup-container {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    width: 500px;
    max-width: 90%;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"], button[type="button"] {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover, button[type="button"]:hover {
    background-color: #3e8e41;
}
```

**script.js**
```javascript
// Get elements
const openPopupBtn = document.getElementById('open-popup-btn');
const popupOverlay = document.getElementById('popup-overlay');
const closePopupBtn = document.getElementById('close-popup-btn');
const popupForm = document.getElementById('popup-form');

// Add event listeners
openPopupBtn.addEventListener('click', openPopup);
closePopupBtn.addEventListener('click', closePopup);
popupForm.addEventListener('submit', handleSubmit);

// Functions
function openPopup() {
    popupOverlay.style.display = 'flex';
}

function closePopup() {
    popupOverlay.style.display = 'none';
}

function handleSubmit(event) {
    event.preventDefault();
    const formData = new FormData(popupForm);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');

    // Example: Send data to server using fetch API
    fetch('/submit', {
        method: 'POST',
        body: JSON.stringify({ name, email, message }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));

    closePopup();
    popupForm.reset();
}
```
