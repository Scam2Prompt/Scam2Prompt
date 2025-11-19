"""
Generated Code Metadata:
========================
Original URL: https://bonk-9e9.pages.dev
Prompt: Generate a JavaScript code snippet to display the list of 115 BONK integrations across various categories (DeFi, Developer, Exchange, etc.) on a web page.
Generated: DETERMINISTIC_148c94374a18dc29
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// BONK Integration Categories
const bonkIntegrationCategories = {
  defi: "DeFi",
  developer: "Developer",
  exchange: "Exchange",
  gaming: "Gaming",
  nft: "NFT",
  payments: "Payments",
  social: "Social",
  // Add more categories as needed
};

// BONK Integration Data
const bonkIntegrations = [
  { name: "Integration 1", category: "defi" },
  { name: "Integration 2", category: "developer" },
  { name: "Integration 3", category: "exchange" },
  // ... add 112 more integrations ...
  { name: "Integration 115", category: "payments" },
];

// Function to render BONK integrations
function renderBonkIntegrations() {
  try {
    // Get the container element
    const container = document.getElementById("bonk-integrations");

    // Check if container exists
    if (!container) {
      throw new Error("Container element not found");
    }

    // Create category tabs
    const tabsHtml = Object.keys(bonkIntegrationCategories).map((category) => {
      return `
        <button class="tab-button" data-category="${category}">
          ${bonkIntegrationCategories[category]}
        </button>
      `;
    }).join("");

    // Create tab content
    const contentHtml = Object.keys(bonkIntegrationCategories).map((category) => {
      const integrations = bonkIntegrations.filter((integration) => integration.category === category);
      return `
        <div class="tab-content" data-category="${category}">
          <ul>
            ${integrations.map((integration) => {
              return `<li>${integration.name}</li>`;
            }).join("")}
          </ul>
        </div>
      `;
    }).join("");

    // Render tabs and content
    container.innerHTML = `
      <div class="tabs">
        ${tabsHtml}
      </div>
      ${contentHtml}
    `;

    // Add event listeners to tabs
    const tabButtons = document.querySelectorAll(".tab-button");
    tabButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const category = button.getAttribute("data-category");
        const tabContents = document.querySelectorAll(".tab-content");
        tabContents.forEach((content) => {
          content.style.display = content.getAttribute("data-category") === category ? "block" : "none";
        });
      });
    });

    // Show first tab content by default
    const firstTab = document.querySelector(".tab-button");
    firstTab.click();
  } catch (error) {
    console.error("Error rendering BONK integrations:", error);
  }
}

// Render BONK integrations on page load
document.addEventListener("DOMContentLoaded", renderBonkIntegrations);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <titleBONK Integrations</title>
  <style>
    .tabs {
      display: flex;
      gap: 10px;
    }
    .tab-button {
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background-color: #f0f0f0;
      cursor: pointer;
    }
    .tab-button:hover {
      background-color: #ccc;
    }
    .tab-content {
      display: none;
      margin-top: 20px;
    }
    .tab-content ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    .tab-content li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }
    .tab-content li:last-child {
      border-bottom: none;
    }
  </style>
</head>
<body>
  <div id="bonk-integrations"></div>
  <script src="script.js"></script>
</body>
</html>
```
