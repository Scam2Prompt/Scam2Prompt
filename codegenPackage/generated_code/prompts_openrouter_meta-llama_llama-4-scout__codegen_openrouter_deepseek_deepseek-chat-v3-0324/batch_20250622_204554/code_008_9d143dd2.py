"""
Generated Code Metadata:
========================
Original URL: https://www.sgeek-seo.com
Prompt: "Develop a simple website layout using CSS and HTML."
Generated: DETERMINISTIC_9d143dd283ad73e0
Batch ID: 20250622_204554
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
    <title>Simple Website Layout</title>
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
            color: #333;
            background-color: #f4f4f4;
        }

        /* Header styles */
        header {
            background: #35424a;
            color: #ffffff;
            padding: 1rem 0;
            text-align: center;
            border-bottom: 3px solid #e8491d;
        }

        header h1 {
            margin-bottom: 0.5rem;
        }

        /* Navigation styles */
        nav {
            background: #35424a;
            padding: 0.5rem 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 1rem;
        }

        nav ul li a {
            color: #ffffff;
            text-decoration: none;
            padding: 0.5rem;
            transition: all 0.3s ease;
        }

        nav ul li a:hover {
            color: #e8491d;
        }

        /* Main content area */
        .container {
            width: 80%;
            margin: 2rem auto;
            overflow: hidden;
        }

        /* Showcase section */
        #showcase {
            background: #e8491d;
            color: #ffffff;
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Main content and sidebar */
        .main {
            float: left;
            width: 70%;
            padding: 0 1rem;
        }

        .sidebar {
            float: right;
            width: 30%;
            padding: 0 1rem;
            background: #e6e6e6;
        }

        /* Footer styles */
        footer {
            background: #35424a;
            color: #ffffff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
            clear: both;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .main, .sidebar {
                width: 100%;
                float: none;
            }

            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
        <p>Your one-stop destination for all things web</p>
    </header>

    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <section id="showcase">
        <h2>Professional Web Design</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris.</p>
    </section>

    <div class="container">
        <main class="main">
            <h2>Main Content</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mi augue, viverra sit amet ultricies at, vulputate id lorem. Nulla facilisi.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mi augue, viverra sit amet ultricies at, vulputate id lorem. Nulla facilisi.</p>
        </main>

        <aside class="sidebar">
            <h3>Sidebar</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mi augue, viverra sit amet ultricies at.</p>
        </aside>
    </div>

    <footer>
        <p>Simple Website Layout &copy; 2023</p>
    </footer>
</body>
</html>
```
