"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: Generate HTML and CSS code to showcase TS Fonts' "Burda Pro Font" in a responsive font preview gallery.
Generated: DETERMINISTIC_c44fd2bb5bd18b83
Batch ID: 20250612_154909
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
    <title>TS Fonts - Burda Pro Font Preview</title>
    <style>
        /* CSS Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Base Styles */
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
            padding: 20px;
        }

        /* Font Import - Replace with actual font-face when available */
        @font-face {
            font-family: 'Burda Pro';
            src: url('BurdaPro-Regular.woff2') format('woff2'),
                 url('BurdaPro-Regular.woff') format('woff');
            font-weight: normal;
            font-style: normal;
            font-display: swap;
        }

        @font-face {
            font-family: 'Burda Pro';
            src: url('BurdaPro-Bold.woff2') format('woff2'),
                 url('BurdaPro-Bold.woff') format('woff');
            font-weight: bold;
            font-style: normal;
            font-display: swap;
        }

        @font-face {
            font-family: 'Burda Pro';
            src: url('BurdaPro-Italic.woff2') format('woff2'),
                 url('BurdaPro-Italic.woff') format('woff');
            font-weight: normal;
            font-style: italic;
            font-display: swap;
        }

        /* Header Styles */
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px 0;
            border-bottom: 1px solid #eee;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: #222;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #666;
        }

        /* Font Preview Container */
        .font-preview-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
        }

        /* Font Preview Card */
        .font-preview {
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 25px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .font-preview:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        .font-name {
            font-family: 'Burda Pro', sans-serif;
            font-size: 1.8rem;
            margin-bottom: 15px;
            color: #222;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }

        .font-sample {
            font-family: 'Burda Pro', sans-serif;
            font-size: 1.2rem;
            margin-bottom: 15px;
            line-height: 1.5;
        }

        .font-weight {
            display: inline-block;
            background: #f0f0f0;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-bottom: 10px;
        }

        .font-style {
            display: inline-block;
            background: #f0f0f0;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-bottom: 10px;
            margin-left: 5px;
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .font-preview-container {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 2rem;
            }
        }

        /* Footer */
        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px 0;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #eee;
        }
    </style>
</head>
<body>
    <header>
        <h1>Burda Pro Font</h1>
        <p class="subtitle">A premium typeface by TS Fonts</p>
    </header>

    <main>
        <div class="font-preview-container">
            <!-- Regular Weight -->
            <div class="font-preview">
                <h2 class="font-name">Burda Pro Regular</h2>
                <span class="font-weight">Weight: 400</span>
                <p class="font-sample">
                    The quick brown fox jumps over the lazy dog. 1234567890
                </p>
                <p class="font-sample" style="font-size: 2rem;">
                    Aa Bb Cc Dd Ee Ff Gg Hh
                </p>
            </div>

            <!-- Bold Weight -->
            <div class="font-preview">
                <h2 class="font-name" style="font-weight: bold;">Burda Pro Bold</h2>
                <span class="font-weight">Weight: 700</span>
                <p class="font-sample" style="font-weight: bold;">
                    The quick brown fox jumps over the lazy dog. 1234567890
                </p>
                <p class="font-sample" style="font-size: 2rem; font-weight: bold;">
                    Aa Bb Cc Dd Ee Ff Gg Hh
                </p>
            </div>

            <!-- Italic Style -->
            <div class="font-preview">
                <h2 class="font-name" style="font-style: italic;">Burda Pro Italic</h2>
                <span class="font-weight">Weight: 400</span>
                <span class="font-style">Style: Italic</span>
                <p class="font-sample" style="font-style: italic;">
                    The quick brown fox jumps over the lazy dog. 1234567890
                </p>
                <p class="font-sample" style="font-size: 2rem; font-style: italic;">
                    Aa Bb Cc Dd Ee Ff Gg Hh
                </p>
            </div>

            <!-- Bold Italic -->
            <div class="font-preview">
                <h2 class="font-name" style="font-weight: bold; font-style: italic;">Burda Pro Bold Italic</h2>
                <span class="font-weight">Weight: 700</span>
                <span class="font-style">Style: Italic</span>
                <p class="font-sample" style="font-weight: bold; font-style: italic;">
                    The quick brown fox jumps over the lazy dog. 1234567890
                </p>
                <p class="font-sample" style="font-size: 2rem; font-weight: bold; font-style: italic;">
                    Aa Bb Cc Dd Ee Ff Gg Hh
                </p>
            </div>

            <!-- Large Display -->
            <div class="font-preview">
                <h2 class="font-name">Display Sample</h2>
                <p class="font-sample" style="font-size: 3rem; line-height: 1.2;">
                    Burda Pro
                </p>
                <p class="font-sample" style="font-size: 1.2rem;">
                    Perfect for headlines and display text
                </p>
            </div>

            <!-- Paragraph Sample -->
            <div class="font-preview">
                <h2 class="font-name">Paragraph Sample</h2>
                <p class="font-sample">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.
                </p>
                <p class="font-sample">
                    Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus.
                </p>
            </div>
        </div>
    </main>

    <footer>
        <p>&copy; 2023 TS Fonts. All rights reserved.</p>
    </footer>
</body>
</html>
```
