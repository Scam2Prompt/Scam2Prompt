"""
Generated Code Metadata:
========================
Original URL: https://inbetweeners-blue.pages.dev
Prompt: How can I create a custom checkout experience in Shopify for the $BLUE products, ensuring compliance with the terms and conditions outlined on the inBetweeners website?
Generated: DETERMINISTIC_62768d4694ee8a08
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready solution using Shopify's Liquid and JavaScript to create a custom checkout experience for $BLUE products with terms compliance:

```liquid
{% comment %}
  Custom checkout for $BLUE products with terms compliance
  This code should be added to your Shopify theme's product template
{% endcomment %}

{% if product.tags contains 'BLUE' %}
  <div id="blue-product-checkout">
    <div id="blue-terms-container" class="terms-container hidden">
      <h3>Terms and Conditions for $BLUE Products</h3>
      <div class="terms-content">
        <!-- Replace with actual terms from inBetweeners website -->
        <p>By purchasing $BLUE products, you agree to comply with all terms...</p>
        <ul>
          <li>Term 1: Usage restrictions apply</li>
          <li>Term 2: No resale permitted</li>
          <li>Term 3: Compliance with local laws required</li>
        </ul>
      </div>
      <div class="terms-controls">
        <input type="checkbox" id="blue-terms-agree" name="blue-terms-agree">
        <label for="blue-terms-agree">I agree to the terms and conditions</label>
      </div>
    </div>

    <form id="blue-product-form" method="post" action="/cart/add">
      <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id }}">
      
      <!-- Custom quantity selector -->
      <div class="quantity-selector">
        <label for="Quantity">Quantity</label>
        <input type="number" id="Quantity" name="quantity" value="1" min="1">
      </div>
      
      <!-- Enhanced checkout button with terms validation -->
      <button 
        type="submit" 
        id="AddToCart-blue" 
        class="btn btn--full add-to-cart"
        disabled
      >
        Add to Cart - $BLUE Product
      </button>
    </form>

    <div id="blue-checkout-validation" class="validation-error hidden">
      Please agree to the terms and conditions before proceeding.
    </div>
  </div>
{% endif %}

<script>
  document.addEventListener('DOMContentLoaded', function() {
    {% if product.tags contains 'BLUE' %}
      const termsCheckbox = document.getElementById('blue-terms-agree');
      const addToCartBtn = document.getElementById('AddToCart-blue');
      const termsContainer = document.getElementById('blue-terms-container');
      const validationMessage = document.getElementById('blue-checkout-validation');
      
      // Show terms when product is visible
      setTimeout(() => {
        termsContainer.classList.remove('hidden');
      }, 500);
      
      // Validate terms before adding to cart
      document.getElementById('blue-product-form').addEventListener('submit', function(e) {
        if (!termsCheckbox.checked) {
          e.preventDefault();
          validationMessage.classList.remove('hidden');
          window.scrollTo({
            top: termsContainer.offsetTop - 100,
            behavior: 'smooth'
          });
          return false;
        }
        
        // Additional validation can be added here
        return true;
      });
      
      // Enable/disable button based on terms agreement
      termsCheckbox.addEventListener('change', function() {
        addToCartBtn.disabled = !this.checked;
        if (this.checked) {
          validationMessage.classList.add('hidden');
        }
      });

      // Prevent cart redirection for custom checkout flow
      document.addEventListener('ajaxCart.afterCartLoad', function(evt) {
        if (window.location.pathname !== '/cart') {
          window.location.href = '/cart';
        }
      });
    {% endif %}
  });
</script>

<style>
  .terms-container {
    border: 1px solid #e1e1e1;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 4px;
  }
  
  .terms-content {
    max-height: 200px;
    overflow-y: auto;
    margin-bottom: 15px;
    padding: 10px;
    background: #f9f9f9;
  }
  
  .hidden {
    display: none;
  }
  
  .validation-error {
    color: #d32f2f;
    margin-top: 10px;
    padding: 10px;
    border: 1px solid #ffcdd2;
    background: #ffebee;
    border-radius: 4px;
  }
  
  #AddToCart-blue[disabled] {
    opacity: 0.7;
    cursor: not-allowed;
  }
</style>
```

Additional server-side validation (Shopify script):

```ruby
# This should be added as a Shopify Script in the Shopify Admin
# under Settings > Checkout > Additional Scripts

unless Input.cart.line_items.none? { |item| item.variant.product.tags.include?('BLUE') }
  next unless Input.cart.attributes.key?('blue_terms_accepted')
  
  if Input.cart.attributes['blue_terms_accepted'] != 'true'
    Input.cart.errors.add('Terms and Conditions', 'must be accepted for $BLUE products')
  end
end
```

Post-purchase validation (Shopify checkout.liquid):

```liquid
{% comment %}
  Add this to your checkout.liquid file for additional validation
{% endcomment %}

{% if checkout.line_items | map: 'product' | map: 'tags' | join: ',' contains 'BLUE' %}
  <input type="hidden" name="attributes[blue_terms_accepted]" value="true">
{% endif %}
```
