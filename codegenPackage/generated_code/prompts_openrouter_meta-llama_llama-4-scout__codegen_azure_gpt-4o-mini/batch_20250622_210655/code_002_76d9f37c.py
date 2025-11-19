"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Generate a JavaScript code snippet to create a dynamic pricing table for desert safari tour packages, including different activities like quad bike, buggy tour, and VIP services."
Generated: DETERMINISTIC_76d9f37c713ca9b4
Batch ID: 20250622_210655
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
    <title>Desert Safari Tour Packages</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .pricing-table {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .package {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            width: 30%;
            text-align: center;
        }
        .package h2 {
            margin: 0 0 10px;
        }
        .package p {
            margin: 5px 0;
        }
        .package button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .package button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

<h1>Desert Safari Tour Packages</h1>
<div class="pricing-table" id="pricingTable"></div>

<script>
    // Tour package data
    const packages = [
        {
            name: "Standard Package",
            price: 100,
            activities: ["Quad Bike", "Sandboarding"],
            vip: false
        },
        {
            name: "Adventure Package",
            price: 150,
            activities: ["Quad Bike", "Buggy Tour", "Sandboarding"],
            vip: false
        },
        {
            name: "VIP Package",
            price: 250,
            activities: ["Quad Bike", "Buggy Tour", "VIP Dinner", "Private Guide"],
            vip: true
        }
    ];

    // Function to create pricing table
    function createPricingTable() {
        const pricingTable = document.getElementById('pricingTable');

        // Check if pricingTable exists
        if (!pricingTable) {
            console.error("Pricing table element not found.");
            return;
        }

        // Loop through each package and create HTML elements
        packages.forEach(pkg => {
            const packageDiv = document.createElement('div');
            packageDiv.className = 'package';

            // Create package name
            const packageName = document.createElement('h2');
            packageName.textContent = pkg.name;
            packageDiv.appendChild(packageName);

            // Create package price
            const packagePrice = document.createElement('p');
            packagePrice.textContent = `Price: $${pkg.price}`;
            packageDiv.appendChild(packagePrice);

            // Create activities list
            const activitiesList = document.createElement('p');
            activitiesList.textContent = `Activities: ${pkg.activities.join(', ')}`;
            packageDiv.appendChild(activitiesList);

            // Create VIP services note if applicable
            if (pkg.vip) {
                const vipNote = document.createElement('p');
                vipNote.textContent = "Includes VIP services.";
                packageDiv.appendChild(vipNote);
            }

            // Create button to book the package
            const bookButton = document.createElement('button');
            bookButton.textContent = "Book Now";
            bookButton.onclick = () => bookPackage(pkg.name);
            packageDiv.appendChild(bookButton);

            // Append package to pricing table
            pricingTable.appendChild(packageDiv);
        });
    }

    // Function to handle package booking
    function bookPackage(packageName) {
        // Simulate booking process
        try {
            // Here you would typically send a request to your server
            console.log(`Booking ${packageName}...`);
            alert(`You have successfully booked the ${packageName}!`);
        } catch (error) {
            console.error("Error booking package:", error);
            alert("There was an error booking your package. Please try again.");
        }
    }

    // Initialize the pricing table on page load
    window.onload = createPricingTable;
</script>

</body>
</html>
```
