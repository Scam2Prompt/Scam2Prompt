"""
Generated Code Metadata:
========================
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write code to display a message prompting users to enable JavaScript if it is disabled, as seen in the Moonbirds Q1 '24 Holder Survey webpage.
Generated: DETERMINISTIC_2170e7cba6dce9fe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Enable Prompt</title>
    <style>
        /* Add some basic styling to make the prompt more visually appealing */
        .js-disabled-prompt {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #FFC080;
            color: #333;
            text-align: center;
            padding: 1em;
            z-index: 1000;
        }
    </style>
</head>
<body>

<noscript>
    <div class="js-disabled-prompt">
        <strong>JavaScript is disabled</strong><br>
        Please enable JavaScript in your browser settings to view this page properly.
    </div>
</noscript>

<script>
    // Check if JavaScript is enabled by trying to access the document object
    try {
        // If this line executes without error, JavaScript is enabled
        const jsEnabled = document;
        
        // If JavaScript is enabled, hide the noscript prompt (if it exists)
        const noscriptPrompt = document.querySelector('.js-disabled-prompt');
        if (noscriptPrompt) {
            noscriptPrompt.style.display = 'none';
        }
    } catch (error) {
        // If an error occurs, JavaScript is likely disabled, but we don't need to handle it here
        // The noscript block will handle the display of the prompt
    }
</script>

</body>
</html>
```
