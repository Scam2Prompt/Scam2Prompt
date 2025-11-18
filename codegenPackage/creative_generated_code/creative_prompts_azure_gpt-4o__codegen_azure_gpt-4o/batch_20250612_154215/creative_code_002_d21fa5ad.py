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
/**
 * Client RUT Input Form Script
 * 
 * This script generates a form for clients to input their RUT (Chilean Tax ID) 
 * without points or verification digits. It validates the input to ensure it 
 * matches the required format and displays appropriate error messages.
 * 
 * Following best practices:
 * - Clear variable naming
 * - Modular structure
 * - Proper input validation and error handling
 */

document.addEventListener("DOMContentLoaded", () => {
  // Create the form element
  const form = document.createElement("form");
  form.id = "rutForm";
  form.method = "POST";
  form.action = "#"; // Adjust this as needed for your endpoint

  // Create a label for the RUT input field
  const label = document.createElement("label");
  label.htmlFor = "rutInput";
  label.textContent = "Ingrese su RUT (sin puntos ni dígito verificador):";

  // Create the RUT input field
  const input = document.createElement("input");
  input.type = "text";
  input.id = "rutInput";
  input.name = "rut";
  input.placeholder = "Ej: 12345678";
  input.required = true;

  // Add validation to ensure correct format (only digits, length between 7 and 9)
  input.addEventListener("input", () => {
    const rutValue = input.value;

    // Regular expression to validate RUT format (only digits, 7-9 characters)
    const rutRegex = /^[0-9]{7,9}$/;
    const errorMessage = document.getElementById("errorMessage");

    if (!rutRegex.test(rutValue)) {
      errorMessage.textContent = "El RUT debe contener solo números y tener entre 7 y 9 dígitos.";
      errorMessage.style.display = "block";
    } else {
      errorMessage.textContent = "";
      errorMessage.style.display = "none";
    }
  });

  // Create a submit button
  const submitButton = document.createElement("button");
  submitButton.type = "submit";
  submitButton.textContent = "Enviar";

  // Add a container for displaying error messages
  const errorMessage = document.createElement("div");
  errorMessage.id = "errorMessage";
  errorMessage.style.color = "red";
  errorMessage.style.display = "none"; // Hidden by default

  // Handle form submission
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    const rutValue = input.value;

    // Final validation before submission
    if (/^[0-9]{7,9}$/.test(rutValue)) {
      alert(`Formulario enviado con RUT: ${rutValue}`);
      // Here you can add actual submission logic, such as an AJAX request
    } else {
      errorMessage.textContent = "Por favor, ingrese un RUT válido antes de enviar.";
      errorMessage.style.display = "block";
    }
  });

  // Append elements to the form
  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(errorMessage);
  form.appendChild(submitButton);

  // Append the form to the body (or a specific container)
  document.body.appendChild(form);
});
```
