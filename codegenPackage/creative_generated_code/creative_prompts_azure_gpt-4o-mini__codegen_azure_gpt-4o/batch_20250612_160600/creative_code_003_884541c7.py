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
  This code snippet retrieves and displays the sale price of a product from Adhive Marketplace
  in a Shopify theme. Ensure you have the necessary API integrations or custom fields added
  to your Shopify store for compatibility with Adhive Marketplace data.
{% endcomment %}

<!-- Check if the product has a sale price provided by Adhive Marketplace -->
{% if product.metafields.adhive.sale_price %}
  <div class="product-sale-price">
    <!-- Display the sale price -->
    <p>Sale Price: {{ product.metafields.adhive.sale_price | money }}</p>
  </div>
{% else %}
  <!-- Fallback if no sale price is available -->
  <div class="product-regular-price">
    <p>Regular Price: {{ product.price | money }}</p>
  </div>
{% endif %}

{% comment %}
  Notes:
  - Replace "adhive.sale_price" with the appropriate namespace and key from your metafields configuration.
  - Ensure the product metafields for Adhive data are properly populated in your Shopify admin.
  - The `money` filter converts the price to the store's currency format.
{% endcomment %}
```
