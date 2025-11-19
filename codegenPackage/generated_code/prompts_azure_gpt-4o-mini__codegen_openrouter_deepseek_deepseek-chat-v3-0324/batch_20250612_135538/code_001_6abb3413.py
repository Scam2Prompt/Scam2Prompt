"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: How can I implement a multilingual maintenance page in HTML/CSS that includes messages in Italian, English, and Spanish, as seen on the Giorgiobarbagelata site?
Generated: DETERMINISTIC_6abb34137f6c801f
Batch ID: 20250612_135538
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
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .maintenance-container {
            max-width: 800px;
            width: 100%;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 40px;
            text-align: center;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #2c3e50;
        }
        
        p {
            font-size: 1.1rem;
            margin-bottom: 30px;
        }
        
        .language-selector {
            margin-bottom: 30px;
        }
        
        .language-btn {
            background: none;
            border: 1px solid #ddd;
            padding: 8px 16px;
            margin: 0 5px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .language-btn:hover {
            background-color: #f0f0f0;
        }
        
        .language-btn.active {
            background-color: #3498db;
            color: white;
            border-color: #3498db;
        }
        
        .logo {
            max-width: 200px;
            margin-bottom: 30px;
        }
        
        .contact-info {
            margin-top: 30px;
            font-style: italic;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <img src="logo.png" alt="Company Logo" class="logo">
        
        <div class="language-selector">
            <button class="language-btn active" data-lang="en">English</button>
            <button class="language-btn" data-lang="it">Italiano</button>
            <button class="language-btn" data-lang="es">Español</button>
        </div>
        
        <div id="en" class="language-content">
            <h1>Maintenance in Progress</h1>
            <p>We're currently performing scheduled maintenance on our website. We apologize for any inconvenience and appreciate your patience.</p>
            <p>Our team is working hard to improve your experience. The site will be back online shortly.</p>
            <p class="contact-info">For urgent inquiries, please contact us at support@example.com</p>
        </div>
        
        <div id="it" class="language-content" style="display: none;">
            <h1>Manutenzione in Corso</h1>
            <p>Stiamo eseguendo una manutenzione programmata sul nostro sito web. Ci scusiamo per eventuali disagi e apprezziamo la vostra pazienza.</p>
            <p>Il nostro team sta lavorando duramente per migliorare la vostra esperienza. Il sito tornerà online a breve.</p>
            <p class="contact-info">Per richieste urgenti, contattateci all'indirizzo support@example.com</p>
        </div>
        
        <div id="es" class="language-content" style="display: none;">
            <h1>Mantenimiento en Progreso</h1>
            <p>Actualmente estamos realizando un mantenimiento programado en nuestro sitio web. Nos disculpamos por cualquier inconveniente y agradecemos su paciencia.</p>
            <p>Nuestro equipo está trabajando duro para mejorar su experiencia. El sitio volverá a estar en línea en breve.</p>
            <p class="contact-info">Para consultas urgentes, contáctenos en support@example.com</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const languageButtons = document.querySelectorAll('.language-btn');
            const languageContents = document.querySelectorAll('.language-content');
            
            languageButtons.forEach(button => {
                button.addEventListener('click', function() {
                    // Remove active class from all buttons
                    languageButtons.forEach(btn => btn.classList.remove('active'));
                    
                    // Add active class to clicked button
                    this.classList.add('active');
                    
                    // Hide all language contents
                    languageContents.forEach(content => {
                        content.style.display = 'none';
                    });
                    
                    // Show selected language content
                    const lang = this.getAttribute('data-lang');
                    document.getElementById(lang).style.display = 'block';
                });
            });
            
            // Check browser language preference
            const userLang = navigator.language || navigator.userLanguage;
            const supportedLangs = ['en', 'it', 'es'];
            const defaultLang = 'en';
            
            if (supportedLangs.includes(userLang.substring(0, 2))) {
                const langToShow = userLang.substring(0, 2);
                document.querySelector(`.language-btn[data-lang="${langToShow}"]`).click();
            }
        });
    </script>
</body>
</html>
```
