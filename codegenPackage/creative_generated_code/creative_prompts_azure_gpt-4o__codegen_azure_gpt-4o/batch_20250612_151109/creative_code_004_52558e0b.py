"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Write code in HTML and CSS to create a visual representation of wall tiles in sizes like 300x300 MM and 300x600 MM, as described on the ITACA Ceramic website.
Generated: DETERMINISTIC_52558e0b3f556c4d
Batch ID: 20250612_151109
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
    <title>Wall Tiles</title>
    <style>
        /* General styling for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #f8f9fa;
            min-height: 100vh;
        }

        h1 {
            margin-top: 20px;
            color: #333;
        }

        /* Container for tiles */
        .tile-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
            justify-content: center;
        }

        /* Styling for 300x300 MM tiles */
        .tile-300x300 {
            width: 300px;
            height: 300px;
            background-color: #007bff; /* Blue color */
            border: 3px solid #0056b3; /* Darker blue border */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
        }

        /* Styling for 300x600 MM tiles */
        .tile-300x600 {
            width: 300px;
            height: 600px;
            background-color: #28a745; /* Green color */
            border: 3px solid #1c7430; /* Darker green border */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
        }

        /* Add hover effect for tiles */
        .tile-300x300:hover,
        .tile-300x600:hover {
            transform: scale(1.05);
            transition: transform 0.3s ease;
        }
    </style>
</head>
<body>
    <h1>Wall Tiles Display</h1>
    <div class="tile-container">
        <!-- Example 300x300 MM tile -->
        <div class="tile-300x300">
            300 x 300 MM
        </div>
        <!-- Example 300x600 MM tile -->
        <div class="tile-300x600">
            300 x 600 MM
        </div>
    </div>
</body>
</html>
```
