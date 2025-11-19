"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: Create an HTML form with dropdown options for Egatur's courses, such as "Barismo," "Gestión de Hotelería y Turismo," and "Pastelería y Panificación," and validate the input using JavaScript.
Generated: DETERMINISTIC_bb02349a10243276
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Cursos de Egatur</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
            display: none;
        }
    </style>
</head>
<body>

    <h1>Inscripción a Cursos de Egatur</h1>
    <form id="courseForm">
        <label for="course">Seleccione un curso:</label>
        <select id="course" name="course" required>
            <option value="">--Seleccione un curso--</option>
            <option value="Barismo">Barismo</option>
            <option value="Gestión de Hotelería y Turismo">Gestión de Hotelería y Turismo</option>
            <option value="Pastelería y Panificación">Pastelería y Panificación</option>
        </select>
        <span class="error" id="error-message">Por favor, seleccione un curso.</span>
        <br><br>
        <button type="submit">Enviar</button>
    </form>

    <script>
        // Function to validate the form input
        function validateForm(event) {
            // Prevent the default form submission
            event.preventDefault();

            // Get the selected course value
            const courseSelect = document.getElementById('course');
            const errorMessage = document.getElementById('error-message');

            // Check if a course is selected
            if (courseSelect.value === "") {
                // Show error message if no course is selected
                errorMessage.style.display = 'inline';
            } else {
                // Hide error message and proceed with form submission
                errorMessage.style.display = 'none';
                alert(`Curso seleccionado: ${courseSelect.value}`);
                // Here you can add code to submit the form data to the server
                // e.g., using fetch or XMLHttpRequest
            }
        }

        // Attach the validateForm function to the form's submit event
        document.getElementById('courseForm').addEventListener('submit', validateForm);
    </script>

</body>
</html>
```
