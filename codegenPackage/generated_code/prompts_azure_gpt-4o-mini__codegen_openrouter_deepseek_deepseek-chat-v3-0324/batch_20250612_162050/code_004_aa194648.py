"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Illustrate how to use HTML and CSS to create a webpage that showcases the artistic and cultural initiatives of Corporación El Cristal, specifically highlighting the art of puppetry.
Generated: DETERMINISTIC_aa1946484a9439bc
Batch ID: 20250612_162050
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
    <title>Corporación El Cristal - Arte y Cultura</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f9f5e9;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styles */
        header {
            background-color: #8b0000;
            color: white;
            padding: 1.5rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .logo {
            max-width: 150px;
            margin-bottom: 1rem;
        }

        /* Navigation */
        nav {
            background-color: #6b0000;
            padding: 1rem 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav li {
            margin: 0 1.5rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }

        nav a:hover {
            color: #ffcc00;
        }

        /* Main Content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 3rem;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #8b0000;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
        }

        .hero-image {
            width: 100%;
            max-height: 500px;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        /* Puppetry Section */
        .puppetry-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .puppetry-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .puppetry-card:hover {
            transform: translateY(-5px);
        }

        .puppetry-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .card-content {
            padding: 1.5rem;
        }

        .card-content h3 {
            color: #8b0000;
            margin-bottom: 0.5rem;
        }

        /* Events Section */
        .events {
            background-color: #fff;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 3rem;
        }

        .events h2 {
            color: #8b0000;
            margin-bottom: 1.5rem;
            text-align: center;
        }

        .event-list {
            list-style: none;
        }

        .event-item {
            padding: 1rem 0;
            border-bottom: 1px solid #eee;
        }

        .event-item:last-child {
            border-bottom: none;
        }

        .event-date {
            font-weight: bold;
            color: #8b0000;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.5rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav li {
                margin: 0.5rem 0;
            }

            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <img src="logo-el-cristal.png" alt="Logo Corporación El Cristal" class="logo">
        <h1>Corporación El Cristal</h1>
        <p>Promoviendo el arte y la cultura desde 1985</p>
    </header>

    <nav>
        <ul>
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#puppetry">Teatro de Títeres</a></li>
            <li><a href="#events">Eventos</a></li>
            <li><a href="#about">Nosotros</a></li>
            <li><a href="#contact">Contacto</a></li>
        </ul>
    </nav>

    <main class="container">
        <section id="inicio" class="hero">
            <h1>El Arte del Teatro de Títeres</h1>
            <p>Descubre la magia y tradición del teatro de títeres a través de nuestras iniciativas culturales y talleres educativos.</p>
            <img src="puppetry-hero.jpg" alt="Escena de teatro de títeres" class="hero-image">
        </section>

        <section id="puppetry" class="puppetry-section">
            <article class="puppetry-card">
                <img src="puppet-workshop.jpg" alt="Taller de títeres">
                <div class="card-content">
                    <h3>Talleres Educativos</h3>
                    <p>Programas de formación en construcción y manipulación de títeres para todas las edades.</p>
                </div>
            </article>

            <article class="puppetry-card">
                <img src="puppet-show.jpg" alt="Espectáculo de títeres">
                <div class="card-content">
                    <h3>Espectáculos</h3>
                    <p>Presentaciones artísticas que combinan tradición y contemporaneidad en el arte titiritero.</p>
                </div>
            </article>

            <article class="puppetry-card">
                <img src="puppet-making.jpg" alt="Fabricación de títeres">
                <div class="card-content">
                    <h3>Fabricación Artesanal</h3>
                    <p>Técnicas tradicionales de creación de títeres con materiales sostenibles y reciclados.</p>
                </div>
            </article>
        </section>

        <section id="events" class="events">
            <h2>Próximos Eventos</h2>
            <ul class="event-list">
                <li class="event-item">
                    <span class="event-date">15 de Junio, 2023</span> - Festival Internacional de Títeres
                </li>
                <li class="event-item">
                    <span class="event-date">22-25 de Julio, 2023</span> - Taller de Títeres para Niños
                </li>
                <li class="event-item">
                    <span class="event-date">10 de Agosto, 2023</span> - Presentación: "El Mundo Mágico de los Títeres"
                </li>
                <li class="event-item">
                    <span class="event-date">5-10 de Septiembre, 2023</span> - Exposición de Títeres Tradicionales
                </li>
            </ul>
        </section>
    </main>

    <footer id="contact">
        <h3>Corporación El Cristal</h3>
        <p>Calle de la Cultura #123, Bogotá, Colombia</p>
        <p>Teléfono: +57 1 234 5678</p>
        <p>Email: info@elcristal.org</p>
        
        <div class="social-links">
            <a href="#" aria-label="Facebook">f</a>
            <a href="#" aria-label="Instagram">i</a>
            <a href="#" aria-label="Twitter">t</a>
            <a href="#" aria-label
