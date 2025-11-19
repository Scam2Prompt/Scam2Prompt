"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bernwears.com
Prompt: How can I build a user interface for a clothing customization tool that allows customers to select fabrics and designs, similar to the services offered by Bern Wears?
Generated: DETERMINISTIC_40c878ed8107d9f5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready code snippet for building a web-based user interface using HTML, CSS, and JavaScript. This example assumes you are using modern web development practices and includes comments for clarity. It is modular and can be adapted for integration into a larger application.

---

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clothing Customization Tool</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="header">
    <h1>Customize Your Clothing</h1>
    <p>Select fabrics and designs to create your perfect outfit</p>
  </header>

  <main>
    <section class="fabric-section">
      <h2>Select Fabric</h2>
      <div id="fabric-options" class="options"></div>
    </section>

    <section class="design-section">
      <h2>Select Design</h2>
      <div id="design-options" class="options"></div>
    </section>

    <button id="submit-customization" class="submit-btn">Submit Customization</button>
  </main>

  <footer class="footer">
    <p>© 2023 Custom Clothing Inc.</p>
  </footer>

  <script src="app.js"></script>
</body>
</html>
```

---

### `styles.css`
```css
/* General styles for the page */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

.header {
  text-align: center;
  background-color: #333;
  color: #fff;
  padding: 20px;
}

main {
  padding: 20px;
}

h2 {
  margin-bottom: 10px;
}

.options {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.option {
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #fff;
  cursor: pointer;
  text-align: center;
  width: 150px;
}

.option:hover {
  background-color: #f0f0f0;
}

.option.selected {
  border-color: #007bff;
  background-color: #cce4ff;
}

.submit-btn {
  display: block;
  margin: 20px auto;
  padding: 10px 15px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

.submit-btn:hover {
  background-color: #0056b3;
}

.footer {
  text-align: center;
  padding: 10px;
  background-color: #333;
  color: #fff;
}
```

---

### `app.js`
```javascript
// Mock data for fabrics and designs
const fabricOptions = [
  { id: 1, name: "Cotton" },
  { id: 2, name: "Silk" },
  { id: 3, name: "Denim" },
  { id: 4, name: "Wool" },
  { id: 5, name: "Linen" },
];

const designOptions = [
  { id: 1, name: "Casual Shirt" },
  { id: 2, name: "Formal Suit" },
  { id: 3, name: "Evening Dress" },
  { id: 4, name: "T-Shirt" },
  { id: 5, name: "Jacket" },
];

// DOM references
const fabricContainer = document.getElementById("fabric-options");
const designContainer = document.getElementById("design-options");
const submitButton = document.getElementById("submit-customization");

// State variables
let selectedFabric = null;
let selectedDesign = null;

// Utility function to create option buttons
function createOptionElement(option, container, onSelectCallback) {
  const element = document.createElement("div");
  element.className = "option";
  element.textContent = option.name;

  element.addEventListener("click", () => {
    // Clear previous selection within the container
    Array.from(container.children).forEach((child) =>
      child.classList.remove("selected")
    );
    element.classList.add("selected");

    onSelectCallback(option);
  });

  container.appendChild(element);
}

// Populate fabric and design options
function populateOptions() {
  fabricOptions.forEach((fabric) =>
    createOptionElement(fabric, fabricContainer, (selected) => {
      selectedFabric = selected;
    })
  );

  designOptions.forEach((design) =>
    createOptionElement(design, designContainer, (selected) => {
      selectedDesign = selected;
    })
  );
}

// Handle form submission
function handleSubmit() {
  if (!selectedFabric || !selectedDesign) {
    alert("Please select both a fabric and a design.");
    return;
  }

  // In production, send this data to the server
  console.log("Customization Submitted:", {
    fabric: selectedFabric.name,
    design: selectedDesign.name,
  });

  alert(
    `You have customized your clothing with:\nFabric: ${selectedFabric.name}\nDesign: ${selectedDesign.name}`
  );
}

// Initialize the app
function initializeApp() {
  populateOptions();
  submitButton.addEventListener("click", handleSubmit);
}

// Run the app
initializeApp();
```

---

This code provides a functional, client-side interface for clothing customization. You can extend it by integrating with a backend API for saving customer choices or fetching options from a server.
