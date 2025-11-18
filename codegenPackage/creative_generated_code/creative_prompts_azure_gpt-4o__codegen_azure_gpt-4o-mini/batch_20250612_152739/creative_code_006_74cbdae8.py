"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://araform.org
Prompt: Provide code in HTML/CSS to design a responsive webpage showcasing the "Corsi Gratuiti per disoccupati in tutta la Sardegna" section, including buttons for course registration.
Generated: DETERMINISTIC_74cbdae8a9cd6b37
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="it">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corsi Gratuiti per Disoccupati in Sardegna</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <h1>Corsi Gratuiti per Disoccupati in tutta la Sardegna</h1>
        <nav>
            <ul>
                <li><a href="#courses">Corsi</a></li>
                <li><a href="#registration">Registrazione</a></li>
                <li><a href="#contact">Contatti</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="courses">
            <h2>I Nostri Corsi</h2>
            <div class="course-card">
                <h3>Corso di Programmazione</h3>
                <p>Impara le basi della programmazione in vari linguaggi.</p>
                <button onclick="register('Corso di Programmazione')">Registrati</button>
            </div>
            <div class="course-card">
                <h3>Corso di Marketing Digitale</h3>
                <p>Scopri le strategie di marketing per il mondo digitale.</p>
                <button onclick="register('Corso di Marketing Digitale')">Registrati</button>
            </div>
            <div class="course-card">
                <h3>Corso di Design Grafico</h3>
                <p>Impara a creare design accattivanti con software professionali.</p>
                <button onclick="register('Corso di Design Grafico')">Registrati</button>
            </div>
        </section>

        <section id="registration">
            <h2>Registrazione</h2>
            <form id="registration-form" onsubmit="return handleRegistration(event);">
                <label for="name">Nome:</label>
                <input type="text" id="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                
                <label for="course">Corso:</label>
                <select id="course" required>
                    <option value="">Seleziona un corso</option>
                    <option value="Corso di Programmazione">Corso di Programmazione</option>
                    <option value="Corso di Marketing Digitale">Corso di Marketing Digitale</option>
                    <option value="Corso di Design Grafico">Corso di Design Grafico</option>
                </select>
                
                <button type="submit">Invia Registrazione</button>
            </form>
        </section>

        <section id="contact">
            <h2>Contatti</h2>
            <p>Per qualsiasi informazione, contattaci all'indirizzo email: info@corsi-sardegna.it</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Corsi Gratuiti Sardegna. Tutti i diritti riservati.</p>
    </footer>

    <script>
        // Function to handle course registration
        function register(courseName) {
            alert(`Hai scelto di registrarti per: ${courseName}`);
        }

        // Function to handle form submission
        function handleRegistration(event) {
            event.preventDefault(); // Prevent default form submission
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const course = document.getElementById('course').value;

            if (name && email && course) {
                alert(`Registrazione completata per ${name} al corso ${course}.`);
                document.getElementById('registration-form').reset(); // Reset the form
            } else {
                alert('Si prega di completare tutti i campi richiesti.');
            }
            return false; // Prevent form submission
        }
    </script>
</body>

</html>
```

```css
/* styles.css */

/* Reset default styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Basic body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    padding: 20px;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    margin: 20px 0;
}

// Course card styles
.course-card {
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.button {
    background: #007bff;
    color: #fff;
    border: none;
    padding: 10px;
    cursor: pointer;
    border-radius: 5px;
}

.button:hover {
    background: #0056b3;
}

/* Form styles */
form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Footer styles */
footer {
    text-align: center;
    margin-top: 20px;
    font-size: 0.8em;
    color: #666;
}

/* Responsive styles */
@media (max-width: 600px) {
    nav ul li {
        display: block;
        margin: 5px 0;
    }
}
```
