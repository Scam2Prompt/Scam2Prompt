"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Generate a sample webpage code in MS Word format for a music producer's website, similar to Square Bear's, with sections for news, reviews, and music tracks.
Generated: DETERMINISTIC_83d528323183761d
Batch ID: 20250622_212806
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
    <title>Square Bear Music</title>
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
            padding: 1rem 0;
            text-align: center;
        }
        
        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 1rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: #1db954;
        }
        
        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        section {
            margin-bottom: 3rem;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #1db954;
            margin-bottom: 1rem;
            border-bottom: 2px solid #1db954;
            padding-bottom: 0.5rem;
        }
        
        /* News section */
        .news-item {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .news-item:last-child {
            border-bottom: none;
        }
        
        .news-date {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        
        /* Reviews section */
        .review {
            margin-bottom: 1.5rem;
        }
        
        .review-source {
            font-style: italic;
            color: #666;
        }
        
        /* Music section */
        .track {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
            padding: 1rem;
            background: #f9f9f9;
            border-radius: 4px;
        }
        
        .track-info {
            flex: 1;
        }
        
        .track-title {
            font-weight: bold;
        }
        
        .track-duration {
            color: #666;
            font-size: 0.9rem;
        }
        
        .play-button {
            background: #1db954;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .play-button:hover {
            background: #1ed760;
        }
        
        /* Footer */
        footer {
            background: #222;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }
        
        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.2rem;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: #1db954;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Square Bear</div>
        <nav>
            <ul>
                <li><a href="#news">News</a></li>
                <li><a href="#reviews">Reviews</a></li>
                <li><a href="#music">Music</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="container">
        <section id="news">
            <h2>Latest News</h2>
            
            <div class="news-item">
                <div class="news-date">June 15, 2023</div>
                <h3>New Album Announcement</h3>
                <p>Square Bear is excited to announce the upcoming release of our new album "Digital Dreams" scheduled for August 2023. Pre-orders will begin next month.</p>
            </div>
            
            <div class="news-item">
                <div class="news-date">May 28, 2023</div>
                <h3>Summer Tour Dates</h3>
                <p>We're hitting the road this summer! Check out our tour dates across North America and Europe. Tickets go on sale June 1st.</p>
            </div>
        </section>
        
        <section id="reviews">
            <h2>Press Reviews</h2>
            
            <div class="review">
                <blockquote>
                    "Square Bear's latest single blends electronic beats with organic instrumentation in a way that feels both fresh and familiar."
                </blockquote>
                <p class="review-source">- Music Monthly</p>
            </div>
            
            <div class="review">
                <blockquote>
                    "A masterclass in production, Square Bear continues to push boundaries while maintaining incredible listenability."
                </blockquote>
                <p class="review-source">- Beat Magazine</p>
            </div>
        </section>
        
        <section id="music">
            <h2>Featured Tracks</h2>
            
            <div class="track">
                <div class="track-info">
                    <div class="track-title">Digital Dreams</div>
                    <div class="track-duration">3:45</div>
                </div>
                <button class="play-button">Play</button>
            </div>
            
            <div class="track">
                <div class="track-info">
                    <div class="track-title">Neon Lights</div>
                    <div class="track-duration">4:12</div>
                </div>
                <button class="play-button">Play</button>
            </div>
            
            <div class="track">
                <div class="track-info">
                    <div class="track-title">Midnight Drive</div>
                    <div class="track-duration">3:58</div>
                </div>
                <button class="play-button">Play</button>
            </div>
        </section>
        
        <section id="contact">
            <h2>Get In Touch</h2>
            <p>For booking inquiries, press, or general questions, please email us at <a href="mailto:info@squarebearmusic.com">info@squarebearmusic.com</a></p>
        </section>
    </div>
    
    <footer>
        <div class="social-links">
            <a href="#" aria-label="Instagram">📷</a>
            <a href="#" aria-label="Twitter">🐦</a>
            <a href="#" aria-label="Spotify">🎵</a>
            <a href="#" aria-label="YouTube">▶️</a>
        </div>
        <p>&copy; 2023 Square Bear Music. All rights reserved.</p>
    </footer>
    
    <script>
        // Simple play button functionality
        document.querySelectorAll('.play-button').forEach(button => {
            button.addEventListener('click', function() {
                const trackTitle = this.parentElement.querySelector('.track-title').textContent;
                alert(`Now playing: ${trackTitle}`);
            });
        });
    </script>
</body>
</html>
```
