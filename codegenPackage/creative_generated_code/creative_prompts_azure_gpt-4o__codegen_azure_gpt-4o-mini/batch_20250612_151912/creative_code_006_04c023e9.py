"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Create a Shopify theme customization script to display regular and sale prices for products, inspired by the Adhive Marketplace layout.
Generated: DETERMINISTIC_04c023e9ca67bcb7
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```liquid
{% comment %}
  This script customizes the product display in a Shopify theme to show both regular and sale prices.
  It is inspired by the Adhive Marketplace layout.
{% endcomment %}

{% if product %}
  <div class="product">
    <h2 class="product-title">{{ product.title }}</h2>
    
    {% comment %}
      Check if the product is on sale by verifying if there's a compare at price.
    {% endcomment %}
    {% if product.compare_at_price > product.price %}
      <div class="product-price">
        <span class="sale-price">{{ product.price | money }}</span>
        <span class="regular-price">
          {{ product.compare_at_price | money }}
        </span>
      </div>
    {% else %}
      <div class="product-price">
        <span class="regular-price">{{ product.price | money }}</span>
      </div>
    {% endif %}
    
    {% comment %}
      Display the product image, if available.
    {% endcomment %}
    {% if product.images.size > 0 %}
      <img src="{{ product.images.first.src | img_url: 'medium' }}" alt="{{ product.title }}" class="product-image" />
    {% endif %}
    
    {% comment %}
      Link to the product page for more details.
    {% endcomment %}
    <a href="{{ product.url }}" class="view-product">View Product</a>
  </div>
{% else %}
  <div class="error-message">
    <p>Product not found. Please check back later.</p>
  </div>
{% endif %}
```
