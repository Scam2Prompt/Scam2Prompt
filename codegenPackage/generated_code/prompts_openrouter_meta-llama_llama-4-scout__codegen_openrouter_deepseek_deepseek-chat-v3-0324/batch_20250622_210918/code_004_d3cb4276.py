"""
Generated Code Metadata:
========================
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Create a web page using HTML, CSS, and JavaScript that showcases a Japanese-inspired NFT collection, similar to the Hikeshi NFT project, with a focus on seasonal changes and patterns.
Generated: DETERMINISTIC_d3cb427679c6d9a9
Batch ID: 20250622_210918
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2000/svg": {
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
    <title>Hana no Shō - Japanese NFT Collection</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Noto Sans JP', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Typography */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap');

        h1, h2, h3 {
            font-weight: 500;
            letter-spacing: 1px;
        }

        /* Header Styles */
        header {
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            color: white;
            padding: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header-content {
            position: relative;
            z-index: 2;
        }

        .header-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.1;
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="none"><path fill="white" d="M50,0 C60,20 80,30 100,50 C80,70 60,80 50,100 C40,80 20,70 0,50 C20,30 40,20 50,0 Z"></path></svg>');
            background-size: 30px 30px;
        }

        /* Navigation */
        nav {
            background-color: #2c3e50;
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav li {
            margin: 0 1rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav a:hover {
            background-color: #34495e;
        }

        /* Main Content */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .intro {
            text-align: center;
            margin-bottom: 3rem;
        }

        .intro p {
            max-width: 800px;
            margin: 1rem auto;
        }

        /* NFT Gallery */
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .nft-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .nft-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }

        .nft-image {
            width: 100%;
            height: 280px;
            object-fit: cover;
        }

        .nft-info {
            padding: 1.5rem;
        }

        .nft-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }

        .nft-season {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .spring { background-color: #f8bbd0; color: #c2185b; }
        .summer { background-color: #b3e5fc; color: #0277bd; }
        .autumn { background-color: #ffcc80; color: #e65100; }
        .winter { background-color: #e0f7fa; color: #00838f; }

        .nft-price {
            font-weight: bold;
            margin-top: 0.5rem;
        }

        /* Season Filter */
        .season-filter {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
            flex-wrap: wrap;
        }

        .season-btn {
            padding: 0.5rem 1rem;
            margin: 0.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .season-btn:hover {
            opacity: 0.8;
        }

        .season-btn.active {
            transform: scale(1.05);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.5rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav li {
                margin: 0.5rem 0;
            }

            .gallery {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-bg"></div>
        <div class="header-content">
            <h1>Hana no Shō</h1>
            <p>季節の美 - Beauty of the Seasons</p>
        </div>
    </header>

    <nav>
        <ul>
            <li><a href="#collection">Collection</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#roadmap">Roadmap</a></li>
            <li><a href="#team">Team</a></li>
        </ul>
    </nav>

    <main>
        <section id="collection" class="intro">
            <h2>Japanese-Inspired NFT Collection</h2>
            <p>Each NFT in our collection represents the ephemeral beauty of Japan's four seasons, blending traditional motifs with modern digital artistry.</p>
        </section>

        <div class="season-filter">
            <button class="season-btn spring active" data-season="all">All Seasons</button>
            <button class="season-btn spring" data-season="spring">Spring</button>
            <button class="season-btn summer" data-season="summer">Summer</button>
            <button class="season-btn autumn" data-season="autumn">Autumn</button>
            <button class="season-btn winter" data-season="winter">Winter</button>
        </div>

        <div class="gallery" id="nft-gallery">
            <!-- NFTs will be loaded here via JavaScript -->
        </div>

        <section id="about" class="intro">
            <h2>About Hana no Shō</h2>
            <p>Inspired by Japan's rich cultural heritage and the concept of mono no aware (the pathos of things), our NFT collection captures the transient beauty of nature's cycles.</p>
            <p>Each piece is handcrafted by our team of digital artists, combining traditional Japanese aesthetics with blockchain technology.</p>
        </section>

        <section id="roadmap" class="intro">
            <h2>Roadmap</h2>
            <p>Our journey is divided into four seasons, mirroring the natural world we celebrate:</p>
            <ul style="text-align: left; max-width: 600px; margin: 1rem auto;">
                <li>Spring: Collection launch and community building</li>
                <li>Summer: Physical art exhibitions in Tokyo and Kyoto</li>
                <li>Autumn: Collaborations with traditional Japanese artists</li>
                <li>Winter
