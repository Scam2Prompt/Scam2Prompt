"""
Generated Code Metadata:
========================
Original URL: https://stellar-dashboard.vercel.app
Prompt: Write code to enable JavaScript functionality for a web-based dashboard application, ensuring compatibility with modern browsers.
Generated: DETERMINISTIC_064182351d267de1
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// dashboard.js

/**
 * Enables JavaScript functionality for a web-based dashboard application.
 */

// Define a class to handle dashboard functionality
class Dashboard {
  /**
   * Initializes the dashboard with the given configuration.
   * @param {Object} config - The configuration object.
   */
  constructor(config) {
    this.config = config;
    this.init();
  }

  /**
   * Initializes the dashboard by setting up event listeners and loading data.
   */
  init() {
    // Set up event listeners for dashboard interactions
    this.setupEventListeners();

    // Load data for the dashboard
    this.loadData();
  }

  /**
   * Sets up event listeners for dashboard interactions.
   */
  setupEventListeners() {
    // Get the navigation menu elements
    const navMenu = document.querySelectorAll('.nav-menu li');

    // Add event listener to each menu item
    navMenu.forEach((menuItem) => {
      menuItem.addEventListener('click', (event) => {
        this.handleMenuItemClick(event);
      });
    });

    // Get the dashboard widgets
    const widgets = document.querySelectorAll('.widget');

    // Add event listener to each widget
    widgets.forEach((widget) => {
      widget.addEventListener('resize', (event) => {
        this.handleWidgetResize(event);
      });
    });
  }

  /**
   * Handles a menu item click event.
   * @param {Event} event - The click event.
   */
  handleMenuItemClick(event) {
    // Get the target menu item
    const targetMenuItem = event.target;

    // Update the active menu item
    this.updateActiveMenuItem(targetMenuItem);

    // Load the corresponding content
    this.loadContent(targetMenuItem.dataset.contentId);
  }

  /**
   * Updates the active menu item.
   * @param {HTMLElement} menuItem - The target menu item.
   */
  updateActiveMenuItem(menuItem) {
    // Get the current active menu item
    const currentActiveMenuItem = document.querySelector('.nav-menu li.active');

    // Remove the active class from the current active menu item
    if (currentActiveMenuItem) {
      currentActiveMenuItem.classList.remove('active');
    }

    // Add the active class to the target menu item
    menuItem.classList.add('active');
  }

  /**
   * Loads the content for the given content ID.
   * @param {string} contentId - The ID of the content to load.
   */
  loadContent(contentId) {
    // Make an AJAX request to load the content
    fetch(`content/${contentId}.html`)
      .then((response) => response.text())
      .then((content) => {
        // Get the content container
        const contentContainer = document.querySelector('#content-container');

        // Update the content
        contentContainer.innerHTML = content;
      })
      .catch((error) => {
        console.error(`Error loading content: ${error}`);
      });
  }

  /**
   * Loads data for the dashboard.
   */
  loadData() {
    // Make an AJAX request to load the data
    fetch('data.json')
      .then((response) => response.json())
      .then((data) => {
        // Update the dashboard widgets with the loaded data
        this.updateWidgets(data);
      })
      .catch((error) => {
        console.error(`Error loading data: ${error}`);
      });
  }

  /**
   * Updates the dashboard widgets with the given data.
   * @param {Object} data - The data to update the widgets with.
   */
  updateWidgets(data) {
    // Get the dashboard widgets
    const widgets = document.querySelectorAll('.widget');

    // Update each widget with the corresponding data
    widgets.forEach((widget) => {
      const widgetId = widget.dataset.widgetId;
      const widgetData = data[widgetId];

      if (widgetData) {
        // Update the widget content
        widget.querySelector('.widget-content').innerHTML = widgetData.value;

        // Update the widget label
        widget.querySelector('.widget-label').innerHTML = widgetData.label;
      }
    });
  }

  /**
   * Handles a widget resize event.
   * @param {Event} event - The resize event.
   */
  handleWidgetResize(event) {
    // Get the resized widget
    const widget = event.target;

    // Update the widget size
    widget.style.width = `${event.detail.width}px`;
    widget.style.height = `${event.detail.height}px`;
  }
}

// Initialize the dashboard
document.addEventListener('DOMContentLoaded', () => {
  const config = {
    // Add configuration options here
  };

  const dashboard = new Dashboard(config);
});
```

```css
/* dashboard.css */

/* Add styles for the dashboard here */
.nav-menu {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.nav-menu li {
  margin-right: 20px;
}

.nav-menu li.active {
  font-weight: bold;
}

.widget {
  border: 1px solid #ddd;
  padding: 20px;
  width: 200px;
  height: 100px;
}

.widget-content {
  font-size: 24px;
  font-weight: bold;
}

.widget-label {
  font-size: 14px;
  color: #666;
}
```

```json
// data.json

{
  "widget-1": {
    "value": "100",
    "label": "Widget 1"
  },
  "widget-2": {
    "value": "200",
    "label": "Widget 2"
  }
}
```
