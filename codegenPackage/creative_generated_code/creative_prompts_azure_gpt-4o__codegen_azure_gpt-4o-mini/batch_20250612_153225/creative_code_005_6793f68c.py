"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica16.vercel.app
Prompt: Write code for a modal window that allows users to select a blockchain network (Solana, Ethereum, Polygon) and integrates it into a login system, inspired by Matrica's design.
Generated: DETERMINISTIC_6793f68c1d081cdb
Batch ID: 20250612_153225
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
    <title>Blockchain Network Modal</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <button id="loginButton">Login</button>

    <!-- Modal Structure -->
    <div id="networkModal" class="modal">
        <div class="modal-content">
            <span class="close-button">&times;</span>
            <h2>Select a Blockchain Network</h2>
            <form id="networkForm">
                <label for="networkSelect">Choose a network:</label>
                <select id="networkSelect" required>
                    <option value="" disabled selected>Select a network</option>
                    <option value="solana">Solana</option>
                    <option value="ethereum">Ethereum</option>
                    <option value="polygon">Polygon</option>
                </select>
                <button type="submit">Continue</button>
            </form>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the modal */
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgba(0, 0, 0, 0.5); /* Black background with opacity */
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
}

.close-button {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close-button:hover,
.close-button:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
```

```javascript
// script.js

document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.getElementById('loginButton');
    const modal = document.getElementById('networkModal');
    const closeButton = document.querySelector('.close-button');
    const networkForm = document.getElementById('networkForm');

    // Function to open modal
    const openModal = () => {
        modal.style.display = 'block';
    };

    // Function to close modal
    const closeModal = () => {
        modal.style.display = 'none';
    };

    // Event listener for the login button to open the modal
    loginButton.addEventListener('click', openModal);
    
    // Event listener for the close button to close the modal
    closeButton.addEventListener('click', closeModal);
    
    // Event listener for form submission
    networkForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission
        const selectedNetwork = document.getElementById('networkSelect').value;

        // Basic error handling for network selection
        if (!selectedNetwork) {
            alert('Please select a blockchain network');
            return;
        }

        // Proceed with login logic here
        console.log(`Logging in with the ${selectedNetwork} network`);

        // Close the modal after selection
        closeModal();
    });

    // Close modal if the user clicks outside of it
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });
});
```
