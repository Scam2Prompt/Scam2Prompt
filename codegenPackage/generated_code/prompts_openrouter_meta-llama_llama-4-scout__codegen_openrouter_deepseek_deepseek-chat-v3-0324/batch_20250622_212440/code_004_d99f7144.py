"""
Generated Code Metadata:
========================
Original URL: https://poocoinconectswap.blogspot.com
Prompt: Develop an e-commerce category page for "Sapatos Femininos" featuring sandals, social shoes, and sports shoes.
Generated: DETERMINISTIC_d99f7144bb6130fc
Batch ID: 20250622_212440
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300x200?text=Sand\u00e1lia+1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Esportivo+1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Social+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Sand\u00e1lia+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Esportivo+2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Social+1": {
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
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sapatos Femininos - Sandálias, Sociais e Esportivos</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f8f8f8;
            color: #333;
        }
        
        header {
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 15px;
        }
        
        nav ul li a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
        }
        
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }
        
        .page-title {
            text-align: center;
            margin-bottom: 30px;
            font-size: 28px;
        }
        
        .category-filter {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
        }
        
        .category-filter button {
            padding: 10px 20px;
            margin: 0 10px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .category-filter button:hover, 
        .category-filter button.active {
            background-color: #333;
            color: #fff;
        }
        
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
        }
        
        .product-card {
            background-color: #fff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .product-card:hover {
            transform: translateY(-5px);
        }
        
        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .product-info {
            padding: 15px;
        }
        
        .product-title {
            font-size: 16px;
            margin-bottom: 10px;
        }
        
        .product-price {
            font-weight: bold;
            color: #e63946;
            margin-bottom: 10px;
        }
        
        .product-rating {
            color: #f4a261;
            margin-bottom: 10px;
        }
        
        .add-to-cart {
            width: 100%;
            padding: 10px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .add-to-cart:hover {
            background-color: #555;
        }
        
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Minha Loja</div>
        <nav>
            <ul>
                <li><a href="#">Início</a></li>
                <li><a href="#">Sapatos</a></li>
                <li><a href="#">Bolsas</a></li>
                <li><a href="#">Acessórios</a></li>
                <li><a href="#">Contato</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="container">
        <h1 class="page-title">Sapatos Femininos</h1>
        
        <div class="category-filter">
            <button class="active">Todos</button>
            <button data-category="sandals">Sandálias</button>
            <button data-category="social">Sociais</button>
            <button data-category="sports">Esportivos</button>
        </div>
        
        <div class="products-grid">
            <!-- Sandália 1 -->
            <div class="product-card" data-category="sandals">
                <img src="https://via.placeholder.com/300x200?text=Sandália+1" alt="Sandália Feminina" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Sandália Comfort</h3>
                    <div class="product-price">R$ 129,90</div>
                    <div class="product-rating">★★★★☆</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
            
            <!-- Sandália 2 -->
            <div class="product-card" data-category="sandals">
                <img src="https://via.placeholder.com/300x200?text=Sandália+2" alt="Sandália Feminina" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Sandália Premium</h3>
                    <div class="product-price">R$ 199,90</div>
                    <div class="product-rating">★★★★★</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
            
            <!-- Social 1 -->
            <div class="product-card" data-category="social">
                <img src="https://via.placeholder.com/300x200?text=Social+1" alt="Sapato Social Feminino" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Social Elegance</h3>
                    <div class="product-price">R$ 179,90</div>
                    <div class="product-rating">★★★★☆</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
            
            <!-- Social 2 -->
            <div class="product-card" data-category="social">
                <img src="https://via.placeholder.com/300x200?text=Social+2" alt="Sapato Social Feminino" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Social Classic</h3>
                    <div class="product-price">R$ 159,90</div>
                    <div class="product-rating">★★★☆☆</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
            
            <!-- Esportivo 1 -->
            <div class="product-card" data-category="sports">
                <img src="https://via.placeholder.com/300x200?text=Esportivo+1" alt="Tênis Esportivo Feminino" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Tênis Runner</h3>
                    <div class="product-price">R$ 229,90</div>
                    <div class="product-rating">★★★★★</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
            
            <!-- Esportivo 2 -->
            <div class="product-card" data-category="sports">
                <img src="https://via.placeholder.com/300x200?text=Esportivo+2" alt="Tênis Esportivo Feminino" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Tênis Fitness</h3>
                    <div class="product-price">R$ 199,90</div>
                    <div class="product-rating">★★★★☆</div>
                    <button class="add-to-cart">Adicionar ao Carrinho</button>
                </div>
            </div>
        </div>
    </div>
    
    <footer>
        <p>&copy; 2023 Minha Loja. Todos os direitos reservados.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const filterButtons = document.querySelectorAll('.category-filter button');
            const productCards = document.querySelectorAll('.product
