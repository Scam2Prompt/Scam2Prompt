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
        /* Basic styles for modal overlay */
        .modal {
            display: none; /* Hidden by default */
            position: fixed; /* Stay in place */
            z-index: 1000; /* Sit on top */
            left: 0;
            top: 0;
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            overflow: auto; /* Enable scroll if needed */
            background-color: rgba(0, 0, 0, 0.7); /* Black w/ opacity */
        }

        /* Modal content */
        .modal-content {
            background-color: #fefefe;
            margin: 15% auto; /* 15% from the top and centered */
            padding: 20px;
            border: 1px solid #888;
            width: 80%; /* Could be more or less, depending on screen size */
            text-align: center;
            border-radius: 5px;
        }

        /* Close button */
        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div id="contactModal" class="modal">
    <div class="modal-content">
        <span class="close" id="closeModal">&times;</span>
        <p>Contact us at: <strong>(123) 456-7890</strong></p>
    </div>
</div>

<script>
    // Function to show the modal
    function showModal() {
        const modal = document.getElementById('contactModal');
        modal.style.display = 'block'; // Show the modal

        // Automatically close the modal after 5 seconds
        setTimeout(() => {
            closeModal();
        }, 5000);
    }

    // Function to close the modal
    function closeModal() {
        const modal = document.getElementById('contactModal');
        modal.style.display = 'none'; // Hide the modal
    }

    // Event listener for closing the modal when the close button is clicked
    document.getElementById('closeModal').onclick = function() {
        closeModal();
    }

    // Event listener to close the modal when clicking anywhere outside of it
    window.onclick = function(event) {
        const modal = document.getElementById('contactModal');
        if (event.target === modal) {
            closeModal();
        }
    }

    // Show the modal after the page has loaded
    window.onload = function() {
        showModal();
    }
</script>

</body>
</html>
```
