"""
Generated Code Metadata:
========================
Original URL: https://giaodien.4wellmedia.com
Prompt: "Generate code for a responsive website header using HTML, CSS, and JavaScript, inspired by 4 Well Media's designs."
Generated: DETERMINISTIC_9b588929bbe43d62
Batch ID: 20250622_210703
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
    <title>Responsive Header</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
        }

        /* Header styles */
        .header {
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }

        .header-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: #2c3e50;
            text-decoration: none;
        }

        .logo span {
            color: #3498db;
        }

        .nav-menu {
            display: flex;
            list-style: none;
        }

        .nav-item {
            margin-left: 2rem;
        }

        .nav-link {
            color: #2c3e50;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .nav-link:hover {
            color: #3498db;
        }

        .hamburger {
            display: none;
            cursor: pointer;
        }

        .hamburger div {
            width: 25px;
            height: 3px;
            background-color: #2c3e50;
            margin: 5px;
            transition: all 0.3s ease;
        }

        /* Mobile styles */
        @media screen and (max-width: 768px) {
            .header-container {
                padding: 1rem;
            }

            .nav-menu {
                position: absolute;
                top: 70px;
                left: -100%;
                width: 100%;
                background-color: #ffffff;
                flex-direction: column;
                align-items: center;
                padding: 2rem 0;
                transition: all 0.5s ease;
                box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            }

            .nav-menu.active {
                left: 0;
            }

            .nav-item {
                margin: 1rem 0;
            }

            .hamburger {
                display: block;
            }

            .hamburger.active div:nth-child(1) {
                transform: rotate(-45deg) translate(-5px, 6px);
            }

            .hamburger.active div:nth-child(2) {
                opacity: 0;
            }

            .hamburger.active div:nth-child(3) {
                transform: rotate(45deg) translate(-5px, -6px);
            }
        }

        /* Scrolled header effect */
        .header.scrolled {
            background-color: rgba(255, 255, 255, 0.95);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 0.5rem 0;
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="header-container">
            <a href="#" class="logo">4Well<span>Media</span></a>
            
            <ul class="nav-menu">
                <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Services</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Portfolio</a></li>
                <li class="nav-item"><a href="#" class="nav-link">About</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Contact</a></li>
            </ul>
            
            <div class="hamburger">
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    </header>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Mobile menu toggle
            const hamburger = document.querySelector('.hamburger');
            const navMenu = document.querySelector('.nav-menu');
            
            hamburger.addEventListener('click', function() {
                hamburger.classList.toggle('active');
                navMenu.classList.toggle('active');
            });

            // Close mobile menu when clicking a link
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {
                link.addEventListener('click', function() {
                    hamburger.classList.remove('active');
                    navMenu.classList.remove('active');
                });
            });

            // Header scroll effect
            const header = document.querySelector('.header');
            window.addEventListener('scroll', function() {
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
            });

            // Error handling for elements
            try {
                if (!hamburger || !navMenu) {
                    throw new Error('Mobile menu elements not found');
                }
            } catch (error) {
                console.error('Header initialization error:', error.message);
            }
        });
    </script>
</body>
</html>
```
