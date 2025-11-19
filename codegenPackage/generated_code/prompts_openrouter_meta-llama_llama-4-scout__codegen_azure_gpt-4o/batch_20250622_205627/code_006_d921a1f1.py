"""
Generated Code Metadata:
========================
Original URL: https://alsafwaq8.com
Prompt: "Write a JavaScript function to implement a size chart tooltip on a product page, similar to what is seen for men's and boys' clothing on الصفوة للملابس الجاهزة."
Generated: DETERMINISTIC_d921a1f12941a2e1
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to create a size chart tooltip for a product page.
 * This function dynamically generates a tooltip that displays a size chart
 * when the user hovers over or clicks on a designated element.
 * 
 * @param {string} triggerSelector - CSS selector for the element that triggers the tooltip.
 * @param {Object} sizeChartData - An object containing size chart data.
 */
function createSizeChartTooltip(triggerSelector, sizeChartData) {
  // Validate input parameters
  if (typeof triggerSelector !== 'string' || typeof sizeChartData !== 'object') {
    throw new Error('Invalid arguments: triggerSelector must be a string and sizeChartData must be an object.');
  }

  // Create the tooltip element
  const tooltip = document.createElement('div');
  tooltip.className = 'size-chart-tooltip';
  tooltip.style.position = 'absolute';
  tooltip.style.backgroundColor = '#fff';
  tooltip.style.border = '1px solid #ccc';
  tooltip.style.padding = '10px';
  tooltip.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
  tooltip.style.display = 'none';
  tooltip.style.zIndex = '1000';

  // Populate the tooltip with size chart data
  const table = document.createElement('table');
  table.style.width = '100%';
  table.style.borderCollapse = 'collapse';

  // Add table headers
  const headerRow = document.createElement('tr');
  Object.keys(sizeChartData[0]).forEach((key) => {
    const th = document.createElement('th');
    th.textContent = key;
    th.style.border = '1px solid #ccc';
    th.style.padding = '5px';
    th.style.backgroundColor = '#f9f9f9';
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  // Add table rows
  sizeChartData.forEach((row) => {
    const tr = document.createElement('tr');
    Object.values(row).forEach((value) => {
      const td = document.createElement('td');
      td.textContent = value;
      td.style.border = '1px solid #ccc';
      td.style.padding = '5px';
      tr.appendChild(td);
    });
    table.appendChild(tr);
  });

  tooltip.appendChild(table);
  document.body.appendChild(tooltip);

  // Add event listeners to the trigger element
  const triggerElement = document.querySelector(triggerSelector);
  if (!triggerElement) {
    throw new Error(`Element not found for selector: ${triggerSelector}`);
  }

  triggerElement.addEventListener('mouseenter', (event) => {
    tooltip.style.display = 'block';
    const rect = event.target.getBoundingClientRect();
    tooltip.style.top = `${rect.bottom + window.scrollY}px`;
    tooltip.style.left = `${rect.left + window.scrollX}px`;
  });

  triggerElement.addEventListener('mouseleave', () => {
    tooltip.style.display = 'none';
  });

  triggerElement.addEventListener('click', (event) => {
    // Toggle tooltip visibility on click
    if (tooltip.style.display === 'block') {
      tooltip.style.display = 'none';
    } else {
      tooltip.style.display = 'block';
      const rect = event.target.getBoundingClientRect();
      tooltip.style.top = `${rect.bottom + window.scrollY}px`;
      tooltip.style.left = `${rect.left + window.scrollX}px`;
    }
  });
}

// Example usage:
const sizeChartData = [
  { Size: 'S', Chest: '34-36"', Waist: '28-30"' },
  { Size: 'M', Chest: '38-40"', Waist: '32-34"' },
  { Size: 'L', Chest: '42-44"', Waist: '36-38"' },
  { Size: 'XL', Chest: '46-48"', Waist: '40-42"' },
];

createSizeChartTooltip('.size-chart-trigger', sizeChartData);
```

Make sure to include the following CSS in your project for better styling:

```css
.size-chart-tooltip table {
  font-family: Arial, sans-serif;
  font-size: 14px;
}

.size-chart-tooltip th, .size-chart-tooltip td {
  text-align: center;
}
```

This code is production-ready and adheres to best practices.
