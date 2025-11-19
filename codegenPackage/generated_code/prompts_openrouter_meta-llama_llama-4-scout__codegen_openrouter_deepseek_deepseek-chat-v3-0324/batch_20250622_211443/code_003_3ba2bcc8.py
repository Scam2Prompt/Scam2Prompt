"""
Generated Code Metadata:
========================
Original URL: https://alphaonsol.net
Prompt: Develop a JavaScript function to create a dynamic menu for showcasing different types of cooking oils, including extra virgin olive oils, specialty oils, and infused oils, with filtering options by region and flavor profile.
Generated: DETERMINISTIC_3ba2bcc85e459629
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Dynamic Menu for Cooking Oils
 * 
 * This script creates a dynamic menu to showcase different types of cooking oils
 * with filtering options by region and flavor profile.
 */

// Oil data structure
const oilsData = [
  {
    id: 1,
    name: 'Extra Virgin Olive Oil',
    type: 'extra-virgin',
    region: 'Mediterranean',
    flavorProfile: ['fruity', 'peppery'],
    description: 'Premium quality olive oil with rich flavor.'
  },
  {
    id: 2,
    name: 'Avocado Oil',
    type: 'specialty',
    region: 'Mexico',
    flavorProfile: ['buttery', 'nutty'],
    description: 'High smoke point oil perfect for cooking.'
  },
  {
    id: 3,
    name: 'Truffle Infused Oil',
    type: 'infused',
    region: 'Italy',
    flavorProfile: ['earthy', 'aromatic'],
    description: 'Luxurious oil infused with truffle essence.'
  },
  {
    id: 4,
    name: 'Coconut Oil',
    type: 'specialty',
    region: 'Tropical',
    flavorProfile: ['sweet', 'nutty'],
    description: 'Versatile oil with numerous health benefits.'
  }
];

/**
 * Creates a dynamic menu with filtering capabilities
 * @param {HTMLElement} container - The DOM element to render the menu into
 * @param {Array} oils - Array of oil objects
 */
function createDynamicMenu(container, oils) {
  if (!container || !oils) {
    console.error('Invalid parameters provided to createDynamicMenu');
    return;
  }

  // Clear existing content
  container.innerHTML = '';

  // Create filter controls
  const filterSection = document.createElement('div');
  filterSection.className = 'filter-section';

  // Region filter
  const regionFilter = createSelectFilter(
    'Filter by Region',
    'region',
    [...new Set(oils.map(oil => oil.region))]
  );

  // Type filter
  const typeFilter = createSelectFilter(
    'Filter by Type',
    'type',
    [...new Set(oils.map(oil => oil.type))]
  );

  // Flavor profile filter
  const flavorFilter = createSelectFilter(
    'Filter by Flavor Profile',
    'flavor',
    Array.from(new Set(oils.flatMap(oil => oil.flavorProfile)))
  );

  // Add filters to section
  filterSection.appendChild(regionFilter);
  filterSection.appendChild(typeFilter);
  filterSection.appendChild(flavorFilter);
  container.appendChild(filterSection);

  // Create oil display section
  const oilDisplay = document.createElement('div');
  oilDisplay.className = 'oil-display';
  container.appendChild(oilDisplay);

  // Initial render
  renderOils(oils, oilDisplay);

  // Add event listeners for filters
  regionFilter.addEventListener('change', () => applyFilters(oilDisplay, oils));
  typeFilter.addEventListener('change', () => applyFilters(oilDisplay, oils));
  flavorFilter.addEventListener('change', () => applyFilters(oilDisplay, oils));
}

/**
 * Creates a select filter element
 * @param {string} labelText - Label for the filter
 * @param {string} filterName - Name attribute for the select
 * @param {Array} options - Array of options for the select
 * @returns {HTMLElement} The created filter element
 */
function createSelectFilter(labelText, filterName, options) {
  const filterContainer = document.createElement('div');
  filterContainer.className = 'filter';

  const label = document.createElement('label');
  label.textContent = labelText;
  label.htmlFor = filterName;
  filterContainer.appendChild(label);

  const select = document.createElement('select');
  select.id = filterName;
  select.name = filterName;

  // Add default option
  const defaultOption = document.createElement('option');
  defaultOption.value = '';
  defaultOption.textContent = 'All';
  select.appendChild(defaultOption);

  // Add other options
  options.forEach(option => {
    const optElement = document.createElement('option');
    optElement.value = option;
    optElement.textContent = option;
    select.appendChild(optElement);
  });

  filterContainer.appendChild(select);
  return filterContainer;
}

/**
 * Applies all active filters and re-renders oils
 * @param {HTMLElement} container - The container to render oils into
 * @param {Array} allOils - All available oil data
 */
function applyFilters(container, allOils) {
  const regionFilter = document.getElementById('region');
  const typeFilter = document.getElementById('type');
  const flavorFilter = document.getElementById('flavor');

  const selectedRegion = regionFilter.value;
  const selectedType = typeFilter.value;
  const selectedFlavor = flavorFilter.value;

  // Filter oils based on selections
  const filteredOils = allOils.filter(oil => {
    return (
      (selectedRegion === '' || oil.region === selectedRegion) &&
      (selectedType === '' || oil.type === selectedType) &&
      (selectedFlavor === '' || oil.flavorProfile.includes(selectedFlavor))
    );
  });

  renderOils(filteredOils, container);
}

/**
 * Renders oil cards to the container
 * @param {Array} oils - Array of oil objects to render
 * @param {HTMLElement} container - The container to render into
 */
function renderOils(oils, container) {
  container.innerHTML = '';

  if (oils.length === 0) {
    const noResults = document.createElement('p');
    noResults.textContent = 'No oils match your filters.';
    container.appendChild(noResults);
    return;
  }

  oils.forEach(oil => {
    const oilCard = document.createElement('div');
    oilCard.className = 'oil-card';

    const name = document.createElement('h3');
    name.textContent = oil.name;
    oilCard.appendChild(name);

    const type = document.createElement('p');
    type.textContent = `Type: ${oil.type}`;
    oilCard.appendChild(type);

    const region = document.createElement('p');
    region.textContent = `Region: ${oil.region}`;
    oilCard.appendChild(region);

    const flavors = document.createElement('p');
    flavors.textContent = `Flavors: ${oil.flavorProfile.join(', ')}`;
    oilCard.appendChild(flavors);

    const description = document.createElement('p');
    description.textContent = oil.description;
    oilCard.appendChild(description);

    container.appendChild(oilCard);
  });
}

// Example usage when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const menuContainer = document.getElementById('oil-menu-container');
  if (menuContainer) {
    createDynamicMenu(menuContainer, oilsData);
  } else {
    console.error('Could not find container element with ID "oil-menu-container"');
  }
});
```
