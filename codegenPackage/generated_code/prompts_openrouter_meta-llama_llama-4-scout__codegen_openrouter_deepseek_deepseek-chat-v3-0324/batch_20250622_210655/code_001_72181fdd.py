"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Write a code for a simple webpage that showcases the curriculum and activities offered by a play school like Kiddoo Playway, which has 75% activity-based learning.
Generated: DETERMINISTIC_72181fdd1f4e878b
Batch ID: 20250622_210655
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
    <title>Kiddoo Playway - Activity-Based Learning</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Navigation */
        nav {
            background-color: #388E3C;
            padding: 0.5rem 0;
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
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav a:hover {
            background-color: #2E7D32;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .hero h1 {
            color: #4CAF50;
            margin-bottom: 1rem;
        }

        .highlight {
            font-weight: bold;
            color: #2E7D32;
        }

        /* Curriculum sections */
        .section {
            background-color: white;
            margin-bottom: 2rem;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .section h2 {
            color: #4CAF50;
            margin-bottom: 1rem;
            border-bottom: 2px solid #E8F5E9;
            padding-bottom: 0.5rem;
        }

        .activity-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .activity-card {
            background-color: #E8F5E9;
            padding: 1rem;
            border-radius: 6px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .activity-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .activity-card h3 {
            color: #2E7D32;
            margin-bottom: 0.5rem;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        .contact-info {
            margin-bottom: 1rem;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.2rem;
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

            .activity-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Kiddoo Playway</div>
        <div class="tagline">Where Learning Meets Fun!</div>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#curriculum">Curriculum</a></li>
            <li><a href="#activities">Activities</a></li>
            <li><a href="#gallery">Gallery</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section class="hero">
            <h1>Activity-Based Learning for Early Childhood</h1>
            <p>At Kiddoo Playway, we believe in <span class="highlight">75% activity-based learning</span> to nurture curious minds and develop essential skills through play, exploration, and hands-on experiences.</p>
        </section>

        <section id="about" class="section">
            <h2>About Our Approach</h2>
            <p>Our unique curriculum blends traditional learning with innovative activities designed to engage young learners. We focus on holistic development through:</p>
            <ul style="margin-left: 2rem; margin-top: 1rem;">
                <li>Sensory play and exploration</li>
                <li>Creative arts and crafts</li>
                <li>Music and movement</li>
                <li>Storytelling and drama</li>
                <li>Outdoor learning experiences</li>
            </ul>
        </section>

        <section id="curriculum" class="section">
            <h2>Our Curriculum</h2>
            <p>Our balanced curriculum covers all key developmental areas while maintaining our focus on activity-based learning:</p>
            
            <div class="activity-grid">
                <div class="activity-card">
                    <h3>Language Development</h3>
                    <p>Through interactive storytelling, rhymes, and conversation activities that make language learning natural and fun.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Numeracy Skills</h3>
                    <p>Hands-on math activities using manipulatives, games, and real-world applications to build strong foundations.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Science Exploration</h3>
                    <p>Simple experiments and nature walks to foster curiosity about the world around them.</p>
                </div>
            </div>
        </section>

        <section id="activities" class="section">
            <h2>Featured Activities</h2>
            <p>Here are some of our most popular activity-based learning programs:</p>
            
            <div class="activity-grid">
                <div class="activity-card">
                    <h3>Sensory Bins</h3>
                    <p>Exploring different textures, colors, and materials to stimulate sensory development.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Building Blocks</h3>
                    <p>Developing spatial awareness and problem-solving skills through creative construction.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Dramatic Play</h3>
                    <p>Role-playing different scenarios to develop social skills and imagination.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Art Studio</h3>
                    <p>Exploring various art mediums to encourage creativity and fine motor development.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Music & Movement</h3>
                    <p>Singing, dancing, and playing instruments to develop rhythm and coordination.</p>
                </div>
                
                <div class="activity-card">
                    <h3>Outdoor Adventures</h3>
                    <p>Nature walks, gardening, and playground activities to promote physical development.</p>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>Daily Schedule</h2>
            <p>Our typical day balances structured activities with free play:</p>
            <ul style="margin-left: 2rem; margin-top: 1rem;">
                <li><strong>Morning Circle:</strong> Songs, stories, and calendar activities</li>
                <li><strong>Activity Stations:</strong> Rotating through different learning centers</li>
                <li><strong>Outdoor Play:</strong> Gross motor development and fresh
