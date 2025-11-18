"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Recommend a JavaScript library for animating pop-up card designs, such as the heart pop-up cards described on Craft Intra.
Generated: DETERMINISTIC_731cd6e1e9f99202
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script recommends the "GSAP" (GreenSock Animation Platform) JavaScript library
 * for creating smooth and customizable animations for pop-up card designs.
 * Below is an example implementation of GSAP to animate a heart pop-up card.
 * 
 * Installation:
 * Run `npm install gsap` to add GSAP to your project.
 */

// Import GSAP library
import { gsap } from "gsap";

// Function to animate a heart pop-up card
function animateHeartPopupCard(cardElement) {
  try {
    // Ensure the cardElement exists
    if (!cardElement) {
      throw new Error("Card element is not provided or invalid.");
    }

    // Set the initial state of the card (hidden)
    gsap.set(cardElement, { scale: 0, opacity: 0 });

    // Create a pop-up animation
    gsap.to(cardElement, {
      duration: 1, // Animation duration in seconds
      scale: 1,    // Scale up to normal size
      opacity: 1,  // Fade in the card
      ease: "elastic.out(1, 0.5)", // Use elastic easing for a bounce effect
    });

  } catch (error) {
    // Handle errors gracefully
    console.error("Error occurred while animating the heart pop-up card:", error.message);
  }
}

// Example usage:
// Assuming there's an HTML element with the ID "heartCard".
const heartCard = document.getElementById("heartCard");
animateHeartPopupCard(heartCard);
```

```html
<!-- Example HTML structure for the heart card -->
<div id="heartCard" style="width: 200px; height: 200px; background: pink; border-radius: 50%; display: flex; align-items: center; justify-content: center;">
  ❤️
</div>
```

```css
/* Example CSS for basic styling */
#heartCard {
  transform-origin: center;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
  font-size: 50px;
  text-align: center;
}
```

Ensure GSAP is installed and imported properly before running the code.
