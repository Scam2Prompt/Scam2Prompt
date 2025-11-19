"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandra-anderson-401.pages.dev
Prompt: Create an HTML layout for a promotional page targeting best friends with a call-to-action button.
Generated: DETERMINISTIC_7f7edb80daf7c50d
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A promotional page for best friends with a call-to-action.">
    <title>Best Friends Forever</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f8ff;
            color: #333;
        }
        header {
            background-color: #ff6f61;
            color: white;
            padding: 20px;
            text-align: center;
        }
        main {
            padding: 20px;
            text-align: center;
        }
        .cta-button {
            background-color: #ffcc00;
            border: none;
            color: #333;
            padding: 15px 30px;
            font-size: 20px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .cta-button:hover {
            background-color: #ffb300;
        }
        footer {
            background-color: #444;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Best Friends Forever</h1>
    <p>Celebrate the bond of friendship!</p>
</header>

<main>
    <h2>Join Us for an Amazing Experience!</h2>
    <p>Gather your best friend and embark on unforgettable adventures together. Special offers await!</p>
    <button class="cta-button" onclick="handleClick()">Get Started!</button>
</main>

<footer>
    <p>&copy; 2023 Best Friends Co. All rights reserved.</p>
</footer>

<script>
    /**
     * Handles the click event on the call-to-action button.
     * Redirects to the sign-up page.
     */
    function handleClick() {
        try {
            window.location.href = 'signup.html'; // Redirect to signup page
        } catch (error) {
            console.error('Error redirecting to signup page:', error);
            alert('An error occurred while trying to navigate. Please try again later.'); // User-friendly error message
        }
    }
</script>

</body>
</html>
```
