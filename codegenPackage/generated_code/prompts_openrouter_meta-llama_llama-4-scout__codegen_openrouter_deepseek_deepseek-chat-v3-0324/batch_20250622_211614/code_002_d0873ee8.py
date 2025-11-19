"""
Generated Code Metadata:
========================
Original URL: https://hdadpanaderos.es
Prompt: Generate HTML and CSS code for a simple webpage that lists the Junta de Gobierno and Comisión del Régimen y Gobierno de la Hermandad, including their roles and contact information.
Generated: DETERMINISTIC_d0873ee858c304f3
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the HTML and CSS code for the requested webpage:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hermandad - Junta de Gobierno y Comisión</title>
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

        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Header */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 5px solid #e74c3c;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        /* Sections */
        section {
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 25px;
            margin-bottom: 30px;
        }

        section h2 {
            color: #2c3e50;
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }

        /* Member cards */
        .member {
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }

        .member:last-child {
            border-bottom: none;
        }

        .member-info {
            flex: 1;
            min-width: 250px;
        }

        .member h3 {
            color: #2c3e50;
            margin-bottom: 5px;
        }

        .member p {
            margin-bottom: 5px;
        }

        .member-contact {
            margin-top: 10px;
        }

        .member-contact a {
            color: #e74c3c;
            text-decoration: none;
        }

        .member-contact a:hover {
            text-decoration: underline;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .member {
                flex-direction: column;
            }
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 20px;
            background-color: #2c3e50;
            color: white;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Hermandad de [Nombre]</h1>
            <p>Junta de Gobierno y Comisión del Régimen y Gobierno</p>
        </div>
    </header>

    <main class="container">
        <section id="junta-gobierno">
            <h2>Junta de Gobierno</h2>
            
            <div class="member">
                <div class="member-info">
                    <h3>Hermano Mayor</h3>
                    <p>Nombre: Juan Pérez García</p>
                    <p>Rol: Presidente y representante legal de la Hermandad</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34123456789">+34 123 456 789</a></p>
                        <p>Email: <a href="mailto:hermanomayor@hermandad.com">hermanomayor@hermandad.com</a></p>
                    </div>
                </div>
            </div>

            <div class="member">
                <div class="member-info">
                    <h3>Secretario</h3>
                    <p>Nombre: María López Fernández</p>
                    <p>Rol: Responsable de documentación y actas</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34987654321">+34 987 654 321</a></p>
                        <p>Email: <a href="mailto:secretario@hermandad.com">secretario@hermandad.com</a></p>
                    </div>
                </div>
            </div>

            <div class="member">
                <div class="member-info">
                    <h3>Tesorero</h3>
                    <p>Nombre: Carlos Gómez Martínez</p>
                    <p>Rol: Gestión económica y presupuestos</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34567891234">+34 567 891 234</a></p>
                        <p>Email: <a href="mailto:tesorero@hermandad.com">tesorero@hermandad.com</a></p>
                    </div>
                </div>
            </div>
        </section>

        <section id="comision-regimen">
            <h2>Comisión del Régimen y Gobierno</h2>
            
            <div class="member">
                <div class="member-info">
                    <h3>Presidente</h3>
                    <p>Nombre: Ana Ruiz Díaz</p>
                    <p>Rol: Coordinación de la Comisión</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34912345678">+34 912 345 678</a></p>
                        <p>Email: <a href="mailto:presidente.comision@hermandad.com">presidente.comision@hermandad.com</a></p>
                    </div>
                </div>
            </div>

            <div class="member">
                <div class="member-info">
                    <h3>Vocal de Protocolo</h3>
                    <p>Nombre: Luis Sánchez Pérez</p>
                    <p>Rol: Organización de actos y ceremonias</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34654321987">+34 654 321 987</a></p>
                        <p>Email: <a href="mailto:protocolo@hermandad.com">protocolo@hermandad.com</a></p>
                    </div>
                </div>
            </div>

            <div class="member">
                <div class="member-info">
                    <h3>Vocal de Formación</h3>
                    <p>Nombre: Isabel Torres Jiménez</p>
                    <p>Rol: Organización de actividades formativas</p>
                    <div class="member-contact">
                        <p>Teléfono: <a href="tel:+34789123456">+34 789 123 456</a></p>
                        <p>Email: <a href="mailto:formacion@hermandad.com">formacion@hermandad.com</a></p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Hermandad de [Nombre]. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
```
