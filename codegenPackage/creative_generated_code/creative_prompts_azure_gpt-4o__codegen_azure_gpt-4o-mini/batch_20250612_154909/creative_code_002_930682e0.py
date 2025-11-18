"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Create a code snippet to programmatically apply the "Zunburk Font V3" to a web page using CSS.
Generated: DETERMINISTIC_930682e03b0805b0
Batch ID: 20250612_154909
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
    <title>Apply Zunburk Font V3</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to the Zunburk Font Demo</h1>
    <p>This text is styled with the Zunburk Font V3.</p>

    <script>
        // Function to dynamically load a font
        function loadFont(fontName, fontUrl) {
            const fontFace = new FontFace(fontName, `url(${fontUrl})`);

            // Add the font to the document
            fontFace.load().then(function(loadedFont) {
                document.fonts.add(loadedFont);
                console.log(`${fontName} loaded successfully.`);
            }).catch(function(error) {
                console.error(`Failed to load ${fontName}: ${error}`);
            });
        }

        // Load the "Zunburk Font V3"
        loadFont('ZunburkFontV3', 'path/to/zunburk-font-v3.woff2');
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Apply the Zunburk Font V3 to the body */
body {
    font-family: 'ZunburkFontV3', sans-serif; /* Fallback to sans-serif */
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0; /* Light grey background for contrast */
    color: #333; /* Dark grey text color for readability */
}

/* Style for headings */
h1 {
    font-size: 2em;
    margin-bottom: 10px;
}

/* Style for paragraphs */
p {
    font-size: 1.2em;
    line-height: 1.5;
}
```
