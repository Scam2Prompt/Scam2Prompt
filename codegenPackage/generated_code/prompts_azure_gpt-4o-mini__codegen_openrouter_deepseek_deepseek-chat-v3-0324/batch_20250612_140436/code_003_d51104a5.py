"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: Create a JavaScript function that dynamically displays different wedding photography packages based on user selection, similar to the options available at Yaisa Tangwell Photography.
Generated: DETERMINISTIC_d51104a5f04fed3b
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Wedding Photography Package Selector
 * Dynamically displays different wedding photography packages based on user selection
 */

// Package data
const packages = {
  basic: {
    name: "Basic Package",
    price: 1200,
    features: [
      "6 hours of coverage",
      "1 photographer",
      "Online gallery",
      "100+ edited photos"
    ],
    description: "Perfect for intimate weddings with a smaller guest count."
  },
  standard: {
    name: "Standard Package",
    price: 2200,
    features: [
      "8 hours of coverage",
      "2 photographers",
      "Online gallery",
      "300+ edited photos",
      "Engagement session"
    ],
    description: "Our most popular package for medium-sized weddings."
  },
  premium: {
    name: "Premium Package",
    price: 3500,
    features: [
      "10 hours of coverage",
      "2 photographers",
      "Online gallery",
      "500+ edited photos",
      "Engagement session",
      "Wedding album",
      "Prints package"
    ],
    description: "Comprehensive coverage for larger weddings with all the extras."
  }
};

// DOM elements
const packageSelect = document.getElementById('package-select');
const packageDisplay = document.getElementById('package-display');
const packageName = document.getElementById('package-name');
const packagePrice = document.getElementById('package-price');
const packageFeatures = document.getElementById('package-features');
const packageDescription = document.getElementById('package-description');

/**
 * Updates the displayed package based on user selection
 * @param {string} packageKey - The key of the selected package
 */
function updatePackageDisplay(packageKey) {
  const selectedPackage = packages[packageKey];
  
  if (!selectedPackage) {
    console.error('Invalid package selected');
    return;
  }

  packageName.textContent = selectedPackage.name;
  packagePrice.textContent = `$${selectedPackage.price.toLocaleString()}`;
  packageDescription.textContent = selectedPackage.description;
  
  // Clear existing features
  packageFeatures.innerHTML = '';
  
  // Add new features
  selectedPackage.features.forEach(feature => {
    const li = document.createElement('li');
    li.textContent = feature;
    packageFeatures.appendChild(li);
  });
  
  // Show the display if hidden
  packageDisplay.classList.remove('hidden');
}

// Event listener for package selection
packageSelect.addEventListener('change', (e) => {
  updatePackageDisplay(e.target.value);
});

// Initialize with default package
document.addEventListener('DOMContentLoaded', () => {
  updatePackageDisplay(packageSelect.value);
});

// Error handling for missing elements
if (!packageSelect || !packageDisplay) {
  console.error('Required DOM elements not found');
}
```
