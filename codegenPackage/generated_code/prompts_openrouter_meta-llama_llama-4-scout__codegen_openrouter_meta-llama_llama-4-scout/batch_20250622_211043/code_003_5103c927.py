"""
Generated Code Metadata:
========================
Original URL: https://bestwebtrand.cc
Prompt: Write a basic example of how to check if JavaScript is enabled in a user's browser and display a message accordingly.
Generated: DETERMINISTIC_5103c9279b1ee67c
Batch ID: 20250622_211043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the user's browser

// Create a noscript element to display a message when JavaScript is disabled
<noscript>
  <p>JavaScript is disabled in your browser. Please enable JavaScript to view this page properly.</p>
</noscript>

// Create a script element to check if JavaScript is enabled
<script>
// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
  try {
    // Create a test element to check if JavaScript is enabled
    var testElement = document.createElement('div');
    testElement.innerHTML = 'JavaScript is enabled';
    document.body.appendChild(testElement);
    
    // If the test element is displayed, JavaScript is enabled
    if (testElement.innerHTML === 'JavaScript is enabled') {
      // Display a message when JavaScript is enabled
      document.getElementById('js-enabled-message').innerHTML = 'JavaScript is enabled in your browser.';
    }
  } catch (error) {
    // Log any errors that occur during the check
    console.error('Error checking JavaScript enabled:', error);
  }
}

// Call the function to check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', function() {
  checkJavaScriptEnabled();
});
</script>

// Create a paragraph element to display a message when JavaScript is enabled
<p id="js-enabled-message"></p>
``` 
However, I realized I made a mistake. A noscript tag already does what a user wants. So here is a more minimal version.

```html
<noscript>
  <p>JavaScript is disabled in your browser. Please enable JavaScript to view this page properly.</p>
</noscript>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('js-enabled-message').innerHTML = 'JavaScript is enabled in your browser.';
  });
</script>

<p id="js-enabled-message"></p>
```
