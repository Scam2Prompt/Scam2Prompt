"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Write code to implement shortcuts for interacting with a COVID-19 graph, such as +/- keys for daily changes and spacebar for play/pause functionality, as outlined on the website.
Generated: DETERMINISTIC_139a62720c1cdd58
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * COVID-19 Graph Interaction Shortcuts
 * Handles keyboard shortcuts for interacting with a COVID-19 graph visualization.
 * Features:
 * - '+'/'-' keys for daily changes
 * - Spacebar for play/pause functionality
 */

class COVIDGraphShortcuts {
  constructor(graphController) {
    this.graphController = graphController;
    this.isPlaying = false;
    this.animationInterval = null;
    this.animationSpeed = 1000; // ms between updates

    // Bind event handlers
    this.handleKeyDown = this.handleKeyDown.bind(this);
    this.togglePlayPause = this.togglePlayPause.bind(this);
    this.nextDay = this.nextDay.bind(this);
    this.prevDay = this.prevDay.bind(this);

    // Initialize event listeners
    this.initialize();
  }

  /**
   * Initialize event listeners
   */
  initialize() {
    document.addEventListener('keydown', this.handleKeyDown);
  }

  /**
   * Clean up event listeners
   */
  destroy() {
    document.removeEventListener('keydown', this.handleKeyDown);
    this.stopAnimation();
  }

  /**
   * Handle keydown events
   * @param {KeyboardEvent} event 
   */
  handleKeyDown(event) {
    // Prevent default behavior for handled keys
    const handledKeys = [' ', '+', '-', 'ArrowRight', 'ArrowLeft'];
    if (handledKeys.includes(event.key)) {
      event.preventDefault();
    }

    switch (event.key) {
      case ' ':
        this.togglePlayPause();
        break;
      case '+':
      case 'ArrowRight':
        this.nextDay();
        break;
      case '-':
      case 'ArrowLeft':
        this.prevDay();
        break;
    }
  }

  /**
   * Toggle play/pause animation
   */
  togglePlayPause() {
    if (this.isPlaying) {
      this.stopAnimation();
    } else {
      this.startAnimation();
    }
  }

  /**
   * Start automatic animation
   */
  startAnimation() {
    if (!this.isPlaying) {
      this.isPlaying = true;
      this.animationInterval = setInterval(() => {
        this.nextDay();
      }, this.animationSpeed);
    }
  }

  /**
   * Stop automatic animation
   */
  stopAnimation() {
    if (this.isPlaying) {
      clearInterval(this.animationInterval);
      this.isPlaying = false;
      this.animationInterval = null;
    }
  }

  /**
   * Advance to next day
   */
  nextDay() {
    this.graphController.nextDay();
  }

  /**
   * Go back to previous day
   */
  prevDay() {
    this.graphController.prevDay();
  }
}

// Example usage:
// const graphController = { nextDay: () => {}, prevDay: () => {} };
// const shortcuts = new COVIDGraphShortcuts(graphController);
// To clean up: shortcuts.destroy();
```
