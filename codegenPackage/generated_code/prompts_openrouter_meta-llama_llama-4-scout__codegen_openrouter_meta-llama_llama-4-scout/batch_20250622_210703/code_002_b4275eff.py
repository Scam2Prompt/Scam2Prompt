"""
Generated Code Metadata:
========================
Original URL: https://novamidiapublicidade.com.br
Prompt: "Generate a sample code for a landing page that incorporates branding elements, such as a custom visual identity, for a marketing agency like Nova Mídia Publicidade."
Generated: DETERMINISTIC_b4275effb9b77d38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nova Mídia Publicidade</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home" class="logo">Nova Mídia Publicidade</a></li>
                <li><a href="#servicos">Serviços</a></li>
                <li><a href="#portfolio">Portfólio</a></li>
                <li><a href="#sobre">Sobre</a></li>
                <li><a href="#contato">Contato</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Desenvolvemos soluções criativas para o seu negócio</h1>
        <p>Nova Mídia Publicidade - Agência de Marketing Digital</p>
        <button>Descubra mais</button>
    </section>

    <!-- Serviços Section -->
    <section id="servicos">
        <h2>Nossos Serviços</h2>
        <div class="servicos-grid">
            <div class="servico">
                <h3>Marketing Digital</h3>
                <p>Desenvolvemos estratégias personalizadas para aumentar a presença online do seu negócio.</p>
            </div>
            <div class="servico">
                <h3>Design Gráfico</h3>
                <p>Nossa equipe de designers cria materiais visuais incríveis para a sua marca.</p>
            </div>
            <div class="servico">
                <h3>Desenvolvimento Web</h3>
                <p>Desenvolvemos sites responsivos e aplicativos móveis para a sua empresa.</p>
            </div>
        </div>
    </section>

    <!-- Portfólio Section -->
    <section id="portfolio">
        <h2>Nossos Trabalhos</h2>
        <div class="portfolio-grid">
            <div class="trabalho">
                <img src="img/trabalho1.jpg" alt="Trabalho 1">
                <h3>Campanha de Lançamento de Produto</h3>
            </div>
            <div class="trabalho">
                <img src="img/trabalho2.jpg" alt="Trabalho 2">
                <h3>Rebranding de Marca</h3>
            </div>
            <div class="trabalho">
                <img src="img/trabalho3.jpg" alt="Trabalho 3">
                <h3>Site Institucional</h3>
            </div>
        </div>
    </section>

    <!-- Sobre Section -->
    <section id="sobre">
        <h2>Sobre Nós</h2>
        <p>A Nova Mídia Publicidade é uma agência de marketing digital que busca soluções criativas e inovadoras para os nossos clientes.</p>
    </section>

    <!-- Contato Section -->
    <section id="contato">
        <h2>Fale Conosco</h2>
        <form>
            <input type="text" placeholder="Nome">
            <input type="email" placeholder="E-mail">
            <textarea placeholder="Mensagem"></textarea>
            <button>Enviar</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Nova Mídia Publicidade. Todos os direitos reservados.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #3498db;
    --secondary-color: #f1c40f;
    --font-family: Arial, sans-serif;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-family);
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

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

header nav a.logo {
    font-size: 1.5em;
    font-weight: bold;
}

#home {
    background-image: linear-gradient(to bottom, var(--primary-color), var(--secondary-color));
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#home h1 {
    font-size: 2.5em;
}

#home p {
    font-size: 1.2em;
}

button {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
}

button:hover {
    background-color: var(--secondary-color);
}

#servicos {
    padding: 2em;
}

.servicos-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.servico {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.servico h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

#portfolio {
    padding: 2em;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.trabalho {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.trabalho img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.trabalho h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

#sobre {
    padding: 2em;
}

#contato {
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

form button {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to button
document.querySelector('#home button').addEventListener('click', () => {
    // Scroll to serviços section
    document.querySelector('#servicos').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to form submission
document.querySelector('#contato form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Add form submission logic here
    console.log('Form submitted');
});
```
