"""
Generated Code Metadata:
========================
Original URL: https://demo-8g2.pages.dev
Prompt: Design a footer section for an e-commerce website including contact information, social media links, and terms & conditions.
Generated: DETERMINISTIC_f398fc3471d0de13
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Footer Section -->
<footer class="footer">
  <div class="container">
    <!-- Contact Information -->
    <div class="footer-contact">
      <h4>Contact Us</h4>
      <ul>
        <li>
          <i class="fas fa-phone"></i>
          <span>Phone: +1 234 567 890</span>
        </li>
        <li>
          <i class="fas fa-envelope"></i>
          <span>Email: <a href="mailto:info@example.com">info@example.com</a></span>
        </li>
        <li>
          <i class="fas fa-map-marker-alt"></i>
          <span>Address: 123 Main St, Anytown, USA 12345</span>
        </li>
      </ul>
    </div>
    <!-- Social Media Links -->
    <div class="footer-social">
      <h4>Follow Us</h4>
      <ul>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">
            <i class="fab fa-facebook-f"></i>
          </a>
        </li>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">
            <i class="fab fa-twitter"></i>
          </a>
        </li>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">
            <i class="fab fa-instagram"></i>
          </a>
        </li>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">
            <i class="fab fa-linkedin-in"></i>
          </a>
        </li>
      </ul>
    </div>
    <!-- Terms & Conditions -->
    <div class="footer-terms">
      <ul>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">Terms of Service</a>
        </li>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">Privacy Policy</a>
        </li>
        <li>
          <a href="#" target="_blank" rel="noopener noreferrer">Return Policy</a>
        </li>
      </ul>
    </div>
  </div>
  <!-- Copyright Information -->
  <div class="footer-copyright">
    <p>&copy; 2023 Example E-commerce Website. All Rights Reserved.</p>
  </div>
</footer>

<!-- CSS Styling for Footer -->
<style>
  .footer {
    background-color: #333;
    color: #fff;
    padding: 40px 0;
  }
  .footer .container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .footer-contact, .footer-social, .footer-terms {
    margin-bottom: 20px;
    width: 30%;
  }
  .footer-contact h4, .footer-social h4 {
    margin-top: 0;
  }
  .footer-contact ul, .footer-social ul, .footer-terms ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .footer-contact li, .footer-social li, .footer-terms li {
    margin-bottom: 10px;
  }
  .footer-contact a, .footer-social a, .footer-terms a {
    color: #fff;
    text-decoration: none;
  }
  .footer-social a:hover {
    color: #ccc;
  }
  .footer-copyright {
    background-color: #444;
    padding: 10px;
    text-align: center;
    clear: both;
  }
  .footer-copyright p {
    margin: 0;
  }
</style>

<!-- JavaScript for Social Media Link Validation -->
<script>
  // Function to validate social media links
  function validateSocialMediaLinks() {
    const socialMediaLinks = document.querySelectorAll('.footer-social a');
    socialMediaLinks.forEach(link => {
      try {
        const url = new URL(link.href);
        if (!url.protocol || !url.host) {
          console.error('Invalid social media link:', link.href);
        }
      } catch (error) {
        console.error('Error validating social media link:', link.href, error);
      }
    });
  }

  // Call the function on page load
  document.addEventListener('DOMContentLoaded', validateSocialMediaLinks);
</script>
```
