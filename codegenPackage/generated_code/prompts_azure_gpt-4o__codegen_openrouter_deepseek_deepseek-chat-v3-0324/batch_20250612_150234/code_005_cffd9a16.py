"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Write HTML and CSS code to design a user interface for a digital radio platform, inspired by Radio S's layout, featuring sections for "Radio Uživo," "Muzički Mix," and "Podcast."
Generated: DETERMINISTIC_cffd9a162572566e
Batch ID: 20250612_150234
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300x150?text=Rock+Mix": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x150?text=Hip-Hop+Mix": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x150?text=Pop+Mix": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x150?text=Electronic+Mix": {
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
    <title>Digital Radio Platform</title>
    <style>
        /* Reset and Base Styles */
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

        /* Header Styles */
        header {
            background-color: #1a1a2e;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
        }

        .logo span {
            color: #e94560;
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
            color: #e94560;
        }

        /* Main Content Styles */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .section-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e94560;
            color: #1a1a2e;
        }

        /* Radio Player Styles */
        .player-container {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }

        .player-controls {
            display: flex;
            align-items: center;
            margin-top: 1rem;
        }

        .play-btn {
            background-color: #e94560;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 1.2rem;
            cursor: pointer;
            margin-right: 1rem;
            transition: background-color 0.3s;
        }

        .play-btn:hover {
            background-color: #d13354;
        }

        .volume-control {
            margin-left: auto;
            display: flex;
            align-items: center;
        }

        .volume-control input {
            margin-left: 0.5rem;
        }

        /* Content Grid Styles */
        .content-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1rem;
        }

        .card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card-img {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }

        .card-content {
            padding: 1rem;
        }

        .card-title {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .card-description {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }

        .card-btn {
            background-color: #1a1a2e;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background-color 0.3s;
        }

        .card-btn:hover {
            background-color: #e94560;
        }

        /* Footer Styles */
        footer {
            background-color: #1a1a2e;
            color: white;
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
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
            color: #e94560;
        }

        /* Responsive Styles */
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
            }

            nav ul li {
                margin: 0 0.5rem;
            }

            .content-grid {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Radio<span>Platform</span></div>
        <nav>
            <ul>
                <li><a href="#live">Radio Uživo</a></li>
                <li><a href="#mix">Muzički Mix</a></li>
                <li><a href="#podcasts">Podcast</a></li>
                <li><a href="#about">O Nama</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <section id="live">
            <h2 class="section-title">Radio Uživo</h2>
            <div class="player-container">
                <h3>Trenutno se emituje: Popularna Muzika</h3>
                <div class="player-controls">
                    <button class="play-btn">▶</button>
                    <div class="now-playing">00:00 / 03:45</div>
                    <div class="volume-control">
                        <span>🔊</span>
                        <input type="range" min="0" max="100" value="80">
                    </div>
                </div>
            </div>
        </section>

        <section id="mix">
            <h2 class="section-title">Muzički Mix</h2>
            <div class="content-grid">
                <div class="card">
                    <img src="https://via.placeholder.com/300x150?text=Pop+Mix" alt="Pop Mix" class="card-img">
                    <div class="card-content">
                        <h3 class="card-title">Pop Mix</h3>
                        <p class="card-description">Najbolje pop pesme ovog leta</p>
                        <button class="card-btn">Slušaj</button>
                    </div>
                </div>
                <div class="card">
                    <img src="https://via.placeholder.com/300x150?text=Rock+Mix" alt="Rock Mix" class="card-img">
                    <div class="card-content">
                        <h3 class="card-title">Rock Mix</h3>
                        <p class="card-description">Klasici i novi rock hitovi</p>
                        <button class="card-btn">Slušaj</button>
                    </div>
                </div>
                <div class="card">
                    <img src="https://via.placeholder.com/300x150?text=Hip-Hop+Mix" alt="Hip-Hop Mix" class="card-img">
                    <div class="card-content">
                        <h3 class="card-title">Hip-Hop Mix</h3>
                        <p class="card-description">Najbolji hip-hop izvođači</p>
                        <button class="card-btn">Slušaj</button>
                    </div>
                </div>
                <div class="card">
                    <img src="https://via.placeholder.com/300x150?text=Electronic+Mix" alt="Electronic Mix" class="card-img">
                    <div class="card-content">
                        <h3 class="card-title">Electronic Mix</h3>
                        <p class="card-description">Elektronika za klub i kuću</p>
                        <button class="card-btn">Slušaj</button>
                    </div>
                </div>
            </div>
        </section>

        <section id="podcasts">
            <h2 class="section-title">
