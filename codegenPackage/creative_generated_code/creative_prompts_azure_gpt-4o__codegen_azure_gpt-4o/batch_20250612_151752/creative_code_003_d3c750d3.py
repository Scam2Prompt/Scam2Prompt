"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wooof.online
Prompt: Create a Jekyll layout template that mimics the minimalist design style of wooof.online, including a toggle menu and footer.
Generated: DETERMINISTIC_d3c750d3e985a39f
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title | default: site.title }}</title>
  <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
  <script>
    /* Toggle menu functionality */
    function toggleMenu() {
      const menu = document.getElementById("nav-menu");
      menu.classList.toggle("open");
    }
  </script>
</head>
<body>
  <!-- Header Section -->
  <header>
    <div class="container header-container">
      <div class="logo">
        <a href="{{ site.baseurl | default: '/' }}">{{ site.title }}</a>
      </div>
      <button class="menu-toggle" onclick="toggleMenu()" aria-label="Toggle Menu">
        <!-- Hamburger icon -->
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </button>
    </div>
    <nav id="nav-menu" class="nav-menu">
      <ul>
        <li><a href="{{ site.baseurl }}/">Home</a></li>
        <li><a href="{{ site.baseurl }}/about/">About</a></li>
        <li><a href="{{ site.baseurl }}/contact/">Contact</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content Section -->
  <main class="container">
    {{ content }}
  </main>

  <!-- Footer Section -->
  <footer>
    <div class="container footer-container">
      <p>&copy; {{ site.time | date: '%Y' }} {{ site.title }}. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* File: style.css */

/* Resets */
body, h1, h2, h3, p, ul, li, a {
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
  box-sizing: border-box;
}

/* Layout */
body {
  background-color: #f9f9f9;
  color: #333;
  font-size: 16px;
  line-height: 1.6;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
header {
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}

.logo a {
  text-decoration: none;
  font-size: 1.5em;
  color: #333;
}

.menu-toggle {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.menu-toggle .bar {
  width: 25px;
  height: 3px;
  background-color: #333;
  margin: 2px 0;
}

.nav-menu {
  display: none;
  flex-direction: column;
  background-color: #fff;
  border-top: 1px solid #ddd;
}

.nav-menu.open {
  display: flex;
}

.nav-menu ul {
  list-style: none;
  padding: 10px;
}

.nav-menu a {
  text-decoration: none;
  color: #333;
  padding: 5px 0;
  display: block;
}

/* Main Content */
main {
  padding: 20px 0;
}

/* Footer */
footer {
  background-color: #fff;
  border-top: 1px solid #ddd;
  text-align: center;
  padding: 10px 0;
}

footer p {
  font-size: 0.9em;
  color: #666;
}
```
