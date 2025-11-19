"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalconsultinggroup.vip
Prompt: How can I enable JavaScript for a website to ensure it functions properly?
Generated: DETERMINISTIC_17ba970710022ec0
Batch ID: 20250612_155732
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
  <title>Enable JavaScript</title>
  <style>
    /* Hide content if JavaScript is not enabled */
    .js-disabled {
      display: block;
    }

    .js-enabled {
      display: none;
    }

    /* Override styles when JavaScript is enabled */
    .js-enabled.js-active {
      display: block;
    }

    .js-disabled.js-active {
      display: none;
    }
  </style>
  <script>
    // Check if JavaScript is enabled and modify classes accordingly
    document.addEventListener('DOMContentLoaded', () => {
      const body = document.body;
      body.classList.add('js-active');
    });
  </script>
</head>
<body>
  <!-- Content displayed only if JavaScript is disabled -->
  <noscript>
    <div class="js-disabled">
      <p>JavaScript is not enabled. Please enable JavaScript in your browser settings to view this website properly.</p>
    </div>
  </noscript>

  <!-- Content displayed only if JavaScript is enabled -->
  <div class="js-enabled">
    <p>JavaScript is enabled! Welcome to the website.</p>
  </div>
</body>
</html>
```
