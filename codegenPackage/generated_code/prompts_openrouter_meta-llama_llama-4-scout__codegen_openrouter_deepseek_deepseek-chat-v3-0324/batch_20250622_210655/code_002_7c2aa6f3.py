"""
Generated Code Metadata:
========================
Original URL: https://danieldefilippi.com
Prompt: Generate HTML and CSS code for a menu system similar to the one on Daniel Defilippi's website, with options for Inicio, Sobre mi, Exposiciones, Obra, and Galería.
Generated: DETERMINISTIC_7c2aa6f32425cc06
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
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menú de Navegación</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Navigation container */
        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Main navigation */
        .main-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }

        /* Logo styles */
        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            text-decoration: none;
            color: #333;
        }

        /* Menu items */
        .menu {
            display: flex;
            list-style: none;
        }

        .menu-item {
            margin-left: 2rem;
            position: relative;
        }

        .menu-item:first-child {
            margin-left: 0;
        }

        .menu-link {
            text-decoration: none;
            color: #333;
            font-size: 1rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: color 0.3s ease;
            padding: 0.5rem 0;
            position: relative;
        }

        .menu-link:hover {
            color: #666;
        }

        /* Active state */
        .menu-link.active {
            color: #000;
            font-weight: 600;
        }

        /* Underline animation */
        .menu-link::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: 0;
            left: 0;
            background-color: #000;
            transition: width 0.3s ease;
        }

        .menu-link:hover::after {
            width: 100%;
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

            .menu {
                position: fixed;
                top: 0;
                left: -100%;
                width: 80%;
                height: 100vh;
                background-color: #fff;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: left 0.3s ease;
                z-index: 1000;
            }

            .menu.active {
                left: 0;
            }

            .menu-item {
                margin: 1rem 0;
            }

            .menu-link {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="nav-container">
        <nav class="main-nav">
            <a href="#" class="logo">Daniel Defilippi</a>
            
            <div class="mobile-menu-toggle">☰</div>
            
            <ul class="menu">
                <li class="menu-item">
                    <a href="#" class="menu-link active">Inicio</a>
                </li>
                <li class="menu-item">
                    <a href="#" class="menu-link">Sobre mi</a>
                </li>
                <li class="menu-item">
                    <a href="#" class="menu-link">Exposiciones</a>
                </li>
                <li class="menu-item">
                    <a href="#" class="menu-link">Obra</a>
                </li>
                <li class="menu-item">
                    <a href="#" class="menu-link">Galería</a>
                </li>
            </ul>
        </nav>
    </div>

    <script>
        // Mobile menu toggle functionality
        document.querySelector('.mobile-menu-toggle').addEventListener('click', function() {
            document.querySelector('.menu').classList.toggle('active');
        });

        // Close menu when clicking on a link (for mobile)
        document.querySelectorAll('.menu-link').forEach(link => {
            link.addEventListener('click', function() {
                document.querySelector('.menu').classList.remove('active');
                
                // Update active state
                document.querySelectorAll('.menu-link').forEach(item => {
                    item.classList.remove('active');
                });
                this.classList.add('active');
            });
        });
    </script>
</body>
</html>
```
