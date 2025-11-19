"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wooof.online
Prompt: How can I customize the primary navigation for a Jekyll site to achieve a look and feel like that of wooof.online?
Generated: DETERMINISTIC_1858c67ff6dd6372
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a customizable primary navigation for a Jekyll site, similar to wooof.online:

### `navigation.html` (Partial Template)
Create a partial template for the navigation.

```html
<!-- _includes/navigation.html -->
<nav class="primary-navigation">
  <ul class="nav-list">
    <!-- Loop through site navigation items defined in _config.yml -->
    {% for item in site.data.navigation %}
    <li class="nav-item">
      <a href="{{ item.url }}" class="nav-link {% if page.url == item.url %}active{% endif %}">
        {{ item.title }}
      </a>
    </li>
    {% endfor %}
  </ul>
</nav>

<!-- In case of no navigation items, display a fallback -->
{% unless site.data.navigation %}
<p class="no-nav-warning">No navigation items found. Update `_data/navigation.yml` to add links.</p>
{% endunless %}
```

---

### `_data/navigation.yml` (Navigation Data)
Define your navigation items in a Jekyll data file.

```yaml
# _data/navigation.yml
- title: Home
  url: /
- title: About
  url: /about/
- title: Blog
  url: /blog/
- title: Contact
  url: /contact/
```

---

### `main.scss` (CSS for Navigation)
Customize the look and feel of the navigation bar in your site's main stylesheet.

```scss
/* assets/css/main.scss */
.primary-navigation {
  background-color: #f8f9fa; /* Light gray background */
  border-bottom: 2px solid #e0e0e0; /* Subtle border */

  .nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center; /* Centers navigation items */
  }

  .nav-item {
    margin: 0 1rem; /* Horizontal spacing between links */

    .nav-link {
      text-decoration: none;
      color: #333; /* Dark text color */
      font-weight: bold;
      transition: color 0.3s ease;

      &:hover {
        color: #0073e6; /* Blue hover effect */
      }

      &.active {
        color: #0073e6; /* Highlight for active page */
        border-bottom: 2px solid #0073e6; /* Underline active link */
      }
    }
  }
}

.no-nav-warning {
  color: #e63946; /* Warning color */
  font-style: italic;
  text-align: center;
}
```

---

### `_layouts/default.html` (Include Navigation in Layout)
Include the navigation partial in the default layout.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title | default: site.title }}</title>
  <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
</head>
<body>
  <!-- Include navigation -->
  {% include navigation.html %}

  <!-- Main content -->
  <main>
    {{ content }}
  </main>
</body>
</html>
```

---

### Error Handling in Build Process
Ensure the site gracefully handles cases where `_data/navigation.yml` is missing or empty.

- Jekyll inherently skips loops if `site.data.navigation` is not present or empty.
- A fallback warning is provided in the `navigation.html` partial.

This implementation is clean, modular, and easy to customize for your Jekyll site.
