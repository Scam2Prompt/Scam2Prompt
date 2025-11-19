"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: Write HTML and CSS code to create a responsive navigation bar similar to the one described in the Avenger Bootstrap template, including toggle functionality.
Generated: DETERMINISTIC_8897fe55bfb83114
Batch ID: 20250612_151255
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
    <title>Responsive Navbar</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Navbar container */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #2c3e50;
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        /* Logo/brand */
        .navbar-brand {
            color: white;
            font-size: 1.5rem;
            font-weight: bold;
            text-decoration: none;
        }

        /* Navigation links */
        .navbar-nav {
            display: flex;
            list-style: none;
        }

        .nav-item {
            margin-left: 1.5rem;
        }

        .nav-link {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .nav-link:hover {
            color: #3498db;
        }

        /* Toggle button for mobile */
        .navbar-toggler {
            display: none;
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Active state for links */
        .nav-link.active {
            color: #3498db;
            font-weight: bold;
        }

        /* Mobile styles */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                align-items: flex-start;
                padding: 1rem;
            }

            .navbar-nav {
                display: none;
                flex-direction: column;
                width: 100%;
                margin-top: 1rem;
            }

            .navbar-nav.show {
                display: flex;
            }

            .nav-item {
                margin: 0.5rem 0;
                margin-left: 0;
            }

            .navbar-toggler {
                display: block;
                position: absolute;
                right: 1rem;
                top: 1rem;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="#" class="navbar-brand">Avenger</a>
        
        <button class="navbar-toggler" id="navbarToggler">☰</button>
        
        <ul class="navbar-nav" id="navbarNav">
            <li class="nav-item">
                <a href="#" class="nav-link active">Home</a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link">About</a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link">Services</a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link">Portfolio</a>
            </li>
            <li class="nav-item">
                <a href="#" class="nav-link">Contact</a>
            </li>
        </ul>
    </nav>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const toggler = document.getElementById('navbarToggler');
            const nav = document.getElementById('navbarNav');

            toggler.addEventListener('click', function() {
                nav.classList.toggle('show');
            });

            // Close navbar when clicking on a link (mobile)
            const navLinks = document.querySelectorAll('.nav-link');
            navLinks.forEach(link => {
                link.addEventListener('click', function() {
                    if (window.innerWidth <= 768) {
                        nav.classList.remove('show');
                    }
                });
            });
        });
    </script>
</body>
</html>
```
