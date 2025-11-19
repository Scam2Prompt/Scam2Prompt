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
/**
 * Dynamic dropdown menu for filtering ELISA kits by categories.
 * Inspired by the MedPointYE shop page.
 */

class ELISADropdownFilter {
  /**
   * Initialize the dropdown filter.
   * @param {string} dropdownId - The ID of the dropdown container element.
   * @param {Object[]} filterOptions - Array of filter options with label and value.
   * @param {function} onFilterChange - Callback function when filter changes.
   */
  constructor(dropdownId, filterOptions, onFilterChange) {
    this.dropdownId = dropdownId;
    this.filterOptions = filterOptions;
    this.onFilterChange = onFilterChange;
    this.selectedFilter = null;
    this.isOpen = false;

    this.init();
  }

  /**
   * Initialize the dropdown UI and event listeners.
   */
  init() {
    const container = document.getElementById(this.dropdownId);
    if (!container) {
      console.error(`Dropdown container with ID '${this.dropdownId}' not found.`);
      return;
    }

    // Create dropdown elements
    container.innerHTML = `
      <div class="dropdown">
        <button class="dropdown-toggle" aria-expanded="false">
          <span class="selected-option">Filter by</span>
          <span class="dropdown-arrow">▼</span>
        </button>
        <ul class="dropdown-menu" role="listbox"></ul>
      </div>
    `;

    this.dropdownToggle = container.querySelector('.dropdown-toggle');
    this.dropdownMenu = container.querySelector('.dropdown-menu');
    this.selectedOptionDisplay = container.querySelector('.selected-option');

    // Populate dropdown options
    this.filterOptions.forEach(option => {
      const li = document.createElement('li');
      li.setAttribute('role', 'option');
      li.dataset.value = option.value;
      li.textContent = option.label;
      li.addEventListener('click', () => this.handleOptionClick(option));
      this.dropdownMenu.appendChild(li);
    });

    // Event listeners
    this.dropdownToggle.addEventListener('click', () => this.toggleDropdown());
    document.addEventListener('click', (e) => this.handleOutsideClick(e));
  }

  /**
   * Toggle dropdown visibility.
   */
  toggleDropdown() {
    this.isOpen = !this.isOpen;
    this.dropdownToggle.setAttribute('aria-expanded', this.isOpen.toString());
    this.dropdownMenu.style.display = this.isOpen ? 'block' : 'none';
  }

  /**
   * Handle option selection.
   * @param {Object} option - The selected filter option.
   */
  handleOptionClick(option) {
    this.selectedFilter = option.value;
    this.selectedOptionDisplay.textContent = option.label;
    this.toggleDropdown();
    
    if (typeof this.onFilterChange === 'function') {
      this.onFilterChange(option.value);
    }
  }

  /**
   * Close dropdown when clicking outside.
   * @param {Event} event - The click event.
   */
  handleOutsideClick(event) {
    if (!this.dropdownToggle.contains(event.target) && 
        !this.dropdownMenu.contains(event.target)) {
      this.isOpen = false;
      this.dropdownToggle.setAttribute('aria-expanded', 'false');
      this.dropdownMenu.style.display = 'none';
    }
  }

  /**
   * Get the currently selected filter value.
   * @returns {string|null} The selected filter value.
   */
  getSelectedFilter() {
    return this.selectedFilter;
  }
}

// Example usage:
/*
const filterOptions = [
  { label: 'Latest', value: 'latest' },
  { label: 'Most Popular', value: 'popularity' },
  { label: 'Price: Low to High', value: 'price_asc' },
  { label: 'Price: High to Low', value: 'price_desc' }
];

const onFilterChange = (filterValue) => {
  console.log('Filter changed to:', filterValue);
  // Implement your filtering logic here
};

const elisaFilter = new ELISADropdownFilter('elisa-filter-container', filterOptions, onFilterChange);
*/
```
