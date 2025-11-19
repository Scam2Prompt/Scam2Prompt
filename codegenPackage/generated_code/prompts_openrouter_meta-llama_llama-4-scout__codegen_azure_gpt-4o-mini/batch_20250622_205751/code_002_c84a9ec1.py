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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Waiting Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="message">
            <h1>Estamos preparando algo especial para você!</h1>
            <p>Aguarde um momento enquanto carregamos a informação.</p>
            <div class="loader"></div>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Set the body to use full viewport height */
body {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background-color: #f0f0f0; /* Light background color */
}

/* Container for the waiting message */
.container {
    text-align: center;
}

/* Style for the main message */
.message h1 {
    font-size: 2.5rem;
    color: #333; /* Dark text color */
    margin-bottom: 10px;
}

/* Style for the sub-message */
.message p {
    font-size: 1.2rem;
    color: #666; /* Lighter text color */
    margin-bottom: 20px;
}

/* Loader animation */
.loader {
    border: 8px solid #f3f3f3; /* Light grey */
    border-top: 8px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1s linear infinite; /* Spin animation */
}

/* Keyframes for the loader animation */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```
