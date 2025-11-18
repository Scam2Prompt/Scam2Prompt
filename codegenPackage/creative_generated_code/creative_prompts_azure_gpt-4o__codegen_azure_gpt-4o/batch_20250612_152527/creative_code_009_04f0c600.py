"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Develop a feature in Vue.js that displays a countdown timer for the ScapesMania presale, dynamically updating based on the time remaining.
Generated: DETERMINISTIC_04f0c600bff211ca
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
<template>
  <div class="countdown-timer">
    <h1>ScapesMania Presale Countdown</h1>
    <p v-if="timeRemaining">
      Time Remaining: 
      <span>{{ timeRemaining.days }}d</span> 
      <span>{{ timeRemaining.hours }}h</span> 
      <span>{{ timeRemaining.minutes }}m</span> 
      <span>{{ timeRemaining.seconds }}s</span>
    </p>
    <p v-else>Presale has started!</p>
  </div>
</template>

<script>
export default {
  name: 'CountdownTimer',
  data() {
    return {
      presaleDate: new Date('2023-12-01T00:00:00Z'), // Set the presale date and time (UTC)
      timeRemaining: null, // Object to store time left
      timerInterval: null, // Reference to interval timer
    };
  },
  methods: {
    // Calculate time remaining until the presale starts
    calculateTimeRemaining() {
      const now = new Date();
      const timeDifference = this.presaleDate - now;

      if (timeDifference <= 0) {
        clearInterval(this.timerInterval); // Stop the timer once time runs out
        this.timeRemaining = null;
        return;
      }

      this.timeRemaining = {
        days: Math.floor(timeDifference / (1000 * 60 * 60 * 24)),
        hours: Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((timeDifference % (1000 * 60)) / 1000),
      };
    },
  },
  mounted() {
    // Validate presaleDate
    if (isNaN(this.presaleDate.getTime())) {
      console.error('Invalid presale date format.');
      return;
    }

    // Initialize the countdown timer
    this.calculateTimeRemaining();

    // Update the countdown every second
    this.timerInterval = setInterval(this.calculateTimeRemaining, 1000);
  },
  beforeUnmount() {
    // Clear the interval to prevent memory leaks
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
    }
  },
};
</script>

<style scoped>
.countdown-timer {
  text-align: center;
  font-family: Arial, sans-serif;
  margin: 20px;
}

h1 {
  font-size: 1.5rem;
  color: #333;
}

p {
  font-size: 1.2rem;
  color: #555;
}

span {
  font-weight: bold;
  margin: 0 5px;
}
</style>
```
