"""
Generated Code Metadata:
========================
Original URL: https://extenso-mayotte.fr
Prompt: How can I implement a temporary maintenance page using HTML and CSS?
Generated: DETERMINISTIC_d117db6faf3aa15e
Batch ID: 20250612_135409
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
    <title>Temporary Maintenance Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="maintenance-container">
        <h1>Temporarily Unavailable</h1>
        <p>We are currently performing maintenance. Please check back later.</p>
        <p id="countdown">Redirecting in 30 seconds...</p>
    </div>

    <script>
        // Redirect to homepage after 30 seconds
        const countdownElement = document.getElementById('countdown');
        let seconds = 30;
        const intervalId = setInterval(() => {
            if (seconds > 0) {
                countdownElement.textContent = `Redirecting in ${seconds} seconds...`;
                seconds--;
            } else {
                clearInterval(intervalId);
                // Replace with your actual homepage URL
                window.location.href = '/';
            }
        }, 1000);
    </script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.maintenance-container {
    text-align: center;
    background-color: #fff;
    padding: 40px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.maintenance-container h1 {
    color: #333;
}

.maintenance-container p {
    color: #666;
    margin-bottom: 20px;
}
```
