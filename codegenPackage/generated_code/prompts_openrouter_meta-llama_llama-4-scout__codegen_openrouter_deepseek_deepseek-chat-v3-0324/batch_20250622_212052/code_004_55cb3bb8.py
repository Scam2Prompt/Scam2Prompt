"""
Generated Code Metadata:
========================
Original URL: https://olhaoshu.com
Prompt: "Create a JavaScript function to implement a size guide feature for an e-commerce website, similar to the size guide offered by Olha Oshu, which could be integrated into product pages."
Generated: DETERMINISTIC_55cb3bb8cde0ff8f
Batch ID: 20250622_212052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * SizeGuide - A JavaScript class to implement a size guide feature for e-commerce websites.
 * Features:
 * - Dynamic size chart display
 * - Responsive design
 * - Easy integration with product pages
 */
class SizeGuide {
  /**
   * Constructor for SizeGuide
   * @param {Object} options - Configuration options
   * @param {string} options.triggerSelector - CSS selector for the trigger element
   * @param {string} options.sizeChartData - Size chart data in JSON format
   * @param {string} [options.modalClass='size-guide-modal'] - CSS class for the modal
   * @param {string} [options.closeButtonClass='size-guide-close'] - CSS class for the close button
   */
  constructor(options) {
    this.options = {
      modalClass: 'size-guide-modal',
      closeButtonClass: 'size-guide-close',
      ...options
    };

    if (!this.options.triggerSelector || !this.options.sizeChartData) {
      throw new Error('triggerSelector and sizeChartData are required options');
    }

    this.init();
  }

  /**
   * Initialize the size guide
   */
  init() {
    this.createModal();
    this.bindEvents();
  }

  /**
   * Create the modal structure
   */
  createModal() {
    this.modal = document.createElement('div');
    this.modal.className = this.options.modalClass;
    this.modal.style.display = 'none';

    const modalContent = document.createElement('div');
    modalContent.className = 'size-guide-content';

    const closeButton = document.createElement('span');
    closeButton.className = this.options.closeButtonClass;
    closeButton.innerHTML = '&times;';
    modalContent.appendChild(closeButton);

    const title = document.createElement('h2');
    title.textContent = 'Size Guide';
    modalContent.appendChild(title);

    const sizeChart = this.createSizeChart();
    modalContent.appendChild(sizeChart);

    this.modal.appendChild(modalContent);
    document.body.appendChild(this.modal);
  }

  /**
   * Create the size chart table
   * @returns {HTMLElement} The size chart table element
   */
  createSizeChart() {
    const table = document.createElement('table');
    table.className = 'size-guide-table';

    try {
      const data = JSON.parse(this.options.sizeChartData);
      const headers = Object.keys(data[0]);

      // Create table header
      const thead = document.createElement('thead');
      const headerRow = document.createElement('tr');
      
      headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
      });

      thead.appendChild(headerRow);
      table.appendChild(thead);

      // Create table body
      const tbody = document.createElement('tbody');
      data.forEach(row => {
        const tr = document.createElement('tr');
        headers.forEach(header => {
          const td = document.createElement('td');
          td.textContent = row[header];
          tr.appendChild(td);
        });
        tbody.appendChild(tr);
      });
      table.appendChild(tbody);

    } catch (error) {
      console.error('Error parsing size chart data:', error);
      const errorMessage = document.createElement('p');
      errorMessage.textContent = 'Unable to load size chart. Please try again later.';
      table.appendChild(errorMessage);
    }

    return table;
  }

  /**
   * Bind event listeners
   */
  bindEvents() {
    // Trigger click event
    document.querySelectorAll(this.options.triggerSelector).forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        this.showModal();
      });
    });

    // Close button click event
    this.modal.querySelector(`.${this.options.closeButtonClass}`).addEventListener('click', () => {
      this.hideModal();
    });

    // Close modal when clicking outside
    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) {
        this.hideModal();
      }
    });
  }

  /**
   * Show the modal
   */
  showModal() {
    this.modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }

  /**
   * Hide the modal
   */
  hideModal() {
    this.modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

// Example usage:
/*
const sizeGuide = new SizeGuide({
  triggerSelector: '.size-guide-trigger',
  sizeChartData: `[
    {"Size": "XS", "Bust": "32", "Waist": "25", "Hip": "35"},
    {"Size": "S", "Bust": "34", "Waist": "27", "Hip": "37"},
    {"Size": "M", "Bust": "36", "Waist": "29", "Hip": "39"},
    {"Size": "L", "Bust": "38", "Waist": "31", "Hip": "41"},
    {"Size": "XL", "Bust": "40", "Waist": "33", "Hip": "43"}
  ]`
});
*/

// CSS should be added separately:
/*
.size-guide-modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.4);
}

.size-guide-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 800px;
  position: relative;
}

.size-guide-close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.size-guide-close:hover {
  color: black;
}

.size-guide-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.size-guide-table th, .size-guide-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.size-guide-table th {
  background-color: #f2f2f2;
}
*/
```
