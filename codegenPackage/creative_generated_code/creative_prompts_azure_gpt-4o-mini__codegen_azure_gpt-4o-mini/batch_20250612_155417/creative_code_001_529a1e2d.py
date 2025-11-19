"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safesteth.com
Prompt: How can I implement a pop-up feature for appointment scheduling on a healthcare website, inspired by the pop-up options described on SafeSteth.com?
Generated: DETERMINISTIC_529a1e2d98f5a8de
Batch ID: 20250612_155417
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
    <title>Appointment Scheduler</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>

    <button id="scheduleAppointmentBtn">Schedule Appointment</button>

    <!-- Modal Structure -->
    <div id="appointmentModal" class="modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2>Schedule an Appointment</h2>
            <form id="appointmentForm">
                <label for="patientName">Name:</label>
                <input type="text" id="patientName" required>

                <label for="appointmentDate">Date:</label>
                <input type="date" id="appointmentDate" required>

                <label for="appointmentTime">Time:</label>
                <input type="time" id="appointmentTime" required>

                <button type="submit">Submit</button>
            </form>
        </div>
    </div>

</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the modal */
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
}

.close-btn {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close-btn:hover,
.close-btn:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
```

```javascript
// script.js

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("appointmentModal");
    const btn = document.getElementById("scheduleAppointmentBtn");
    const span = document.getElementsByClassName("close-btn")[0];
    const form = document.getElementById("appointmentForm");

    // Open the modal when the user clicks the button
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Close the modal when the user clicks on <span> (x)
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Close the modal when the user clicks anywhere outside of the modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Handle form submission
    form.onsubmit = function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Collect form data
        const patientName = document.getElementById("patientName").value;
        const appointmentDate = document.getElementById("appointmentDate").value;
        const appointmentTime = document.getElementById("appointmentTime").value;

        // Basic validation
        if (!patientName || !appointmentDate || !appointmentTime) {
            alert("Please fill out all fields.");
            return;
        }

        // Here, you would typically send the data to your server
        // For demo purpose, we just log it to the console
        console.log({
            patientName: patientName,
            appointmentDate: appointmentDate,
            appointmentTime: appointmentTime
        });

        // Close the modal after form submission
        modal.style.display = "none";
        alert("Appointment scheduled successfully!");
    }
});
```
