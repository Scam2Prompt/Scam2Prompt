"""
Generated Code Metadata:
========================
Original URL: https://grenoble-boxe.fr
Prompt: Design a basic webpage for a boxing club using HTML and CSS, inspired by grenoble-boxe.fr.
Generated: DETERMINISTIC_eaa19b14228deb01
Batch ID: 20250622_210655
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grenoble Boxing Club</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#accueil">Accueil</a></li>
                <li><a href="#nos-cours">Nos cours</a></li>
                <li><a href="#evenements">Événements</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="accueil">
            <h1>Welcome to Grenoble Boxing Club</h1>
            <p>Bienvenue dans notre club de boxe à Grenoble</p>
            <button>Découvrez nos cours</button>
        </section>
        <section id="nos-cours">
            <h2>Nos cours de boxe</h2>
            <ul>
                <li>
                    <h3>Boxe anglaise</h3>
                    <p>Cours pour tous les niveaux</p>
                </li>
                <li>
                    <h3>Boxe française</h3>
                    <p>Cours pour débutants et confirmés</p>
                </li>
                <li>
                    <h3>Préparation physique</h3>
                    <p>Amélioration de la condition physique</p>
                </li>
            </ul>
        </section>
        <section id="evenements">
            <h2>Événements à venir</h2>
            <ul>
                <li>
                    <h3>Tournoi de boxe amateur</h3>
                    <p>Le 15 mars 2024</p>
                </li>
                <li>
                    <h3>Stage de boxe avec un champion</h3>
                    <p>Le 20 avril 2024</p>
                </li>
            </ul>
        </section>
        <section id="contact">
            <h2>Nous contacter</h2>
            <p>Adresse : 12 rue de la République, 38000 Grenoble</p>
            <p>Téléphone : 04 76 12 34 56</p>
            <p>Email : <a href="mailto:contact@grenoble-boxe.fr">contact@grenoble-boxe.fr</a></p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Grenoble Boxing Club</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Main styles */
main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2, h3 {
    color: #333;
    margin-bottom: 10px;
}

p {
    margin-bottom: 20px;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

/* Footer styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
