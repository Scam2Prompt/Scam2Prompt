"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wooof.online
Prompt: Generate a code snippet to implement a custom navigation menu for a Jekyll site similar to wooof.online.
Generated: DETERMINISTIC_ace72be1a7be7e41
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- _includes/navigation.html -->
<!-- Custom Navigation Menu for Jekyll Site -->
<nav class="navigation-menu">
  <ul class="menu-list">
    {% for link in site.data.navigation %}
      <li class="menu-item">
        <a href="{{ link.url }}" class="menu-link {% if page.url == link.url %}active{% endif %}">
          {{ link.name }}
        </a>
      </li>
    {% endfor %}
  </ul>
</nav>
```

```yaml
# _data/navigation.yml
# Navigation Menu Data
- name: Home
  url: /
- name: About
  url: /about/
- name: Blog
  url: /blog/
- name: Contact
  url: /contact/
```

```scss
/* assets/css/navigation.scss */
/* Styles for Custom Navigation Menu */
.navigation-menu {
  background-color: #f8f9fa;
  padding: 10px;
  border-bottom: 1px solid #e0e0e0;
}

.menu-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.menu-item {
  margin-right: 15px;
}

.menu-link {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: color 0.3s ease;
}

.menu-link:hover {
  color: #007bff;
}

.menu-link.active {
  color: #007bff;
  text-decoration: underline;
}
```

```rb
# _config.yml
# Ensure Jekyll reads the navigation data file
collections:
  data: true

# Include Sass preprocessing for styling
sass:
  sass_dir: assets/css
```

```html
<!-- Use the navigation menu in a layout -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }}</title>
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
  <!-- Include the Navigation Menu -->
  {% include navigation.html %}
  <main>
    <!-- Page Content -->
    {{ content }}
  </main>
</body>
</html>
```
