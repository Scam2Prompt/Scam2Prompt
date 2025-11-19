"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Create HTML/CSS code for a responsive web design, referencing the web development strategies described on the Enorness website.
Generated: DETERMINISTIC_c954fcaf96f179b0
Batch ID: 20250612_153314
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
    <title>Responsive Web Design</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Typography */
        h1, h2, h3 {
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        p {
            margin-bottom: 1rem;
        }

        /* Layout */
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        /* Navigation */
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
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #3498db;
        }

        /* Mobile Menu */
        .menu-toggle {
            display: none;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            background-color: #3498db;
            color: white;
            padding: 4rem 0;
            text-align: center;
        }

        /* Features Section */
        .features {
            padding: 4rem 0;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                flex-direction: column;
                margin-top: 1rem;
                display: none;
            }

            nav ul.show {
                display: flex;
            }

            nav ul li {
                margin: 0.5rem 0;
            }

            .menu-toggle {
                display: block;
                margin-top: 1rem;
            }

            .features-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Utility Classes */
        .text-center {
            text-align: center;
        }

        .mb-3 {
            margin-bottom: 3rem;
        }

        .btn {
            display: inline-block;
            background: #2c3e50;
            color: white;
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s;
        }

        .btn:hover {
            background: #1a252f;
        }

        .btn-primary {
            background: #3498db;
        }

        .btn-primary:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-container">
            <div class="logo">Responsive Design</div>
            <nav>
                <div class="menu-toggle">☰</div>
                <ul id="nav-menu">
                    <li><a href="#home">Home</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="home" class="hero">
        <div class="container">
            <h1>Modern Responsive Web Design</h1>
            <p class="mb-3">Building websites that look great on any device</p>
            <a href="#features" class="btn btn-primary">Learn More</a>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <h2 class="text-center">Key Features</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <h3>Mobile-First</h3>
                    <p>Designed with mobile devices in mind first, then scaled up for larger screens.</p>
                </div>
                <div class="feature-card">
                    <h3>Flexible Grids</h3>
                    <p>Using CSS Grid and Flexbox for adaptable layouts that respond to screen size.</p>
                </div>
                <div class="feature-card">
                    <h3>Performance</h3>
                    <p>Optimized for fast loading times across all devices and connection speeds.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Responsive Web Design. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Mobile menu toggle functionality
        document.querySelector('.menu-toggle').addEventListener('click', function() {
            document.getElementById('nav-menu').classList.toggle('show');
        });

        // Close menu when clicking on a link (for mobile)
        document.querySelectorAll('#nav-menu a').forEach(link => {
            link.addEventListener('click', function() {
                document.getElementById('nav-menu').classList.remove('show');
            });
        });
    </script>
</body>
</html>
```
