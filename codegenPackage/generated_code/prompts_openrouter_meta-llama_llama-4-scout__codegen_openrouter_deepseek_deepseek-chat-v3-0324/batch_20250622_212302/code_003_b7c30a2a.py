"""
Generated Code Metadata:
========================
Original URL: https://apnastores.com
Prompt: Design a simple e-commerce website using HTML, CSS, and JavaScript that allows users to purchase game vouchers and top-ups, inspired by the layout and features of ApnaStores.
Generated: DETERMINISTIC_b7c30a2a9670b426
Batch ID: 20250622_212302
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/1920x600": {
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameTop - Your Gaming Store</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
        }

        .logo span {
            color: #3498db;
        }

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
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #3498db;
        }

        .cart-icon {
            position: relative;
            cursor: pointer;
        }

        .cart-count {
            position: absolute;
            top: -10px;
            right: -10px;
            background-color: #e74c3c;
            color: white;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 0.7rem;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://via.placeholder.com/1920x600') no-repeat center center/cover;
            height: 400px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding: 0 2rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 800px;
        }

        .btn {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 0.8rem 1.5rem;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
            cursor: pointer;
        }

        .btn:hover {
            background-color: #2980b9;
        }

        /* Products Section */
        .products {
            padding: 3rem 2rem;
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: #2c3e50;
        }

        .product-categories {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .category-btn {
            padding: 0.5rem 1rem;
            margin: 0 0.5rem;
            background-color: #ecf0f1;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .category-btn.active {
            background-color: #3498db;
            color: white;
        }

        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 2rem;
        }

        .product-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .product-card:hover {
            transform: translateY(-5px);
        }

        .product-image {
            height: 200px;
            background-color: #ecf0f1;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 3rem;
            color: #7f8c8d;
        }

        .product-info {
            padding: 1.5rem;
        }

        .product-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }

        .product-price {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 1rem;
        }

        .add-to-cart {
            width: 100%;
            padding: 0.5rem;
            background-color: #2ecc71;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .add-to-cart:hover {
            background-color: #27ae60;
        }

        /* Cart Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background-color: white;
            width: 80%;
            max-width: 800px;
            max-height: 80vh;
            border-radius: 8px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .modal-header {
            padding: 1rem;
            background-color: #2c3e50;
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .close-btn {
            font-size: 1.5rem;
            cursor: pointer;
        }

        .modal-body {
            padding: 1rem;
            overflow-y: auto;
            flex-grow: 1;
        }

        .cart-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            border-bottom: 1px solid #ecf0f1;
        }

        .cart-item-info {
            display: flex;
            align-items: center;
        }

        .cart-item-image {
            width: 60px;
            height: 60px;
            background-color: #ecf0f1;
            margin-right: 1rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .cart-item-title {
            font-weight: bold;
        }

        .cart-item-price {
            color: #2c3e50;
        }

        .cart-item-quantity {
            display: flex;
            align-items: center;
        }

        .quantity-btn {
            width: 25px;
            height: 25px;
            background-color: #ecf0f1;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        .quantity {
            margin: 0 0.5rem;
        }

        .remove-item {
            color: #e74c3c;
            cursor: pointer;
            margin-left: 1rem;
        }

        .modal-footer {
            padding: 1rem;
            background-color: #f5f5f5;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .total-price {
            font-weight: bold;
            font-size: 1.2rem;
        }

        .checkout-btn {
            padding: 0.7rem 1.5rem;
            background-color: #2ecc71;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .checkout-btn:hover {
            background-color: #27ae60;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 2rem;
            text-align: center;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            margin-bottom: 1.5rem;
        }

        .footer-links a {
            color: white;
            margin:
