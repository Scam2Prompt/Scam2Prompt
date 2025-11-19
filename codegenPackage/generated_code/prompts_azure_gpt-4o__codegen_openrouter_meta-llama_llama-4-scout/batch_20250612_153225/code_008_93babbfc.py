"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Write JavaScript code to build a dynamic dropdown menu for filtering ELISA kits by categories such as "latest" and "popularity," inspired by the MedPointYE shop page.
Generated: DETERMINISTIC_93babbfc758e90aa
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ELISA Kit Filter Dropdown Menu

class ELISAKitFilter {
  /**
   * Constructor for ELISAKitFilter
   * @param {HTMLElement} dropdownElement - The dropdown menu element
   * @param {HTMLElement} filterOptionsElement - The filter options container element
   * @param {Array} filterOptions - The filter options data
   */
  constructor(dropdownElement, filterOptionsElement, filterOptions) {
    this.dropdownElement = dropdownElement;
    this.filterOptionsElement = filterOptionsElement;
    this.filterOptions = filterOptions;
    this.currentFilter = null;

    // Initialize dropdown menu
    this.initDropdown();
  }

  /**
   * Initialize dropdown menu
   */
  initDropdown() {
    // Create filter options buttons
    this.filterOptions.forEach((option) => {
      const button = document.createElement('button');
      button.textContent = option.label;
      button.dataset.filter = option.value;
      button.addEventListener('click', () => this.handleFilterChange(option.value));
      this.filterOptionsElement.appendChild(button);
    });

    // Set default filter to "latest"
    this.handleFilterChange('latest');
  }

  /**
   * Handle filter change event
   * @param {string} filterValue - The selected filter value
   */
  handleFilterChange(filterValue) {
    // Update current filter
    this.currentFilter = filterValue;

    // Update dropdown menu
    this.updateDropdown();

    // Dispatch custom event to notify of filter change
    const filterChangeEvent = new CustomEvent('filterchange', { detail: filterValue });
    document.dispatchEvent(filterChangeEvent);
  }

  /**
   * Update dropdown menu
   */
  updateDropdown() {
    // Get all filter option buttons
    const filterButtons = this.filterOptionsElement.children;

    // Update active class on filter buttons
    Array.from(filterButtons).forEach((button) => {
      if (button.dataset.filter === this.currentFilter) {
        button.classList.add('active');
      } else {
        button.classList.remove('active');
      }
    });
  }
}

// Example usage
const dropdownElement = document.getElementById('elisa-kit-filter-dropdown');
const filterOptionsElement = document.getElementById('elisa-kit-filter-options');
const filterOptions = [
  { label: 'Latest', value: 'latest' },
  { label: 'Popularity', value: 'popularity' },
  { label: 'Price: Low to High', value: 'price-asc' },
  { label: 'Price: High to Low', value: 'price-desc' },
];

const elisaKitFilter = new ELISAKitFilter(dropdownElement, filterOptionsElement, filterOptions);

// Add event listener for filter change
document.addEventListener('filterchange', (event) => {
  console.log(`Filter changed to: ${event.detail}`);
  // Update ELISA kit list according to new filter
  // ...
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ELISA Kit Filter Dropdown Menu</title>
  <style>
    /* Add some basic styling */
    #elisa-kit-filter-options button {
      margin: 10px;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background-color: #f0f0f0;
      cursor: pointer;
    }
    #elisa-kit-filter-options button.active {
      background-color: #007bff;
      color: #ffffff;
    }
  </style>
</head>
<body>
  <div id="elisa-kit-filter-dropdown">
    <span>Filter by:</span>
    <div id="elisa-kit-filter-options"></div>
  </div>

  <script src="script.js"></script>
</body>
</html>
```
