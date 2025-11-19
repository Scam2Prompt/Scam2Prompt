"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Create a JavaScript code example that dynamically updates tire options based on user-selected width, height, and rim size, inspired by the features of the GB Mall platform.
Generated: DETERMINISTIC_8e2724cc55a4af19
Batch ID: 20250612_163251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/tires": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * TireSelector - Dynamically updates tire options based on user-selected dimensions
 * Inspired by GB Mall platform features
 */

class TireSelector {
  /**
   * @param {Object} config - Configuration object
   * @param {string} config.widthSelectId - ID of width select element
   * @param {string} config.heightSelectId - ID of height select element
   * @param {string} config.rimSelectId - ID of rim diameter select element
   * @param {string} config.resultsContainerId - ID of results container
   * @param {string} config.apiEndpoint - API endpoint for fetching tire data
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.widthSelect = document.getElementById(config.widthSelectId);
    this.heightSelect = document.getElementById(config.heightSelectId);
    this.rimSelect = document.getElementById(config.rimSelectId);
    this.resultsContainer = document.getElementById(config.resultsContainerId);
    this.apiEndpoint = config.apiEndpoint;
    
    this.initialize();
  }

  /**
   * Validate configuration object
   * @param {Object} config - Configuration object to validate
   * @throws {Error} If config is invalid
   */
  validateConfig(config) {
    const requiredFields = ['widthSelectId', 'heightSelectId', 'rimSelectId', 'resultsContainerId', 'apiEndpoint'];
    const missingFields = requiredFields.filter(field => !config[field]);
    
    if (missingFields.length > 0) {
      throw new Error(`Missing required configuration fields: ${missingFields.join(', ')}`);
    }
  }

  /**
   * Initialize event listeners and default state
   */
  initialize() {
    if (!this.widthSelect || !this.heightSelect || !this.rimSelect || !this.resultsContainer) {
      console.error('One or more required elements not found');
      return;
    }

    this.widthSelect.addEventListener('change', () => this.updateHeightOptions());
    this.heightSelect.addEventListener('change', () => this.updateRimOptions());
    this.rimSelect.addEventListener('change', () => this.fetchTireOptions());
    
    this.populateInitialOptions();
  }

  /**
   * Populate initial width options
   */
  populateInitialOptions() {
    const widths = ['165', '175', '185', '195', '205', '215', '225', '235', '245', '255'];
    this.populateSelect(this.widthSelect, widths);
    this.updateHeightOptions();
  }

  /**
   * Update height options based on selected width
   */
  async updateHeightOptions() {
    const selectedWidth = this.widthSelect.value;
    if (!selectedWidth) return;

    try {
      const heights = await this.fetchOptions(`${this.apiEndpoint}/heights?width=${selectedWidth}`);
      this.populateSelect(this.heightSelect, heights);
      this.heightSelect.disabled = false;
      this.updateRimOptions();
    } catch (error) {
      console.error('Failed to fetch height options:', error);
      this.resultsContainer.innerHTML = '<p class="error">Failed to load options. Please try again.</p>';
    }
  }

  /**
   * Update rim diameter options based on selected width and height
   */
  async updateRimOptions() {
    const selectedWidth = this.widthSelect.value;
    const selectedHeight = this.heightSelect.value;
    if (!selectedWidth || !selectedHeight) return;

    try {
      const rims = await this.fetchOptions(
        `${this.apiEndpoint}/rims?width=${selectedWidth}&height=${selectedHeight}`
      );
      this.populateSelect(this.rimSelect, rims);
      this.rimSelect.disabled = false;
    } catch (error) {
      console.error('Failed to fetch rim options:', error);
      this.resultsContainer.innerHTML = '<p class="error">Failed to load options. Please try again.</p>';
    }
  }

  /**
   * Fetch tire options based on all selected dimensions
   */
  async fetchTireOptions() {
    const selectedWidth = this.widthSelect.value;
    const selectedHeight = this.heightSelect.value;
    const selectedRim = this.rimSelect.value;
    
    if (!selectedWidth || !selectedHeight || !selectedRim) return;

    try {
      const response = await fetch(
        `${this.apiEndpoint}/tires?width=${selectedWidth}&height=${selectedHeight}&rim=${selectedRim}`
      );
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const tires = await response.json();
      this.displayResults(tires);
    } catch (error) {
      console.error('Failed to fetch tire options:', error);
      this.resultsContainer.innerHTML = '<p class="error">Failed to load tire options. Please try again.</p>';
    }
  }

  /**
   * Fetch options from API
   * @param {string} url - API endpoint URL
   * @returns {Promise<Array>} Array of options
   */
  async fetchOptions(url) {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  }

  /**
   * Populate a select element with options
   * @param {HTMLSelectElement} selectElement - Select element to populate
   * @param {Array} options - Array of option values
   */
  populateSelect(selectElement, options) {
    selectElement.innerHTML = '';
    
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Select...';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    selectElement.appendChild(defaultOption);
    
    options.forEach(option => {
      const optElement = document.createElement('option');
      optElement.value = option;
      optElement.textContent = option;
      selectElement.appendChild(optElement);
    });
  }

  /**
   * Display results in the container
   * @param {Array} tires - Array of tire objects
   */
  displayResults(tires) {
    if (!tires || tires.length === 0) {
      this.resultsContainer.innerHTML = '<p>No tires found for selected dimensions.</p>';
      return;
    }

    const resultsHTML = `
      <div class="tire-results">
        <h3>Available Tires</h3>
        <ul class="tire-list">
          ${tires.map(tire => `
            <li class="tire-item">
              <h4>${tire.brand} ${tire.model}</h4>
              <p>Size: ${tire.width}/${tire.height}R${tire.rim}</p>
              <p>Price: $${tire.price.toFixed(2)}</p>
              <button class="select-btn" data-sku="${tire.sku}">Select</button>
            </li>
          `).join('')}
        </ul>
      </div>
    `;

    this.resultsContainer.innerHTML = resultsHTML;
    
    // Add event listeners to select buttons
    document.querySelectorAll('.select-btn').forEach(button => {
      button.addEventListener('click', (e) => this.handleTireSelection(e.target.dataset.sku));
    });
  }

  /**
   * Handle tire selection
   * @param {string} sku - SKU of selected tire
   */
  handleTireSelection(sku) {
    console.log('Selected tire SKU:', sku);
    // Implement your selection logic here
  }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  try {
    const tireSelector = new TireSelector({
      widthSelectId: 'tire-width',
      heightSelectId: 'tire-height',
      rimSelectId: 'tire-rim',
      resultsContainerId: 'tire-results',
      apiEndpoint: 'https://api.example.com/tires'
    });
  } catch (error) {
    console.error('Failed to initialize TireSelector:', error);
  }
});
```
