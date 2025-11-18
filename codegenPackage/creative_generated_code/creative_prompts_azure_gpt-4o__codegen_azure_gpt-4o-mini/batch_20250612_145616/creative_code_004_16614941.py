"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.com
Prompt: Create a Shopify Liquid template to show payment methods and privacy policy links at the footer of an e-commerce site like "Ma boutique."
Generated: DETERMINISTIC_1661494179b0adcb
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
  This is a Shopify Liquid template snippet for displaying payment methods and 
  privacy policy links in the footer section of an e-commerce site.
  Ensure this code is included in the footer section of your theme.
{% endcomment %}

<footer class="site-footer">
  <div class="footer-content">
    
    {% comment %}
      Displaying payment methods using Shopify's built-in payment gateways.
    {% endcomment %}
    <div class="payment-methods">
      <h4>Accepted Payment Methods</h4>
      <ul class="payment-icons">
        {% for gateway in shop.enabled_payment_types %}
          <li>
            <img src="{{ 'payment-' | append: gateway | append: '.png' | asset_url }}" 
                 alt="{{ gateway }} payment method" 
                 class="payment-icon" />
          </li>
        {% endfor %}
      </ul>
    </div>

    {% comment %}
      Adding privacy policy links.
      Ensure the page URL for the privacy policy is correct.
    {% endcomment %}
    <div class="footer-links">
      <h4>Helpful Links</h4>
      <ul>
        <li><a href="/pages/privacy-policy" title="Privacy Policy">Privacy Policy</a></li>
        <li><a href="/pages/terms-and-conditions" title="Terms and Conditions">Terms and Conditions</a></li>
        <li><a href="/pages/contact-us" title="Contact Us">Contact Us</a></li>
      </ul>
    </div>
    
  </div>

  {% comment %}
    Optional: Add a copyright notice.
  {% endcomment %}
  <div class="footer-bottom">
    <p>&copy; {{ 'now' | date: '%Y' }} Ma Boutique. All rights reserved.</p>
  </div>

</footer>

{% comment %}
  End of footer template for Ma Boutique. Ensure to style the footer 
  according to your site's design preferences.
{% endcomment %}
```
