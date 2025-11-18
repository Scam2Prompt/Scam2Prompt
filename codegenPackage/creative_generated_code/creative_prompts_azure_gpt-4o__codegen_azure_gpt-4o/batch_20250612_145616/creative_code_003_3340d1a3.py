"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.com
Prompt: Write code to display featured products with promotional pricing on the homepage of a Shopify store, referencing the structure used on "Ma boutique."
Generated: DETERMINISTIC_3340d1a34a510be6
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```liquid
{% comment %}
  Featured Products Section with Promotional Pricing
  This code displays a section of featured products with promotional pricing on the homepage.
  Ensure this code is placed in the appropriate section file within your Shopify theme (e.g., "featured-products.liquid").
{% endcomment %}

<section class="featured-products">
  <div class="container">
    <h2 class="section-title">Featured Products</h2>
    <div class="product-grid">
      {% for product in collections['featured-products'].products %}
        <div class="product-item">
          <a href="{{ product.url }}" class="product-link">
            <div class="product-image">
              <img 
                src="{{ product.featured_image | img_url: 'medium' }}" 
                alt="{{ product.title }}" 
                loading="lazy"
              >
            </div>
            <div class="product-details">
              <h3 class="product-title">{{ product.title }}</h3>
              
              {% comment %}
                Display promotional price if available; otherwise, display regular price.
              {% endcomment %}
              <div class="product-pricing">
                {% if product.compare_at_price > product.price %}
                  <span class="product-price product-price--sale">
                    {{ product.price | money }}
                  </span>
                  <span class="product-price product-price--original">
                    {{ product.compare_at_price | money }}
                  </span>
                {% else %}
                  <span class="product-price">
                    {{ product.price | money }}
                  </span>
                {% endif %}
              </div>
            </div>
          </a>
        </div>
      {% endfor %}
    </div>
  </div>
</section>

<style>
/* Basic styling for the Featured Products Section */
.featured-products {
  padding: 2rem 0;
}
.featured-products .section-title {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}
.product-item {
  border: 1px solid #e1e1e1;
  border-radius: 4px;
  overflow: hidden;
  background: #fff;
  transition: transform 0.2s;
}
.product-item:hover {
  transform: translateY(-5px);
}
.product-link {
  text-decoration: none;
  color: inherit;
}
.product-image img {
  width: 100%;
  display: block;
}
.product-details {
  padding: 1rem;
  text-align: center;
}
.product-title {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}
.product-pricing {
  font-size: 1rem;
}
.product-price--sale {
  color: #e60023;
  font-weight: bold;
}
.product-price--original {
  text-decoration: line-through;
  color: #999;
  margin-left: 0.5rem;
}
</style>

{% comment %}
  Notes:
  - The 'featured-products' collection must be created in Shopify and populated with the desired products.
  - Ensure the collection handle matches 'featured-products' or update it accordingly.
  - The pricing logic assumes 'compare_at_price' is used to define promotional pricing.
  - CSS classes can be adjusted as needed to match your store's design system.
{% endcomment %}
```
