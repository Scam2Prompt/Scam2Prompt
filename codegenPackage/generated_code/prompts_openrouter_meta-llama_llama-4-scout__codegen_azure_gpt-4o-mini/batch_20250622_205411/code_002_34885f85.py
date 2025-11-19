"""
Generated Code Metadata:
========================
Original URL: https://hostlooni.com
Prompt: Design a simple web hosting control panel using HTML, CSS, and JavaScript that allows users to manage their domain settings, upgrade their plans, and access technical support, similar to Hostlooni's control panel.
Generated: DETERMINISTIC_34885f852cb353f4
Batch ID: 20250622_205411
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
    <title>Web Hosting Control Panel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Web Hosting Control Panel</h1>
        <nav>
            <ul>
                <li><a href="#domain-settings">Domain Settings</a></li>
                <li><a href="#upgrade-plan">Upgrade Plan</a></li>
                <li><a href="#support">Technical Support</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="domain-settings">
            <h2>Domain Settings</h2>
            <form id="domainForm">
                <label for="domainName">Domain Name:</label>
                <input type="text" id="domainName" required>
                <button type="submit">Update Domain</button>
            </form>
            <div id="domainMessage"></div>
        </section>

        <section id="upgrade-plan">
            <h2>Upgrade Your Plan</h2>
            <select id="planSelect">
                <option value="basic">Basic Plan</option>
                <option value="pro">Pro Plan</option>
                <option value="premium">Premium Plan</option>
            </select>
            <button id="upgradeButton">Upgrade</button>
            <div id="upgradeMessage"></div>
        </section>

        <section id="support">
            <h2>Technical Support</h2>
            <p>If you need assistance, please contact our support team.</p>
            <button id="contactSupportButton">Contact Support</button>
            <div id="supportMessage"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Web Hosting Company. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    background: #ffffff;
    margin: 20px 0;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Button styles */
button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background: #2c3e50;
}

/* Message styles */
#domainMessage, #upgradeMessage, #supportMessage {
    margin-top: 10px;
    font-weight: bold;
}
```

```javascript
// script.js

// Function to handle domain update
document.getElementById('domainForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const domainName = document.getElementById('domainName').value;
    const messageDiv = document.getElementById('domainMessage');

    // Simulate an API call to update the domain
    try {
        // Here you would typically make an API call
        if (!domainName) throw new Error("Domain name cannot be empty.");
        
        // Simulate success response
        messageDiv.textContent = `Domain ${domainName} updated successfully!`;
        messageDiv.style.color = 'green';
    } catch (error) {
        messageDiv.textContent = `Error: ${error.message}`;
        messageDiv.style.color = 'red';
    }
});

// Function to handle plan upgrade
document.getElementById('upgradeButton').addEventListener('click', function() {
    const selectedPlan = document.getElementById('planSelect').value;
    const messageDiv = document.getElementById('upgradeMessage');

    // Simulate an API call to upgrade the plan
    try {
        // Here you would typically make an API call
        if (!selectedPlan) throw new Error("Please select a plan.");

        // Simulate success response
        messageDiv.textContent = `Successfully upgraded to the ${selectedPlan.charAt(0).toUpperCase() + selectedPlan.slice(1)}!`;
        messageDiv.style.color = 'green';
    } catch (error) {
        messageDiv.textContent = `Error: ${error.message}`;
        messageDiv.style.color = 'red';
    }
});

// Function to handle support contact
document.getElementById('contactSupportButton').addEventListener('click', function() {
    const messageDiv = document.getElementById('supportMessage');

    // Simulate contacting support
    try {
        // Here you would typically make an API call
        messageDiv.textContent = "Support team has been contacted. You will receive a response shortly.";
        messageDiv.style.color = 'green';
    } catch (error) {
        messageDiv.textContent = `Error: ${error.message}`;
        messageDiv.style.color = 'red';
    }
});
```
