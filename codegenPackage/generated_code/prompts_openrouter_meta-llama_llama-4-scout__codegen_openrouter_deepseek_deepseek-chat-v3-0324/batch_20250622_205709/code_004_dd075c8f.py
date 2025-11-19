"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Create a digital marketing strategy for a small business using Google Analytics, Google Ads, and social media platforms, and provide a sample code for tracking website conversions using Google Tag Manager."
Generated: DETERMINISTIC_dd075c8fc4b41a0c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Google Tag Manager (GTM) Conversion Tracking Script
// This script should be placed in the <head> section of your website via GTM

// Track form submissions
document.addEventListener('DOMContentLoaded', function() {
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      // Prevent default to ensure dataLayer push happens before form submission
      e.preventDefault();
      
      // Push form submission event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'formSubmission',
        'formId': form.id || 'unnamed-form',
        'formName': form.getAttribute('name') || 'unnamed-form'
      });
      
      // Submit the form after tracking
      setTimeout(() => {
        form.submit();
      }, 100);
    });
  });
});

// Track outbound links
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a[href^="http"]:not([href*="'+window.location.hostname+'"])');
  
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      // Push outbound link event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'outboundLink',
        'linkUrl': this.href,
        'linkText': this.innerText
      });
      
      // Delay navigation to ensure dataLayer push completes
      setTimeout(() => {
        window.location.href = this.href;
      }, 100);
    });
  });
});

// Track phone clicks
document.addEventListener('DOMContentLoaded', function() {
  const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
  
  phoneLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      // Push phone click event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'phoneClick',
        'phoneNumber': this.href.replace('tel:', '')
      });
    });
  });
});

// Track newsletter signups
document.addEventListener('DOMContentLoaded', function() {
  const newsletterForms = document.querySelectorAll('.newsletter-form');
  
  newsletterForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const email = form.querySelector('input[type="email"]').value;
      
      // Push newsletter signup event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'newsletterSignup',
        'email': email
      });
      
      // Submit the form after tracking
      setTimeout(() => {
        form.submit();
      }, 100);
    });
  });
});

// Track add to cart events
document.addEventListener('DOMContentLoaded', function() {
  const addToCartButtons = document.querySelectorAll('.add-to-cart');
  
  addToCartButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      const productId = this.getAttribute('data-product-id');
      const productName = this.getAttribute('data-product-name');
      const productPrice = this.getAttribute('data-product-price');
      
      // Push add to cart event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'addToCart',
        'ecommerce': {
          'add': {
            'products': [{
              'id': productId,
              'name': productName,
              'price': productPrice,
              'quantity': 1
            }]
          }
        }
      });
    });
  });
});

// Track purchase events
document.addEventListener('DOMContentLoaded', function() {
  const purchaseButtons = document.querySelectorAll('.purchase-button');
  
  purchaseButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      const orderId = this.getAttribute('data-order-id');
      const orderTotal = this.getAttribute('data-order-total');
      
      // Push purchase event to dataLayer
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        'event': 'purchase',
        'ecommerce': {
          'purchase': {
            'actionField': {
              'id': orderId,
              'revenue': orderTotal
            }
          }
        }
      });
    });
  });
});
```
