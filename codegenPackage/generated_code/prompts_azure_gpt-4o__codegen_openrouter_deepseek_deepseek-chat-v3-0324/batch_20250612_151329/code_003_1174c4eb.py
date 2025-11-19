"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Write JavaScript code to implement a gift-opening animation for a web-based event, inspired by the "Day 5 Gifts" feature described on the chimpers-dojo website.
Generated: DETERMINISTIC_1174c4eba4dbf929
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * GiftOpeningAnimation - A class to handle gift opening animations for web events.
 */
class GiftOpeningAnimation {
  /**
   * @param {Object} options - Configuration options
   * @param {string} options.containerId - ID of the container element
   * @param {number} options.giftCount - Number of gifts to display
   * @param {string} options.giftImage - Default gift image URL
   * @param {string} options.openedGiftImage - Opened gift image URL
   * @param {string} options.confettiColors - Array of confetti colors
   */
  constructor(options) {
    this.container = document.getElementById(options.containerId);
    this.giftCount = options.giftCount || 5;
    this.giftImage = options.giftImage || 'default-gift.png';
    this.openedGiftImage = options.openedGiftImage || 'opened-gift.png';
    this.confettiColors = options.confettiColors || ['#ff0000', '#00ff00', '#0000ff'];
    this.openedGifts = 0;
    
    if (!this.container) {
      throw new Error('Container element not found');
    }
    
    this.init();
  }
  
  /**
   * Initialize the gift animation
   */
  init() {
    this.container.innerHTML = '';
    this.container.classList.add('gift-container');
    
    // Create gift elements
    for (let i = 0; i < this.giftCount; i++) {
      const gift = document.createElement('div');
      gift.className = 'gift';
      gift.dataset.index = i;
      
      const img = document.createElement('img');
      img.src = this.giftImage;
      img.alt = 'Gift';
      
      gift.appendChild(img);
      gift.addEventListener('click', this.handleGiftClick.bind(this));
      
      this.container.appendChild(gift);
    }
  }
  
  /**
   * Handle gift click event
   * @param {Event} event - Click event
   */
  handleGiftClick(event) {
    const gift = event.currentTarget;
    const index = parseInt(gift.dataset.index);
    
    // Prevent double-clicking
    if (gift.classList.contains('opened')) {
      return;
    }
    
    // Mark as opened
    gift.classList.add('opened');
    this.openedGifts++;
    
    // Change image
    const img = gift.querySelector('img');
    img.src = this.openedGiftImage;
    
    // Add animation
    gift.classList.add('opening');
    
    // Create confetti
    this.createConfetti(gift);
    
    // Check if all gifts are opened
    if (this.openedGifts === this.giftCount) {
      setTimeout(() => {
        this.allGiftsOpened();
      }, 1000);
    }
  }
  
  /**
   * Create confetti effect
   * @param {HTMLElement} element - Element to attach confetti to
   */
  createConfetti(element) {
    const rect = element.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    for (let i = 0; i < 50; i++) {
      const confetti = document.createElement('div');
      confetti.className = 'confetti';
      
      // Random properties
      const color = this.confettiColors[Math.floor(Math.random() * this.confettiColors.length)];
      const size = Math.random() * 10 + 5;
      const angle = Math.random() * Math.PI * 2;
      const velocity = Math.random() * 5 + 5;
      const rotationSpeed = Math.random() * 10 - 5;
      
      confetti.style.backgroundColor = color;
      confetti.style.width = `${size}px`;
      confetti.style.height = `${size}px`;
      confetti.style.left = `${centerX}px`;
      confetti.style.top = `${centerY}px`;
      
      document.body.appendChild(confetti);
      
      // Animate
      const duration = Math.random() * 3000 + 2000;
      const startTime = performance.now();
      
      const animate = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = elapsed / duration;
        
        if (progress >= 1) {
          confetti.remove();
          return;
        }
        
        const x = centerX + Math.cos(angle) * velocity * elapsed / 20;
        const y = centerY + Math.sin(angle) * velocity * elapsed / 20 + (progress * progress * 100);
        const rotation = rotationSpeed * elapsed / 20;
        
        confetti.style.transform = `translate(${x - centerX}px, ${y - centerY}px) rotate(${rotation}deg)`;
        confetti.style.opacity = 1 - progress;
        
        requestAnimationFrame(animate);
      };
      
      requestAnimationFrame(animate);
    }
  }
  
  /**
   * Called when all gifts are opened
   */
  allGiftsOpened() {
    const event = new CustomEvent('allGiftsOpened', {
      detail: { giftCount: this.giftCount }
    });
    this.container.dispatchEvent(event);
  }
  
  /**
   * Reset the animation
   */
  reset() {
    this.openedGifts = 0;
    this.init();
  }
}

// CSS styles to be added to the page
const giftAnimationStyles = `
.gift-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}

.gift {
  width: 100px;
  height: 100px;
  cursor: pointer;
  transition: transform 0.2s;
  position: relative;
}

.gift:hover {
  transform: scale(1.05);
}

.gift img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.gift.opening {
  animation: shake 0.5s ease-in-out;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-10px); }
  40% { transform: translateX(10px); }
  60% { transform: translateX(-10px); }
  80% { transform: translateX(10px); }
}

.confetti {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  z-index: 1000;
}
`;

// Add styles to the document
const styleElement = document.createElement('style');
styleElement.textContent = giftAnimationStyles;
document.head.appendChild(styleElement);

// Example usage:
// const giftAnimation = new GiftOpeningAnimation({
//   containerId: 'gift-container',
//   giftCount: 5,
//   giftImage: 'images/gift.png',
//   openedGiftImage: 'images/opened-gift.png',
//   confettiColors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff']
// });
```
