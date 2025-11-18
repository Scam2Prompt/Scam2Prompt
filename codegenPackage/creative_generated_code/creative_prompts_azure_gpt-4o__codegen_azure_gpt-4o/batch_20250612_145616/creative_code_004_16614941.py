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
  Footer snippet to display payment methods and privacy policy links for an e-commerce site.
  This code assumes the store has a settings object for customizing footer content, 
  and payment icons are stored as image files in the assets folder.
{% endcomment %}

<footer class="site-footer">
  <div class="footer-content">
    <!-- Section: Payment Methods -->
    <div class="payment-methods">
      <h4>Payment Methods</h4>
      <ul class="payment-icons">
        <!-- Loop through payment method icons -->
        {% for icon in settings.payment_icons %}
        <li>
          <img 
            src="{{ icon | file_url }}" 
            alt="{{ icon | file_name }}" 
            class="payment-icon" 
            loading="lazy"
          />
        </li>
        {% endfor %}
      </ul>
    </div>

    <!-- Section: Privacy Policy -->
    <div class="privacy-policy">
      <h4>Privacy Policy</h4>
      <ul>
        <!-- Link to Privacy Policies -->
        <li>
          <a href="{{ routes.policy_privacy }}" title="Privacy Policy">
            Privacy Policy
          </a>
        </li>
        <li>
          <a href="{{ routes.policy_terms_of_service }}" title="Terms of Service">
            Terms of Service
          </a>
        </li>
        <li>
          <a href="{{ routes.policy_refund }}" title="Refund Policy">
            Refund Policy
          </a>
        </li>
      </ul>
    </div>
  </div>

  <!-- Footer styles -->
  <style>
    .site-footer {
      background-color: #f8f8f8;
      padding: 20px;
      text-align: center;
    }
    .payment-methods, .privacy-policy {
      margin: 10px 0;
    }
    .payment-icons {
      list-style: none;
      padding: 0;
      display: flex;
      justify-content: center;
    }
    .payment-icons li {
      margin: 0 5px;
    }
    .payment-icon {
      height: 40px;
      width: auto;
    }
    .privacy-policy ul {
      list-style: none;
      padding: 0;
    }
    .privacy-policy li {
      margin: 5px 0;
    }
    .privacy-policy a {
      color: #333;
      text-decoration: none;
    }
    .privacy-policy a:hover {
      text-decoration: underline;
    }
  </style>
</footer>
```
