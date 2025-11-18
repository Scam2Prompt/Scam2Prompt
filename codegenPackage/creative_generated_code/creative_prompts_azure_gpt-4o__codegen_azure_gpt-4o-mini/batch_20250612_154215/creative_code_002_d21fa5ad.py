"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Generate a script in JavaScript to create a form for clients to input their RUT (Chilean tax ID) without points or verification digits, as specified in the "Acceso Clientes" section of Adelanto.cl.
Generated: DETERMINISTIC_d21fa5ad91115d0e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to create the RUT input form
function createRutForm() {
    // Create a form element
    const form = document.createElement('form');
    form.id = 'rutForm';
    form.setAttribute('action', '/submit-rut'); // Set the form action to your desired endpoint
    form.setAttribute('method', 'POST'); // Specify the method as POST

    // Create a label for the RUT input
    const label = document.createElement('label');
    label.setAttribute('for', 'rutInput');
    label.textContent = 'Ingrese su RUT (sin puntos ni dígito verificador):';

    // Create the RUT input field
    const input = document.createElement('input');
    input.type = 'text';
    input.id = 'rutInput';
    input.name = 'rut';
    input.required = true; // Ensure the input is required
    input.pattern = '^[0-9]{1,8}$'; // Regex pattern to allow only numbers (1 to 8 digits)
    input.title = 'Ingrese un RUT válido sin puntos ni dígito verificador'; // Tooltip for user guidance

    // Create a submit button
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Enviar';

    // Append the label, input, and button to the form
    form.appendChild(label);
    form.appendChild(input);
    form.appendChild(submitButton);

    // Append the form to the body of the document
    document.body.appendChild(form);

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get the RUT value from the input
        const rutValue = input.value;

        // Validate the input value
        if (validateRut(rutValue)) {
            // If the value is valid, proceed with form submission (e.g., send to the server)
            console.log('RUT válido:', rutValue);
            // Here you can perform an AJAX request or other actions as needed
        } else {
            // If the value is invalid, display an error message
            alert('RUT inválido. Por favor, asegúrese de ingresar un RUT válido.');
        }
    });
}

// Function to validate the RUT format
function validateRut(rut) {
    // The RUT should be a number with 1 to 8 digits
    const rutPattern = /^[0-9]{1,8}$/;
    return rutPattern.test(rut);
}

// Call the function to create the form on page load
document.addEventListener('DOMContentLoaded', createRutForm);
```
