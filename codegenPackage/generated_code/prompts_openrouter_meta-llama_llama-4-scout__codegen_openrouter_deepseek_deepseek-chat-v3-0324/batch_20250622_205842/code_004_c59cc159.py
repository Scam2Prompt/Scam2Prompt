"""
Generated Code Metadata:
========================
Original URL: https://2857qualifications.blogspot.com
Prompt: Create a simple blog layout using HTML and CSS for a technical documentation site.
Generated: DETERMINISTIC_c59cc1596c5e9c28
Batch ID: 20250622_205842
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
    <title>TechDocs Blog</title>
    <style>
        /* Reset and base styles */
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

        /* Layout container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

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

        /* Main content area */
        main {
            padding: 2rem 0;
        }

        /* Blog post styles */
        .blog-post {
            background: white;
            margin-bottom: 2rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .post-header {
            padding: 1.5rem;
            border-bottom: 1px solid #eee;
        }

        .post-title {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: #2c3e50;
        }

        .post-meta {
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        .post-content {
            padding: 1.5rem;
        }

        .post-content p {
            margin-bottom: 1rem;
        }

        .read-more {
            display: inline-block;
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
            margin-top: 1rem;
        }

        .read-more:hover {
            text-decoration: underline;
        }

        /* Sidebar styles */
        .sidebar {
            background: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        .sidebar-title {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            color: #2c3e50;
        }

        .sidebar ul {
            list-style: none;
        }

        .sidebar ul li {
            margin-bottom: 0.5rem;
        }

        .sidebar ul li a {
            color: #3498db;
            text-decoration: none;
        }

        .sidebar ul li a:hover {
            text-decoration: underline;
        }

        /* Footer styles */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive layout */
        @media (min-width: 768px) {
            .main-content {
                display: grid;
                grid-template-columns: 2fr 1fr;
                gap: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container header-content">
            <div class="logo">TechDocs</div>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Documentation</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container">
        <div class="main-content">
            <div class="blog-content">
                <article class="blog-post">
                    <div class="post-header">
                        <h2 class="post-title">Getting Started with React Hooks</h2>
                        <div class="post-meta">Posted on May 15, 2023 by Admin</div>
                    </div>
                    <div class="post-content">
                        <p>React Hooks provide a way to use state and other React features without writing classes. In this post, we'll explore the basics of useState and useEffect hooks.</p>
                        <p>Hooks are functions that let you "hook into" React state and lifecycle features from function components. They don't work inside classes — they let you use React without classes.</p>
                        <a href="#" class="read-more">Read more...</a>
                    </div>
                </article>

                <article class="blog-post">
                    <div class="post-header">
                        <h2 class="post-title">Understanding CSS Grid Layout</h2>
                        <div class="post-meta">Posted on April 28, 2023 by Editor</div>
                    </div>
                    <div class="post-content">
                        <p>CSS Grid Layout is a powerful tool that allows for two-dimensional layouts to be created on the web. This guide covers the fundamental concepts of grid layout.</p>
                        <p>With Grid Layout, you can create complex designs more easily and consistently across browsers. It works by turning an HTML element into a grid container with rows and columns.</p>
                        <a href="#" class="read-more">Read more...</a>
                    </div>
                </article>
            </div>

            <aside class="sidebar">
                <h3 class="sidebar-title">Categories</h3>
                <ul>
                    <li><a href="#">JavaScript</a></li>
                    <li><a href="#">CSS</a></li>
                    <li><a href="#">HTML</a></li>
                    <li><a href="#">React</a></li>
                    <li><a href="#">Node.js</a></li>
                </ul>

                <h3 class="sidebar-title">Recent Posts</h3>
                <ul>
                    <li><a href="#">Getting Started with React Hooks</a></li>
                    <li><a href="#">Understanding CSS Grid Layout</a></li>
                    <li><a href="#">TypeScript Best Practices</a></li>
                    <li><a href="#">Optimizing Web Performance</a></li>
                </ul>
            </aside>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 TechDocs. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```
