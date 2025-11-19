"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Generate code in JavaScript to display a list of automotive service center addresses dynamically, including locations such as Passo Fundo and Novo Hamburgo, using data from a JSON file.
Generated: DETERMINISTIC_c22f435eba819af9
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Fetch and display automotive service center addresses from JSON data
document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const serviceCentersList = document.getElementById('service-centers-list');
    const loadingIndicator = document.getElementById('loading-indicator');
    const errorMessage = document.getElementById('error-message');

    // Function to fetch JSON data
    async function fetchServiceCenters() {
        try {
            loadingIndicator.style.display = 'block';
            errorMessage.style.display = 'none';

            const response = await fetch('service-centers.json');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            displayServiceCenters(data);
        } catch (error) {
            console.error('Error fetching service centers:', error);
            errorMessage.textContent = 'Failed to load service centers. Please try again later.';
            errorMessage.style.display = 'block';
        } finally {
            loadingIndicator.style.display = 'none';
        }
    }

    // Function to display service centers
    function displayServiceCenters(centers) {
        if (!Array.isArray(centers) || centers.length === 0) {
            errorMessage.textContent = 'No service centers available.';
            errorMessage.style.display = 'block';
            return;
        }

        serviceCentersList.innerHTML = centers.map(center => `
            <li class="service-center-item">
                <h3>${center.name}</h3>
                <p>${center.address}</p>
                <p>${center.city}, ${center.state}</p>
                <p>Phone: ${center.phone}</p>
            </li>
        `).join('');
    }

    // Initialize
    fetchServiceCenters();
});
```

```html
<!-- Example HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automotive Service Centers</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        #service-centers-list {
            list-style: none;
            padding: 0;
        }
        .service-center-item {
            background: #f4f4f4;
            margin-bottom: 10px;
            padding: 15px;
            border-radius: 5px;
        }
        #loading-indicator, #error-message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            text-align: center;
        }
        #loading-indicator {
            background: #ffffe0;
            display: none;
        }
        #error-message {
            background: #ffdddd;
            color: #d8000c;
            display: none;
        }
    </style>
</head>
<body>
    <h1>Automotive Service Centers</h1>
    <div id="loading-indicator">Loading service centers...</div>
    <div id="error-message"></div>
    <ul id="service-centers-list"></ul>

    <script src="script.js"></script>
</body>
</html>
```

```json
// Example service-centers.json
[
    {
        "name": "Passo Fundo Auto Service",
        "address": "Rua Tiradentes, 1234",
        "city": "Passo Fundo",
        "state": "RS",
        "phone": "(54) 1234-5678"
    },
    {
        "name": "Novo Hamburgo Car Care",
        "address": "Avenida Brasil, 567",
        "city": "Novo Hamburgo",
        "state": "RS",
        "phone": "(51) 9876-5432"
    },
    {
        "name": "Porto Alegre Automotive",
        "address": "Rua dos Andradas, 789",
        "city": "Porto Alegre",
        "state": "RS",
        "phone": "(51) 3456-7890"
    }
]
```
