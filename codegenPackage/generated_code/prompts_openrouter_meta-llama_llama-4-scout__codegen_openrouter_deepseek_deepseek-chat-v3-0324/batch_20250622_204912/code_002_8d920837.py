"""
Generated Code Metadata:
========================
Original URL: https://thegraphicdesigner.link
Prompt: "Write a code snippet for a basic online store using HTML and CSS that lists graphic design services and allows item removal."
Generated: DETERMINISTIC_8d92083766e7cdd8
Batch ID: 20250622_204912
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
    <title>Graphic Design Services Store</title>
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

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5rem;
        }

        .services-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .service-item {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 20px;
            transition: transform 0.3s ease;
        }

        .service-item:hover {
            transform: translateY(-5px);
        }

        .service-item h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .service-item p {
            color: #666;
            margin-bottom: 15px;
        }

        .price {
            font-weight: bold;
            color: #e74c3c;
            font-size: 1.2rem;
            margin-bottom: 15px;
        }

        .remove-btn {
            background-color: #e74c3c;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .remove-btn:hover {
            background-color: #c0392b;
        }

        .empty-message {
            text-align: center;
            padding: 20px;
            color: #666;
            font-style: italic;
        }

        @media (max-width: 768px) {
            .services-list {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Graphic Design Services</h1>
        </div>
    </header>

    <div class="container">
        <div class="services-list" id="servicesContainer">
            <!-- Service items will be dynamically added here -->
            <div class="service-item">
                <h3>Logo Design</h3>
                <p>Professional logo creation with 3 initial concepts and unlimited revisions.</p>
                <div class="price">$199</div>
                <button class="remove-btn" onclick="removeService(this)">Remove</button>
            </div>
            <div class="service-item">
                <h3>Brand Identity</h3>
                <p>Complete brand package including colors, typography, and style guide.</p>
                <div class="price">$499</div>
                <button class="remove-btn" onclick="removeService(this)">Remove</button>
            </div>
            <div class="service-item">
                <h3>Social Media Kit</h3>
                <p>Custom templates for all major social platforms with matching aesthetic.</p>
                <div class="price">$299</div>
                <button class="remove-btn" onclick="removeService(this)">Remove</button>
            </div>
            <div class="service-item">
                <h3>Print Design</h3>
                <p>Business cards, letterheads, and other printed materials design.</p>
                <div class="price">$249</div>
                <button class="remove-btn" onclick="removeService(this)">Remove</button>
            </div>
            <div class="service-item">
                <h3>Web Graphics</h3>
                <p>Custom banners, icons, and other web elements for your site.</p>
                <div class="price">$349</div>
                <button class="remove-btn" onclick="removeService(this)">Remove</button>
            </div>
        </div>
    </div>

    <script>
        function removeService(button) {
            const serviceItem = button.parentElement;
            const servicesContainer = document.getElementById('servicesContainer');
            
            serviceItem.classList.add('fade-out');
            setTimeout(() => {
                serviceItem.remove();
                
                // Check if all items are removed
                if (servicesContainer.children.length === 0) {
                    const emptyMessage = document.createElement('div');
                    emptyMessage.className = 'empty-message';
                    emptyMessage.textContent = 'No services available.';
                    servicesContainer.appendChild(emptyMessage);
                }
            }, 300);
        }
    </script>
</body>
</html>
```
