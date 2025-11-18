"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Write JavaScript code to implement a "Quick view" feature for listings such as "Παπαδόπουλος - Κοπτικά εργαλεία," displaying details like phone number and address in a modal window.
Generated: DETERMINISTIC_3d1856a12923f91f
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for reference (not included in code output)
// <button class="quick-view-btn" data-name="Παπαδόπουλος - Κοπτικά εργαλεία" data-phone="123-456-7890" data-address="123 Tool Street, Athens">Quick View</button>
// <div id="modal" class="modal hidden">
//   <div class="modal-content">
//     <span class="close-btn">&times;</span>
//     <h2 id="modal-title"></h2>
//     <p id="modal-phone"></p>
//     <p id="modal-address"></p>
//   </div>
// </div>

/**
 * JavaScript Code for Quick View Feature
 */

document.addEventListener("DOMContentLoaded", () => {
  // Select all quick view buttons and the modal elements
  const quickViewButtons = document.querySelectorAll(".quick-view-btn");
  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modal-title");
  const modalPhone = document.getElementById("modal-phone");
  const modalAddress = document.getElementById("modal-address");
  const closeButton = document.querySelector(".close-btn");

  /**
   * Opens the modal and populates it with listing details
   * @param {Event} event - The click event
   */
  const openModal = (event) => {
    try {
      // Get data attributes from the clicked button
      const button = event.currentTarget;
      const name = button.dataset.name;
      const phone = button.dataset.phone;
      const address = button.dataset.address;

      // Populate the modal content
      modalTitle.textContent = name;
      modalPhone.textContent = `Phone: ${phone}`;
      modalAddress.textContent = `Address: ${address}`;

      // Display the modal
      modal.classList.remove("hidden");
    } catch (error) {
      console.error("Error opening modal:", error);
    }
  };

  /**
   * Closes the modal
   */
  const closeModal = () => {
    modal.classList.add("hidden");
  };

  // Add event listeners to all quick view buttons
  quickViewButtons.forEach((button) =>
    button.addEventListener("click", openModal)
  );

  // Add event listener to close button
  closeButton.addEventListener("click", closeModal);

  // Optional: Close modal when clicking outside the modal content
  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
});

/**
 * CSS classes used:
 * .hidden { display: none; }
 * .modal { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.5); display: flex; justify-content: center; align-items: center; }
 * .modal-content { background-color: #fff; padding: 20px; border-radius: 5px; width: 300px; text-align: center; }
 * .close-btn { position: absolute; top: 10px; right: 10px; cursor: pointer; font-size: 20px; }
 */
```
