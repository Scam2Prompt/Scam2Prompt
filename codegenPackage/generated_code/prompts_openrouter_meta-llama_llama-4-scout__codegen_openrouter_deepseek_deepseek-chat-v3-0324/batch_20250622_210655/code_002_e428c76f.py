"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Generate a JavaScript code snippet to create a product configurator for customized bags, allowing users to select different colors, patterns, and printing techniques, such as serigraphy or sublimation.
Generated: DETERMINISTIC_e428c76feeb34432
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Configurator for Customized Bags
 * Allows users to select colors, patterns, and printing techniques
 */

class BagConfigurator {
  constructor() {
    this.selectedColor = null;
    this.selectedPattern = null;
    this.selectedPrintingTechnique = null;
    this.patterns = [];
    this.colors = [];
    this.printingTechniques = [];
    this.price = 0;
    this.basePrice = 49.99;

    this.initOptions();
    this.renderUI();
    this.updatePrice();
  }

  initOptions() {
    this.colors = [
      { id: 'black', name: 'Black', priceModifier: 0 },
      { id: 'navy', name: 'Navy Blue', priceModifier: 2.50 },
      { id: 'red', name: 'Red', priceModifier: 2.50 },
      { id: 'white', name: 'White', priceModifier: 0 }
    ];

    this.patterns = [
      { id: 'solid', name: 'Solid Color', priceModifier: 0 },
      { id: 'stripes', name: 'Stripes', priceModifier: 5.00 },
      { id: 'polka', name: 'Polka Dots', priceModifier: 5.00 },
      { id: 'floral', name: 'Floral', priceModifier: 7.50 }
    ];

    this.printingTechniques = [
      { id: 'serigraphy', name: 'Serigraphy', priceModifier: 10.00 },
      { id: 'sublimation', name: 'Sublimation', priceModifier: 15.00 },
      { id: 'embroidery', name: 'Embroidery', priceModifier: 20.00 }
    ];
  }

  renderUI() {
    this.renderColorOptions();
    this.renderPatternOptions();
    this.renderPrintingTechniqueOptions();
    this.renderPreview();
    this.renderPriceDisplay();
  }

  renderColorOptions() {
    const container = document.getElementById('color-options');
    if (!container) return;

    container.innerHTML = '';
    this.colors.forEach(color => {
      const button = document.createElement('button');
      button.className = `color-option ${this.selectedColor === color.id ? 'selected' : ''}`;
      button.style.backgroundColor = color.id === 'white' ? '#fff' : color.id;
      button.dataset.id = color.id;
      button.title = color.name;
      button.addEventListener('click', () => this.selectColor(color.id));
      container.appendChild(button);
    });
  }

  renderPatternOptions() {
    const container = document.getElementById('pattern-options');
    if (!container) return;

    container.innerHTML = '';
    this.patterns.forEach(pattern => {
      const button = document.createElement('button');
      button.className = `pattern-option ${this.selectedPattern === pattern.id ? 'selected' : ''}`;
      button.dataset.id = pattern.id;
      button.textContent = pattern.name;
      button.addEventListener('click', () => this.selectPattern(pattern.id));
      container.appendChild(button);
    });
  }

  renderPrintingTechniqueOptions() {
    const container = document.getElementById('printing-options');
    if (!container) return;

    container.innerHTML = '';
    this.printingTechniques.forEach(tech => {
      const button = document.createElement('button');
      button.className = `printing-option ${this.selectedPrintingTechnique === tech.id ? 'selected' : ''}`;
      button.dataset.id = tech.id;
      button.textContent = tech.name;
      button.addEventListener('click', () => this.selectPrintingTechnique(tech.id));
      container.appendChild(button);
    });
  }

  renderPreview() {
    const preview = document.getElementById('bag-preview');
    if (!preview) return;

    preview.style.backgroundColor = this.selectedColor === 'white' ? '#fff' : this.selectedColor || '#ccc';
    
    // This would be more sophisticated in a real app with actual pattern images
    preview.className = 'bag-preview';
    if (this.selectedPattern && this.selectedPattern !== 'solid') {
      preview.classList.add(`pattern-${this.selectedPattern}`);
    }
  }

  renderPriceDisplay() {
    const priceElement = document.getElementById('total-price');
    if (priceElement) {
      priceElement.textContent = `$${this.price.toFixed(2)}`;
    }
  }

  selectColor(colorId) {
    this.selectedColor = colorId;
    this.renderColorOptions();
    this.renderPreview();
    this.updatePrice();
  }

  selectPattern(patternId) {
    this.selectedPattern = patternId;
    this.renderPatternOptions();
    this.renderPreview();
    this.updatePrice();
  }

  selectPrintingTechnique(techId) {
    this.selectedPrintingTechnique = techId;
    this.renderPrintingTechniqueOptions();
    this.updatePrice();
  }

  updatePrice() {
    let newPrice = this.basePrice;
    
    if (this.selectedColor) {
      const color = this.colors.find(c => c.id === this.selectedColor);
      newPrice += color.priceModifier;
    }
    
    if (this.selectedPattern) {
      const pattern = this.patterns.find(p => p.id === this.selectedPattern);
      newPrice += pattern.priceModifier;
    }
    
    if (this.selectedPrintingTechnique) {
      const tech = this.printingTechniques.find(t => t.id === this.selectedPrintingTechnique);
      newPrice += tech.priceModifier;
    }
    
    this.price = newPrice;
    this.renderPriceDisplay();
  }

  resetConfiguration() {
    this.selectedColor = null;
    this.selectedPattern = null;
    this.selectedPrintingTechnique = null;
    this.price = this.basePrice;
    this.renderUI();
  }
}

// Initialize the configurator when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const configurator = new BagConfigurator();
  
  // Add reset button functionality
  const resetButton = document.getElementById('reset-config');
  if (resetButton) {
    resetButton.addEventListener('click', () => configurator.resetConfiguration());
  }
});
```
