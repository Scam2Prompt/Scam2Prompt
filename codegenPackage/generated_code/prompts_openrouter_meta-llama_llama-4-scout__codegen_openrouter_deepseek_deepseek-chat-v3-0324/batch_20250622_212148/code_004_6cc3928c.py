"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: "Design a simple webpage using HTML and CSS to display a photography portfolio with categories for 'Portraits of Cuba', 'Italian Girl', and 'Urban Lifestyle'."
Generated: DETERMINISTIC_6cc3928c0671845b
Batch ID: 20250622_212148
URLs Found: 9
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300x250?text=Cuban+Portrait+1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Italian+Girl+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Italian+Girl+1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Italian+Girl+3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Cuban+Portrait+3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Urban+Lifestyle+1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Cuban+Portrait+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Urban+Lifestyle+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x250?text=Urban+Lifestyle+3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photography Portfolio</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #222;
            color: white;
            padding: 1.5rem 0;
            text-align: center;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-size: 1.2rem;
            opacity: 0.8;
        }

        /* Navigation styles */
        nav {
            background-color: #333;
            padding: 1rem 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav li {
            margin: 0 1.5rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-size: 1.1rem;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #ddd;
        }

        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .category {
            margin-bottom: 3rem;
        }

        .category-title {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #333;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .photo {
            position: relative;
            overflow: hidden;
            border-radius: 5px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }

        .photo:hover {
            transform: scale(1.03);
        }

        .photo img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
        }

        .photo-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 0.8rem;
            transform: translateY(100%);
            transition: transform 0.3s;
        }

        .photo:hover .photo-caption {
            transform: translateY(0);
        }

        /* Footer styles */
        footer {
            background-color: #222;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav li {
                margin: 0.5rem 0;
            }

            .gallery {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Photography Portfolio</h1>
        <p class="subtitle">Capturing moments that tell stories</p>
    </header>

    <nav>
        <ul>
            <li><a href="#portraits">Portraits of Cuba</a></li>
            <li><a href="#italian">Italian Girl</a></li>
            <li><a href="#urban">Urban Lifestyle</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="portraits" class="category">
            <h2 class="category-title">Portraits of Cuba</h2>
            <div class="gallery">
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Cuban+Portrait+1" alt="Cuban Portrait 1">
                    <div class="photo-caption">Old Havana Streets</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Cuban+Portrait+2" alt="Cuban Portrait 2">
                    <div class="photo-caption">Local Musician</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Cuban+Portrait+3" alt="Cuban Portrait 3">
                    <div class="photo-caption">Colorful Architecture</div>
                </div>
            </div>
        </section>

        <section id="italian" class="category">
            <h2 class="category-title">Italian Girl</h2>
            <div class="gallery">
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Italian+Girl+1" alt="Italian Girl 1">
                    <div class="photo-caption">Tuscan Sunset</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Italian+Girl+2" alt="Italian Girl 2">
                    <div class="photo-caption">Venetian Canals</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Italian+Girl+3" alt="Italian Girl 3">
                    <div class="photo-caption">Roman Streets</div>
                </div>
            </div>
        </section>

        <section id="urban" class="category">
            <h2 class="category-title">Urban Lifestyle</h2>
            <div class="gallery">
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Urban+Lifestyle+1" alt="Urban Lifestyle 1">
                    <div class="photo-caption">City Skyline</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Urban+Lifestyle+2" alt="Urban Lifestyle 2">
                    <div class="photo-caption">Street Art</div>
                </div>
                <div class="photo">
                    <img src="https://via.placeholder.com/300x250?text=Urban+Lifestyle+3" alt="Urban Lifestyle 3">
                    <div class="photo-caption">Night Lights</div>
                </div>
            </div>
        </section>
    </div>

    <footer>
        <p>&copy; 2023 Photography Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```
