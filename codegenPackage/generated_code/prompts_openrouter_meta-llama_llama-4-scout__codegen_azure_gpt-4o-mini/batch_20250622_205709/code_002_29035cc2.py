"""
Generated Code Metadata:
========================
Original URL: https://institutovidaesportiva.com.br
Prompt: Generate a code snippet in JavaScript to create a simple webpage that displays the services offered by Instituto Vida Esportiva, including Medicina de Performance, Emagrecimento, and Dor e Lesão.
Generated: DETERMINISTIC_29035cc2c698aee0
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instituto Vida Esportiva - Serviços</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        header {
            background: #007BFF;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        .service-list {
            list-style-type: none;
            padding: 0;
        }
        .service-item {
            background: white;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<header>
    <h1>Instituto Vida Esportiva</h1>
    <h2>Serviços Oferecidos</h2>
</header>

<main>
    <ul class="service-list" id="serviceList">
        <!-- Services will be dynamically inserted here -->
    </ul>
</main>

<script>
    // Array of services offered by Instituto Vida Esportiva
    const services = [
        "Medicina de Performance",
        "Emagrecimento",
        "Dor e Lesão"
    ];

    // Function to display services on the webpage
    function displayServices() {
        const serviceList = document.getElementById('serviceList');

        // Check if the service list element exists
        if (!serviceList) {
            console.error('Element with id "serviceList" not found.');
            return;
        }

        // Iterate over the services array and create list items
        services.forEach(service => {
            const listItem = document.createElement('li');
            listItem.className = 'service-item';
            listItem.textContent = service;
            serviceList.appendChild(listItem);
        });
    }

    // Call the function to display services
    displayServices();
</script>

</body>
</html>
```
