"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Develop a Shopify Liquid template to display featured products such as "LUXXE SLIM" and "LUXXE RENEW" with dynamic pricing and stock availability.
Generated: DETERMINISTIC_95f7763506c263bc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
<!-- Featured Products Section -->
<section class="featured-products">
  <h2>Featured Products</h2>
  <ul class="product-list">
    {% assign featured_products = site.products | where: 'featured', true %}
    {% for product in featured_products %}
      <li class="product-list-item">
        <h3>{{ product.title }}</h3>
        <img src="{{ product.images | first | src }}" alt="{{ product.title }}">

        <!-- Pricing Section -->
        <div class="pricing">
          {% if product.price == product.compare_at_price %}
            <span class="price">{{ product.price | money }}</span>
          {% else %}
            <span class="original-price">{{ product.compare_at_price | money }}</span>
            <span class="discounted-price">{{ product.price | money }}</span>
          {% endif %}
        </div>

        <!-- Stock Availability Section -->
        <div class="stock-availability">
          {% if product.variants[0].inventory_quantity > 0 %}
            <span class="in-stock">In Stock</span>
          {% else %}
            <span class="out-of-stock">Out of Stock</span>
          {% endif %}
        </div>

        <!-- Call to Action Section -->
        <div class="cta">
          <a href="{{ product.url }}" class="btn">View Product</a>
          {% if product.variants[0].inventory_quantity > 0 %}
            <a href="{{ product.url }}?add-to-cart={{ product.variants[0].id }}" class="btn add-to-cart">Add to Cart</a>
          {% else %}
            <span class="sold-out">Sold Out</span>
          {% endif %}
        </div>
      </li>
    {% endfor %}
  </ul>
</section>
```

```liquid
<!-- LUXXE SLIM and LUXXE RENEW Specific Template -->
{% for product in site.products %}
  {% if product.title contains 'LUXXE SLIM' or product.title contains 'LUXXE RENEW' %}
    <div class="product-luxxe">
      <h2>{{ product.title }}</h2>
      <p>{{ product.description }}</p>
      <p>Price: {{ product.price | money }}</p>
      {% if product.variants[0].inventory_quantity > 0 %}
        <p>In Stock: {{ product.variants[0].inventory_quantity }}</p>
      {% else %}
        <p>Out of Stock</p>
      {% endif %}
      <a href="{{ product.url }}">View Product</a>
    </div>
  {% endif %}
{% endfor %}
```
