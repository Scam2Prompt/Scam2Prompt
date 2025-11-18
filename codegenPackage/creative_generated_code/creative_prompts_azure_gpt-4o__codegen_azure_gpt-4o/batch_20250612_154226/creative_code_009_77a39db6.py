"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallmemes.com
Prompt: Create a CSS template for styling product quick-view modals similar to those on the "Wall Memes" website, ensuring responsiveness and user-friendly design.
Generated: DETERMINISTIC_77a39db64b1b57da
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Product Quick-View Modal Styles */

/* Base styles for the modal container */
.product-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 90%; /* Responsive width for smaller screens */
  max-width: 500px; /* Limit maximum width for larger screens */
  background-color: #ffffff; /* Neutral background */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
  border-radius: 8px; /* Rounded corners for a modern look */
  z-index: 1000; /* Ensure modal appears above other elements */
  overflow: hidden; /* Prevent content overflow */
}

/* Modal header */
.product-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background-color: #f5f5f5; /* Light gray background for header */
  border-bottom: 1px solid #e0e0e0; /* Separator line */
}

.product-modal-header h2 {
  font-size: 1.25rem; /* Medium font size */
  font-weight: 600; /* Slightly bold text */
  margin: 0;
  color: #333333; /* Dark text for readability */
}

.product-modal-header .close-button {
  cursor: pointer;
  font-size: 1rem; /* Button font size */
  color: #666666; /* Slightly lighter text */
  background: none;
  border: none;
  padding: 0;
  transition: color 0.2s ease-in-out;
}

.product-modal-header .close-button:hover {
  color: #333333; /* Darker color on hover */
}

/* Modal content */
.product-modal-content {
  padding: 16px;
  color: #4f4f4f; /* Neutral text color */
}

.product-modal-content img {
  width: 100%; /* Full width image */
  border-radius: 4px; /* Rounded corners on images */
  margin-bottom: 12px;
}

.product-modal-content .product-title {
  font-size: 1.5rem;
  font-weight: 700; /* Bold title */
  margin-bottom: 8px;
  color: #222222; /* Slightly darker text */
}

.product-modal-content .product-description {
  font-size: 1rem;
  line-height: 1.4; /* Improved readability */
  margin-bottom: 16px;
}

/* Modal footer */
.product-modal-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background-color: #f5f5f5; /* Light gray background for footer */
  border-top: 1px solid #e0e0e0; /* Separator line */
}

.product-modal-footer .price {
  font-size: 1.25rem;
  font-weight: 600;
  color: #333333; /* Dark text */
}

.product-modal-footer .action-buttons {
  display: flex;
  gap: 12px; /* Spacing between buttons */
}

.product-modal-footer .action-buttons button {
  padding: 8px 16px;
  font-size: 1rem;
  border: none;
  border-radius: 4px; /* Rounded corners for buttons */
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.product-modal-footer .action-buttons button.add-to-cart {
  background-color: #007bff; /* Primary button color */
  color: #ffffff;
}

.product-modal-footer .action-buttons button.add-to-cart:hover {
  background-color: #0056b3; /* Darker shade on hover */
}

.product-modal-footer .action-buttons button.view-details {
  background-color: #f8f9fa; /* Secondary button color */
  color: #333333;
}

.product-modal-footer .action-buttons button.view-details:hover {
  background-color: #e2e6ea; /* Darker shade on hover */
}

/* Overlay styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  z-index: 999; /* Ensure overlay appears below the modal */
}

/* Responsive styles for smaller screens */
@media (max-width: 768px) {
  .product-modal {
    width: 95%; /* Adjust modal width */
    max-width: none; /* Remove the max-width constraint */
  }

  .product-modal-content img {
    height: auto; /* Ensure images scale properly */
  }
}
```
