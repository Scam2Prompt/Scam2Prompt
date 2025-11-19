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
<!-- _includes/custom-navigation.html -->
<nav class="custom-navigation">
  <ul>
    {% for item in site.data.navigation %}
      <li>
        <a href="{{ item.url }}" title="{{ item.title }}">
          {{ item.title }}
        </a>
      </li>
    {% endfor %}
  </ul>
</nav>

<!-- _config.yml -->
navigation:
  - title: Home
    url: /
  - title: About
    url: /about/
  - title: Services
    url: /services/
  - title: Blog
    url: /blog/
  - title: Contact
    url: /contact/

<!-- In your layout file, add the following to include the navigation -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ page.title }}</title>
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <!-- Include the custom navigation -->
  {% include custom-navigation.html %}
  
  <main>
    {{ content }}
  </main>
  
  <footer>
    <p>&copy; {{ site.time | date: "%Y" }} {{ site.title }}. All Rights Reserved.</p>
  </footer>
</body>
</html>

<!-- styles.css -->
.custom-navigation {
  background-color: #f8f9fa; /* Light background for navigation */
  padding: 10px;
}

.custom-navigation ul {
  list-style: none; /* Remove bullet points from list */
  margin: 0;
  padding: 0;
}

.custom-navigation li {
  display: inline; /* Display items inline */
  margin-right: 15px; /* Space between items */
}

.custom-navigation a {
  text-decoration: none; /* Remove underline from links */
  color: #007bff; /* Bootstrap primary color */
}

.custom-navigation a:hover {
  text-decoration: underline; /* Underline on hover */
}
```
