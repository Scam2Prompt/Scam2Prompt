"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Generate a JavaScript code snippet to create a simple website for a community volunteer group, inspired by the website of the Gruppo Comunale dei Volontari di Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_4acfcb4cc0e49d3c
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gruppo Comunale Volontari Protezione Civile</title>
    <style>
        /* Reset and base styles */
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
        
        /* Header styles */
        header {
            background-color: #e74c3c;
            color: white;
            padding: 1rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .logo {
            max-width: 100px;
            margin-bottom: 1rem;
        }
        
        /* Navigation */
        nav {
            background-color: #c0392b;
            padding: 0.5rem 0;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav li {
            margin: 0 1rem;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        
        nav a:hover {
            background-color: #a5281b;
        }
        
        /* Main content */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        section {
            margin-bottom: 2rem;
            background: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        h1, h2, h3 {
            color: #e74c3c;
            margin-bottom: 1rem;
        }
        
        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            nav li {
                margin: 0.5rem 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <img src="logo.png" alt="Logo Protezione Civile" class="logo">
        <h1>Gruppo Comunale Volontari Protezione Civile</h1>
        <p>Torre d'Isola</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">Chi Siamo</a></li>
            <li><a href="#activities">Attività</a></li>
            <li><a href="#join">Diventa Volontario</a></li>
            <li><a href="#contacts">Contatti</a></li>
        </ul>
    </nav>
    
    <main>
        <section id="home">
            <h2>Benvenuti</h2>
            <p>Il Gruppo Comunale dei Volontari di Protezione Civile di Torre d'Isola è un'organizzazione senza scopo di lucro che opera per la sicurezza e la protezione della comunità.</p>
        </section>
        
        <section id="about">
            <h2>Chi Siamo</h2>
            <p>Siamo un gruppo di cittadini volontari che operano per la protezione civile nel territorio comunale di Torre d'Isola. La nostra missione è contribuire alla sicurezza e al benessere della comunità.</p>
        </section>
        
        <section id="activities">
            <h2>Le Nostre Attività</h2>
            <ul>
                <li>Monitoraggio del territorio</li>
                <li>Supporto in emergenze</li>
                <li>Prevenzione e informazione</li>
                <li>Collaborazione con le istituzioni</li>
            </ul>
        </section>
        
        <section id="join">
            <h2>Diventa Volontario</h2>
            <p>Se vuoi contribuire alla sicurezza della nostra comunità, unisciti a noi! Compila il modulo per maggiori informazioni.</p>
            <form id="volunteerForm">
                <div>
                    <label for="name">Nome:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div>
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div>
                    <label for="phone">Telefono:</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <div>
                    <label for="message">Messaggio:</label>
                    <textarea id="message" name="message" rows="4"></textarea>
                </div>
                <button type="submit">Invia</button>
            </form>
        </section>
        
        <section id="contacts">
            <h2>Contatti</h2>
            <p>Email: info@protezioneciviletoredisola.it</p>
            <p>Telefono: +39 123 456789</p>
            <p>Sede: Via Municipio, 1 - Torre d'Isola</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Gruppo Comunale Volontari Protezione Civile Torre d'Isola</p>
        <p>Tutti i diritti riservati</p>
    </footer>

    <script>
        // Form submission handling
        document.getElementById('volunteerForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                message: document.getElementById('message').value
            };
            
            // Here you would typically send the data to a server
            console.log('Form submitted:', formData);
            
            // Show success message
            alert('Grazie per il tuo interesse! Ti contatteremo al più presto.');
            
            // Reset form
            this.reset();
        });
        
        // Smooth scrolling for navigation
        document.querySelectorAll('nav a').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 20,
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>
</body>
</html>
```
