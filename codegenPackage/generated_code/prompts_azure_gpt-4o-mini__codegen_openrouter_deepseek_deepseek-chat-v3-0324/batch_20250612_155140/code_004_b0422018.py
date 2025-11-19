"""
Generated Code Metadata:
========================
Original URL: https://betty-moore-873.pages.dev
Prompt: What JavaScript code can I use to display a modal with a promotional message when a user clicks on an image?
Generated: DETERMINISTIC_b0422018b4afc710
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Modal functionality for promotional message on image click
document.addEventListener('DOMContentLoaded', function() {
    // Get all promotional images
    const promoImages = document.querySelectorAll('.promo-image');
    
    // Create modal elements
    const modal = document.createElement('div');
    modal.className = 'promo-modal';
    modal.style.display = 'none';
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0,0,0,0.7)';
    modal.style.zIndex = '1000';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    
    const modalContent = document.createElement('div');
    modalContent.className = 'promo-modal-content';
    modalContent.style.backgroundColor = '#fff';
    modalContent.style.padding = '20px';
    modalContent.style.borderRadius = '8px';
    modalContent.style.maxWidth = '500px';
    modalContent.style.width = '80%';
    
    const closeButton = document.createElement('span');
    closeButton.className = 'promo-modal-close';
    closeButton.innerHTML = '&times;';
    closeButton.style.position = 'absolute';
    closeButton.style.top = '10px';
    closeButton.style.right = '20px';
    closeButton.style.fontSize = '28px';
    closeButton.style.fontWeight = 'bold';
    closeButton.style.cursor = 'pointer';
    
    const promoMessage = document.createElement('div');
    promoMessage.className = 'promo-message';
    promoMessage.innerHTML = '<h2>Special Offer!</h2><p>Get 20% off your next purchase with code: PROMO20</p>';
    
    // Assemble modal
    modalContent.appendChild(closeButton);
    modalContent.appendChild(promoMessage);
    modal.appendChild(modalContent);
    document.body.appendChild(modal);
    
    // Add click event to all promo images
    promoImages.forEach(function(image) {
        image.addEventListener('click', function() {
            modal.style.display = 'flex';
        });
    });
    
    // Close modal when clicking close button
    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });
    
    // Close modal when clicking outside content
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
    
    // Close modal with ESC key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            modal.style.display = 'none';
        }
    });
});
```
