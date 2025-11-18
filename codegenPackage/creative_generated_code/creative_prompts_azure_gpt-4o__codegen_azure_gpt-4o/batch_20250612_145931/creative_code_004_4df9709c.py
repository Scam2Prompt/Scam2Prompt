"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v-tempe.online
Prompt: Develop a JavaScript snippet to transfer UTM parameters from the current URL to external links, ensuring compatibility with the "v-tempe.online" site's traffic tracking system.
Generated: DETERMINISTIC_4df9709c8aa45776
Batch ID: 20250612_145931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript snippet to transfer UTM parameters from the current URL to external links
// ensuring compatibility with the "v-tempe.online" site's traffic tracking system.

document.addEventListener('DOMContentLoaded', () => {
  // Function to extract UTM parameters from the URL
  function getUTMParameters() {
    const urlParams = new URLSearchParams(window.location.search);
    const utmParams = {};
    // List of UTM parameters to capture
    const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
    
    utmKeys.forEach(key => {
      if (urlParams.has(key)) {
        utmParams[key] = urlParams.get(key);
      }
    });
    
    return utmParams;
  }

  // Function to append UTM parameters to a URL
  function appendUTMParameters(url, utmParams) {
    const newUrl = new URL(url);
    Object.entries(utmParams).forEach(([key, value]) => {
      newUrl.searchParams.set(key, value);
    });
    return newUrl.toString();
  }

  // Function to update all external links with UTM parameters
  function updateExternalLinks(utmParams) {
    const links = document.querySelectorAll('a[href]');

    links.forEach(link => {
      try {
        const href = link.getAttribute('href');
        // Only process external links and ensure they are for "v-tempe.online"
        if (href.startsWith('http') && href.includes('v-tempe.online')) {
          // Append UTM parameters to the link
          const updatedHref = appendUTMParameters(href, utmParams);
          link.setAttribute('href', updatedHref);
        }
      } catch (error) {
        console.error('Error processing link:', link, error);
      }
    });
  }

  // Main execution
  const utmParams = getUTMParameters();
  if (Object.keys(utmParams).length > 0) {
    updateExternalLinks(utmParams);
  }
});
```
