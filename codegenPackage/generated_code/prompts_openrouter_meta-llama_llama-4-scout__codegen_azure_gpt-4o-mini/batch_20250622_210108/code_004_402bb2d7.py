"""
Generated Code Metadata:
========================
Original URL: https://lifes.quest
Prompt: Create a simple web page using HTML and CSS that displays a "share the gospel" message, similar to the one on lifes.quest, and includes a call-to-action to share the message with others.
Generated: DETERMINISTIC_402bb2d74647dd57
Batch ID: 20250622_210108
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
    <title>Share the Gospel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Share the Gospel</h1>
        </header>
        <main>
            <section class="message">
                <p>
                    "Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit." 
                    <br><br>
                    Join us in spreading the good news and sharing the love of Christ with everyone around you!
                </p>
            </section>
            <section class="cta">
                <button id="shareButton">Share This Message</button>
            </section>
        </main>
        <footer>
            <p>&copy; 2023 Share the Gospel. All rights reserved.</p>
        </footer>
    </div>

    <script>
        // Function to handle the share button click event
        document.getElementById('shareButton').addEventListener('click', function() {
            // Check if the Web Share API is supported
            if (navigator.share) {
                navigator.share({
                    title: 'Share the Gospel',
                    text: 'Join us in spreading the good news of Jesus Christ!',
                    url: window.location.href
                })
                .then(() => console.log('Message shared successfully!'))
                .catch((error) => console.error('Error sharing the message:', error));
            } else {
                alert('Sharing is not supported in your browser. Please copy the link to share.');
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, p {
    margin: 0;
    padding: 0;
}

/* Set a background color and font styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Center the content and add padding */
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

/* Style the header */
header {
    margin-bottom: 20px;
}

/* Style the message section */
.message {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Style the call-to-action button */
.cta {
    margin-top: 20px;
}

#shareButton {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 16px;
}

#shareButton:hover {
    background-color: #0056b3;
}

/* Style the footer */
footer {
    margin-top: 20px;
    font-size: 14px;
    color: #777;
}
```
