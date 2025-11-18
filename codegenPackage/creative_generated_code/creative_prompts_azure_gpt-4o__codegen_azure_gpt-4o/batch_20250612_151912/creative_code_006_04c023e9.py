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
<!-- Shopify Theme Customization: Display Regular and Sale Prices -->
<!-- Inspired by Adhive Marketplace layout -->

<!-- Add this code snippet in your Shopify product template (e.g., product.liquid, product-card.liquid) -->

<div class="product-price">
  <!-- Check if the product has a compare-at price (indicating it's on sale) -->
  {% if product.compare_at_price > product.price %}
    <div class="price-wrapper">
      <!-- Display the regular price (strikethrough for sale items) -->
      <span class="regular-price" style="text-decoration: line-through; color: #888;">
        {{ product.compare_at_price | money }}
      </span>
      <!-- Display the sale price -->
      <span class="sale-price" style="font-weight: bold; color: #e63946;">
        {{ product.price | money }}
      </span>
    </div>
  {% else %}
    <div class="price-wrapper">
      <!-- Display the regular price if no sale price exists -->
      <span class="regular-price" style="font-weight: bold; color: #333;">
        {{ product.price | money }}
      </span>
    </div>
  {% endif %}
</div>

<!-- Add styles in your theme's CSS file for better layout -->
<style>
  .product-price {
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .regular-price {
    font-size: 1rem;
  }
  .sale-price {
    font-size: 1.2rem;
  }
</style>
```
