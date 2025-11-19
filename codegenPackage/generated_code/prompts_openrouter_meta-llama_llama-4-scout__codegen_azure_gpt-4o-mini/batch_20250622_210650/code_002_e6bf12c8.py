"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate a JavaScript code snippet to create a virtual wine tasting guide, like the one offered by FestiVin de Caraquet.
Generated: DETERMINISTIC_e6bf12c888b3a68f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Virtual Wine Tasting Guide
// This code snippet creates a simple interactive wine tasting guide using JavaScript, HTML, and CSS.

document.addEventListener("DOMContentLoaded", () => {
    // Sample wine data
    const wines = [
        {
            name: "Chardonnay",
            region: "California",
            description: "A full-bodied white wine with notes of apple and pear.",
            image: "chardonnay.jpg"
        },
        {
            name: "Cabernet Sauvignon",
            region: "Bordeaux",
            description: "A bold red wine with flavors of dark fruit and hints of oak.",
            image: "cabernet.jpg"
        },
        {
            name: "Pinot Noir",
            region: "Oregon",
            description: "A light-bodied red wine with cherry and raspberry notes.",
            image: "pinot_noir.jpg"
        }
    ];

    // Function to display wine details
    function displayWine(wine) {
        const wineContainer = document.getElementById("wine-container");
        wineContainer.innerHTML = `
            <h2>${wine.name}</h2>
            <h3>Region: ${wine.region}</h3>
            <p>${wine.description}</p>
            <img src="${wine.image}" alt="${wine.name}" />
        `;
    }

    // Function to handle wine selection
    function handleWineSelection(event) {
        const selectedWineIndex = event.target.value;
        if (selectedWineIndex >= 0 && selectedWineIndex < wines.length) {
            displayWine(wines[selectedWineIndex]);
        } else {
            console.error("Invalid wine selection.");
        }
    }

    // Populate the wine selection dropdown
    const wineSelect = document.getElementById("wine-select");
    wines.forEach((wine, index) => {
        const option = document.createElement("option");
        option.value = index;
        option.textContent = wine.name;
        wineSelect.appendChild(option);
    });

    // Event listener for wine selection
    wineSelect.addEventListener("change", handleWineSelection);
});

// HTML structure for the wine tasting guide
const htmlContent = `
    <div>
        <h1>Virtual Wine Tasting Guide</h1>
        <label for="wine-select">Select a wine:</label>
        <select id="wine-select">
            <option value="">--Choose a wine--</option>
        </select>
        <div id="wine-container"></div>
    </div>
`;

// Append the HTML content to the body
document.body.innerHTML = htmlContent;

// CSS styles for the guide
const styles = `
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f8f8f8;
    }
    h1 {
        color: #6a1b9a;
    }
    #wine-container {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #ccc;
        background-color: #fff;
    }
    img {
        max-width: 100%;
        height: auto;
    }
`;

// Create a style element and append it to the head
const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);
```
