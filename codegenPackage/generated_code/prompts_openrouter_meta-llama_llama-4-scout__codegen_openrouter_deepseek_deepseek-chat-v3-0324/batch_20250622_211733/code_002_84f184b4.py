"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Generate a code snippet in JavaScript to create a simple webpage that displays the horarios de atención of the Terminal Tunja and allows users to toggle between different days of the week.
Generated: DETERMINISTIC_84f184b4ec98fdc0
Batch ID: 20250622_211733
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
    <title>Terminal Tunja - Horarios de Atención</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .days-container {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .day-button {
            padding: 10px 15px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
            flex: 1;
            min-width: 100px;
            text-align: center;
        }
        .day-button:hover {
            background-color: #2980b9;
        }
        .day-button.active {
            background-color: #2c3e50;
        }
        .schedule-display {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            min-height: 100px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .schedule-time {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .schedule-day {
            font-size: 18px;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <h1>Terminal Tunja - Horarios de Atención</h1>
    
    <div class="days-container">
        <button class="day-button" data-day="lunes">Lunes</button>
        <button class="day-button" data-day="martes">Martes</button>
        <button class="day-button" data-day="miercoles">Miércoles</button>
        <button class="day-button" data-day="jueves">Jueves</button>
        <button class="day-button" data-day="viernes">Viernes</button>
        <button class="day-button" data-day="sabado">Sábado</button>
        <button class="day-button" data-day="domingo">Domingo</button>
    </div>
    
    <div class="schedule-display">
        <div class="schedule-time">5:00 AM - 9:00 PM</div>
        <div class="schedule-day">Lunes</div>
    </div>

    <script>
        // Horarios de atención para cada día
        const schedules = {
            lunes: { time: '5:00 AM - 9:00 PM', day: 'Lunes' },
            martes: { time: '5:00 AM - 9:00 PM', day: 'Martes' },
            miercoles: { time: '5:00 AM - 9:00 PM', day: 'Miércoles' },
            jueves: { time: '5:00 AM - 9:00 PM', day: 'Jueves' },
            viernes: { time: '5:00 AM - 9:00 PM', day: 'Viernes' },
            sabado: { time: '5:00 AM - 8:00 PM', day: 'Sábado' },
            domingo: { time: '5:00 AM - 8:00 PM', day: 'Domingo' }
        };

        // Elementos del DOM
        const dayButtons = document.querySelectorAll('.day-button');
        const scheduleTimeElement = document.querySelector('.schedule-time');
        const scheduleDayElement = document.querySelector('.schedule-day');

        // Función para cambiar el día activo y mostrar el horario correspondiente
        function setActiveDay(day) {
            // Validar que el día exista en los horarios
            if (!schedules[day]) {
                console.error('Día no válido:', day);
                return;
            }

            // Remover clase active de todos los botones
            dayButtons.forEach(button => {
                button.classList.remove('active');
            });

            // Añadir clase active al botón seleccionado
            const activeButton = document.querySelector(`.day-button[data-day="${day}"]`);
            if (activeButton) {
                activeButton.classList.add('active');
            }

            // Actualizar el display con el horario del día seleccionado
            scheduleTimeElement.textContent = schedules[day].time;
            scheduleDayElement.textContent = schedules[day].day;
        }

        // Event listeners para los botones de día
        dayButtons.forEach(button => {
            button.addEventListener('click', () => {
                const day = button.getAttribute('data-day');
                setActiveDay(day);
            });
        });

        // Inicializar con el día actual
        function getCurrentDay() {
            const days = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'];
            const today = new Date().getDay();
            return days[today];
        }

        // Al cargar la página, mostrar el horario del día actual
        document.addEventListener('DOMContentLoaded', () => {
            const today = getCurrentDay();
            setActiveDay(today);
        });
    </script>
</body>
</html>
```
