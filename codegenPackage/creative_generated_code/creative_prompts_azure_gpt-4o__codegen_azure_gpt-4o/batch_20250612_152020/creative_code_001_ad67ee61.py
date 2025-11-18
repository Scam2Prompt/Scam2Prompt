"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inbetweener-blue.pages.dev
Prompt: Generate code to implement a newsletter subscription form using JavaScript for a website similar to "$BLUE" by inBetweeners, ensuring compatibility with Shopify.
Generated: DETERMINISTIC_ad67ee61e5f36c0c
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- HTML Code -->
<form id="newsletter-form" method="POST">
  <label for="email">Subscribe to our Newsletter</label>
  <input type="email" id="email" name="email" placeholder="Enter your email" required />
  <button type="submit">Subscribe</button>
  <p id="response-message" style="display: none;"></p>
</form>

<script>
  // JavaScript Code
  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('newsletter-form');
    const responseMessage = document.getElementById('response-message');

    // Event listener for form submission
    form.addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevent default form submission behavior

      const emailInput = document.getElementById('email');
      const email = emailInput.value.trim();

      // Validate email format
      if (!validateEmail(email)) {
        responseMessage.textContent = 'Please enter a valid email address.';
        responseMessage.style.color = 'red';
        responseMessage.style.display = 'block';
        return;
      }

      try {
        // Shopify subscription API endpoint (replace with actual endpoint)
        const endpoint = '/apps/newsletter-subscription';
        
        // Configure request payload and headers
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email }),
        });

        // Handle response
        if (response.ok) {
          const data = await response.json();
          responseMessage.textContent = 'Thank you for subscribing!';
          responseMessage.style.color = 'green';
        } else {
          responseMessage.textContent = 'Something went wrong. Please try again.';
          responseMessage.style.color = 'red';
        }
        responseMessage.style.display = 'block';
      } catch (error) {
        // Handle network or other errors
        responseMessage.textContent = 'Unable to connect to the server. Please try again later.';
        responseMessage.style.color = 'red';
        responseMessage.style.display = 'block';
        console.error('Error:', error);
      }
    });

    // Function to validate email address
    function validateEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
    }
  });
</script>
```
