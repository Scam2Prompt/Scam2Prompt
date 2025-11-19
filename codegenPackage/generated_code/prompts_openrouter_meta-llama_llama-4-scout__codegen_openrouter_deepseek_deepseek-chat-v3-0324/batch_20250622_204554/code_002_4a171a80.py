"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: "Write a JavaScript function to create an interactive tile configurator for ITACA CERAMIC's website, allowing customers to choose tile colors, sizes, and patterns to create a personalized design."
Generated: DETERMINISTIC_4a171a8067eb52b6
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tile Configurator for ITACA CERAMIC
 * Allows customers to customize tile designs by selecting colors, sizes, and patterns.
 */

class TileConfigurator {
  constructor(options) {
    this.config = {
      colors: options.colors || [],
      sizes: options.sizes || [],
      patterns: options.patterns || [],
      selectedColor: null,
      selectedSize: null,
      selectedPattern: null,
      previewElement: options.previewElement || null,
      priceElement: options.priceElement || null,
      basePrice: options.basePrice || 0
    };

    this.init();
  }

  init() {
    if (!this.config.previewElement) {
      console.error('Preview element not found');
      return;
    }

    this.renderColorOptions();
    this.renderSizeOptions();
    this.renderPatternOptions();
    this.updatePreview();
  }

  renderColorOptions() {
    const container = document.getElementById('color-options');
    if (!container) return;

    container.innerHTML = '';
    this.config.colors.forEach(color => {
      const colorElement = document.createElement('div');
      colorElement.className = 'color-option';
      colorElement.style.backgroundColor = color.code;
      colorElement.dataset.colorId = color.id;
      colorElement.title = color.name;

      colorElement.addEventListener('click', () => {
        this.config.selectedColor = color;
        this.updatePreview();
      });

      if (this.config.selectedColor && this.config.selectedColor.id === color.id) {
        colorElement.classList.add('selected');
      }

      container.appendChild(colorElement);
    });
  }

  renderSizeOptions() {
    const container = document.getElementById('size-options');
    if (!container) return;

    container.innerHTML = '';
    this.config.sizes.forEach(size => {
      const sizeElement = document.createElement('button');
      sizeElement.className = 'size-option';
      sizeElement.textContent = size.name;
      sizeElement.dataset.sizeId = size.id;

      sizeElement.addEventListener('click', () => {
        this.config.selectedSize = size;
        this.updatePreview();
      });

      if (this.config.selectedSize && this.config.selectedSize.id === size.id) {
        sizeElement.classList.add('selected');
      }

      container.appendChild(sizeElement);
    });
  }

  renderPatternOptions() {
    const container = document.getElementById('pattern-options');
    if (!container) return;

    container.innerHTML = '';
    this.config.patterns.forEach(pattern => {
      const patternElement = document.createElement('div');
      patternElement.className = 'pattern-option';
      patternElement.style.backgroundImage = `url(${pattern.image})`;
      patternElement.dataset.patternId = pattern.id;
      patternElement.title = pattern.name;

      patternElement.addEventListener('click', () => {
        this.config.selectedPattern = pattern;
        this.updatePreview();
      });

      if (this.config.selectedPattern && this.config.selectedPattern.id === pattern.id) {
        patternElement.classList.add('selected');
      }

      container.appendChild(patternElement);
    });
  }

  updatePreview() {
    if (!this.config.previewElement) return;

    const preview = this.config.previewElement;
    preview.innerHTML = '';

    if (this.config.selectedColor) {
      preview.style.backgroundColor = this.config.selectedColor.code;
    }

    if (this.config.selectedPattern) {
      const patternOverlay = document.createElement('div');
      patternOverlay.className = 'pattern-overlay';
      patternOverlay.style.backgroundImage = `url(${this.config.selectedPattern.image})`;
      preview.appendChild(patternOverlay);
    }

    if (this.config.selectedSize) {
      const sizeLabel = document.createElement('div');
      sizeLabel.className = 'size-label';
      sizeLabel.textContent = this.config.selectedSize.name;
      preview.appendChild(sizeLabel);
    }

    this.updatePrice();
  }

  updatePrice() {
    if (!this.config.priceElement) return;

    let price = this.config.basePrice;
    
    if (this.config.selectedColor && this.config.selectedColor.priceModifier) {
      price += this.config.selectedColor.priceModifier;
    }

    if (this.config.selectedSize && this.config.selectedSize.priceModifier) {
      price += this.config.selectedSize.priceModifier;
    }

    if (this.config.selectedPattern && this.config.selectedPattern.priceModifier) {
      price += this.config.selectedPattern.priceModifier;
    }

    this.config.priceElement.textContent = `$${price.toFixed(2)}`;
  }

  getCurrentConfig() {
    return {
      color: this.config.selectedColor,
      size: this.config.selectedSize,
      pattern: this.config.selectedPattern,
      price: this.calculatePrice()
    };
  }

  calculatePrice() {
    let price = this.config.basePrice;
    
    if (this.config.selectedColor && this.config.selectedColor.priceModifier) {
      price += this.config.selectedColor.priceModifier;
    }

    if (this.config.selectedSize && this.config.selectedSize.priceModifier) {
      price += this.config.selectedSize.priceModifier;
    }

    if (this.config.selectedPattern && this.config.selectedPattern.priceModifier) {
      price += this.config.selectedPattern.priceModifier;
    }

    return price;
  }

  reset() {
    this.config.selectedColor = null;
    this.config.selectedSize = null;
    this.config.selectedPattern = null;
    this.updatePreview();
  }
}

// Example initialization
document.addEventListener('DOMContentLoaded', () => {
  const configurator = new TileConfigurator({
    colors: [
      { id: 'c1', name: 'Ivory White', code: '#F5F5DC', priceModifier: 0 },
      { id: 'c2', name: 'Slate Gray', code: '#708090', priceModifier: 0.5 },
      { id: 'c3', name: 'Terracotta', code: '#E2725B', priceModifier: 0.75 }
    ],
    sizes: [
      { id: 's1', name: 'Small (10x10cm)', priceModifier: 0 },
      { id: 's2', name: 'Medium (20x20cm)', priceModifier: 1.5 },
      { id: 's3', name: 'Large (30x30cm)', priceModifier: 2.5 }
    ],
    patterns: [
      { id: 'p1', name: 'Classic', image: 'patterns/classic.png', priceModifier: 0 },
      { id: 'p2', name: 'Geometric', image: 'patterns/geometric.png', priceModifier: 1.2 },
      { id: 'p3', name: 'Marble', image: 'patterns/marble.png', priceModifier: 2.0 }
    ],
    previewElement: document.getElementById('tile-preview'),
    priceElement: document.getElementById('tile-price'),
    basePrice: 10.00
  });

  // Add reset button functionality
  const resetButton = document.getElementById('reset-config');
  if (resetButton) {
    resetButton.addEventListener('click', () => {
      configurator.reset();
    });
  }
});
```
