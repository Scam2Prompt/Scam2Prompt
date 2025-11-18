"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-playmemoria.com
Prompt: Generate code for a responsive UI element that prompts users to rotate their screen when accessing the "Memoria" platform on mobile devices.
Generated: DETERMINISTIC_be6b53836ca2ac74
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a responsive UI element that prompts users to rotate their screen when accessing the "Memoria" platform on mobile devices. This code uses HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Memoria Platform</title>
  <style>
    /* Base styling for the overlay */
    #rotate-screen-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      z-index: 9999;
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
      box-sizing: border-box;
    }

    #rotate-screen-overlay.hidden {
      display: none; /* Hide overlay when not needed */
    }

    #rotate-screen-icon {
      font-size: 5rem;
      margin-bottom: 20px;
    }

    #rotate-screen-message {
      font-size: 1.5rem;
      line-height: 1.8;
    }

    /* Responsive design for smaller screens */
    @media (max-width: 768px) {
      #rotate-screen-message {
        font-size: 1.2rem;
      }
    }
  </style>
</head>
<body>
  <!-- Overlay element -->
  <div id="rotate-screen-overlay" class="hidden">
    <div id="rotate-screen-icon">🔄</div>
    <div id="rotate-screen-message">
      Please rotate your device to landscape mode for the best experience on the Memoria platform.
    </div>
  </div>

  <script>
    // Function to check orientation and toggle overlay visibility
    function checkOrientation() {
      const overlay = document.getElementById('rotate-screen-overlay');
      
      // If the device is in portrait mode, show the overlay
      if (window.innerHeight > window.innerWidth) {
        overlay.classList.remove('hidden');
      } else {
        // If the device is in landscape mode, hide the overlay
        overlay.classList.add('hidden');
      }
    }

    // Event listener for orientation change or screen resize
    window.addEventListener('resize', checkOrientation);
    window.addEventListener('orientationchange', checkOrientation);

    // Initial check to ensure overlay status is correct on page load
    document.addEventListener('DOMContentLoaded', checkOrientation);
  </script>
</body>
</html>
```
