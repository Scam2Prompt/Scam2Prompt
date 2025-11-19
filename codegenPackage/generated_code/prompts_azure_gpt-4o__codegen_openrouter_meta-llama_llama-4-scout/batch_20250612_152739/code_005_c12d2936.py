"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Write JavaScript code to create an interactive portfolio section for a website, showcasing "Projects," "Clients," and "Cooperations," as seen on dionlineaja.id.
Generated: DETERMINISTIC_c12d2936c07de810
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// portfolio.js

class PortfolioSection {
  /**
   * Initialize the portfolio section.
   * @param {HTMLElement} container - The container element for the portfolio section.
   */
  constructor(container) {
    this.container = container;
    this.tabs = ['projects', 'clients', 'cooperations'];
    this.activeTab = 'projects';

    // Initialize the tab buttons and content.
    this.initTabs();
    this.initContent();
  }

  /**
   * Initialize the tab buttons.
   */
  initTabs() {
    const tabButtonsContainer = document.createElement('div');
    tabButtonsContainer.classList.add('tab-buttons');

    this.tabs.forEach((tab) => {
      const button = document.createElement('button');
      button.textContent = tab.charAt(0).toUpperCase() + tab.slice(1);
      button.dataset.tab = tab;

      // Add event listener for tab button click.
      button.addEventListener('click', () => this.handleTabClick(tab));

      tabButtonsContainer.appendChild(button);
    });

    this.container.appendChild(tabButtonsContainer);
  }

  /**
   * Initialize the content for each tab.
   */
  initContent() {
    const contentContainer = document.createElement('div');
    contentContainer.classList.add('tab-content');

    this.tabs.forEach((tab) => {
      const content = document.createElement('div');
      content.classList.add('tab-pane');
      content.dataset.tab = tab;

      // Sample content for demonstration purposes.
      content.innerHTML = `
        <h2>${tab.charAt(0).toUpperCase() + tab.slice(1)}</h2>
        <p>This is the content for ${tab}.</p>
      `;

      contentContainer.appendChild(content);
    });

    this.container.appendChild(contentContainer);

    // Hide all content except the active tab.
    this.hideContent();
    this.showContent(this.activeTab);
  }

  /**
   * Handle tab button click event.
   * @param {string} tab - The tab that was clicked.
   */
  handleTabClick(tab) {
    if (this.activeTab === tab) return;

    this.hideContent();
    this.showContent(tab);
    this.activeTab = tab;
  }

  /**
   * Hide all tab content.
   */
  hideContent() {
    const contentPanes = this.container.querySelectorAll('.tab-pane');
    contentPanes.forEach((pane) => pane.classList.remove('active'));
  }

  /**
   * Show the content for a specific tab.
   * @param {string} tab - The tab to show.
   */
  showContent(tab) {
    const contentPane = this.container.querySelector(`.tab-pane[data-tab="${tab}"]`);
    contentPane.classList.add('active');

    // Update tab buttons.
    const tabButtons = this.container.querySelectorAll('.tab-buttons button');
    tabButtons.forEach((button) => {
      if (button.dataset.tab === tab) {
        button.classList.add('active');
      } else {
        button.classList.remove('active');
      }
    });
  }
}

// Initialize the portfolio section.
document.addEventListener('DOMContentLoaded', () => {
  const portfolioContainer = document.getElementById('portfolio');
  if (portfolioContainer) {
    new PortfolioSection(portfolioContainer);
  } else {
    console.error('Portfolio container not found.');
  }
});
```

```css
/* styles.css */

#portfolio {
  max-width: 800px;
  margin: 40px auto;
}

.tab-buttons {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.tab-buttons button {
  background-color: #f0f0f0;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
}

.tab-buttons button.active {
  background-color: #007bff;
  color: #ffffff;
}

.tab-content {
  padding: 20px;
}

.tab-pane {
  display: none;
}

.tab-pane.active {
  display: block;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Portfolio Section</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="portfolio"></div>
  <script src="portfolio.js"></script>
</body>
</html>
```
