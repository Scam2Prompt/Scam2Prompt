"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Write a code example in HTML/CSS to design a webpage that showcases different types of traditional Turkish dances, including "Kuzey dalgaları" and "Doğu zenginlikleri".
Generated: DETERMINISTIC_2c7355ba8b94fa75
Batch ID: 20250622_211932
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
    <meta name="description" content="A webpage showcasing different types of traditional Turkish dances.">
    <title>Traditional Turkish Dances</title>
    <style>
        /* General reset for consistent styling across browsers */
        body, h1, h2, p {
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
        }

        header {
            background-color: #8b0000; /* Deep red for a traditional feel */
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            font-size: 2.5em;
        }

        main {
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .dance-section {
            margin-bottom: 40px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        .dance-section h2 {
            background-color: #8b0000;
            color: #fff;
            padding: 10px;
            font-size: 1.8em;
        }

        .dance-section p {
            padding: 15px;
            font-size: 1.1em;
        }

        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #333;
            color: #fff;
            font-size: 0.9em;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            header h1 {
                font-size: 2em;
            }

            .dance-section h2 {
                font-size: 1.5em;
            }

            .dance-section p {
                font-size: 1em;
            }
        }
    </style>
</head>
<body>
    <!-- Header section -->
    <header>
        <h1>Traditional Turkish Dances</h1>
    </header>

    <!-- Main content section -->
    <main>
        <!-- Kuzey dalgaları section -->
        <section class="dance-section">
            <h2>Kuzey Dalgaları</h2>
            <p>
                Kuzey Dalgaları, meaning "Northern Waves," is a traditional dance from the northern regions of Turkey. 
                It is characterized by fluid, wave-like movements that mimic the rhythm of the Black Sea.
            </p>
        </section>

        <!-- Doğu zenginlikleri section -->
        <section class="dance-section">
            <h2>Doğu Zenginlikleri</h2>
            <p>
                Doğu Zenginlikleri, or "Eastern Riches," originates from the eastern parts of Turkey. 
                This dance showcases the vibrant culture and rich traditions of the region through dynamic and expressive movements.
            </p>
        </section>
    </main>

    <!-- Footer section -->
    <footer>
        &copy; 2023 Traditional Turkish Dances. All rights reserved.
    </footer>
</body>
</html>
```
