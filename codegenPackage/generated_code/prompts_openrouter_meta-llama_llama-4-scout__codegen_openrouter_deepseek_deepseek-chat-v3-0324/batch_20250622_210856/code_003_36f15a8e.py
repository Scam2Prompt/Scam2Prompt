"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Create a code snippet in HTML/CSS to design a simple and intuitive navigation menu for a website offering DIY legal forms, inspired by the layout on launchlawinc.com.
Generated: DETERMINISTIC_36f15a8e23b32c0c
Batch ID: 20250622_210856
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
    <title>Legal Forms - Navigation</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        /* Navigation container */
        .nav-container {
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        /* Main navigation */
        .main-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Logo styling */
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2c3e50;
            text-decoration: none;
        }

        .logo span {
            color: #3498db;
        }

        /* Navigation links */
        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            transition: color 0.3s ease;
            padding: 0.5rem 0;
            position: relative;
        }

        .nav-links a:hover {
            color: #3498db;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: 0;
            left: 0;
            background-color: #3498db;
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* CTA button */
        .cta-button {
            background-color: #3498db;
            color: white;
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            font-weight: 600;
            transition: background-color 0.3s ease;
        }

        .cta-button:hover {
            background-color: #2980b9;
            color: white;
        }

        /* Mobile menu toggle */
        .mobile-menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .mobile-menu-toggle {
                display: block;
            }

            .nav-links {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 70px;
                left: 0;
                width: 100%;
                background-color: white;
                padding: 1rem 0;
                box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            }

            .nav-links.active {
                display: flex;
            }

            .nav-links li {
                margin: 0.5rem 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="nav-container">
        <nav class="main-nav">
            <a href="/" class="logo">Legal<span>Forms</span></a>
            
            <div class="mobile-menu-toggle">☰</div>
            
            <ul class="nav-links">
                <li><a href="/forms">Forms</a></li>
                <li><a href="/pricing">Pricing</a></li>
                <li><a href="/resources">Resources</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact" class="cta-button">Get Started</a></li>
            </ul>
        </nav>
    </div>

    <script>
        // Mobile menu toggle functionality
        document.querySelector('.mobile-menu-toggle').addEventListener('click', function() {
            document.querySelector('.nav-links').classList.toggle('active');
        });
    </script>
</body>
</html>
```
