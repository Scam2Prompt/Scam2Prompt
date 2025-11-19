"""
Generated Code Metadata:
========================
Original URL: https://365onlinenews.com
Prompt: Design a simple news website using HTML, CSS, and JavaScript, inspired by the layout and features of 365 Online News.
Generated: DETERMINISTIC_eaf51fca395a473c
Batch ID: 20250622_210650
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://source.unsplash.com/random/600x400/?soccer": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://source.unsplash.com/random/600x400/?technology": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://kit.fontawesome.com/a076d05399.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://source.unsplash.com/random/600x400/?conference": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://source.unsplash.com/random/600x400/?stockmarket": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation of a simple news website inspired by 365 Online News:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>365 News</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #1a1a1a;
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: #fff;
            text-decoration: none;
        }

        .logo span {
            color: #ff6600;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 1.5rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #ff6600;
        }

        /* Main content styles */
        main {
            padding: 2rem 0;
        }

        .hero {
            background-color: #fff;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #1a1a1a;
        }

        .hero p {
            color: #666;
            margin-bottom: 1.5rem;
        }

        .news-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .news-card {
            background-color: #fff;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .news-card:hover {
            transform: translateY(-5px);
        }

        .news-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .news-content {
            padding: 1.5rem;
        }

        .news-content h3 {
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }

        .news-content p {
            color: #666;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .news-meta {
            display: flex;
            justify-content: space-between;
            color: #888;
            font-size: 0.8rem;
        }

        .category-tag {
            display: inline-block;
            background-color: #ff6600;
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 3px;
            font-size: 0.7rem;
            margin-bottom: 0.5rem;
        }

        .read-more {
            display: inline-block;
            background-color: #1a1a1a;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 3px;
            text-decoration: none;
            font-size: 0.9rem;
            transition: background-color 0.3s;
        }

        .read-more:hover {
            background-color: #ff6600;
        }

        /* Footer styles */
        footer {
            background-color: #1a1a1a;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .footer-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.2rem;
            transition: color 0.3s;
        }

        .social-links a:hover {
            color: #ff6600;
        }

        .copyright {
            font-size: 0.9rem;
            color: #aaa;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
                justify-content: center;
            }

            nav ul li {
                margin: 0 0.5rem;
            }

            .news-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <a href="#" class="logo">365<span>News</span></a>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Politics</a></li>
                        <li><a href="#">Business</a></li>
                        <li><a href="#">Technology</a></li>
                        <li><a href="#">Sports</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="container">
        <section class="hero">
            <h1>Latest Breaking News</h1>
            <p>Stay updated with the most recent news stories from around the world, 24/7.</p>
        </section>

        <section class="news-grid" id="news-container">
            <!-- News articles will be loaded here by JavaScript -->
        </section>
    </main>

    <footer>
        <div class="container footer-content">
            <a href="#" class="logo">365<span>News</span></a>
            <div class="social-links">
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-youtube"></i></a>
            </div>
            <p class="copyright">© 2023 365 News. All rights reserved.</p>
        </div>
    </footer>

    <!-- Font Awesome for icons -->
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>

    <script>
        // Sample news data (in a real app, this would come from an API)
        const newsData = [
            {
                id: 1,
                title: "Global Summit Addresses Climate Change Concerns",
                excerpt: "World leaders gather to discuss urgent measures against rising global temperatures.",
                category: "Politics",
                date: "May 15, 2023",
                imageUrl: "https://source.unsplash.com/random/600x400/?conference"
            },
            {
                id: 2,
                title: "Tech Giant Unveils Revolutionary AI Assistant",
                excerpt: "New artificial intelligence platform promises to transform how we interact with technology.",
                category: "Technology",
                date: "May 14, 2023",
                imageUrl: "https://source.unsplash.com/random/600x400/?technology"
            },
            {
                id: 3,
                title: "Stock Markets Reach Record Highs",
                excerpt: "Global markets surge as economic recovery exceeds expectations.",
                category: "Business",
                date: "May 14, 2023",
                imageUrl: "https://source.unsplash.com/random/600x400/?stockmarket"
            },
            {
                id: 4,
                title: "National Team Advances to Championship Finals",
                excerpt: "Historic victory secures spot in international tournament after decade-long drought.",
                category: "Sports",
                date: "May 13, 2023",
                imageUrl: "https://source.unsplash.com/random/600x400/?soccer"
            },
            {
                id: 5,
                title: "Breakthrough in
