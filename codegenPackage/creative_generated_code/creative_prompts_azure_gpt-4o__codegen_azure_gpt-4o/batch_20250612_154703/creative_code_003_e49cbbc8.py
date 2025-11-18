"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getbonus.eu
Prompt: Write code to dynamically load content on a webpage only if JavaScript is enabled, similar to how the GetBonus app requires JavaScript for proper operation.
Generated: DETERMINISTIC_e49cbbc8e98e3b08
Batch ID: 20250612_154703
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
  <title>Dynamically Load Content</title>
  <style>
    /* Fallback content visible only if JavaScript is disabled */
    .no-js-content {
      display: block;
    }

    .js-content {
      display: none;
    }

    /* Content shown when JavaScript is enabled */
    .js-enabled .no-js-content {
      display: none;
    }

    .js-enabled .js-content {
      display: block;
    }
  </style>
</head>
<body>
  <div class="no-js-content">
    <p>JavaScript is disabled. Please enable JavaScript to view this content.</p>
  </div>
  <div class="js-content">
    <!-- Placeholder for the dynamic content -->
    <p>Loading dynamic content...</p>
    <div id="dynamic-content"></div>
  </div>

  <script>
    // Add a class to the root element of the document when JavaScript is enabled
    document.documentElement.classList.add('js-enabled');

    // Simulate dynamic loading of content
    function loadDynamicContent() {
      const dynamicContentContainer = document.getElementById('dynamic-content');

      // Clear existing content
      dynamicContentContainer.innerHTML = '';

      try {
        // Dynamically create new content
        const newContent = document.createElement('p');
        newContent.textContent = 'Welcome! This content was loaded dynamically because JavaScript is enabled.';
        dynamicContentContainer.appendChild(newContent);

        // Additional dynamic content can be loaded here
        // For example: Fetching content from an API
      } catch (error) {
        console.error('Error loading dynamic content:', error);

        // Display fallback message in case of error
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'An error occurred while loading content. Please try again later.';
        errorMessage.style.color = 'red';
        dynamicContentContainer.appendChild(errorMessage);
      }
    }

    // Load content dynamically after the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', loadDynamicContent);
  </script>
</body>
</html>
```
