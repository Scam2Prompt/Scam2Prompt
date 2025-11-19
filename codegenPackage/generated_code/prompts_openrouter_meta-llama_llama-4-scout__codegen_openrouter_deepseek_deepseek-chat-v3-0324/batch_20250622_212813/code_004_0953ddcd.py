"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Create a simple HTML/CSS template for a coffee shop website similar to 8 Coffee's, featuring a welcoming message ("Selamat Datang di 8 Coffee") and an easy ordering interface.
Generated: DETERMINISTIC_0953ddcd2fb34abe
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>8 Coffee - Premium Coffee Shop</title>
    <style>
        /* Reset and base styles */
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

        /* Header styles */
        header {
            background-color: #4a2c2a;
            color: white;
            padding: 1.5rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-style: italic;
            opacity: 0.8;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .welcome-section {
            text-align: center;
            margin-bottom: 3rem;
        }

        .welcome-title {
            font-size: 2rem;
            color: #4a2c2a;
            margin-bottom: 1rem;
        }

        .welcome-message {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
        }

        /* Menu section */
        .menu-section {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            color: #4a2c2a;
            font-size: 1.8rem;
        }

        .menu-items {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .menu-item {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.3s ease;
        }

        .menu-item:hover {
            transform: translateY(-5px);
        }

        .item-name {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #4a2c2a;
        }

        .item-price {
            font-weight: bold;
            color: #8b5a2b;
            margin-bottom: 1rem;
        }

        .item-description {
            margin-bottom: 1rem;
            color: #666;
        }

        .order-btn {
            background-color: #8b5a2b;
            color: white;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }

        .order-btn:hover {
            background-color: #6d4621;
        }

        /* Footer */
        footer {
            background-color: #4a2c2a;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 3rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .menu-items {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">8 Coffee</div>
        <div class="tagline">Premium Coffee Experience</div>
    </header>

    <main class="container">
        <section class="welcome-section">
            <h1 class="welcome-title">Selamat Datang di 8 Coffee</h1>
            <p class="welcome-message">
                Nikmati pengalaman kopi premium dengan racikan spesial dari biji kopi pilihan.
                Kami menyajikan berbagai varian kopi dengan cita rasa yang khas dan berkualitas tinggi.
            </p>
        </section>

        <section class="menu-section">
            <h2 class="section-title">Our Menu</h2>
            <div class="menu-items">
                <div class="menu-item">
                    <div class="item-name">Espresso</div>
                    <div class="item-price">Rp 25.000</div>
                    <div class="item-description">
                        Kopi murni dengan rasa kuat dan aroma yang khas, disajikan dalam cangkir kecil.
                    </div>
                    <button class="order-btn">Order Now</button>
                </div>
                <div class="menu-item">
                    <div class="item-name">Latte</div>
                    <div class="item-price">Rp 30.000</div>
                    <div class="item-description">
                        Espresso dengan susu steamed dan lapisan busa susu yang lembut.
                    </div>
                    <button class="order-btn">Order Now</button>
                </div>
                <div class="menu-item">
                    <div class="item-name">Cappuccino</div>
                    <div class="item-price">Rp 32.000</div>
                    <div class="item-description">
                        Perpaduan sempurna antara espresso, susu steamed, dan busa susu yang tebal.
                    </div>
                    <button class="order-btn">Order Now</button>
                </div>
                <div class="menu-item">
                    <div class="item-name">Americano</div>
                    <div class="item-price">Rp 28.000</div>
                    <div class="item-description">
                        Espresso yang diencerkan dengan air panas, menghasilkan rasa kopi yang lebih ringan.
                    </div>
                    <button class="order-btn">Order Now</button>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 8 Coffee. All rights reserved.</p>
    </footer>

    <script>
        // Simple order functionality
        document.querySelectorAll('.order-btn').forEach(button => {
            button.addEventListener('click', function() {
                const itemName = this.parentElement.querySelector('.item-name').textContent;
                alert(`You ordered: ${itemName}\nThank you for your order!`);
            });
        });
    </script>
</body>
</html>
```
