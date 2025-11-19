"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: Create a Shopify theme customization script to display regular and sale prices for products, inspired by the Adhive Marketplace layout.
Generated: DETERMINISTIC_04c023e9ca67bcb7
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
{% comment %}
  This script customizes the Shopify theme to display both regular and sale prices for products.
  It is inspired by the Adhive Marketplace layout.
{% endcomment %}

{% assign products = collections.all.products %}

<div class="product-list">
  {% for product in products %}
    <div class="product-item" id="product-{{ product.id }}">
      <h2 class="product-title">{{ product.title }}</h2>
      
      {% comment %}
        Check if the product is on sale by verifying if it has a compare at price.
      {% endcomment %}
      {% if product.compare_at_price > product.price %}
        <div class="product-price">
          <span class="sale-price">{{ product.price | money }}</span>
          <span class="regular-price">{{ product.compare_at_price | money }}</span>
        </div>
      {% else %}
        <div class="product-price">
          <span class="regular-price">{{ product.price | money }}</span>
        </div>
      {% endif %}
      
      {% comment %}
        Display the product image and a link to the product page.
      {% endcomment %}
      <a href="{{ product.url }}">
        <img src="{{ product.featured_image | img_url: 'medium' }}" alt="{{ product.title }}" class="product-image" />
      </a>
    </div>
  {% endfor %}
</div>

{% comment %}
  Error handling: If there are no products in the collection, display a message.
{% endcomment %}
{% if products.size == 0 %}
  <div class="no-products">
    <p>No products available at this time.</p>
  </div>
{% endif %}
```
