"""
Generated Code Metadata:
========================
Original URL: https://zellerscanada.ca
Prompt: Generate HTML and CSS code for a responsive navigation menu with a cart icon, similar to the one on the Zellers Canada website.
Generated: DETERMINISTIC_1154c9d45f943639
Batch ID: 20250622_212519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
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
    <title>Responsive Navigation Menu</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f8f8f8;
        }

        /* Header and navigation styles */
        header {
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        .main-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
        }

        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 30px;
        }

        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #e63946;
        }

        .cart-icon {
            position: relative;
            font-size: 20px;
            color: #333;
            cursor: pointer;
        }

        .cart-count {
            position: absolute;
            top: -10px;
            right: -10px;
            background-color: #e63946;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 12px;
            font-weight: bold;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #333;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background-color: #fff;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                padding-top: 30px;
                transition: left 0.3s ease;
            }

            .nav-links.active {
                left: 0;
            }

            .nav-links li {
                margin: 15px 0;
            }

            .mobile-menu-btn {
                display: block;
            }

            .cart-icon {
                margin-left: auto;
                margin-right: 20px;
            }
        }

        @media (min-width: 769px) {
            .nav-links {
                display: flex !important;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="nav-container">
            <nav class="main-nav">
                <a href="#" class="logo">ZELLERS</a>
                
                <button class="mobile-menu-btn">
                    <i class="fas fa-bars"></i>
                </button>

                <ul class="nav-links">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Shop</a></li>
                    <li><a href="#">Deals</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>

                <div class="cart-icon">
                    <i class="fas fa-shopping-cart"></i>
                    <span class="cart-count">3</span>
                </div>
            </nav>
        </div>
    </header>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const navLinks = document.querySelector('.nav-links');

            mobileMenuBtn.addEventListener('click', function() {
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
