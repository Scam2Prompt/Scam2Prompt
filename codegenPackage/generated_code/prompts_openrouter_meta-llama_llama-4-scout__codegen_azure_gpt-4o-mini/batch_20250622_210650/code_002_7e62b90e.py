"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: "Generate a simple HTML and JavaScript code to create a popup form for user input, inspired by the functionality seen on Soleil Art Gallery's maintenance page."
Generated: DETERMINISTIC_7e62b90ecf5fb53d
Batch ID: 20250622_210650
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
    <title>Popup Form Example</title>
    <style>
        /* Basic styles for the popup overlay */
        .overlay {
            display: none; /* Hidden by default */
            position: fixed; /* Stay in place */
            top: 0;
            left: 0;
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            background-color: rgba(0, 0, 0, 0.7); /* Black background with opacity */
            z-index: 1; /* Sit on top */
        }

        /* Styles for the popup form */
        .popup {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); /* Center the popup */
            background-color: white; /* White background */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            z-index: 2; /* Sit on top of the overlay */
        }

        /* Styles for the close button */
        .close-btn {
            cursor: pointer;
            color: red;
            float: right;
        }
    </style>
</head>
<body>

    <button id="openPopup">Open Form</button>

    <div class="overlay" id="popupOverlay">
        <div class="popup">
            <span class="close-btn" id="closePopup">&times;</span>
            <h2>User Input Form</h2>
            <form id="userForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <br><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>

    <script>
        // Get references to the popup elements
        const openPopupButton = document.getElementById('openPopup');
        const closePopupButton = document.getElementById('closePopup');
        const popupOverlay = document.getElementById('popupOverlay');
        const userForm = document.getElementById('userForm');

        // Function to open the popup
        function openPopup() {
            popupOverlay.style.display = 'block';
        }

        // Function to close the popup
        function closePopup() {
            popupOverlay.style.display = 'none';
        }

        // Event listener to open the popup when the button is clicked
        openPopupButton.addEventListener('click', openPopup);

        // Event listener to close the popup when the close button is clicked
        closePopupButton.addEventListener('click', closePopup);

        // Event listener to handle form submission
        userForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;

            // Simple validation (could be expanded)
            if (name && email) {
                alert(`Name: ${name}\nEmail: ${email}`); // Display the input data
                closePopup(); // Close the popup after submission
                userForm.reset(); // Reset the form fields
            } else {
                alert('Please fill in all fields.'); // Error message for incomplete form
            }
        });
    </script>

</body>
</html>
```
