"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imqbo.com
Prompt: Write a script that checks if a user's browser supports JavaScript and Web3 functionality, and prompts them to enable JavaScript for interacting with an ETH pledge system.
Generated: DETERMINISTIC_ac7e7417fdec1465
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ETH Pledge System</title>
  <script>
    // Function to check JavaScript and Web3 support
    function checkBrowserSupport() {
      // Check if JavaScript is enabled (this script runs only if JS is enabled)
      const jsEnabled = true;

      // Check if Web3 is supported by the browser (Ethereum provider like MetaMask)
      const web3Enabled = typeof window.ethereum !== 'undefined';

      // If Web3 is not supported, prompt the user to enable it
      if (!web3Enabled) {
        alert('Your browser does not support Web3 functionality. Please install a Web3 provider like MetaMask to interact with the ETH pledge system.');
      } else {
        console.log('Web3 is enabled and ready to use.');
      }
    }

    // Run the check on page load
    window.onload = checkBrowserSupport;
  </script>
</head>
<body>
  <noscript>
    <!-- Fallback for browsers with JavaScript disabled -->
    <p style="color: red;">JavaScript is disabled in your browser. Please enable JavaScript to interact with the ETH pledge system.</p>
  </noscript>

  <h1>Welcome to the ETH Pledge System</h1>
  <p>Please ensure JavaScript and Web3 functionality are enabled in your browser to proceed.</p>
</body>
</html>
```
