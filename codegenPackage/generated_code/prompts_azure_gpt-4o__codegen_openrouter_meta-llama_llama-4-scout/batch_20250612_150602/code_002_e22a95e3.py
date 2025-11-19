"""
Generated Code Metadata:
========================
Original URL: https://bonkbox-claim.web.app
Prompt: Develop a web application using JavaScript that mimics the BONKBOXES whitelist system, including a feature that prompts users to enable JavaScript.
Generated: DETERMINISTIC_e22a95e36cb15c48
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <titleBONKBOXES Whitelist System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <noscript>
        <div id="noscript-overlay">
            <h1>JavaScript is required</h1>
            <p>Please enable JavaScript to access this application.</p>
        </div>
    </noscript>
    <div id="app"></div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
}

#noscript-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

#noscript-overlay h1 {
    font-size: 24px;
    margin-bottom: 16px;
}

#app {
    display: none;
}
```

```javascript
// script.js
class BonkboxWhitelistSystem {
    /**
     * Initialize the whitelist system.
     */
    constructor() {
        this.whitelist = [];
        this.userInput = null;
        this.init();
    }

    /**
     * Initialize the application.
     */
    init() {
        this.checkJavaScriptEnabled();
        this.renderApp();
        this.addEventListeners();
    }

    /**
     * Check if JavaScript is enabled.
     */
    checkJavaScriptEnabled() {
        const noscriptOverlay = document.getElementById('noscript-overlay');
        if (noscriptOverlay) {
            noscriptOverlay.style.display = 'none';
        }
        document.getElementById('app').style.display = 'block';
    }

    /**
     * Render the application.
     */
    renderApp() {
        const appContainer = document.getElementById('app');
        appContainer.innerHTML = `
            <h1>BONKBOXES Whitelist System</h1>
            <input id="user-input" type="text" placeholder="Enter your ID">
            <button id="submit-btn">Submit</button>
            <div id="result"></div>
        `;
    }

    /**
     * Add event listeners.
     */
    addEventListeners() {
        const submitBtn = document.getElementById('submit-btn');
        submitBtn.addEventListener('click', () => this.checkWhitelist());
    }

    /**
     * Check if the user's ID is in the whitelist.
     */
    checkWhitelist() {
        try {
            this.userInput = document.getElementById('user-input').value.trim();
            if (!this.userInput) {
                this.showError('Please enter your ID');
                return;
            }
            if (this.whitelist.includes(this.userInput)) {
                this.showSuccess('You are whitelisted!');
            } else {
                this.showError('You are not whitelisted');
            }
        } catch (error) {
            console.error(error);
            this.showError('An error occurred');
        }
    }

    /**
     * Show a success message.
     * @param {string} message - The message to display.
     */
    showSuccess(message) {
        document.getElementById('result').innerHTML = `
            <p style="color: green;">${message}</p>
        `;
    }

    /**
     * Show an error message.
     * @param {string} message - The message to display.
     */
    showError(message) {
        document.getElementById('result').innerHTML = `
            <p style="color: red;">${message}</p>
        `;
    }
}

// Initialize the whitelist system
const whitelistSystem = new BonkboxWhitelistSystem();
whitelistSystem.whitelist = ['user123', 'user456']; // Example whitelist
```
