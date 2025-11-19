"""
Generated Code Metadata:
========================
Original URL: https://bitsoft360.de
Prompt: Suggest tools or frameworks for creating a responsive domain details page with JavaScript.
Generated: DETERMINISTIC_24d13523f177f76b
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries (assuming Node.js environment)
const express = require('express');
const path = require('path');
const axios = require('axios');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON and urlencoded form data
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// API endpoint to fetch domain details
app.get('/api/domain/:domainName', async (req, res) => {
    try {
        const { domainName } = req.params;
        
        // Validate domain name
        if (!domainName || !/^[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$/.test(domainName)) {
            return res.status(400).json({ error: 'Invalid domain name' });
        }

        // In a real app, you would call a domain API here
        // This is a mock response for demonstration
        const mockResponse = {
            domain: domainName,
            status: 'active',
            creationDate: '2020-01-01',
            expirationDate: '2025-01-01',
            registrar: 'Example Registrar',
            nameservers: ['ns1.example.com', 'ns2.example.com']
        };

        res.json(mockResponse);
    } catch (error) {
        console.error('Error fetching domain details:', error);
        res.status(500).json({ error: 'Failed to fetch domain details' });
    }
});

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Frontend code (public/js/app.js)
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('domainForm');
    const resultsDiv = document.getElementById('results');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const domainInput = document.getElementById('domainInput');
        const domainName = domainInput.value.trim();
        
        if (!domainName) {
            alert('Please enter a domain name');
            return;
        }
        
        try {
            const response = await fetch(`/api/domain/${encodeURIComponent(domainName)}`);
            const data = await response.json();
            
            if (response.ok) {
                displayResults(data);
            } else {
                resultsDiv.innerHTML = `<div class="error">${data.error}</div>`;
            }
        } catch (error) {
            console.error('Error:', error);
            resultsDiv.innerHTML = '<div class="error">Failed to fetch domain details</div>';
        }
    });
    
    function displayResults(data) {
        resultsDiv.innerHTML = `
            <div class="card">
                <h2>${data.domain}</h2>
                <p><strong>Status:</strong> ${data.status}</p>
                <p><strong>Creation Date:</strong> ${data.creationDate}</p>
                <p><strong>Expiration Date:</strong> ${data.expirationDate}</p>
                <p><strong>Registrar:</strong> ${data.registrar}</p>
                <p><strong>Nameservers:</strong> ${data.nameservers.join(', ')}</p>
            </div>
        `;
    }
});

// HTML template (public/index.html)
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Details</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div class="container">
        <h1>Domain Details Lookup</h1>
        <form id="domainForm">
            <input type="text" id="domainInput" placeholder="Enter domain name (e.g., example.com)" required>
            <button type="submit">Search</button>
        </form>
        <div id="results"></div>
    </div>
    <script src="js/app.js"></script>
</body>
</html>
*/

// CSS template (public/css/styles.css)
/*
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
    color: #333;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    text-align: center;
    color: #2c3e50;
}

form {
    display: flex;
    margin-bottom: 20px;
}

input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
}

button {
    padding: 10px 20px;
    background: #3498db;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background: #2980b9;
}

.card {
    background: #f9f9f9;
    border-radius: 5px;
    padding: 20px;
    margin-top: 20px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.error {
    color: #e74c3c;
    padding: 10px;
    background: #fadbd8;
    border-radius: 5px;
}

@media (max-width: 600px) {
    form {
        flex-direction: column;
    }
    
    input, button {
        width: 100%;
        margin-bottom: 10px;
    }
}
*/
```
