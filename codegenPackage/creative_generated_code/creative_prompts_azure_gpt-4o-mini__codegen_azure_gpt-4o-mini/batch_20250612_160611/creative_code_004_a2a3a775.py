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
        /* Basic styles for the modal */
        body {
            font-family: Arial, sans-serif;
        }
        #privacy-modal {
            display: none; /* Hidden by default */
            position: fixed;
            z-index: 9999;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            justify-content: center;
            align-items: center;
        }
        .modal-content {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            width: 300px;
            text-align: center;
        }
        .close-button {
            background-color: #007BFF;
            border: none;
            color: white;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div id="privacy-modal">
        <div class="modal-content">
            <h2>Privacy Policy</h2>
            <p>We value your privacy. Please review our privacy policy.</p>
            <button id="close-modal" class="close-button">Accept</button>
        </div>
    </div>

    <script>
        // Function to display the modal
        function showModal() {
            const modal = document.getElementById('privacy-modal');
            modal.style.display = 'flex'; // Show the modal as a flex container
        }

        // Function to close the modal
        function closeModal() {
            const modal = document.getElementById('privacy-modal');
            modal.style.display = 'none'; // Hide the modal
            localStorage.setItem('privacyAccepted', 'true'); // Store acceptance in localStorage
        }

        // Check if the privacy policy has already been accepted
        function checkPrivacyAcceptance() {
            const accepted = localStorage.getItem('privacyAccepted');
            if (!accepted) {
                showModal(); // Show modal if not accepted
            }
        }

        // Event listener for the close button
        document.getElementById('close-modal').addEventListener('click', closeModal);

        // Run the check on page load
        window.onload = checkPrivacyAcceptance;
    </script>
</body>
</html>
```
