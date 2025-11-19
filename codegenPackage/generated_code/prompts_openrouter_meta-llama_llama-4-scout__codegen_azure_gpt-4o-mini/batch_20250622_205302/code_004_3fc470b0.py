"""
Generated Code Metadata:
========================
Original URL: https://unisate.space
Prompt: "Create a simple webpage with a terms of service and privacy policy link using JavaScript, HTML, and CSS."
Generated: DETERMINISTIC_3fc470b01c38bc0b
Batch ID: 20250622_205302
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
    <title>Terms of Service and Privacy Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
    </header>
    <main>
        <section>
            <h2>Terms of Service</h2>
            <p>By using this website, you agree to the following terms...</p>
            <a href="#termsModal" class="modal-link" onclick="openModal('termsModal')">Read Full Terms of Service</a>
        </section>
        <section>
            <h2>Privacy Policy</h2>
            <p>Your privacy is important to us. Please review our policy...</p>
            <a href="#privacyModal" class="modal-link" onclick="openModal('privacyModal')">Read Full Privacy Policy</a>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Your Company. All rights reserved.</p>
    </footer>

    <!-- Modal for Terms of Service -->
    <div id="termsModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('termsModal')">&times;</span>
            <h2>Terms of Service</h2>
            <p>Full terms of service content goes here...</p>
        </div>
    </div>

    <!-- Modal for Privacy Policy -->
    <div id="privacyModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('privacyModal')">&times;</span>
            <h2>Privacy Policy</h2>
            <p>Full privacy policy content goes here...</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Modal styling */
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal content styling */
.modal-content {
    background-color: #fefefe;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
}

/* Close button styling */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
```

```javascript
// script.js

/**
 * Opens the specified modal by setting its display to block.
 * @param {string} modalId - The ID of the modal to open.
 */
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "block";
    } else {
        console.error(`Modal with ID ${modalId} not found.`);
    }
}

/**
 * Closes the specified modal by setting its display to none.
 * @param {string} modalId - The ID of the modal to close.
 */
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none";
    } else {
        console.error(`Modal with ID ${modalId} not found.`);
    }
}

// Close modals when clicking outside of them
window.onclick = function(event) {
    const termsModal = document.getElementById('termsModal');
    const privacyModal = document.getElementById('privacyModal');
    if (event.target === termsModal) {
        closeModal('termsModal');
    } else if (event.target === privacyModal) {
        closeModal('privacyModal');
    }
};
```
