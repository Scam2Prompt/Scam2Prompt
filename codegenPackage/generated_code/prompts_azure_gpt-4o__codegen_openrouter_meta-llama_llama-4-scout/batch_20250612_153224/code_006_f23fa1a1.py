"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Write code to implement a contact number modal popup on a website, ensuring it closes automatically after a few seconds, as described on the HSR Enterprises site.
Generated: DETERMINISTIC_f23fa1a19216f452
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// contact-modal.js

/**
 * Contact Number Modal Popup Implementation
 */

// Get the modal element
const modal = document.getElementById('contact-modal');

// Get the close button element
const closeButton = document.getElementById('close-button');

// Function to open the modal
function openModal() {
  // Add the 'open' class to the modal
  modal.classList.add('open');
}

// Function to close the modal
function closeModal() {
  // Remove the 'open' class from the modal
  modal.classList.remove('open');
}

// Function to handle close button click
function handleCloseButtonClick() {
  // Close the modal
  closeModal();
}

// Function to handle modal auto-close
function handleAutoClose() {
  // Set a timeout to close the modal after 5 seconds
  setTimeout(() => {
    // Close the modal
    closeModal();
  }, 5000); // 5000 milliseconds = 5 seconds
}

// Add event listener to the close button
closeButton.addEventListener('click', handleCloseButtonClick);

// Open the modal on page load
document.addEventListener('DOMContentLoaded', () => {
  // Open the modal
  openModal();

  // Handle auto-close
  handleAutoClose();
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Number Modal Popup</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Modal container -->
  <div id="contact-modal" class="modal">
    <!-- Modal content -->
    <div class="modal-content">
      <!-- Close button -->
      <button id="close-button" class="close-button">&times;</button>
      <!-- Contact information -->
      <h2>Contact Us</h2>
      <p>Phone: 123-456-7890</p>
      <p>Email: [info@example.com](mailto:info@example.com)</p>
    </div>
  </div>

  <script src="contact-modal.js"></script>
</body>
</html>
```

```css
/* styles.css */

.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: none;
}

.modal.open {
  display: block;
}

.modal-content {
  position: relative;
  background-color: #fff;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 400px;
  text-align: center;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}

.close-button:hover {
  color: #ccc;
}
```
