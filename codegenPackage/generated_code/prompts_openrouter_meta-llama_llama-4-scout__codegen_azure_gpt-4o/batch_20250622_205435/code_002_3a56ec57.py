"""
Generated Code Metadata:
========================
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Design a simple webpage for the Mpeppe ($MPEPE) presale using HTML, CSS, and JavaScript, incorporating a countdown timer and a "buy now" button.
Generated: DETERMINISTIC_3a56ec57cf7b08df
Batch ID: 20250622_205435
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
  <title>Mpeppe ($MPEPE) Presale</title>
  <style>
    /* General styles for the webpage */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
      text-align: center;
    }

    header {
      background-color: #4caf50;
      color: white;
      padding: 20px 0;
    }

    h1 {
      margin: 0;
    }

    .container {
      padding: 20px;
    }

    .countdown {
      font-size: 2em;
      margin: 20px 0;
    }

    .buy-now-btn {
      display: inline-block;
      padding: 15px 30px;
      font-size: 1.2em;
      color: white;
      background-color: #4caf50;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      text-decoration: none;
    }

    .buy-now-btn:hover {
      background-color: #45a049;
    }

    footer {
      margin-top: 20px;
      padding: 10px 0;
      background-color: #333;
      color: white;
    }
  </style>
</head>
<body>
  <!-- Header Section -->
  <header>
    <h1>Mpeppe ($MPEPE) Presale</h1>
    <p>Don't miss out on the opportunity to join the presale!</p>
  </header>

  <!-- Main Content -->
  <div class="container">
    <div class="countdown" id="countdown">
      <!-- Countdown timer will be dynamically updated -->
      Loading countdown...
    </div>
    <a href="#" class="buy-now-btn" id="buyNowBtn">Buy Now</a>
  </div>

  <!-- Footer Section -->
  <footer>
    <p>&copy; 2023 Mpeppe. All rights reserved.</p>
  </footer>

  <script>
    // Countdown Timer Logic
    (function() {
      const countdownElement = document.getElementById('countdown');
      const buyNowButton = document.getElementById('buyNowBtn');

      // Set the target date for the presale end
      const presaleEndDate = new Date('2023-12-31T23:59:59'); // Adjust as needed

      // Function to update the countdown timer
      function updateCountdown() {
        const now = new Date();
        const timeRemaining = presaleEndDate - now;

        if (timeRemaining <= 0) {
          // Presale has ended
          countdownElement.textContent = 'Presale has ended!';
          buyNowButton.style.display = 'none'; // Hide the "Buy Now" button
          return;
        }

        // Calculate days, hours, minutes, and seconds
        const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

        // Update the countdown element
        countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;
      }

      // Update the countdown every second
      setInterval(updateCountdown, 1000);

      // Initial call to display the countdown immediately
      updateCountdown();
    })();

    // Event listener for the "Buy Now" button
    document.getElementById('buyNowBtn').addEventListener('click', function(event) {
      event.preventDefault();
      alert('Redirecting to the purchase page...');
      // Add logic to redirect to the purchase page or handle the buy action
    });
  </script>
</body>
</html>
```
