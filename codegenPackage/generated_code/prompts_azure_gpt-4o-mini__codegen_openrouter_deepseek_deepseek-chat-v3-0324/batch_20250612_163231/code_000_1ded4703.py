"""
Generated Code Metadata:
========================
Original URL: https://oasysgames.live
Prompt: Generate code to implement a countdown timer for the "Ending Soon" campaigns on OasysGames, using the local time settings provided.
Generated: DETERMINISTIC_1ded47032d92fd7e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Countdown Timer for "Ending Soon" Campaigns
 * 
 * This script initializes and manages countdown timers for campaigns
 * based on local time settings.
 */

class CountdownTimer {
  /**
   * Initialize the countdown timer
   * @param {string} endTime - ISO string of the campaign end time
   * @param {string} elementId - ID of the HTML element to display the timer
   */
  constructor(endTime, elementId) {
    this.endTime = new Date(endTime);
    this.elementId = elementId;
    this.timerElement = document.getElementById(elementId);
    
    if (!this.timerElement) {
      console.error(`Element with ID ${elementId} not found`);
      return;
    }
    
    this.updateInterval = null;
    this.initializeTimer();
  }

  /**
   * Initialize and start the countdown timer
   */
  initializeTimer() {
    this.updateTimer();
    this.updateInterval = setInterval(() => this.updateTimer(), 1000);
  }

  /**
   * Update the timer display
   */
  updateTimer() {
    const now = new Date();
    const timeRemaining = this.endTime - now;

    if (timeRemaining <= 0) {
      this.timerElement.textContent = 'Campaign Ended';
      clearInterval(this.updateInterval);
      return;
    }

    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    this.timerElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  /**
   * Stop the countdown timer
   */
  stopTimer() {
    if (this.updateInterval) {
      clearInterval(this.updateInterval);
    }
  }
}

/**
 * Initialize all countdown timers on the page
 */
function initializeAllCountdownTimers() {
  // Find all elements with data-endtime attribute
  const timerElements = document.querySelectorAll('[data-endtime]');
  
  timerElements.forEach(element => {
    const endTime = element.getAttribute('data-endtime');
    const elementId = element.id;
    
    if (!elementId) {
      console.error('Timer element missing ID attribute');
      return;
    }
    
    try {
      new CountdownTimer(endTime, elementId);
    } catch (error) {
      console.error(`Error initializing timer for element ${elementId}:`, error);
      element.textContent = 'Timer Error';
    }
  });
}

// Initialize timers when DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeAllCountdownTimers);
} else {
  initializeAllCountdownTimers();
}
```
