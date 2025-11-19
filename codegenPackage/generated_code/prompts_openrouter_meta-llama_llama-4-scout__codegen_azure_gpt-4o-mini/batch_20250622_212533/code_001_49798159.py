"""
Generated Code Metadata:
========================
Original URL: https://plantagm.com
Prompt: "Write a cookie policy notice in Spanish for a website that analyzes traffic and optimizes user experience."
Generated: DETERMINISTIC_4979815949b1f209
Batch ID: 20250622_212533
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
    <title>Política de Cookies</title>
    <style>
        /* Estilos básicos para el aviso de cookies */
        #cookie-notice {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #333;
            color: #fff;
            padding: 15px;
            text-align: center;
            z-index: 1000;
            display: none; /* Ocultar por defecto */
        }
        #cookie-notice button {
            background-color: #f39c12;
            color: #fff;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            margin-left: 10px;
        }
    </style>
</head>
<body>

    <div id="cookie-notice">
        Este sitio web utiliza cookies para analizar el tráfico y optimizar la experiencia del usuario. 
        Al continuar navegando, aceptas el uso de cookies. 
        <button id="accept-cookies">Aceptar</button>
    </div>

    <script>
        // Función para mostrar el aviso de cookies si no se ha aceptado
        function showCookieNotice() {
            const cookieAccepted = localStorage.getItem('cookiesAccepted');
            if (!cookieAccepted) {
                document.getElementById('cookie-notice').style.display = 'block';
            }
        }

        // Función para manejar la aceptación de cookies
        function acceptCookies() {
            try {
                // Guardar la aceptación en el almacenamiento local
                localStorage.setItem('cookiesAccepted', 'true');
                // Ocultar el aviso de cookies
                document.getElementById('cookie-notice').style.display = 'none';
            } catch (error) {
                console.error('Error al guardar la aceptación de cookies:', error);
            }
        }

        // Asignar el evento de clic al botón de aceptar cookies
        document.getElementById('accept-cookies').addEventListener('click', acceptCookies);

        // Mostrar el aviso de cookies al cargar la página
        window.onload = showCookieNotice;
    </script>

</body>
</html>
```
