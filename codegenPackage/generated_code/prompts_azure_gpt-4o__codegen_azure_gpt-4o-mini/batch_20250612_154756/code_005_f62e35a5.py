"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Create an HTML form with JavaScript validation for users to select a Chevrolet vehicle model and consórcio plan, ensuring the form matches the structure and options from the Consórcio Chevrolet website.
Generated: DETERMINISTIC_f62e35a51993a5ce
Batch ID: 20250612_154756
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
    <title>Chevrolet Consórcio Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <h1>Chevrolet Consórcio Selection</h1>
    <form id="consorcioForm">
        <label for="vehicleModel">Select Chevrolet Vehicle Model:</label>
        <select id="vehicleModel" name="vehicleModel" required>
            <option value="">--Please choose an option--</option>
            <option value="Onix">Onix</option>
            <option value="Tracker">Tracker</option>
            <option value="S10">S10</option>
            <option value="Camaro">Camaro</option>
            <option value="Equinox">Equinox</option>
        </select>
        <span class="error" id="vehicleModelError"></span>
        <br><br>

        <label for="consorcioPlan">Select Consórcio Plan:</label>
        <select id="consorcioPlan" name="consorcioPlan" required>
            <option value="">--Please choose an option--</option>
            <option value="Plan A">Plan A</option>
            <option value="Plan B">Plan B</option>
            <option value="Plan C">Plan C</option>
        </select>
        <span class="error" id="consorcioPlanError"></span>
        <br><br>

        <button type="submit">Submit</button>
    </form>

    <script>
        // Function to validate the form
        function validateForm(event) {
            // Prevent form submission
            event.preventDefault();

            // Clear previous error messages
            document.getElementById('vehicleModelError').textContent = '';
            document.getElementById('consorcioPlanError').textContent = '';

            // Get form values
            const vehicleModel = document.getElementById('vehicleModel').value;
            const consorcioPlan = document.getElementById('consorcioPlan').value;

            // Validate vehicle model selection
            if (!vehicleModel) {
                document.getElementById('vehicleModelError').textContent = 'Please select a vehicle model.';
            }

            // Validate consórcio plan selection
            if (!consorcioPlan) {
                document.getElementById('consorcioPlanError').textContent = 'Please select a consórcio plan.';
            }

            // If both fields are valid, submit the form
            if (vehicleModel && consorcioPlan) {
                alert(`Form submitted successfully!\nVehicle Model: ${vehicleModel}\nConsórcio Plan: ${consorcioPlan}`);
                // Here you can add code to send the form data to the server
            }
        }

        // Attach the validateForm function to the form's submit event
        document.getElementById('consorcioForm').addEventListener('submit', validateForm);
    </script>

</body>
</html>
```
