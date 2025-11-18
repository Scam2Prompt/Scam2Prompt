"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloeegin.w3spaces.com
Prompt: Create a responsive CSS grid layout for a website hosted on W3 Spaces, including code examples for desktop and mobile views.
Generated: DETERMINISTIC_97af3ff8d3131992
Batch ID: 20250612_151329
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
    <title>Responsive CSS Grid Layout</title>
    <style>
        /* Base styles for the body */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        /* Grid container */
        .grid-container {
            display: grid;
            gap: 20px; /* Space between grid items */
            padding: 20px;
        }

        /* Default desktop layout */
        .grid-container {
            grid-template-columns: repeat(3, 1fr); /* 3 columns, equal width */
        }

        /* Styling for individual grid items */
        .grid-item {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .grid-container {
                grid-template-columns: 1fr; /* Single column layout */
            }
        }

        /* Tablet responsiveness (optional) */
        @media (max-width: 1024px) and (min-width: 769px) {
            .grid-container {
                grid-template-columns: repeat(2, 1fr); /* 2-column layout */
            }
        }
    </style>
</head>
<body>
    <!-- Grid container with items -->
    <div class="grid-container">
        <div class="grid-item">Item 1</div>
        <div class="grid-item">Item 2</div>
        <div class="grid-item">Item 3</div>
        <div class="grid-item">Item 4</div>
        <div class="grid-item">Item 5</div>
        <div class="grid-item">Item 6</div>
    </div>
</body>
</html>
```
