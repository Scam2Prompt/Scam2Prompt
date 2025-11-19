"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blast-app.top
Prompt: Develop a sample code for a web app that displays a privacy policy modal when a user first visits the site.
Generated: DETERMINISTIC_a2a3a77502cdeb4a
Batch ID: 20250612_160611
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
  <title>Privacy Policy Modal</title>
  <style>
    /* Basic styling for the modal */
    #privacyModal {
      display: none; /* Initially hidden */
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 1000;
      background: #fff;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      width: 80%;
      max-width: 500px;
    }

    #privacyModalOverlay {
      display: none; /* Initially hidden */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 999;
    }

    .modal-header {
      font-size: 1.5rem;
      font-weight: bold;
      margin-bottom: 10px;
    }

    .modal-body {
      margin-bottom: 20px;
    }

    .modal-footer {
      text-align: right;
    }

    .close-button {
      padding: 10px 20px;
      background-color: #007BFF;
      color: #fff;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    .close-button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Modal overlay -->
  <div id="privacyModalOverlay"></div>

  <!-- Privacy Policy Modal -->
  <div id="privacyModal">
    <div class="modal-header">Privacy Policy</div>
    <div class="modal-body">
      <p>
        This website uses cookies to ensure you get the best experience on our site.
        By continuing to use this site, you consent to our privacy policy and use of cookies.
      </p>
    </div>
    <div class="modal-footer">
      <button class="close-button" id="acceptPolicyButton">Accept</button>
    </div>
  </div>

  <!-- Main content -->
  <h1>Welcome to the Web App</h1>
  <p>Explore the features and functionalities available here.</p>

  <script>
    /**
     * Function to check if the user has already accepted the privacy policy
     * @returns {boolean} True if the policy has been accepted, false otherwise
     */
    function hasUserAcceptedPrivacyPolicy() {
      return localStorage.getItem('privacyPolicyAccepted') === 'true';
    }

    /**
     * Display the privacy policy modal
     */
    function showPrivacyPolicyModal() {
      const modal = document.getElementById('privacyModal');
      const overlay = document.getElementById('privacyModalOverlay');
      modal.style.display = 'block';
      overlay.style.display = 'block';
    }

    /**
     * Hide the privacy policy modal
     */
    function hidePrivacyPolicyModal() {
      const modal = document.getElementById('privacyModal');
      const overlay = document.getElementById('privacyModalOverlay');
      modal.style.display = 'none';
      overlay.style.display = 'none';
    }

    // Event listener for the "Accept" button
    document.getElementById('acceptPolicyButton').addEventListener('click', function () {
      try {
        // Store acceptance in localStorage
        localStorage.setItem('privacyPolicyAccepted', 'true');
        // Hide the modal
        hidePrivacyPolicyModal();
      } catch (error) {
        console.error('Error saving privacy policy acceptance:', error);
      }
    });

    // Display the privacy policy modal only if the user hasn't accepted it yet
    window.addEventListener('DOMContentLoaded', () => {
      if (!hasUserAcceptedPrivacyPolicy()) {
        showPrivacyPolicyModal();
      }
    });
  </script>
</body>
</html>
```
