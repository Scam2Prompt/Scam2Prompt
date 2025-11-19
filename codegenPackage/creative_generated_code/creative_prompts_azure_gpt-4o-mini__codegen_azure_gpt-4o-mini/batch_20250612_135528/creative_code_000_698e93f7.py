"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apysolutions.com
Prompt: Generate a code snippet for a responsive web design that adapts to various screen sizes, as described by APY Solutions.
Generated: DETERMINISTIC_698e93f7ca00712e
Batch ID: 20250612_135528
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
    <title>Responsive Web Design</title>
    <style>
        /* Base styles for body and container */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 1200px;
            margin: auto;
            padding: 20px;
        }

        /* Responsive grid layout using CSS Flexbox */
        .grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px; /* Space between grid items */
        }
        .grid-item {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            padding: 20px;
            flex: 1 1 calc(33.333% - 20px); /* 3 items per row */
            box-sizing: border-box;
        }
        
        /* Media query for tablets */
        @media (max-width: 768px) {
            .grid-item {
                flex: 1 1 calc(50% - 20px); /* 2 items per row */
            }
        }

        /* Media query for mobile devices */
        @media (max-width: 480px) {
            .grid-item {
                flex: 1 1 100%; /* 1 item per row */
            }
        }

        /* Header styling */
        header {
            background-color: #007BFF;
            color: white;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

    <header>
        <h1>Responsive Web Design Example</h1>
    </header>

    <div class="container">
        <div class="grid">
            <!-- Grid items -->
            <div class="grid-item">Item 1</div>
            <div class="grid-item">Item 2</div>
            <div class="grid-item">Item 3</div>
            <div class="grid-item">Item 4</div>
            <div class="grid-item">Item 5</div>
            <div class="grid-item">Item 6</div>
        </div>
    </div>

</body>
</html>
```
