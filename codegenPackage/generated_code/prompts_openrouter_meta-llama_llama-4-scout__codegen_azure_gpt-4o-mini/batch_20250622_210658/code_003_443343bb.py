"""
Generated Code Metadata:
========================
Original URL: https://babydoge-paws.web.app
Prompt: Design a simple front-end interface using HTML/CSS that informs users they are in line for a $PAWS token airdrop and instructs them not to close the page during the distribution process.
Generated: DETERMINISTIC_443343bb3036a2bd
Batch ID: 20250622_210658
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
    <title>$PAWS Token Airdrop</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to the $PAWS Token Airdrop!</h1>
        <p class="instruction">You are currently in line for your $PAWS tokens.</p>
        <p class="warning">Please do not close this page during the distribution process.</p>
        <div class="loader"></div>
    </div>
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

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container styling */
.container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Heading styling */
h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
}

/* Instruction text styling */
.instruction {
    font-size: 1.2em;
    margin-bottom: 10px;
}

/* Warning text styling */
.warning {
    font-size: 1em;
    color: #d9534f; /* Bootstrap danger color */
    margin-bottom: 20px;
}

/* Loader styling */
.loader {
    border: 8px solid #f3f3f3; /* Light grey */
    border-top: 8px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1s linear infinite;
}

/* Animation for the loader */
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```
