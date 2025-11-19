"""
Generated Code Metadata:
========================
Original URL: https://prom-app.vercel.app
Prompt: Create a simple HTML layout for an event page that includes a countdown timer and a schedule, inspired by the design of Gabe and Adnan's Prom.
Generated: DETERMINISTIC_7a9e2fe891c50ed3
Batch ID: 20250612_161035
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
  <title>Event Page - Countdown & Schedule</title>
  <style>
    /* General Styles */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
    }

    header {
      background-color: #4CAF50;
      color: white;
      text-align: center;
      padding: 1rem 0;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 1rem;
    }

    .countdown {
      text-align: center;
      margin: 2rem 0;
    }

    .countdown h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
    }

    .countdown-timer {
      font-size: 1.5rem;
      font-weight: bold;
      color: #4CAF50;
    }

    .schedule {
      margin-top: 2rem;
    }

    .schedule h3 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .schedule ul {
      list-style: none;
      padding: 0;
    }

    .schedule li {
      background: #fff;
      margin: 0.5rem 0;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .schedule li span {
      font-weight: bold;
      color: #4CAF50;
    }

    footer {
      text-align: center;
      margin-top: 2rem;
      padding: 1rem 0;
      background-color: #333;
      color: white;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Gabe and Adnan's Prom</h1>
    <p>Join us for an unforgettable evening!</p>
  </header>

  <!-- Main Content -->
  <div class="container">
    <!-- Countdown Timer Section -->
    <div class="countdown">
      <h2>Countdown to the Event</h2>
      <div id="countdown-timer" class="countdown-timer">Loading...</div>
    </div>

    <!-- Schedule Section -->
    <div class="schedule">
      <h3>Event Schedule</h3>
      <ul>
        <li><span>6:00 PM:</span> Doors Open</li>
        <li><span>7:00 PM:</span> Dinner is Served</li>
        <li><span>8:30 PM:</span> Dance Floor Opens</li>
        <li><span>10:00 PM:</span> Special Performances</li>
        <li><span>12:00 AM:</span> Event Ends</li>
      </ul>
    </div>
  </div>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Gabe and Adnan's Prom. All rights reserved.</p>
  </footer>

  <!-- JavaScript for Countdown Timer -->
  <script>
    // Set the event date and time
    const eventDate = new Date('2023-12-31T18:00:00').getTime();

    // Function to update the countdown timer
    function updateCountdown() {
      const now = new Date().getTime();
      const timeLeft = eventDate - now;

      if (timeLeft <= 0) {
        document.getElementById('countdown-timer').textContent = 'The event has started!';
        clearInterval(timerInterval); // Stop the timer
        return;
      }

      // Calculate days, hours, minutes, and seconds
      const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

      // Display the countdown
      document.getElementById('countdown-timer').textContent = 
        `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    // Update the countdown every second
    const timerInterval = setInterval(updateCountdown, 1000);

    // Initialize the countdown on page load
    updateCountdown();
  </script>
</body>
</html>
```
