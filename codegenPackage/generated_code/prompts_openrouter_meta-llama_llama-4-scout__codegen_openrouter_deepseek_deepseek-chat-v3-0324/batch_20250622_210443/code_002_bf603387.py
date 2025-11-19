"""
Generated Code Metadata:
========================
Original URL: https://cdjuangrande.es
Prompt: Generate HTML and CSS code for a basic webpage structure similar to cdjuangrande.es, including a navigation menu with sections for Noticias, Patrocinadores, and Contacto.
Generated: DETERMINISTIC_bf603387522d07c3
Batch ID: 20250622_210443
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
    <title>Club Deportivo Juangrande</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #1a3e72;
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
        }

        /* Navigation styles */
        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 1.5rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s ease;
        }

        nav ul li a:hover {
            background-color: rgba(255,255,255,0.2);
        }

        /* Main content styles */
        main {
            padding: 2rem 0;
        }

        section {
            margin-bottom: 2rem;
            background-color: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        h1, h2 {
            color: #1a3e72;
            margin-bottom: 1rem;
        }

        /* Footer styles */
        footer {
            background-color: #1a3e72;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }

            nav ul {
                margin-top: 1rem;
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">CD Juangrande</div>
                <nav>
                    <ul>
                        <li><a href="#noticias">Noticias</a></li>
                        <li><a href="#patrocinadores">Patrocinadores</a></li>
                        <li><a href="#contacto">Contacto</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="container">
        <section id="noticias">
            <h2>Noticias</h2>
            <p>Últimas noticias del club deportivo.</p>
        </section>

        <section id="patrocinadores">
            <h2>Patrocinadores</h2>
            <p>Nuestros patrocinadores y colaboradores.</p>
        </section>

        <section id="contacto">
            <h2>Contacto</h2>
            <p>Información de contacto del club.</p>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Club Deportivo Juangrande. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
```
