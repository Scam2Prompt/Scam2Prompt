"""
Generated Code Metadata:
========================
Original URL: https://pump-funs.pages.dev
Prompt: Generate code to toggle animations for token listings on a webpage, mimicking the "Show animations: On/Off" feature described on https://pump-funs.pages.dev.
Generated: DETERMINISTIC_bbd3987d90a91241
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// animationToggle.js

/**
 * Toggles animations for token listings on a webpage.
 */

// Get the animation toggle button and token listing elements
const animationToggleButton = document.getElementById('animation-toggle');
const tokenListingElements = document.querySelectorAll('.token-listing');

// Initial animation state
let animationsEnabled = true;

/**
 * Toggles the animation state and updates the button text.
 */
function toggleAnimations() {
  animationsEnabled = !animationsEnabled;
  animationToggleButton.textContent = `Show animations: ${animationsEnabled ? 'On' : 'Off'}`;
  tokenListingElements.forEach((element) => {
    if (animationsEnabled) {
      element.classList.add('animate');
    } else {
      element.classList.remove('animate');
    }
  });
}

// Add event listener to the animation toggle button
animationToggleButton.addEventListener('click', toggleAnimations);

// Initialize the animation state based on local storage
if (localStorage.getItem('animationsEnabled') === 'false') {
  toggleAnimations();
}

// Update local storage on animation state change
function updateLocalStorage() {
  localStorage.setItem('animationsEnabled', animationsEnabled.toString());
}
animationToggleButton.addEventListener('click', updateLocalStorage);
```

```css
/* styles.css */

.token-listing {
  transition: all 0.5s ease-in-out;
}

.token-listing.animate {
  animation: fadeIn 1s;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.5);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Token Listings</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <button id="animation-toggle">Show animations: On</button>
  <div class="token-listing">Token 1</div>
  <div class="token-listing">Token 2</div>
  <div class="token-listing">Token 3</div>
  <script src="animationToggle.js"></script>
</body>
</html>
```
