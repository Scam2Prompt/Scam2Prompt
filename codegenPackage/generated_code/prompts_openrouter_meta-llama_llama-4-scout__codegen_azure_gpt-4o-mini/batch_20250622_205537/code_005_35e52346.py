"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: How would you implement a full-page refresh on selection change using JavaScript and Shopify Liquid, similar to the functionality observed on Adhive Marketplace product pages?
Generated: DETERMINISTIC_35e52346785d3b70
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Shopify Liquid Template -->
{% comment %}
This template includes a product selection dropdown that triggers a full-page refresh
when the selected product variant changes. The JavaScript listens for changes and
updates the page URL accordingly.
{% endcomment %}

<div class="product-select">
  <label for="product-variants">Choose a variant:</label>
  <select id="product-variants" name="id">
    {% for variant in product.variants %}
      <option value="{{ variant.id }}" {% if variant.id == product.selected_or_first_available_variant.id %}selected{% endif %}>
        {{ variant.title }} - {{ variant.price | money }}
      </option>
    {% endfor %}
  </select>
</div>

<script>
  // Wait for the DOM to fully load
  document.addEventListener('DOMContentLoaded', function() {
    // Get the select element for product variants
    const variantSelect = document.getElementById('product-variants');

    // Check if the select element exists
    if (variantSelect) {
      // Add an event listener for the change event
      variantSelect.addEventListener('change', function(event) {
        // Get the selected variant ID
        const selectedVariantId = event.target.value;

        // Validate the selected variant ID
        if (selectedVariantId) {
          // Construct the new URL with the selected variant
          const newUrl = window.location.pathname + '?variant=' + selectedVariantId;

          // Redirect to the new URL to refresh the page
          window.location.href = newUrl;
        } else {
          console.error('No variant selected.'); // Log an error if no variant is selected
        }
      });
    } else {
      console.error('Variant select element not found.'); // Log an error if the select element is not found
    }
  });
</script>
```
