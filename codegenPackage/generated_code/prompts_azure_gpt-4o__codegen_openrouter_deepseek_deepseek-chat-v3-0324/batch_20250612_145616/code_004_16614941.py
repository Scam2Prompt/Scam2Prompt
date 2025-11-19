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
{% comment %}
  Footer Payment Methods and Privacy Policy Links
  This snippet displays accepted payment methods and links to privacy policy pages.
  It should be included in the footer section of a Shopify theme.
{% endcomment %}

<footer class="site-footer">
  <div class="footer__content">
    {% comment %} Payment Methods Section {% endcomment %}
    <div class="footer__payment-methods">
      <h3 class="footer__heading">{{ 'layout.footer.payment_methods' | t }}</h3>
      <ul class="payment-icons">
        {% for type in shop.enabled_payment_types %}
          <li class="payment-icon">
            {{ type | payment_type_svg_tag: class: 'icon icon--full-color' }}
          </li>
        {% endfor %}
      </ul>
    </div>

    {% comment %} Policy Links Section {% endcomment %}
    <div class="footer__policy-links">
      <h3 class="footer__heading">{{ 'layout.footer.policies' | t }}</h3>
      <ul class="policy-links">
        {% for policy in shop.policies %}
          {% if policy != blank %}
            <li class="policy-link">
              <a href="{{ policy.url }}">{{ policy.title }}</a>
            </li>
          {% endif %}
        {% endfor %}
      </ul>
    </div>

    {% comment %} Copyright Notice {% endcomment %}
    <div class="footer__copyright">
      <small>
        &copy; {{ 'now' | date: "%Y" }}, {{ shop.name | link_to: '/' }}.
        {{ 'layout.footer.copyright' | t }}
      </small>
    </div>
  </div>
</footer>

<style>
  .site-footer {
    background-color: #f9f9f9;
    padding: 2rem 0;
    margin-top: 3rem;
    border-top: 1px solid #e1e1e1;
  }

  .footer__content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: flex-start;
  }

  .footer__heading {
    font-size: 1rem;
    margin-bottom: 1rem;
    color: #333;
  }

  .payment-icons {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .payment-icon {
    width: 40px;
    height: 25px;
  }

  .policy-links {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .policy-link {
    margin-bottom: 0.5rem;
  }

  .policy-link a {
    color: #666;
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .policy-link a:hover {
    color: #000;
  }

  .footer__copyright {
    width: 100%;
    margin-top: 2rem;
    text-align: center;
    color: #666;
  }

  .footer__copyright a {
    color: inherit;
    text-decoration: none;
  }

  @media (max-width: 768px) {
    .footer__content {
      flex-direction: column;
      gap: 2rem;
    }
  }
</style>
```
