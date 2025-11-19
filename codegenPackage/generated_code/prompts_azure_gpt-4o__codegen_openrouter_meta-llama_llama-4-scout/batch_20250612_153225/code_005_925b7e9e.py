"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Create a function in JavaScript to dynamically display product categories such as "Offset Multi Colour Printers" and "House Keeping" on a webpage, with sorting and filtering options.
Generated: DETERMINISTIC_925b7e9ea1e1a73b
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// productCategories.js

/**
 * Product Category class to handle dynamic display, sorting, and filtering of product categories.
 */
class ProductCategory {
  /**
   * Constructor to initialize product categories.
   * @param {Array} categories - List of product categories.
   */
  constructor(categories) {
    this.categories = categories;
  }

  /**
   * Function to display product categories.
   * @param {string} containerId - ID of the container element to display categories.
   */
  displayCategories(containerId) {
    const container = document.getElementById(containerId);
    if (!container) {
      throw new Error(`Container element with ID ${containerId} not found.`);
    }

    // Create category list element
    const categoryList = document.createElement('ul');
    categoryList.id = 'category-list';

    // Add sorting and filtering options
    const sortingOptions = this.getSortingOptions();
    const filteringOptions = this.getFilteringOptions();

    // Create sorting select element
    const sortingSelect = document.createElement('select');
    sortingSelect.id = 'sorting-select';
    sortingOptions.forEach((option) => {
      const optionElement = document.createElement('option');
      optionElement.value = option.value;
      optionElement.text = option.text;
      sortingSelect.appendChild(optionElement);
    });

    // Create filtering select element
    const filteringSelect = document.createElement('select');
    filteringSelect.id = 'filtering-select';
    filteringOptions.forEach((option) => {
      const optionElement = document.createElement('option');
      optionElement.value = option.value;
      optionElement.text = option.text;
      filteringSelect.appendChild(optionElement);
    });

    // Add event listeners for sorting and filtering
    sortingSelect.addEventListener('change', () => {
      this.sortCategories(sortingSelect.value);
      this.renderCategories(categoryList);
    });

    filteringSelect.addEventListener('change', () => {
      this.filterCategories(filteringSelect.value);
      this.renderCategories(categoryList);
    });

    // Render initial categories
    this.renderCategories(categoryList);

    // Append elements to container
    container.appendChild(sortingSelect);
    container.appendChild(filteringSelect);
    container.appendChild(categoryList);
  }

  /**
   * Function to get sorting options.
   * @returns {Array} Sorting options.
   */
  getSortingOptions() {
    return [
      { value: 'alphabetical', text: 'Alphabetical' },
      { value: 'reverseAlphabetical', text: 'Reverse Alphabetical' },
    ];
  }

  /**
   * Function to get filtering options.
   * @returns {Array} Filtering options.
   */
  getFilteringOptions() {
    return [
      { value: 'all', text: 'All' },
      { value: 'printers', text: 'Printers' },
      { value: 'houseKeeping', text: 'House Keeping' },
    ];
  }

  /**
   * Function to render product categories.
   * @param {HTMLElement} categoryList - Category list element.
   */
  renderCategories(categoryList) {
    // Clear existing category list
    categoryList.innerHTML = '';

    // Create category list items
    this.categories.forEach((category) => {
      const categoryListItem = document.createElement('li');
      categoryListItem.textContent = category.name;
      categoryList.appendChild(categoryListItem);
    });
  }

  /**
   * Function to sort product categories.
   * @param {string} sortBy - Sorting option.
   */
  sortCategories(sortBy) {
    switch (sortBy) {
      case 'alphabetical':
        this.categories.sort((a, b) => a.name.localeCompare(b.name));
        break;
      case 'reverseAlphabetical':
        this.categories.sort((a, b) => b.name.localeCompare(a.name));
        break;
      default:
        throw new Error(`Invalid sorting option: ${sortBy}`);
    }
  }

  /**
   * Function to filter product categories.
   * @param {string} filterBy - Filtering option.
   */
  filterCategories(filterBy) {
    switch (filterBy) {
      case 'all':
        this.categories = this.originalCategories;
        break;
      case 'printers':
        this.categories = this.originalCategories.filter((category) => category.type === 'printers');
        break;
      case 'houseKeeping':
        this.categories = this.originalCategories.filter((category) => category.type === 'houseKeeping');
        break;
      default:
        throw new Error(`Invalid filtering option: ${filterBy}`);
    }
  }

  /**
   * Function to initialize product categories.
   */
  initCategories() {
    this.originalCategories = [
      { name: 'Offset Multi Colour Printers', type: 'printers' },
      { name: 'House Keeping', type: 'houseKeeping' },
      { name: 'Digital Printers', type: 'printers' },
      { name: 'Cleaning Supplies', type: 'houseKeeping' },
    ];

    this.categories = [...this.originalCategories];
  }
}

// Example usage
const productCategory = new ProductCategory([]);
productCategory.initCategories();
productCategory.displayCategories('product-categories');

// Example CSS for styling
// <style>
//   #category-list {
//     list-style: none;
//     padding: 0;
//     margin: 0;
//   }
//   #category-list li {
//     padding: 10px;
//     border-bottom: 1px solid #ccc;
//   }
// </style>

// Example HTML
// <div id="product-categories"></div>
```
