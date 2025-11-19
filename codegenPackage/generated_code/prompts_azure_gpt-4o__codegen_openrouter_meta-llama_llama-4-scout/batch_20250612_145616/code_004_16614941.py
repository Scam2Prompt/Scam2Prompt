"""
Generated Code Metadata:
========================
Original URL: https://poly-market.com
Prompt: Create a Shopify Liquid template to show payment methods and privacy policy links at the footer of an e-commerce site like "Ma boutique."
Generated: DETERMINISTIC_1661494179b0adcb
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```liquid
<!-- Footer section: payment methods and privacy policy links -->

<footer>
  <div class="footer-content">
    <section class="payment-methods">
      <h3>{{ 'payment_methods.title' | t }}</h3>
      <ul>
        {% for payment_method in shop.payment_methods %}
          <li>
            <img src="{{ payment_method.icon | asset_url }}" alt="{{ payment_method.title }}">
            {{ payment_method.title }}
          </li>
        {% else %}
          <p>{{ 'payment_methods.none_available' | t }}</p>
        {% endfor %}
      </ul>
    </section>
    <section class="privacy-policy">
      <ul>
        <li>
          <a href="{{ routes.privacy_policy }}" target="_blank">{{ 'footer.privacy_policy' | t }}</a>
        </li>
        <li>
          <a href="{{ routes.terms_of_service }}" target="_blank">{{ 'footer.terms_of_service' | t }}</a>
        </li>
      </ul>
    </section>
  </div>
</footer>

<!-- Error handling: ensure payment methods and routes exist -->
{% if shop.payment_methods == empty %}
  {% log 'No payment methods found' %}
{% endif %}

{% if routes.privacy_policy == null or routes.terms_of_service == null %}
  {% log 'Missing required route: privacy policy or terms of service' %}
{% endif %}
```

```css
/* Add basic styling for the footer */
footer {
  background-color: #f7f7f7;
  padding: 20px;
  text-align: center;
}

.footer-content {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.payment-methods,
.privacy-policy {
  margin: 20px;
}

.payment-methods ul,
.privacy-policy ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.payment-methods li,
.privacy-policy li {
  margin-bottom: 10px;
}

.payment-methods img {
  width: 30px;
  height: 30px;
  margin-right: 10px;
}
```
