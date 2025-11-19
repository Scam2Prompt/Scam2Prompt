"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Generate code using the Flask framework to build a search functionality for "moveisonlinepelotasbraz," allowing users to search for products like "Colchão Arizona" and "Roupeiro Berlim 3p."
Generated: DETERMINISTIC_c23acd7ee35e6656
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
import sqlite3
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Database configuration
DATABASE = 'products.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create products table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL,
            category TEXT
        )
    ''')
    
    # Insert sample data if table is empty
    cursor.execute('SELECT COUNT(*) FROM products')
    if cursor.fetchone()[0] == 0:
        sample_products = [
            ('Colchão Arizona', 'Colchão de molas ensacadas', 1999.90, 'Colchões'),
            ('Roupeiro Berlim 3p', 'Roupeiro 3 portas em MDF', 899.90, 'Móveis'),
            ('Sofá Retrátil', 'Sofá retrátil em couro sintético', 1299.90, 'Móveis'),
            ('Cama Box Casal', 'Cama box casal com colchão', 1599.90, 'Camas')
        ]
        cursor.executemany('INSERT INTO products (name, description, price, category) VALUES (?, ?, ?, ?)', sample_products)
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_products():
    try:
        query = request.args.get('q', '').strip()
        if not query:
            raise BadRequest('Search query cannot be empty')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Search for products matching the query in name or description
        cursor.execute('''
            SELECT * FROM products 
            WHERE name LIKE ? OR description LIKE ?
            ORDER BY name
        ''', (f'%{query}%', f'%{query}%'))
        
        products = cursor.fetchall()
        conn.close()
        
        # Convert Row objects to dictionaries
        products_list = [dict(product) for product in products]
        
        return jsonify({
            'success': True,
            'results': products_list,
            'count': len(products_list)
        })
    except BadRequest as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': 'Internal server error'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Moveis Online Pelotas - Busca</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .search-container {
            margin-bottom: 20px;
        }
        #search-input {
            width: 70%;
            padding: 10px;
            font-size: 16px;
        }
        #search-button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .product {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        .product h3 {
            margin-top: 0;
        }
        .price {
            font-weight: bold;
            color: #E91E63;
        }
    </style>
</head>
<body>
    <h1>Moveis Online Pelotas - Busca</h1>
    
    <div class="search-container">
        <input type="text" id="search-input" placeholder="Busque por produtos (ex: Colchão Arizona, Roupeiro Berlim 3p)">
        <button id="search-button">Buscar</button>
    </div>
    
    <div id="results-container"></div>
    
    <script>
        document.getElementById('search-button').addEventListener('click', searchProducts);
        document.getElementById('search-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchProducts();
            }
        });
        
        function searchProducts() {
            const query = document.getElementById('search-input').value.trim();
            if (!query) {
                alert('Por favor, digite um termo de busca');
                return;
            }
            
            fetch(`/search?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    const resultsContainer = document.getElementById('results-container');
                    
                    if (!data.success) {
                        resultsContainer.innerHTML = `<p>Erro: ${data.error}</p>`;
                        return;
                    }
                    
                    if (data.count === 0) {
                        resultsContainer.innerHTML = '<p>Nenhum produto encontrado.</p>';
                        return;
                    }
                    
                    let html = `<p>${data.count} produto(s) encontrado(s):</p>`;
                    
                    data.results.forEach(product => {
                        html += `
                            <div class="product">
                                <h3>${product.name}</h3>
                                <p>${product.description}</p>
                                <p class="price">R$ ${product.price.toFixed(2)}</p>
                                <p>Categoria: ${product.category}</p>
                            </div>
                        `;
                    });
                    
                    resultsContainer.innerHTML = html;
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('results-container').innerHTML = '<p>Ocorreu um erro ao buscar produtos.</p>';
                });
        }
    </script>
</body>
</html>
```
