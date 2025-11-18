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

```html
<template>
  <div class="countdown-timer">
    <h1>ScapesMania Presale Countdown</h1>
    <div v-if="timeRemaining > 0">
      <p>Time Remaining:</p>
      <div class="timer">
        <span>{{ days }} Days</span>
        <span>{{ hours }} Hours</span>
        <span>{{ minutes }} Minutes</span>
        <span>{{ seconds }} Seconds</span>
      </div>
    </div>
    <div v-else>
      <p>Presale has started!</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      countdownTarget: new Date('2023-11-01T00:00:00Z'), // Presale start time
      timeRemaining: 0,
      timerInterval: null,
    };
  },
  computed: {
    // Compute days, hours, minutes, and seconds from time remaining
    days() {
      return Math.floor(this.timeRemaining / (1000 * 60 * 60 * 24));
    },
    hours() {
      return Math.floor((this.timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    },
    minutes() {
      return Math.floor((this.timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    },
    seconds() {
      return Math.floor((this.timeRemaining % (1000 * 60)) / 1000);
    },
  },
  methods: {
    // Start the countdown
    startCountdown() {
      this.updateTimeRemaining();
      this.timerInterval = setInterval(this.updateTimeRemaining, 1000);
    },
    // Update the remaining time
    updateTimeRemaining() {
      const now = new Date();
      this.timeRemaining = this.countdownTarget - now;

      // Clear the interval if the countdown has ended
      if (this.timeRemaining <= 0) {
        clearInterval(this.timerInterval);
        this.timeRemaining = 0; // Ensure it doesn't go negative
      }
    },
  },
  mounted() {
    // Start the countdown when the component is mounted
    this.startCountdown();
  },
  beforeDestroy() {
    // Clear interval to prevent memory leaks
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
}
.timer {
  font-size: 2em;
  margin: 20px 0;
}
</style>
```
