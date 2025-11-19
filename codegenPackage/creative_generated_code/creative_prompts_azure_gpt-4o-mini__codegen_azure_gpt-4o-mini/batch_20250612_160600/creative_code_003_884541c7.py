"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Provide an example of how to display the sale price of a product from Adhive Marketplace in a Shopify theme.
Generated: DETERMINISTIC_884541c739f16d5c
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```liquid
{% comment %}
  This snippet retrieves and displays the sale price of a product from Adhive Marketplace
  within a Shopify theme. It assumes you have access to the product's sale price variable 
  from Adhive Marketplace API or data layer.
{% endcomment %}

{% assign product_price = product.price | divided_by: 100 %}  {# Convert price from cents to dollars #}
{% assign product_sale_price = product.sale_price | divided_by: 100 %}  {# Convert sale price from cents to dollars #}

{% if product_sale_price > 0 and product_sale_price < product_price %}
  <div class="product-price">
    <span class="original-price" style="text-decoration: line-through; color: gray;">
      ${{ product_price | money }}
    </span>
    <span class="sale-price" style="color: red; font-weight: bold;">
      ${{ product_sale_price | money }}
    </span>
  </div>
{% else %}
  <div class="product-price">
    <span class="regular-price" style="color: black; font-weight: bold;">
      ${{ product_price | money }}
    </span>
  </div>
{% endif %}

{% comment %}
  Ensure the product object is defined and has the necessary attributes 
  before attempting to display prices.
{% endcomment %}
```
