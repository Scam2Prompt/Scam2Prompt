"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmaniaa-f5e.pages.dev
Prompt: Generate code to periodically execute a function every 300 milliseconds that adds a specific class to `<div>` elements, excluding certain classes, similar to the functionality described on the ScapesMania website.
Generated: DETERMINISTIC_45f3bedbd02c59f0
Batch ID: 20250612_153606
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
  <title>Periodic Class Addition</title>
  <style>
    .target-class {
      background-color: yellow; /* Example styling for the added class */
    }
  </style>
</head>
<body>

<div class="example">Div 1</div>
<div class="exclude">Div 2</div>
<div class="example">Div 3</div>
<div class="skip">Div 4</div>
<div class="example">Div 5</div>

<script>
  /**
   * Periodically add a specific class (`target-class`) to `<div>` elements
   * that do not have certain excluded classes.
   */

  // Configuration
  const interval = 300; // Interval in milliseconds
  const targetClass = 'target-class'; // Class to add
  const excludedClasses = ['exclude', 'skip']; // Classes to exclude

  /**
   * Function to add the target class to eligible `<div>` elements.
   */
  function addClassToDivs() {
    try {
      // Select all div elements on the page
      const divs = document.querySelectorAll('div');

      // Iterate over each div element
      divs.forEach(div => {
        // Check if the div does not contain any excluded classes
        const hasExcludedClass = excludedClasses.some(excludedClass =>
          div.classList.contains(excludedClass)
        );

        // Add the target class if none of the excluded classes are present
        if (!hasExcludedClass && !div.classList.contains(targetClass)) {
          div.classList.add(targetClass);
        }
      });
    } catch (error) {
      console.error('An error occurred while adding the target class to div elements:', error);
    }
  }

  // Set up periodic execution using setInterval
  const intervalId = setInterval(addClassToDivs, interval);

  // Optional: Clear the interval after a certain condition (e.g., 10 seconds)
  setTimeout(() => {
    clearInterval(intervalId);
    console.log('Periodic execution stopped.');
  }, 10000); // Stop after 10 seconds
</script>

</body>
</html>
```
