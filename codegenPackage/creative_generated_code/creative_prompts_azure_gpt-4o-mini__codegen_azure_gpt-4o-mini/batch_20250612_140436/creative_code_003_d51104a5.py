"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Create a JavaScript function that dynamically displays different wedding photography packages based on user selection, similar to the options available at Yaisa Tangwell Photography.
Generated: DETERMINISTIC_d51104a5f04fed3b
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Photography Packages</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .package {
            margin: 15px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h1>Wedding Photography Packages</h1>
    <label for="packageSelect">Choose a package:</label>
    <select id="packageSelect">
        <option value="">Select a package</option>
        <option value="basic">Basic Package</option>
        <option value="premium">Premium Package</option>
        <option value="deluxe">Deluxe Package</option>
    </select>

    <div id="packageDetails"></div>

    <script>
        // Function to display the selected photography package details
        function displayPackageDetails() {
            const packageSelect = document.getElementById("packageSelect");
            const packageDetails = document.getElementById("packageDetails");

            // Clear previous package details
            packageDetails.innerHTML = '';

            // Get the selected value
            const selectedPackage = packageSelect.value;

            // Package details
            const packages = {
                basic: {
                    title: "Basic Package",
                    description: "Includes 4 hours of coverage, 100 edited photos, and an online gallery.",
                    price: "$800"
                },
                premium: {
                    title: "Premium Package",
                    description: "Includes 8 hours of coverage, 300 edited photos, and a custom photo book.",
                    price: "$1500"
                },
                deluxe: {
                    title: "Deluxe Package",
                    description: "Includes full-day coverage, 500 edited photos, and a pre-wedding shoot.",
                    price: "$2500"
                }
            };

            // Check if the selected package has details
            if (packages[selectedPackage]) {
                const package = packages[selectedPackage];
                // Create and append package details to the DOM
                const packageDiv = document.createElement("div");
                packageDiv.classList.add("package");
                packageDiv.innerHTML = `
                    <h2>${package.title}</h2>
                    <p>${package.description}</p>
                    <p><strong>Price: ${package.price}</strong></p>
                `;
                packageDetails.appendChild(packageDiv);
            } else {
                // User hasn't selected a valid package
                packageDetails.innerHTML = '<p>Please select a package to see the details.</p>';
            }
        }

        // Add event listener to the select element
        document.getElementById("packageSelect").addEventListener("change", displayPackageDetails);
    </script>

</body>
</html>
```
