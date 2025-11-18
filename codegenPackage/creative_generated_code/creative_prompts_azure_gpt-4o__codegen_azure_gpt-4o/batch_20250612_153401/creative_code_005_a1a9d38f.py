"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-insanitybets.web.app
Prompt: Write code to display a "Terms & Conditions" modal on a web app like InsanityBets, triggered when users attempt to sign up or connect their wallet.
Generated: DETERMINISTIC_a1a9d38f56b5a69b
Batch ID: 20250612_153401
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
  <title>Terms & Conditions Modal</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    /* Styles for the modal */
    .modal {
      display: none; /* Hidden by default */
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 1000;
      width: 90%;
      max-width: 500px;
      background-color: white;
      border-radius: 10px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      padding: 20px;
    }

    .modal-header {
      font-size: 1.5em;
      margin-bottom: 10px;
      font-weight: bold;
    }

    .modal-body {
      font-size: 1em;
      margin-bottom: 20px;
      line-height: 1.5;
    }

    .modal-footer {
      text-align: right;
    }

    .modal-footer button {
      padding: 10px 20px;
      font-size: 1em;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    .modal-footer button.accept {
      background-color: #28a745;
      color: white;
    }

    .modal-footer button.reject {
      background-color: #dc3545;
      color: white;
    }

    /* Overlay styles */
    .overlay {
      display: none; /* Hidden by default */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 999;
    }
  </style>
</head>
<body>
  <!-- Trigger Button -->
  <button id="signupButton">Sign Up</button>
  <button id="walletConnectButton">Connect Wallet</button>

  <!-- Modal Structure -->
  <div class="overlay" id="overlay"></div>
  <div class="modal" id="termsModal">
    <div class="modal-header">Terms & Conditions</div>
    <div class="modal-body">
      By using InsanityBets, you agree to our Terms & Conditions. Please read them carefully before proceeding.
    </div>
    <div class="modal-footer">
      <button class="accept" id="acceptButton">Accept</button>
      <button class="reject" id="rejectButton">Reject</button>
    </div>
  </div>

  <script>
    // Selectors for DOM elements
    const signupButton = document.getElementById('signupButton');
    const walletConnectButton = document.getElementById('walletConnectButton');
    const termsModal = document.getElementById('termsModal');
    const overlay = document.getElementById('overlay');
    const acceptButton = document.getElementById('acceptButton');
    const rejectButton = document.getElementById('rejectButton');

    /**
     * Show the Terms & Conditions modal
     */
    function showModal() {
      termsModal.style.display = 'block';
      overlay.style.display = 'block';
    }

    /**
     * Hide the Terms & Conditions modal
     */
    function hideModal() {
      termsModal.style.display = 'none';
      overlay.style.display = 'none';
    }

    /**
     * Handle modal accept action
     */
    function handleAccept() {
      alert('You have accepted the Terms & Conditions.');
      hideModal();
    }

    /**
     * Handle modal reject action
     */
    function handleReject() {
      alert('You must accept the Terms & Conditions to proceed.');
      hideModal();
    }

    // Event listeners
    signupButton.addEventListener('click', showModal);
    walletConnectButton.addEventListener('click', showModal);
    acceptButton.addEventListener('click', handleAccept);
    rejectButton.addEventListener('click', handleReject);
    overlay.addEventListener('click', hideModal); // Allow closing modal by clicking outside
  </script>
</body>
</html>
```
