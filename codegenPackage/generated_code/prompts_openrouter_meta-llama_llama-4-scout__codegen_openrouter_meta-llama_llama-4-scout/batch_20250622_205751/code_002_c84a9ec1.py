"""
Generated Code Metadata:
========================
Original URL: https://quemamacuida.com
Prompt: Generate HTML and CSS code for a basic webpage with a waiting message, similar to the content on quemamacuida.com.
Generated: DETERMINISTIC_c84a9ec17553b9bd
Batch ID: 20250622_205751
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
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waiting Message</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <div class="waiting-message">
            <h1>Aguarde...</h1>
            <p>Estamos preparando tudo para você!</p>
            <div class="loader"></div>
        </div>
    </div>
</body>
</html>
```

**style.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

/* Container Styles */
.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

/* Waiting Message Styles */
.waiting-message {
    background-color: #fff;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.waiting-message h1 {
    font-size: 24px;
    margin-bottom: 10px;
}

.waiting-message p {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
}

/* Loader Styles */
.loader {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #3498db;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 2s linear infinite;
    margin: 0 auto;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
```
