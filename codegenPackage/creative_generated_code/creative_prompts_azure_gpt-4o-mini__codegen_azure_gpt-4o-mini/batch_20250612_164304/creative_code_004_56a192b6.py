"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Design a simple HTML form that collects user information for scheduling an eye examination, reflecting the services provided by Optic Alizé in Burkina Faso.
Generated: DETERMINISTIC_56a192b69cacb009
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire de Prise de Rendez-vous - Optic Alizé</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Prise de Rendez-vous pour Examen Oculaire</h1>
        <p>Optic Alizé - Burkina Faso</p>
    </header>

    <main>
        <form id="appointmentForm" action="/submit" method="POST">
            <!-- User's Full Name -->
            <label for="fullName">Nom Complet:</label>
            <input type="text" id="fullName" name="fullName" required placeholder="Entrez votre nom complet">

            <!-- User's Email -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Entrez votre adresse email">

            <!-- User's Phone Number -->
            <label for="phone">Numéro de Téléphone:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Entrez votre numéro de téléphone">

            <!-- Preferred Appointment Date -->
            <label for="appointmentDate">Date Préférée:</label>
            <input type="date" id="appointmentDate" name="appointmentDate" required>

            <!-- Services Offered -->
            <label for="services">Services Souhaités:</label>
            <select id="services" name="services" required>
                <option value="" disabled selected>Sélectionnez un service</option>
                <option value="examen">Examen de la Vue</option>
                <option value="consultation">Consultation Spécialisée</option>
                <option value="verres">Verres Correcteurs</option>
                <option value="lunettes">Lunettes de Soleil</option>
            </select>

            <!-- Submit Button -->
            <button type="submit">Prendre Rendez-vous</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Optic Alizé. Tous droits réservés.</p>
    </footer>

    <script>
        // Validates the form before submission
        document.getElementById('appointmentForm').addEventListener('submit', function(event) {
            // Validate required fields
            const fullName = document.getElementById('fullName').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const appointmentDate = document.getElementById('appointmentDate').value;

            if (!fullName || !email || !phone || !appointmentDate) {
                alert('Veuillez remplir tous les champs requis.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
