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

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Egatur Courses</title>
    <style>
        /* Basic styling for form */
        form {
            width: 50%;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        select {
            width: 100%;
            height: 30px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }

        button[type="submit"] {
            width: 100%;
            height: 30px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #3e8e41;
        }

        .error {
            color: red;
            font-size: 12px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <form id="course-form">
        <label for="course">Seleccione un curso:</label>
        <select id="course" name="course">
            <option value="">Seleccione una opción</option>
            <option value="Barismo">Barismo</option>
            <option value="Gestión de Hotelería y Turismo">Gestión de Hotelería y Turismo</option>
            <option value="Pastelería y Panificación">Pastelería y Panificación</option>
        </select>
        <div class="error" id="course-error"></div>
        <button type="submit">Enviar</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('course-form');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    // Prevent default form submission behavior
    e.preventDefault();

    // Get the selected course value
    const course = document.getElementById('course').value;

    // Validate the input
    if (course === '') {
        // Show error message if no course is selected
        document.getElementById('course-error').innerText = 'Debe seleccionar un curso';
    } else {
        // Clear error message if course is selected
        document.getElementById('course-error').innerText = '';

        // You can add additional logic here to handle the selected course
        console.log(`Curso seleccionado: ${course}`);

        // Example: Send the selected course to a server using fetch API
        // fetch('/api/course', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ course })
        // })
        // .then((response) => response.json())
        // .then((data) => console.log(data))
        // .catch((error) => console.error(error));
    }
});
```
