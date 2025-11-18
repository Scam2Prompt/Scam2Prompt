"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Write a JavaScript function that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, similar to the behavior on mtec.cyou.
Generated: DETERMINISTIC_4e776f9f676560b2
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if JavaScript is enabled and redirect if it's disabled.
 * This function works by injecting a `<noscript>` tag into the DOM, which
 * will only execute when JavaScript is disabled.
 */
(function checkJavaScriptSupport() {
  // Create a <noscript> element to handle cases where JavaScript is disabled
  const noScriptElement = document.createElement('noscript');

  // Add an HTML fallback inside the <noscript> tag to perform redirection
  noScriptElement.innerHTML = `
    <meta http-equiv="refresh" content="0;url=/error.html">
  `;

  // Append the <noscript> element to the <body> of the page
  document.body.appendChild(noScriptElement);
})();
```
