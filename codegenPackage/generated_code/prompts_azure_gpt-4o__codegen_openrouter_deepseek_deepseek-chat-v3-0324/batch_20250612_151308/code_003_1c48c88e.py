"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Develop a tool in JavaScript that allows users to input pool dimensions and features to generate a detailed scope for builders, inspired by Poolz's locked-in scope feature.
Generated: DETERMINISTIC_1c48c88e3ecf1394
Batch ID: 20250612_151308
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
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
 * Pool Scope Generator Tool
 * 
 * This tool allows users to input pool dimensions and features
 * to generate a detailed scope for builders.
 */

class PoolScopeGenerator {
  constructor() {
    this.poolData = {
      dimensions: {
        length: 0,
        width: 0,
        depth: {
          shallow: 0,
          deep: 0
        }
      },
      features: [],
      materials: {},
      additionalNotes: ''
    };
  }

  /**
   * Set pool dimensions
   * @param {number} length - Length in feet
   * @param {number} width - Width in feet
   * @param {number} shallowDepth - Shallow end depth in feet
   * @param {number} deepDepth - Deep end depth in feet
   * @throws {Error} If any dimension is invalid
   */
  setDimensions(length, width, shallowDepth, deepDepth) {
    if (!this._validateDimension(length) || 
        !this._validateDimension(width) || 
        !this._validateDimension(shallowDepth) || 
        !this._validateDimension(deepDepth)) {
      throw new Error('All dimensions must be positive numbers');
    }

    if (shallowDepth >= deepDepth) {
      throw new Error('Deep end must be deeper than shallow end');
    }

    this.poolData.dimensions = {
      length,
      width,
      depth: {
        shallow: shallowDepth,
        deep: deepDepth
      }
    };
  }

  /**
   * Validate dimension value
   * @param {number} value - Dimension value to validate
   * @returns {boolean} True if valid
   */
  _validateDimension(value) {
    return typeof value === 'number' && value > 0;
  }

  /**
   * Add feature to pool
   * @param {string} feature - Feature name
   * @param {string} [details] - Optional details about the feature
   */
  addFeature(feature, details = '') {
    if (!feature || typeof feature !== 'string') {
      throw new Error('Feature must be a non-empty string');
    }

    this.poolData.features.push({
      name: feature.trim(),
      details: details.toString().trim()
    });
  }

  /**
   * Set pool materials
   * @param {Object} materials - Materials configuration
   * @param {string} materials.surface - Pool surface material
   * @param {string} materials.coping - Coping material
   * @param {string} materials.decking - Decking material
   */
  setMaterials({ surface, coping, decking }) {
    if (!surface || !coping || !decking) {
      throw new Error('All material fields are required');
    }

    this.poolData.materials = {
      surface: surface.toString().trim(),
      coping: coping.toString().trim(),
      decking: decking.toString().trim()
    };
  }

  /**
   * Set additional notes
   * @param {string} notes - Additional notes about the pool
   */
  setAdditionalNotes(notes) {
    this.poolData.additionalNotes = notes.toString().trim();
  }

  /**
   * Calculate pool volume in gallons
   * @returns {number} Volume in gallons
   */
  calculateVolume() {
    const { length, width, depth } = this.poolData.dimensions;
    const avgDepth = (depth.shallow + depth.deep) / 2;
    return length * width * avgDepth * 7.5; // 7.5 gallons per cubic foot
  }

  /**
   * Generate the scope document
   * @returns {Object} Complete pool scope document
   */
  generateScope() {
    if (!this._validateScopeData()) {
      throw new Error('Incomplete pool data. Please provide all required information.');
    }

    return {
      ...this.poolData,
      volume: this.calculateVolume(),
      timestamp: new Date().toISOString()
    };
  }

