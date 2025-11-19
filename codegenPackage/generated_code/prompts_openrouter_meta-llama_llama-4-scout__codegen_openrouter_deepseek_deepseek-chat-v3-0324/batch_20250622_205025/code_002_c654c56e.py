"""
Generated Code Metadata:
========================
Original URL: https://grandairfares.com
Prompt: Generate HTML and CSS code for a basic responsive navigation menu that could be used on a travel website with sections like "Inicio," "Sobre nosotros," "Destinos," and "Contáctanos."
Generated: DETERMINISTIC_c654c56e443beb47
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Website</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            background-color: #f5f5f5;
        }

        /* Navigation styles */
        .navbar {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #ecf0f1;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 1.5rem;
        }

        .nav-links a {
            color: #ecf0f1;
            text-decoration: none;
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
            background: #3498db;
            bottom: 0;
            left: 0;
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Mobile menu styles */
        .menu-toggle {
            display: none;
            cursor: pointer;
            font-size: 1.5rem;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background-color: #2c3e50;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: left 0.3s ease;
            }

            .nav-links.active {
                left: 0;
            }

            .nav-links li {
                margin: 1.5rem 0;
            }

            .menu-toggle {
                display: block;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="#" class="logo">TravelWorld</a>
            <ul class="nav-links">
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Sobre nosotros</a></li>
                <li><a href="#">Destinos</a></li>
                <li><a href="#">Contáctanos</a></li>
            </ul>
            <div class="menu-toggle">☰</div>
        </div>
    </nav>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const menuToggle = document.querySelector('.menu-toggle');
            const navLinks = document.querySelector('.nav-links');

            menuToggle.addEventListener('click', function() {
                navLinks.classList.toggle('active');
            });

            // Close menu when clicking on a link (mobile)
            document.querySelectorAll('.nav-links a').forEach(link => {
                link.addEventListener('click', function() {
                    if (window.innerWidth <= 768) {
                        navLinks.classList.remove('active');
                    }
                });
            });
        });
    </script>
</body>
</html>
```
