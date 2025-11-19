"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: Generate a code snippet to create a real estate listing page that includes features like "Prodaja stanova" and "Izdavanje" for properties in Podgorica.
Generated: DETERMINISTIC_1db86c66a3101805
Batch ID: 20250612_160013
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
    <title>Real Estate Listings - Podgorica</title>
    <style>
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        header {
            background-color: #007bff;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 1rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .tab {
            padding: 1rem 2rem;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            border-radius: 4px;
            margin: 0 0.5rem;
            transition: background-color 0.3s ease;
        }

        .tab:hover {
            background-color: #0056b3;
        }

        .tab.active {
            background-color: #0056b3;
        }

        .listing {
            display: none;
        }

        .listing.active {
            display: block;
        }

        .property {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .property h3 {
            margin: 0;
            color: #007bff;
        }

        .property p {
            margin: 0.5rem 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Real Estate Listings in Podgorica</h1>
    </header>
    <div class="container">
        <!-- Tabs for switching between "Prodaja stanova" and "Izdavanje" -->
        <div class="tabs">
            <div class="tab active" data-target="prodaja">Prodaja stanova</div>
            <div class="tab" data-target="izdavanje">Izdavanje</div>
        </div>

        <!-- Listings for "Prodaja stanova" -->
        <div id="prodaja" class="listing active">
            <div class="property">
                <h3>Stan na prodaju - Centar</h3>
                <p>Cijena: 120,000 EUR</p>
                <p>Opis: Stan u centru Podgorice, 80m², 2 spavaće sobe.</p>
            </div>
            <div class="property">
                <h3>Stan na prodaju - Preko Morače</h3>
                <p>Cijena: 150,000 EUR</p>
                <p>Opis: Luksuzan stan, 100m², 3 spavaće sobe.</p>
            </div>
        </div>

        <!-- Listings for "Izdavanje" -->
        <div id="izdavanje" class="listing">
            <div class="property">
                <h3>Stan za izdavanje - City kvart</h3>
                <p>Cijena: 500 EUR/mjesečno</p>
                <p>Opis: Moderno opremljen stan, 60m², 1 spavaća soba.</p>
            </div>
            <div class="property">
                <h3>Stan za izdavanje - Stari Aerodrom</h3>
                <p>Cijena: 400 EUR/mjesečno</p>
                <p>Opis: Stan sa terasom, 70m², 2 spavaće sobe.</p>
            </div>
        </div>
    </div>

    <script>
        // JavaScript to handle tab switching
        document.addEventListener('DOMContentLoaded', () => {
            const tabs = document.querySelectorAll('.tab');
            const listings = document.querySelectorAll('.listing');

            tabs.forEach(tab => {
                tab.addEventListener('click', () => {
                    // Remove active class from all tabs
                    tabs.forEach(t => t.classList.remove('active'));
                    // Add active class to the clicked tab
                    tab.classList.add('active');

                    // Hide all listings
                    listings.forEach(listing => listing.classList.remove('active'));
                    // Show the listing corresponding to the clicked tab
                    const target = tab.getAttribute('data-target');
                    document.getElementById(target).classList.add('active');
                });
            });
        });
    </script>
</body>
</html>
```
