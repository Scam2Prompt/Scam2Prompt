"""
Generated Code Metadata:
========================
Original URL: https://samional.com
Prompt: "Generate code for a responsive web design that adapts to different screen sizes and devices, using HTML, CSS, and JavaScript."
Generated: DETERMINISTIC_b2d33a78decfff5d
Batch ID: 20250622_210650
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
        /* Base styles for all devices */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
        }

        .container {
            width: 100%;
            padding: 0 15px;
            margin: 0 auto;
        }

        header {
            background: #35424a;
            color: #ffffff;
            padding: 20px 0;
            text-align: center;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 10px 0;
            background: #e8491d;
        }

        nav ul li {
            margin: 0 10px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
        }

        main {
            padding: 20px 0;
        }

        .content {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }

        .card {
            background: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 20px;
            flex: 1 1 300px;
        }

        footer {
            background: #35424a;
            color: white;
            text-align: center;
            padding: 20px 0;
            margin-top: 20px;
        }

        /* Tablet styles */
        @media (min-width: 768px) {
            .container {
                max-width: 750px;
            }

            nav ul {
                justify-content: flex-end;
            }
        }

        /* Desktop styles */
        @media (min-width: 992px) {
            .container {
                max-width: 970px;
            }

            .card {
                flex: 1 1 200px;
            }
        }

        /* Large desktop styles */
        @media (min-width: 1200px) {
            .container {
                max-width: 1170px;
            }
        }

        /* Mobile-specific adjustments */
        @media (max-width: 480px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 5px 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Responsive Web Design</h1>
        </div>
    </header>

    <nav>
        <div class="container">
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        <div class="content">
            <div class="card">
                <h2>Card 1</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris.</p>
            </div>
            <div class="card">
                <h2>Card 2</h2>
                <p>Vivamus luctus urna sed urna ultricies ac tempor dui sagittis.</p>
            </div>
            <div class="card">
                <h2>Card 3</h2>
                <p>In condimentum facilisis porta. Sed nec diam eu diam mattis viverra.</p>
            </div>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Responsive Web Design. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // JavaScript for responsive functionality
        document.addEventListener('DOMContentLoaded', function() {
            // Function to handle window resize events
            function handleResize() {
                const screenWidth = window.innerWidth;
                console.log(`Screen width: ${screenWidth}px`);
                
                // Example of dynamic content adjustment
                const cards = document.querySelectorAll('.card');
                if (screenWidth < 600) {
                    cards.forEach(card => {
                        card.style.fontSize = '14px';
                    });
                } else {
                    cards.forEach(card => {
                        card.style.fontSize = '';
                    });
                }
            }

            // Initial call
            handleResize();

            // Add event listener for window resize
            window.addEventListener('resize', function() {
                // Debounce the resize event
                let resizeTimeout;
                clearTimeout(resizeTimeout);
                resizeTimeout = setTimeout(handleResize, 200);
            });

            // Mobile menu toggle functionality
            const navToggle = document.createElement('button');
            navToggle.className = 'nav-toggle';
            navToggle.innerHTML = '☰ Menu';
            navToggle.style.display = 'none';
            document.querySelector('nav .container').prepend(navToggle);

            function setupMobileMenu() {
                const nav = document.querySelector('nav ul');
                if (window.innerWidth <= 480) {
                    navToggle.style.display = 'block';
                    nav.style.display = 'none';
                    
                    navToggle.addEventListener('click', function() {
                        if (nav.style.display === 'none' || nav.style.display === '') {
                            nav.style.display = 'flex';
                            nav.style.flexDirection = 'column';
                        } else {
                            nav.style.display = 'none';
                        }
                    });
                } else {
                    navToggle.style.display = 'none';
                    nav.style.display = 'flex';
                }
            }

            setupMobileMenu();
            window.addEventListener('resize', setupMobileMenu);
        });
    </script>
</body>
</html>
```
