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
  <title>Apply Zunburk Font</title>
  
  <!-- Include the Zunburk Font V3 using @font-face -->
  <style>
    /* Define the Zunburk Font V3 */
    @font-face {
      font-family: 'ZunburkFontV3'; /* Font family name */
      src: url('path-to-font/ZunburkFontV3.woff2') format('woff2'), /* Modern browsers */
           url('path-to-font/ZunburkFontV3.woff') format('woff'),   /* Fallback */
           url('path-to-font/ZunburkFontV3.ttf') format('truetype'); /* Older fallback */
      font-weight: normal; /* Default weight */
      font-style: normal;  /* Default style */
    }

    /* Apply the font to the body and other elements */
    body, h1, h2, h3, p {
      font-family: 'ZunburkFontV3', sans-serif; /* Use Zunburk font, fallback to sans-serif */
    }

    /* Example customization */
    h1 {
      font-size: 2.5em;
      color: #333; /* Dark gray for header text */
    }

    p {
      font-size: 1.2em;
      line-height: 1.6; /* Improve readability */
      color: #555; /* Medium gray for paragraph text */
    }
  </style>
</head>
<body>
  <h1>Welcome to the Zunburk Font Showcase</h1>
  <p>This paragraph demonstrates the Zunburk Font V3 applied to text on a web page.</p>
</body>
</html>
```
