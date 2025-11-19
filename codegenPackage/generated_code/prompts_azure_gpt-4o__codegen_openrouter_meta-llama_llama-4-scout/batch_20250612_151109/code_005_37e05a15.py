"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Write JavaScript code to animate a digital banner advertisement for a spanduk display, incorporating transitions and text effects.
Generated: DETERMINISTIC_37e05a15367c588d
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { gsap } from 'gsap';

// Get the banner element
const banner = document.getElementById('spanduk-banner');

// Check if banner element exists
if (!banner) {
  throw new Error('Banner element not found');
}

// Define animation timeline
const timeline = gsap.timeline();

// Set initial banner state
banner.classList.add('initial-state');

// Animation variables
const bannerText = 'Get 20% Off Your First Purchase!';
const animationDuration = 2;
const transitionDelay = 0.5;

// Animate banner text
timeline.to(banner, {
  duration: animationDuration,
  opacity: 1,
  ease: 'power2.inOut',
  delay: transitionDelay,
})

// Animate text effects
timeline.to(banner.querySelector('.text'), {
  duration: animationDuration,
  y: -10,
  ease: 'power2.inOut',
  delay: transitionDelay + animationDuration / 2,
  text: {
    value: bannerText,
    duration: 1,
    ease: 'power2.inOut',
  },
})

// Add fade-in effect to call-to-action (CTA) button
timeline.to(banner.querySelector('.cta-button'), {
  duration: animationDuration,
  opacity: 1,
  ease: 'power2.inOut',
  delay: transitionDelay + animationDuration,
  scale: 1,
})

// Add hover effect to CTA button
banner.querySelector('.cta-button').addEventListener('mouseover', () => {
  gsap.to(banner.querySelector('.cta-button'), {
    duration: 0.5,
    scale: 1.1,
    ease: 'power2.inOut',
  })
})

banner.querySelector('.cta-button').addEventListener('mouseout', () => {
  gsap.to(banner.querySelector('.cta-button'), {
    duration: 0.5,
    scale: 1,
    ease: 'power2.inOut',
  })
})

// Error handling for animation
try {
  timeline.play();
} catch (error) {
  console.error('Error animating banner:', error);
}

// CSS styles for banner (sample)
/* 
#spanduk-banner {
  position: relative;
  width: 100%;
  height: 100vh;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  opacity: 0;
}

#spanduk-banner.initial-state {
  opacity: 0;
}

#spanduk-banner .text {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 20px;
}

#spanduk-banner .cta-button {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
  opacity: 0;
  transform: scale(0.8);
}
*/

// HTML structure for banner (sample)
/* 
<div id="spanduk-banner">
  <div class="text"></div>
  <button class="cta-button">Shop Now</button>
</div>
```
