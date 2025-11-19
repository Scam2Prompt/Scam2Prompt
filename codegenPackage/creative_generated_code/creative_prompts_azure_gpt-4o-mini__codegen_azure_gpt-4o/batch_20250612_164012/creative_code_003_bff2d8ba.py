"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connecting-collabs.vip
Prompt: How do I design a user-friendly interface for session expiration notifications in a web app?
Generated: DETERMINISTIC_bff2d8ba73dfa803
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Session Expiration Notification</title>
  <style>
    /* Styles for the session expiration modal */
    #session-expiration-modal {
      display: none; /* Hidden by default */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5); /* Dimmed background */
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }

    .modal-content {
      background-color: #ffffff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      text-align: center;
      max-width: 400px;
      width: 100%;
    }

    .modal-content h2 {
      margin: 0 0 10px;
    }

    .modal-content p {
      margin-bottom: 20px;
      color: #333;
    }

    .modal-content button {
      padding: 10px 20px;
      background-color: #007bff;
      color: #ffffff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    .modal-content button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Session expiration modal -->
  <div id="session-expiration-modal">
    <div class="modal-content">
      <h2>Session Expiring</h2>
      <p>Your session is about to expire. Would you like to extend it?</p>
      <button id="extend-session-btn">Extend Session</button>
    </div>
  </div>

  <script>
    // JavaScript to handle session expiration notification
    (function () {
      const sessionExpirationModal = document.getElementById('session-expiration-modal');
      const extendSessionButton = document.getElementById('extend-session-btn');

      // Simulated session expiration time (in milliseconds)
      const sessionExpirationTime = 30000; // 30 seconds for demo purposes

      // Show the expiration notification 5 seconds before session expires
      const notificationTime = sessionExpirationTime - 5000;

      // Function to extend the session (simulated here)
      function extendSession() {
        alert('Session extended.');
        sessionExpirationModal.style.display = 'none';
        resetSessionTimer(); // Reset the session timer
      }

      // Function to display the session expiration modal
      function showSessionExpirationModal() {
        sessionExpirationModal.style.display = 'flex';
      }

      // Function to reset the session timer (simulated here)
      function resetSessionTimer() {
        clearTimeout(sessionTimer);
        clearTimeout(notificationTimer);
        startSessionTimer();
      }

      // Start the session timer
      function startSessionTimer() {
        notificationTimer = setTimeout(showSessionExpirationModal, notificationTime);

        sessionTimer = setTimeout(() => {
          alert('Session has expired.');
          sessionExpirationModal.style.display = 'none';
          // Redirect or perform other actions on session expiration
        }, sessionExpirationTime);
      }

      // Attach click event to extend session button
      extendSessionButton.addEventListener('click', extendSession);

      // Start the timer when the page loads
      let notificationTimer, sessionTimer;
      startSessionTimer();
    })();
  </script>
</body>
</html>
```
