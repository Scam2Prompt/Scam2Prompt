"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate HTML and CSS code for a landing page promoting the FestiVin Caraquet event, including sections for "Grandes dégustations," "Séminaires," and "Soirée prestige chez Origines Cuisine maritime."
Generated: DETERMINISTIC_3f4d24c4c5a87496
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://kit.fontawesome.com/a076d05399.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FestiVin Caraquet - Découvrez les vins d'exception</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Header Styles */
        header {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
            color: #fff;
            text-align: center;
            padding: 4rem 2rem;
        }

        .logo {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            font-weight: bold;
        }

        .tagline {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }

        .date {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            font-style: italic;
        }

        .cta-button {
            display: inline-block;
            background: #8b0000;
            color: #fff;
            padding: 0.8rem 2rem;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background 0.3s ease;
        }

        .cta-button:hover {
            background: #6b0000;
        }

        /* Section Styles */
        section {
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: #8b0000;
        }

        .event-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            margin-bottom: 2rem;
            transition: transform 0.3s ease;
        }

        .event-card:hover {
            transform: translateY(-5px);
        }

        .event-title {
            color: #8b0000;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .event-description {
            margin-bottom: 1.5rem;
        }

        .event-details {
            font-style: italic;
            color: #666;
        }

        /* Footer Styles */
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: #fff;
            margin: 0 10px;
            font-size: 1.5rem;
            text-decoration: none;
        }

        /* Responsive Design */
        @media (min-width: 768px) {
            .events-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 2rem;
            }

            .event-card {
                margin-bottom: 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">FestiVin Caraquet</div>
        <div class="tagline">Découvrez les vins d'exception dans une ambiance chaleureuse</div>
        <div class="date">15-17 Octobre 2023</div>
        <a href="#reservation" class="cta-button">Réservez maintenant</a>
    </header>

    <section id="events">
        <h2 class="section-title">Nos Événements Phares</h2>
        <div class="events-container">
            <div class="event-card">
                <h3 class="event-title">Grandes dégustations</h3>
                <p class="event-description">
                    Explorez une sélection exceptionnelle de vins du monde entier, guidés par nos sommeliers experts. 
                    Découvrez des arômes uniques et des accords mets-vins inoubliables.
                </p>
                <p class="event-details">Samedi 16 Octobre | 14h-18h | Salle des Fêtes</p>
                <a href="#reservation" class="cta-button">Participer</a>
            </div>

            <div class="event-card">
                <h3 class="event-title">Séminaires œnologiques</h3>
                <p class="event-description">
                    Approfondissez vos connaissances avec nos séminaires animés par des professionnels du vin. 
                    Thématiques variées : terroirs, cépages, techniques de dégustation et bien plus.
                </p>
                <p class="event-details">Dimanche 17 Octobre | 10h-12h | Salle de Conférence</p>
                <a href="#reservation" class="cta-button">Participer</a>
            </div>

            <div class="event-card">
                <h3 class="event-title">Soirée prestige chez Origines Cuisine maritime</h3>
                <p class="event-description">
                    Une soirée exclusive alliant les meilleurs crus à une cuisine maritime raffinée. 
                    Menu gastronomique préparé par nos chefs étoilés, accompagné de vins d'exception.
                </p>
                <p class="event-details">Vendredi 15 Octobre | 19h-23h | Origines Cuisine maritime</p>
                <a href="#reservation" class="cta-button">Participer</a>
            </div>
        </div>
    </section>

    <section id="reservation">
        <h2 class="section-title">Réservez votre place</h2>
        <form class="reservation-form">
            <div class="form-group">
                <label for="name">Nom complet</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Téléphone</label>
                <input type="tel" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="event">Événement</label>
                <select id="event" name="event" required>
                    <option value="">Sélectionnez un événement</option>
                    <option value="degustation">Grandes dégustations</option>
                    <option value="seminaire">Séminaires œnologiques</option>
                    <option value="soiree">Soirée prestige</option>
                </select>
            </div>
            <div class="form-group">
                <label for="guests">Nombre de personnes</label>
                <input type="number" id="guests" name="guests" min="1" max="10" required>
            </div>
            <button type="submit" class="cta-button">Confirmer la réservation</button>
        </form>
    </section>

    <footer>
        <p>FestiVin Caraquet - Édition 2023</p>
        <div class="social-links">
            <a href="#"><i class="fab fa-facebook"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
        </div>
        <p>Contact : info@festivincaraquet.com | +1 (506) 123-4567</p>
    </footer>

    <!-- Font Awesome for icons -->
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
</body>
</html>
```
