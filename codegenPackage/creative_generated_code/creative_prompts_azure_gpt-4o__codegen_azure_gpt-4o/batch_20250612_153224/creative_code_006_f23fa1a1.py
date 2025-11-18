"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Write code to implement a contact number modal popup on a website, ensuring it closes automatically after a few seconds, as described on the HSR Enterprises site.
Generated: DETERMINISTIC_f23fa1a19216f452
Batch ID: 20250612_153224
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
  <title>Contact Number Modal</title>
  <style>
    /* Modal container styles */
    .modal {
      display: none; /* Initially hidden */
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 300px;
      padding: 20px;
      background: #fff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      z-index: 1000;
    }

    /* Modal overlay styles */
    .modal-overlay {
      display: none; /* Initially hidden */
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 999;
    }

    /* Close button styles */
    .modal-close-btn {
      display: block;
      margin: 10px 0 0;
      padding: 8px 16px;
      background-color: #d9534f;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      text-align: center;
    }

    .modal-close-btn:hover {
      background-color: #c9302c;
    }
  </style>
</head>
<body>
  <!-- Modal overlay -->
  <div class="modal-overlay" id="modalOverlay"></div>

  <!-- Modal content -->
  <div class="modal" id="contactModal">
    <p>Contact Number: +1-234-567-890</p>
    <button class="modal-close-btn" id="closeModalButton">Close</button>
  </div>

  <!-- Trigger button -->
  <button id="showModalButton">Show Contact Number</button>

  <script>
    // Select DOM elements
    const modal = document.getElementById('contactModal');
    const modalOverlay = document.getElementById('modalOverlay');
    const showModalButton = document.getElementById('showModalButton');
    const closeModalButton = document.getElementById('closeModalButton');

    // Function to show modal
    function showModal() {
      modal.style.display = 'block'; // Show the modal
      modalOverlay.style.display = 'block'; // Show the overlay

      // Automatically close modal after 5 seconds
      setTimeout(() => {
        closeModal();
      }, 5000);
    }

    // Function to close modal
    function closeModal() {
      modal.style.display = 'none'; // Hide the modal
      modalOverlay.style.display = 'none'; // Hide the overlay
    }

    // Event listener for showing the modal
    showModalButton.addEventListener('click', () => {
      try {
        showModal();
      } catch (error) {
        console.error('Error showing modal:', error);
      }
    });

    // Event listener for closing the modal
    closeModalButton.addEventListener('click', () => {
      try {
        closeModal();
      } catch (error) {
        console.error('Error closing modal:', error);
      }
    });

    // Close modal when clicking outside of it
    modalOverlay.addEventListener('click', () => {
      try {
        closeModal();
      } catch (error) {
        console.error('Error closing modal:', error);
      }
    });
  </script>
</body>
</html>
```
