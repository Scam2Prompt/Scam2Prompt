"""
Generated Code Metadata:
========================
Original URL: https://verified.myclickfunnels.com
Prompt: Write code to create a multi-step form in a ClickFunnels funnel that collects detailed user information across several pages.
Generated: DETERMINISTIC_35b31931f0941111
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- Multi-Step Form in ClickFunnels -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-Step Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .form-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        .hidden {
            display: none;
        }
        .form-step {
            display: none;
        }
        .form-step.active {
            display: block;
        }
        .button {
            background-color: #007BFF;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
        }
        .button:disabled {
            background-color: #ccc;
        }
    </style>
</head>
<body>

<div class="form-container">
    <form id="multiStepForm">
        <!-- Step 1: User Information -->
        <div class="form-step active" id="step1">
            <h2>User Information</h2>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <button type="button" class="button" onclick="nextStep(1)">Next</button>
        </div>

        <!-- Step 2: Address Information -->
        <div class="form-step" id="step2">
            <h2>Address Information</h2>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required>
            <label for="city">City:</label>
            <input type="text" id="city" name="city" required>
            <button type="button" class="button" onclick="prevStep(2)">Back</button>
            <button type="button" class="button" onclick="nextStep(2)">Next</button>
        </div>

        <!-- Step 3: Confirmation -->
        <div class="form-step" id="step3">
            <h2>Confirmation</h2>
            <p>Please confirm your information:</p>
            <div id="confirmation"></div>
            <button type="button" class="button" onclick="prevStep(3)">Back</button>
            <button type="submit" class="button">Submit</button>
        </div>
    </form>
</div>

<script>
    // Function to show the next step in the form
    function nextStep(currentStep) {
        const currentFormStep = document.getElementById(`step${currentStep}`);
        const nextFormStep = document.getElementById(`step${currentStep + 1}`);

        // Validate current step inputs
        if (!validateStep(currentStep)) {
            alert("Please fill in all required fields.");
            return;
        }

        // Hide current step and show next step
        currentFormStep.classList.remove('active');
        nextFormStep.classList.add('active');

        // Update confirmation step with user input
        if (currentStep === 2) {
            updateConfirmation();
        }
    }

    // Function to show the previous step in the form
    function prevStep(currentStep) {
        const currentFormStep = document.getElementById(`step${currentStep}`);
        const prevFormStep = document.getElementById(`step${currentStep - 1}`);

        // Hide current step and show previous step
        currentFormStep.classList.remove('active');
        prevFormStep.classList.add('active');
    }

    // Function to validate inputs in the current step
    function validateStep(step) {
        const inputs = document.querySelectorAll(`#step${step} input[required]`);
        return Array.from(inputs).every(input => input.value.trim() !== '');
    }

    // Function to update confirmation step with user input
    function updateConfirmation() {
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const address = document.getElementById('address').value;
        const city = document.getElementById('city').value;

        const confirmationDiv = document.getElementById('confirmation');
        confirmationDiv.innerHTML = `
            <p><strong>Name:</strong> ${name}</p>
            <p><strong>Email:</strong> ${email}</p>
            <p><strong>Address:</strong> ${address}</p>
            <p><strong>City:</strong> ${city}</p>
        `;
    }

    // Handle form submission
    document.getElementById('multiStepForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Here you can handle the form data, e.g., send it to a server
        alert("Form submitted successfully!");
        // Optionally, reset the form or redirect the user
        this.reset();
        document.querySelectorAll('.form-step').forEach(step => step.classList.remove('active'));
        document.getElementById('step1').classList.add('active');
    });
</script>

</body>
</html>
```
