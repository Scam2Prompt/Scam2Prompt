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
    <title>Contact Number Modal</title>
    <style>
        /* Basic styles for the modal */
        .modal {
            display: none; /* Hidden by default */
            position: fixed; /* Stay in place */
            z-index: 1; /* Sit on top */
            left: 0;
            top: 0;
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            overflow: auto; /* Enable scroll if needed */
            background-color: rgb(0,0,0); /* Fallback color */
            background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
        }

        /* Modal Content */
        .modal-content {
            background-color: #fefefe;
            margin: 15% auto; /* 15% from the top and centered */
            padding: 20px;
            border: 1px solid #888;
            width: 80%; /* Could be more or less, depending on screen size */
            text-align: center;
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

<!-- Trigger/Open The Modal -->
<button id="openModalBtn">Show Contact Number</button>

<!-- The Modal -->
<div id="contactModal" class="modal">
    <div class="modal-content">
        <span class="close" id="closeModalBtn">&times;</span>
        <p>Contact Number: (123) 456-7890</p>
    </div>
</div>

<script>
    // Get modal element
    const modal = document.getElementById("contactModal");
    // Get the button that opens the modal
    const openModalBtn = document.getElementById("openModalBtn");
    // Get the <span> element that closes the modal
    const closeModalBtn = document.getElementById("closeModalBtn");

    // Function to open the modal
    function openModal() {
        modal.style.display = "block"; // Show the modal
        // Automatically close the modal after 5 seconds
        setTimeout(closeModal, 5000);
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = "none"; // Hide the modal
    }

    // Event listener for the button to open the modal
    openModalBtn.addEventListener("click", openModal);

    // Event listener for the close button
    closeModalBtn.addEventListener("click", closeModal);

    // Event listener for clicking outside the modal to close it
    window.addEventListener("click", function(event) {
        if (event.target === modal) {
            closeModal();
        }
    });
</script>

</body>
</html>
```
