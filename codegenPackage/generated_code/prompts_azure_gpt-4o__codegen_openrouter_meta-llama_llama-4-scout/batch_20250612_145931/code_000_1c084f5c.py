"""
Generated Code Metadata:
========================
Original URL: https://v-tempe.online
Prompt: Write JavaScript code to dynamically display a link or text based on the presence of UTM parameters in the URL, as described on the "v-tempe.online" webpage.
Generated: DETERMINISTIC_1c084f5cd910872d
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamically displays a link or text based on the presence of UTM parameters in the URL.
 */

// Function to get UTM parameters from URL
function getUtmParams() {
  const urlParams = new URLSearchParams(window.location.search);
  const utmParams = {};

  // Check for UTM parameters
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(param => {
    if (urlParams.has(param)) {
      utmParams[param] = urlParams.get(param);
    }
  });

  return utmParams;
}

// Function to display link or text based on UTM parameters
function displayLinkOrText() {
  const utmParams = getUtmParams();
  const linkElement = document.getElementById('link');
  const textElement = document.getElementById('text');

  if (Object.keys(utmParams).length > 0) {
    // Display link if UTM parameters are present
    linkElement.style.display = 'block';
    textElement.style.display = 'none';

    // Update link text with UTM parameters
    const linkText = `Track this link from ${utmParams.utm_source} - ${utmParams.utm_campaign}`;
    linkElement.textContent = linkText;
  } else {
    // Display text if UTM parameters are not present
    linkElement.style.display = 'none';
    textElement.style.display = 'block';
  }
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
  try {
    displayLinkOrText();
  } catch (error) {
    console.error('Error displaying link or text:', error);
  }
});
```

```html
<!-- Example HTML -->
<html>
  <body>
    <a id="link" style="display: none;"></a>
    <p id="text" style="display: none;">No UTM parameters found.</p>
    <script src="script.js"></script>
  </body>
</html>
```
