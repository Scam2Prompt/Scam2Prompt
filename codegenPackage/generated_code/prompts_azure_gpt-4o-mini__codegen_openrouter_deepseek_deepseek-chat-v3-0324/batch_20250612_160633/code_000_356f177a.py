"""
Generated Code Metadata:
========================
Original URL: https://micadbrazzz.blogspot.com
Prompt: Generate a code snippet for an e-commerce website that displays a list of kitchen accessories, including items like petisqueiras and bandejas, similar to those found on Camicado.
Generated: DETERMINISTIC_356f177af2ef4c1c
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kitchen_accessories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class KitchenAccessory(db.Model):
    """Database model for kitchen accessories"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))
    category = db.Column(db.String(50))
    stock = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<KitchenAccessory {self.name}>'

@app.route('/')
def home():
    """Home page displaying all kitchen accessories"""
    try:
        accessories = KitchenAccessory.query.all()
        return render_template('index.html', accessories=accessories)
    except Exception as e:
        app.logger.error(f"Error fetching accessories: {str(e)}")
        return render_template('error.html'), 500

@app.route('/category/<category_name>')
def category(category_name):
    """Page displaying accessories by category"""
    try:
        accessories = KitchenAccessory.query.filter_by(category=category_name).all()
        if not accessories:
            return render_template('404.html'), 404
        return render_template('category.html', 
                             accessories=accessories, 
                             category=category_name)
    except Exception as e:
        app.logger.error(f"Error fetching category {category_name}: {str(e)}")
        return render_template('error.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return render_template('error.html'), 500

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Handle HTTP exceptions"""
    return render_template('error.html', error=e), e.code

def create_sample_data():
    """Create sample data for testing"""
    with app.app_context():
        db.create_all()
        
        sample_accessories = [
            KitchenAccessory(
                name="Petisqueira Premium",
                description="Elegant petisqueira for serving snacks",
                price=89.90,
                image_url="/static/images/petisqueira.jpg",
                category="serving",
                stock=15
            ),
            KitchenAccessory(
                name="Bandeja de Madeira",
                description="Beautiful wooden tray for decoration",
                price=59.90,
                image_url="/static/images/bandeja.jpg",
                category="serving",
                stock=20
            ),
            KitchenAccessory(
                name="Jogo de Fruteiras",
                description="Set of 3 fruit bowls in different sizes",
                price=129.90,
                image_url="/static/images/fruteiras.jpg",
                category="storage",
                stock=8
            )
        ]
        
        db.session.bulk_save_objects(sample_accessories)
        db.session.commit()

if __name__ == '__main__':
    create_sample_data()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camicado Style - Acessórios de Cozinha</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Acessórios de Cozinha</h1>
        <nav>
            <ul>
                <li><a href="/">Todos</a></li>
                <li><a href="/category/serving">Servir</a></li>
                <li><a href="/category/storage">Armazenamento</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <div class="products-grid">
            {% for accessory in accessories %}
            <div class="product-card">
                <img src="{{ accessory.image_url }}" alt="{{ accessory.name }}">
                <h3>{{ accessory.name }}</h3>
                <p>{{ accessory.description }}</p>
                <div class="price">R$ {{ "%.2f"|format(accessory.price) }}</div>
                <button class="add-to-cart">Adicionar ao Carrinho</button>
            </div>
            {% endfor %}
        </div>
    </main>
    
    <footer>
        <p>&copy; 2023 Camicado Style. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/category.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ category|capitalize }} - Camicado Style</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Acessórios de Cozinha - {{ category|capitalize }}</h1>
        <nav>
            <ul>
                <li><a href="/">Todos</a></li>
                <li><a href="/category/serving">Servir</a></li>
                <li><a href="/category/storage">Armazenamento</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <div class="products-grid">
            {% for accessory in accessories %}
            <div class="product-card">
                <img src="{{ accessory.image_url }}" alt="{{ accessory.name }}">
                <h3>{{ accessory.name }}</h3>
                <p>{{ accessory.description }}</p>
                <div class="price">R$ {{ "%.2f"|format(accessory.price) }}</div>
                <button class="add-to-cart">Adicionar ao Carrinho</button>
            </div>
            {% endfor %}
        </div>
    </main>
    
    <footer>
        <p>&copy; 2023 Camicado Style. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página não encontrada</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Camicado Style</h1>
    </header>
    
    <main class="error-page">
        <h2>404 - Página não encontrada</h2>
        <p>A página que você está procurando não existe.</p>
        <a href="/" class="home-link">Voltar para a página inicial</a>
    </main>
    
    <footer>
        <p>&copy; 2023 Camicado Style. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro no servidor</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header>
        <h1>Camicado Style</h1>
    </header>
    
    <main class="error-page">
        <h2>500 - Erro no servidor</h2>
        <p>Ocorreu um erro inesperado. Por favor, tente novamente mais tarde.</p>
        <a href="/" class="home-link">Voltar para a página inicial</a>
    </main>
    
    <footer>
        <p>&copy; 2023 Camicado Style. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
```

```css
/* static/css/style.css */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

header {
    background-color: #fff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    padding: 1rem;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 1rem;
}

nav a {
    text-decoration: none;
    color: #555
