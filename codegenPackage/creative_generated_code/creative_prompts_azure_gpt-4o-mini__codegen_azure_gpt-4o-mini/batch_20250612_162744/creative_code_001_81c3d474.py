"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eligibility-resolv.xyz
Prompt: Provide an example of using `document.write()` to insert a string of HTML into a webpage.
Generated: DETERMINISTIC_81c3d474b5a7fc44
Batch ID: 20250612_162744
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
    <title>Document Write Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
    </style>
</head>
<body>

<script>
    // Function to safely insert HTML into the webpage
    function insertHTML() {
        // Define the HTML string to be inserted
        const htmlContent = `
            <div style="background-color: white; padding: 20px; border: 1px solid #ccc; border-radius: 5px;">
                <h1>Welcome to My Webpage</h1>
                <p>This HTML content was inserted using document.write().</p>
            </div>
        `;
        
        // Check if the document is fully loaded before writing
        if (document.readyState === 'complete') {
            // Insert the HTML string into the document
            document.write(htmlContent);
        } else {
            console.error('Document is not ready. Cannot write HTML.');
        }
    }

    // Call the function to insert HTML
    insertHTML();
</script>

</body>
</html>
```
