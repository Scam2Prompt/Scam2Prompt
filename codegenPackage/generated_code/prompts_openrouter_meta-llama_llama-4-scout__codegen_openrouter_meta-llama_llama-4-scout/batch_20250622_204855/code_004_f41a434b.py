"""
Generated Code Metadata:
========================
Original URL: https://bitkub-claim-bitcoin-bonus.kesug.com
Prompt: Design a simple web cPanel interface using HTML, CSS, and JavaScript that could be used for managing iFastNet Web Hosting services.
Generated: DETERMINISTIC_f41a434be697c1e8
Batch ID: 20250622_204855
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
    <title>iFastNet Web Hosting cPanel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#domains">Domains</a></li>
                <li><a href="#email">Email</a></li>
                <li><a href="#files">File Manager</a></li>
                <li><a href="#settings">Settings</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="domains">
            <h2>Domains</h2>
            <table id="domain-table">
                <thead>
                    <tr>
                        <th>Domain Name</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="domain-tbody">
                    <!-- domains will be populated here -->
                </tbody>
            </table>
            <button id="add-domain-btn">Add Domain</button>
            <form id="add-domain-form" style="display: none;">
                <input type="text" id="domain-name" placeholder="Enter domain name">
                <button id="submit-domain-btn">Submit</button>
            </form>
        </section>
        <section id="email">
            <h2>Email Accounts</h2>
            <table id="email-table">
                <thead>
                    <tr>
                        <th>Email Address</th>
                        <th>Quota</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="email-tbody">
                    <!-- email accounts will be populated here -->
                </tbody>
            </table>
            <button id="add-email-btn">Add Email Account</button>
            <form id="add-email-form" style="display: none;">
                <input type="email" id="email-address" placeholder="Enter email address">
                <input type="number" id="email-quota" placeholder="Enter quota">
                <button id="submit-email-btn">Submit</button>
            </form>
        </section>
        <section id="files">
            <h2>File Manager</h2>
            <iframe id="file-manager-iframe" src="file-manager.html" frameborder="0" width="100%" height="500"></iframe>
        </section>
        <section id="settings">
            <h2>Settings</h2>
            <form id="settings-form">
                <label for="password">Change Password:</label>
                <input type="password" id="password" placeholder="Enter new password">
                <button id="submit-settings-btn">Submit</button>
            </form>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

button {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}

form {
    margin-top: 20px;
}

input[type="text"], input[type="email"], input[type="number"], input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
```

**script.js**
```javascript
// Get elements
const domainTable = document.getElementById('domain-table');
const domainTbody = document.getElementById('domain-tbody');
const addDomainBtn = document.getElementById('add-domain-btn');
const addDomainForm = document.getElementById('add-domain-form');
const submitDomainBtn = document.getElementById('submit-domain-btn');
const domainNameInput = document.getElementById('domain-name');

const emailTable = document.getElementById('email-table');
const emailTbody = document.getElementById('email-tbody');
const addEmailBtn = document.getElementById('add-email-btn');
const addEmailForm = document.getElementById('add-email-form');
const submitEmailBtn = document.getElementById('submit-email-btn');
const emailAddressInput = document.getElementById('email-address');
const emailQuotaInput = document.getElementById('email-quota');

const settingsForm = document.getElementById('settings-form');
const submitSettingsBtn = document.getElementById('submit-settings-btn');
const passwordInput = document.getElementById('password');

// Mock data for demonstration purposes
const domains = [
    { name: 'example.com', status: 'active' },
    { name: 'test.com', status: 'inactive' },
];

const emailAccounts = [
    { email: 'user@example.com', quota: 100 },
    { email: 'user2@example.com', quota: 200 },
];

// Populate domain table
domains.forEach((domain) => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${domain.name}</td>
        <td>${domain.status}</td>
        <td><button class="action-btn">Manage</button></td>
    `;
    domainTbody.appendChild(row);
});

// Populate email table
emailAccounts.forEach((emailAccount) => {
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${emailAccount.email}</td>
        <td>${emailAccount.quota}</td>
        <td><button class="action-btn">Manage</button></td>
    `;
    emailTbody.appendChild(row);
});

// Add event listeners
addDomainBtn.addEventListener('click', () => {
    addDomainForm.style.display = 'block';
});

submitDomainBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const domainName = domainNameInput.value;
    // Add domain logic here
    console.log(`Adding domain: ${domainName}`);
});

addEmailBtn.addEventListener('click', () => {
    addEmailForm.style.display = 'block';
});

submitEmailBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const emailAddress = emailAddressInput.value;
    const emailQuota = emailQuotaInput.value;
    // Add email account logic here
    console.log(`Adding email account: ${emailAddress} with quota ${emailQuota}`);
});

submitSettingsBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const password = passwordInput.value;
    // Change password logic here
    console.log(`Changing password: ${password}`);
});
```

**file-manager.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Manager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #file-list {
            padding: 1em;
        }
        #file-list ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }
        #file-list li {
            padding: 10px;
            border-bottom: 1px solid #ccc;
        }
        #file-list li:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <div id="file-list">
        <h2>File Manager</h2>
        <ul id="file-list-ul">
            <!-- files will be listed here -->
        </ul>
    </div>
    <script>
        // Mock data for demonstration purposes
        const files = [
            { name: 'index.html', type: 'file' },
            {
