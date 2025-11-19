"""
Generated Code Metadata:
========================
Original URL: https://runetech0.github.io
Prompt: "Create a code snippet for a simple blog archive page using Jekyll."
Generated: DETERMINISTIC_41e605a281f72ef2
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
---
layout: default
title: Blog Archive
permalink: /blog/archive/
---

<!-- Blog Archive Page -->
<h1>Blog Archive</h1>

<!-- Check if there are any posts -->
{% if site.posts.size > 0 %}

  <!-- Sort posts by date in descending order -->
  {% assign sorted_posts = site.posts | sort: 'date', 'last' %}

  <!-- Iterate over each year -->
  {% for post in sorted_posts %}
    {% assign post_year = post.date | date: '%Y' %}
    {% if forloop.first or post_year != previous_year %}
      <h2>{{ post_year }}</h2>
      {% assign previous_year = post_year %}
    {% endif %}

    <!-- Display post title and link -->
    <article>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p>{{ post.date | date: '%B %d, %Y' }}</p>
    </article>
  {% endfor %}

{% else %}
  <!-- Display a message if there are no posts -->
  <p>No posts found.</p>
{% endif %}
```

```html
<!-- If you want to make it more complex with HTML and CSS -->
<!-- _layouts/default.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ site.title }}</title>
    <link rel="stylesheet" href="{{ site.url }}/assets/css/style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ site.url }}">Home</a></li>
                <li><a href="{{ site.url }}/blog/archive/">Blog Archive</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {{ content }}
    </main>
    <footer>
        <p>&copy; {{ site.title }} {{ site.time | date: '%Y' }}</p>
    </footer>
</body>
</html>
```

```css
/* assets/css/style.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: block;
    padding: 2em;
}

article {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

article h3 {
    margin-top: 0;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
