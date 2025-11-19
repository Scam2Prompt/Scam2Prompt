"""
Generated Code Metadata:
========================
Original URL: https://bearmybrand.com
Prompt: Create a Shopify store template for a fitness brand, inspired by the custom web development services offered by Bear My Brand, LLC.
Generated: DETERMINISTIC_e06878479e826577
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Shopify Store Template for Fitness Brand**
=============================================

**config.yml**
```yml
title: Fitness Brand
description: Empowering your fitness journey
timezone: America/New_York
```

**layout.liquid**
```liquid
<!DOCTYPE html>
<html>
  <head>
    <title>{{ site.title }}</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{{ 'styles.css' | asset_url }}">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="{{ shop.url }}">Home</a></li>
          <li><a href="{{ shop.url }}/collections">Shop</a></li>
          <li><a href="{{ shop.url }}/about">About</a></li>
        </ul>
      </nav>
    </header>
    <main>
      {% yield %}
    </main>
    <footer>
      <p>&copy; {{ '2023' }} {{ site.title }}</p>
    </footer>
    <script src="{{ 'script.js' | asset_url }}"></script>
  </body>
</html>
```

**styles.css**
```css
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
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2em;
}

footer {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
  clear: both;
}
```

**script.js**
```javascript
// Add event listener to nav links
document.querySelectorAll('header nav a').forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const href = link.getAttribute('href');
    window.history.pushState({}, '', href);
    window.dispatchEvent(new Event('popstate'));
  });
});
```

**index.liquid**
```liquid
{% extends 'layout' %}

{% block content %}
  <h1>Welcome to {{ site.title }}</h1>
  <p>Discover our latest fitness gear and apparel</p>
  <button><a href="{{ shop.url }}/collections">Shop Now</a></button>
{% endblock %}
```

**collections.liquid**
```liquid
{% extends 'layout' %}

{% block content %}
  <h1>Shop Our Collections</h1>
  <ul>
    {% for collection in collections %}
      <li>
        <a href="{{ collection.url }}">{{ collection.title }}</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```

**product.liquid**
```liquid
{% extends 'layout' %}

{% block content %}
  <h1>{{ product.title }}</h1>
  <p>{{ product.description }}</p>
  <p>Price: {{ product.price | money }}</p>
  <form action="{{ product.url | append: '/buy' }}" method="post">
    <input type="hidden" name="id" value="{{ product.id }}">
    <button type="submit">Add to Cart</button>
  </form>
{% endblock %}
```

**cart.liquid**
```liquid
{% extends 'layout' %}

{% block content %}
  <h1>Cart</h1>
  <ul>
    {% for item in cart.items %}
      <li>
        {{ item.product.title }} x {{ item.quantity }}
      </li>
    {% endfor %}
  </ul>
  <p>Total: {{ cart.total_price | money }}</p>
{% endblock %}
```

**theme.liquid**
```liquid
{% layout 'layout' %}

{% block content %}
  {% case page %}
    {% when 'index' %}
      {% include 'index' %}
    {% when 'collections' %}
      {% include 'collections' %}
    {% when 'product' %}
      {% include 'product' %}
    {% when 'cart' %}
      {% include 'cart' %}
  {% endcase %}
{% endblock %}
```
