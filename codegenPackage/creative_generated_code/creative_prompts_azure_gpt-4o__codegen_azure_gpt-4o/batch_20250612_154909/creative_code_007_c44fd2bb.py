"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Generate HTML and CSS code to showcase TS Fonts' "Burda Pro Font" in a responsive font preview gallery.
Generated: DETERMINISTIC_c44fd2bb5bd18b83
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
    <meta name="description" content="Responsive font preview gallery showcasing TS Fonts' Burda Pro Font">
    <title>Font Preview Gallery - Burda Pro</title>
    <style>
        /* General Reset */
        body, h1, h2, h3, p, div {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Body Styling */
        body {
            font-family: "Burda Pro", sans-serif;
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.5;
        }

        /* Responsive Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Gallery Header */
        header {
            text-align: center;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.5rem;
            color: #222;
        }

        header p {
            font-size: 1.2rem;
            color: #666;
        }

        /* Font Preview Gallery */
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .font-preview {
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .font-preview h2 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            color: #222;
        }

        .font-preview p {
            font-size: 1rem;
            color: #555;
        }

        .font-preview span {
            display: block;
            font-size: 2rem;
            margin-top: 20px;
            font-weight: bold;
            color: #444;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            header h1 {
                font-size: 2rem;
            }

            header p {
                font-size: 1rem;
            }

            .font-preview h2 {
                font-size: 1.25rem;
            }

            .font-preview span {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Gallery Header -->
        <header>
            <h1>Burda Pro Font Preview Gallery</h1>
            <p>Explore how the Burda Pro font appears in various styles and sizes.</p>
        </header>

        <!-- Font Preview Gallery -->
        <section class="gallery">
            <div class="font-preview">
                <h2>Regular</h2>
                <p>The standard weight of the Burda Pro font.</p>
                <span style="font-weight: normal;">The quick brown fox jumps over the lazy dog</span>
            </div>
            <div class="font-preview">
                <h2>Bold</h2>
                <p>The bold weight of the Burda Pro font for emphasis.</p>
                <span style="font-weight: bold;">The quick brown fox jumps over the lazy dog</span>
            </div>
            <div class="font-preview">
                <h2>Italic</h2>
                <p>An elegant italic variation for style.</p>
                <span style="font-style: italic;">The quick brown fox jumps over the lazy dog</span>
            </div>
            <div class="font-preview">
                <h2>Light</h2>
                <p>A lighter weight for a more subtle look.</p>
                <span style="font-weight: 300;">The quick brown fox jumps over the lazy dog</span>
            </div>
        </section>
    </div>
</body>
</html>
```