  /**
   * Validate all required scope data is present
   * @returns {boolean} True if data is valid
   */
  _validateScopeData() {
    return (
      this.poolData.dimensions.length > 0 &&
      this.poolData.dimensions.width > 0 &&
      this.poolData.dimensions.depth.shallow > 0 &&
      this.poolData.dimensions.depth.deep > 0 &&
      Object.keys(this.poolData.materials).length === 3
    );
  }
}

// UI Implementation
document.addEventListener('DOMContentLoaded', () => {
  const generator = new PoolScopeGenerator();
  const form = document.getElementById('poolScopeForm');
  const output = document.getElementById('scopeOutput');
  const copyBtn = document.getElementById('copyScopeBtn');
  const downloadBtn = document.getElementById('downloadScopeBtn');

  if (!form || !output || !copyBtn || !downloadBtn) {
    console.error('Required DOM elements not found');
    return;
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    generateScope();
  });

  copyBtn.addEventListener('click', copyScopeToClipboard);
  downloadBtn.addEventListener('click', downloadScope);

  function generateScope() {
    try {
      // Get dimensions
      const length = parseFloat(document.getElementById('poolLength').value);
      const width = parseFloat(document.getElementById('poolWidth').value);
      const shallowDepth = parseFloat(document.getElementById('shallowDepth').value);
      const deepDepth = parseFloat(document.getElementById('deepDepth').value);

      generator.setDimensions(length, width, shallowDepth, deepDepth);

      // Get materials
      const surface = document.getElementById('surfaceMaterial').value;
      const coping = document.getElementById('copingMaterial').value;
      const decking = document.getElementById('deckingMaterial').value;
      generator.setMaterials({ surface, coping, decking });

      // Get features
      const featuresContainer = document.getElementById('featuresContainer');
      const featureInputs = featuresContainer.querySelectorAll('.feature-input');
      
      featureInputs.forEach(input => {
        const featureName = input.querySelector('.feature-name').value;
        const featureDetails = input.querySelector('.feature-details').value;
        if (featureName) {
          generator.addFeature(featureName, featureDetails);
        }
      });

      // Get additional notes
      const notes = document.getElementById('additionalNotes').value;
      generator.setAdditionalNotes(notes);

      // Generate and display scope
      const scope = generator.generateScope();
      output.textContent = JSON.stringify(scope, null, 2);
      output.style.display = 'block';
      copyBtn.style.display = 'inline-block';
      downloadBtn.style.display = 'inline-block';

    } catch (error) {
      alert(`Error generating scope: ${error.message}`);
      console.error(error);
    }
  }

  function copyScopeToClipboard() {
    try {
      navigator.clipboard.writeText(output.textContent);
      alert('Scope copied to clipboard!');
    } catch (error) {
      alert('Failed to copy scope to clipboard');
      console.error(error);
    }
  }

  function downloadScope() {
    try {
      const scope = output.textContent;
      const blob = new Blob([scope], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `pool-scope-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (error) {
      alert('Failed to download scope');
      console.error(error);
    }
  }

  // Feature management
  document.getElementById('addFeatureBtn').addEventListener('click', () => {
    const featuresContainer = document.getElementById('featuresContainer');
    const featureDiv = document.createElement('div');
    featureDiv.className = 'feature-input mb-2';
    featureDiv.innerHTML = `
      <div class="row g-2">
        <div class="col-md-5">
          <input type="text" class="form-control feature-name" placeholder="Feature name" required>
        </div>
        <div class="col-md-5">
          <input type="text" class="form-control feature-details" placeholder="Details (optional)">
        </div>
        <div class="col-md-2">
          <button type="button" class="btn btn-danger remove-feature">Remove</button>
        </div>
      </div>
    `;
    featuresContainer.appendChild(featureDiv);

    featureDiv.querySelector('.remove-feature').addEventListener('click', () => {
      featuresContainer.removeChild(featureDiv);
    });
  });
});

// HTML would be needed to accompany this JavaScript
// Here's a basic template that would work with the above code:
/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pool Scope Generator</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container mt
