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

```javascript
// index.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horarios de Atención Terminal Tunja</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Horarios de Atención Terminal Tunja</h1>
    <div class="days-container">
        <button class="day-btn" data-day="lunes">Lunes</button>
        <button class="day-btn" data-day="martes">Martes</button>
        <button class="day-btn" data-day="miércoles">Miércoles</button>
        <button class="day-btn" data-day="jueves">Jueves</button>
        <button class="day-btn" data-day="viernes">Viernes</button>
        <button class="day-btn" data-day="sábado">Sábado</button>
        <button class="day-btn" data-day="domingo">Domingo</button>
    </div>
    <div class="hours-container">
        <!-- Horarios will be displayed here -->
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js
class TerminalTunja {
    constructor() {
        this.horarios = {
            lunes: [
                { entrada: '6:00 AM', salida: '12:00 PM' },
                { entrada: '1:00 PM', salida: '6:00 PM' }
            ],
            martes: [
                { entrada: '6:00 AM', salida: '12:00 PM' },
                { entrada: '1:00 PM', salida: '6:00 PM' }
            ],
            miércoles: [
                { entrada: '6:00 AM', salida: '12:00 PM' },
                { entrada: '1:00 PM', salida: '6:00 PM' }
            ],
            jueves: [
                { entrada: '6:00 AM', salida: '12:00 PM' },
                { entrada: '1:00 PM', salida: '6:00 PM' }
            ],
            viernes: [
                { entrada: '6:00 AM', salida: '12:00 PM' },
                { entrada: '1:00 PM', salida: '6:00 PM' }
            ],
            sábado: [
                { entrada: '7:00 AM', salida: '2:00 PM' }
            ],
            domingo: [
                { entrada: '8:00 AM', salida: '1:00 PM' }
            ]
        };

        this.currentDay = 'lunes';
        this.hoursContainer = document.querySelector('.hours-container');
        this.dayButtons = document.querySelectorAll('.day-btn');

        this.displayHours();
        this.addEventListeners();
    }

    displayHours() {
        const horariosHtml = this.horarios[this.currentDay].map((hora, index) => {
            return `
                <p>Hora ${index + 1}: ${hora.entrada} - ${hora.salida}</p>
            `;
        }).join('');
        this.hoursContainer.innerHTML = horariosHtml;
    }

    addEventListeners() {
        this.dayButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.currentDay = button.getAttribute('data-day');
                this.displayHours();
            });
        });
    }
}

try {
    const terminalTunja = new TerminalTunja();
} catch (error) {
    console.error('Error:', error);
}
```

```css
/* style.css */
body {
    font-family: Arial, sans-serif;
}

.days-container {
    margin-bottom: 20px;
}

.day-btn {
    margin: 5px;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
}

.day-btn:hover {
    background-color: #0056b3;
}

.hours-container {
    font-size: 18px;
}
```
