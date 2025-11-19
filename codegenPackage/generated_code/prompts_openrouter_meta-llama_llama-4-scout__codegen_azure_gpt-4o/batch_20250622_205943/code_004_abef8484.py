"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a countdown timer for a presale event, similar to the WienerAI presale countdown.
Generated: DETERMINISTIC_abef8484c6180034
Batch ID: 20250622_205943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presale Countdown Timer</title>
  <style>
    /* Basic styling for the page */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }

    h1 {
      margin-top: 50px;
      color: #333;
    }

    #countdown {
      font-size: 2rem;
      color: #ff5722;
      margin-top: 20px;
    }

    .timer-box {
      display: inline-block;
      margin: 0 10px;
      padding: 10px 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }

    .timer-box span {
      display: block;
      font-size: 1.5rem;
      font-weight: bold;
    }

    .timer-box label {
      font-size: 0.9rem;
      color: #666;
    }
  </style>
</head>
<body>
  <h1>Presale Countdown</h1>
  <div id="countdown">
    <div class="timer-box">
      <span id="days">00</span>
      <label>Days</label>
    </div>
    <div class="timer-box">
      <span id="hours">00</span>
      <label>Hours</label>
    </div>
    <div class="timer-box">
      <span id="minutes">00</span>
      <label>Minutes</label>
    </div>
    <div class="timer-box">
      <span id="seconds">00</span>
      <label>Seconds</label>
    </div>
  </div>

  <script>
    // Set the target date for the presale event
    const targetDate = new Date("2023-12-31T23:59:59").getTime();

    // Function to update the countdown timer
    function updateCountdown() {
      const now = new Date().getTime();
      const timeRemaining = targetDate - now;

      // Calculate days, hours, minutes, and seconds
      const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

      // Update the DOM elements
      document.getElementById("days").textContent = days.toString().padStart(2, '0');
      document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
      document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
      document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');

      // If the countdown is over, display a message
      if (timeRemaining < 0) {
        clearInterval(timerInterval);
        document.getElementById("countdown").innerHTML = "<h2>Presale has started!</h2>";
      }
    }

    // Update the countdown every second
    const timerInterval = setInterval(updateCountdown, 1000);

    // Initial call to display the countdown immediately
    updateCountdown();
  </script>
</body>
</html>
```
