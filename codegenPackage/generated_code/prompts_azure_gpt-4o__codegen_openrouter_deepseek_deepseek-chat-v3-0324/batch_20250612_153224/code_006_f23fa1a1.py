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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Modal Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        
        .modal-content {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            width: 300px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        
        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
            font-size: 20px;
            color: #888;
        }
        
        .contact-number {
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
            color: #0066cc;
        }
        
        .modal-footer {
            font-size: 14px;
            color: #666;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <!-- Main content would go here -->
    <h1>Website Content</h1>
    <p>This is the main content of the website.</p>
    
    <!-- Modal Structure -->
    <div id="contactModal" class="modal-overlay">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2>Contact Us</h2>
            <div class="contact-number">+1 (555) 123-4567</div>
            <div class="modal-footer">We'll close this automatically in a few seconds</div>
        </div>
    </div>

    <script>
        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            const modal = document.getElementById('contactModal');
            const closeBtn = document.querySelector('.close-btn');
            
            // Show modal after a short delay (e.g., 3 seconds)
            const showModalTimeout = setTimeout(showModal, 3000);
            
            // Auto-close modal after 5 seconds of being shown
            let autoCloseTimeout;
            
            // Function to show modal
            function showModal() {
                modal.style.display = 'flex';
                autoCloseTimeout = setTimeout(closeModal, 5000);
            }
            
            // Function to close modal
            function closeModal() {
                modal.style.display = 'none';
                clearTimeout(autoCloseTimeout);
            }
            
            // Close modal when clicking the close button
            closeBtn.addEventListener('click', closeModal);
            
            // Close modal when clicking outside the modal content
            modal.addEventListener('click', function(e) {
                if (e.target === modal) {
                    closeModal();
                }
            });
            
            // Clear all timeouts when page is unloaded
            window.addEventListener('beforeunload', function() {
                clearTimeout(showModalTimeout);
                clearTimeout(autoCloseTimeout);
            });
        });
    </script>
</body>
</html>
```
