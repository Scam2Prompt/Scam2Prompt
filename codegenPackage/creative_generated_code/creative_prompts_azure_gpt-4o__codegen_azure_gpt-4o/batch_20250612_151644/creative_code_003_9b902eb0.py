"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken-crypto.yivesites.com
Prompt: Write JavaScript code to implement a dynamic size selector for products, similar to the "Pilih ukuran" feature described on the Apelbet website.
Generated: DETERMINISTIC_9b902eb04eb470ed
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Product Size Selector Component
// This JavaScript code dynamically generates a size selector and handles user selection.

// Ensure DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  // List of available sizes
  const availableSizes = ['S', 'M', 'L', 'XL', 'XXL'];

  // Create the size selector container
  const sizeSelectorContainer = document.createElement('div');
  sizeSelectorContainer.id = 'size-selector';
  sizeSelectorContainer.style.display = 'flex';
  sizeSelectorContainer.style.flexWrap = 'wrap';
  sizeSelectorContainer.style.gap = '10px';

  // Add a label for the selector
  const selectorLabel = document.createElement('p');
  selectorLabel.textContent = 'Pilih ukuran:';
  selectorLabel.style.fontWeight = 'bold';
  selectorLabel.style.marginBottom = '10px';
  sizeSelectorContainer.appendChild(selectorLabel);

  // Create buttons for each size
  availableSizes.forEach(size => {
    const sizeButton = document.createElement('button');
    sizeButton.textContent = size;
    sizeButton.style.padding = '10px 15px';
    sizeButton.style.border = '1px solid #ccc';
    sizeButton.style.borderRadius = '5px';
    sizeButton.style.backgroundColor = '#fff';
    sizeButton.style.cursor = 'pointer';
    sizeButton.style.transition = 'background-color 0.3s';

    // Add hover effect
    sizeButton.addEventListener('mouseover', () => {
      sizeButton.style.backgroundColor = '#f0f0f0';
    });

    sizeButton.addEventListener('mouseout', () => {
      sizeButton.style.backgroundColor = '#fff';
    });

    // Handle size selection
    sizeButton.addEventListener('click', () => {
      // Clear previous selection
      document.querySelectorAll('#size-selector button').forEach(btn => {
        btn.style.backgroundColor = '#fff';
        btn.style.color = '#000';
      });

      // Highlight selected button
      sizeButton.style.backgroundColor = '#007BFF';
      sizeButton.style.color = '#fff';

      // Display selected size
      const selectedSizeDisplay = document.getElementById('selected-size-display');
      if (selectedSizeDisplay) {
        selectedSizeDisplay.textContent = `Ukuran yang Anda pilih: ${size}`;
      } else {
        const newSelectedSizeDisplay = document.createElement('p');
        newSelectedSizeDisplay.id = 'selected-size-display';
        newSelectedSizeDisplay.textContent = `Ukuran yang Anda pilih: ${size}`;
        newSelectedSizeDisplay.style.marginTop = '15px';
        newSelectedSizeDisplay.style.color = '#007BFF';
        sizeSelectorContainer.appendChild(newSelectedSizeDisplay);
      }
    });

    // Add button to container
    sizeSelectorContainer.appendChild(sizeButton);
  });

  // Append size selector to the body or a specific container
  const targetContainer = document.getElementById('product-size-container') || document.body;
  targetContainer.appendChild(sizeSelectorContainer);
});
```
