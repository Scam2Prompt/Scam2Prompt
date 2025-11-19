"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Generate a script in JavaScript to create a form for clients to input their RUT (Chilean tax ID) without points or verification digits, as specified in the "Acceso Clientes" section of Adelanto.cl.
Generated: DETERMINISTIC_d21fa5ad91115d0e
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Create a form for clients to input their RUT (Chilean tax ID)
document.addEventListener("DOMContentLoaded", function () {
    // Create form element
    const form = document.createElement("form");
    form.id = "rutForm";
    form.setAttribute("novalidate", "true"); // Prevent default validation

    // Create input field for RUT
    const rutInput = document.createElement("input");
    rutInput.type = "text";
    rutInput.id = "rutInput";
    rutInput.name = "rut";
    rutInput.placeholder = "Ingrese su RUT sin puntos ni dígito verificador";
    rutInput.required = true; // Make the field required
    rutInput.pattern = "^[0-9]{1,8}$"; // Regex pattern for RUT without points or verification digits

    // Create a submit button
    const submitButton = document.createElement("button");
    submitButton.type = "submit";
    submitButton.textContent = "Enviar";

    // Append input and button to the form
    form.appendChild(rutInput);
    form.appendChild(submitButton);

    // Append form to the body
    document.body.appendChild(form);

    // Form submission event handler
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        // Validate RUT input
        const rutValue = rutInput.value.trim();
        if (!validateRut(rutValue)) {
            alert("RUT inválido. Asegúrese de ingresar solo números sin puntos ni dígito verificador.");
            return;
        }

        // Process the valid RUT (e.g., send to server)
        console.log("RUT ingresado:", rutValue);
        // Here you can add your AJAX call or form submission logic
    });

    /**
     * Validate the RUT format
     * @param {string} rut - The RUT to validate
     * @returns {boolean} - True if valid, false otherwise
     */
    function validateRut(rut) {
        const rutPattern = /^[0-9]{1,8}$/; // RUT must be 1 to 8 digits
        return rutPattern.test(rut);
    }
});
```
