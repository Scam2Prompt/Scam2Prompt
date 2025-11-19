"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Generate a multilingual maintenance page message, including English, Italian, and Spanish, for a personal website.
Generated: DETERMINISTIC_d02f92869f8d0a37
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
    <title>Maintenance Mode</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #e74c3c;
        }
        .language-selector {
            margin: 20px 0;
        }
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .message {
            display: none;
        }
        .active {
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚧 Maintenance Mode</h1>
        
        <div class="language-selector">
            <select id="languageSelector">
                <option value="en">English</option>
                <option value="it">Italiano</option>
                <option value="es">Español</option>
            </select>
        </div>

        <div id="en" class="message active">
            <p>We're currently performing scheduled maintenance on our website.</p>
            <p>We apologize for the inconvenience and appreciate your patience.</p>
            <p>The site will be back online shortly.</p>
        </div>

        <div id="it" class="message">
            <p>Stiamo attualmente eseguendo la manutenzione programmata del nostro sito web.</p>
            <p>Ci scusiamo per l'inconveniente e apprezziamo la vostra pazienza.</p>
            <p>Il sito tornerà online a breve.</p>
        </div>

        <div id="es" class="message">
            <p>Actualmente estamos realizando mantenimiento programado en nuestro sitio web.</p>
            <p>Nos disculpamos por las molestias y agradecemos su paciencia.</p>
            <p>El sitio volverá a estar en línea en breve.</p>
        </div>

        <p><small>Last updated: <span id="updateDate"></span></small></p>
    </div>

    <script>
        // Set last updated date
        document.getElementById('updateDate').textContent = new Date().toLocaleString();

        // Language selector functionality
        document.getElementById('languageSelector').addEventListener('change', function() {
            // Hide all messages
            document.querySelectorAll('.message').forEach(el => {
                el.classList.remove('active');
            });
            
            // Show selected message
            const selectedLanguage = this.value;
            document.getElementById(selectedLanguage).classList.add('active');
        });
    </script>
</body>
</html>
```
