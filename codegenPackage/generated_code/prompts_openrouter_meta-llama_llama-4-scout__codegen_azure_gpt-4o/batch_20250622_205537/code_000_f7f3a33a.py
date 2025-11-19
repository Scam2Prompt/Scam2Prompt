"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: Write a Shopify code snippet to create a product sale page with a discount price similar to the "Anas Ali Shopify Course Complete" product on Adhive Marketplace.
Generated: DETERMINISTIC_f7f3a33a59c97bc5
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
<!-- Shopify Liquid Code for a Product Sale Page with Discount Price -->

<!-- Ensure this code is placed in the appropriate template file, such as 'product.liquid' -->

<!-- Wrapper for the product sale page -->
<div class="product-sale-page">
  <!-- Display the product title -->
  <h1 class="product-title">{{ product.title }}</h1>

  <!-- Product image -->
  <div class="product-image">
    <img src="{{ product.featured_image | img_url: 'large' }}" alt="{{ product.title }}">
  </div>

  <!-- Product price section -->
  <div class="product-pricing">
    <!-- Check if the product has a compare-at price (indicating a discount) -->
    {% if product.compare_at_price > product.price %}
      <!-- Display the original price -->
      <p class="original-price">
        <span>Original Price:</span>
        <span class="price">{{ product.compare_at_price | money }}</span>
      </p>

      <!-- Display the discounted price -->
      <p class="discounted-price">
        <span>Discounted Price:</span>
        <span class="price">{{ product.price | money }}</span>
      </p>

      <!-- Calculate and display the discount percentage -->
      <p class="discount-percentage">
        <span>Discount:</span>
        <span class="percentage">
          {{ 100.0 | minus: (product.price | times: 100.0) | divided_by: product.compare_at_price | round }}%
        </span>
      </p>
    {% else %}
      <!-- If no discount, display the regular price -->
      <p class="regular-price">
        <span>Price:</span>
        <span class="price">{{ product.price | money }}</span>
      </p>
    {% endif %}
  </div>

  <!-- Product description -->
  <div class="product-description">
    <h2>Description</h2>
    <p>{{ product.description }}</p>
  </div>

  <!-- Add to cart button -->
  <form method="post" action="/cart/add">
    <input type="hidden" name="id" value="{{ product.variants.first.id }}">
    <button type="submit" class="add-to-cart-button">Add to Cart</button>
  </form>
</div>

<!-- Styles for the product sale page -->
<style>
  .product-sale-page {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  .product-title {
    font-size: 2em;
    margin-bottom: 20px;
  }

  .product-image img {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px;
  }

  .product-pricing p {
    font-size: 1.2em;
    margin: 10px 0;
  }

  .original-price .price {
    text-decoration: line-through;
    color: #888;
  }

  .discounted-price .price {
    color: #e74c3c;
    font-weight: bold;
  }

  .discount-percentage .percentage {
    color: #27ae60;
    font-weight: bold;
  }

  .add-to-cart-button {
    background-color: #3498db;
    color: #fff;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    font-size: 1em;
  }

  .add-to-cart-button:hover {
    background-color: #2980b9;
  }
</style>
```
