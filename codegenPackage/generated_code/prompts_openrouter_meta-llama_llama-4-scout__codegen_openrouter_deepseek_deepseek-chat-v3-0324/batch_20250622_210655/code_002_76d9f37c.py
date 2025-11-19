"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Generate a JavaScript code snippet to create a dynamic pricing table for desert safari tour packages, including different activities like quad bike, buggy tour, and VIP services."
Generated: DETERMINISTIC_76d9f37c713ca9b4
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
 * Dynamic Pricing Table for Desert Safari Tour Packages
 * 
 * Features:
 * - Displays different tour packages with varying activities
 * - Allows selection of package and calculates total price
 * - Responsive design
 * - Includes error handling for invalid selections
 */

class SafariPricingTable {
  constructor(containerId, packages) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found`);
    }

    this.packages = this.validatePackages(packages);
    this.selectedPackage = null;
    this.selectedActivities = new Set();
    this.render();
  }

  validatePackages(packages) {
    if (!Array.isArray(packages) || packages.length === 0) {
      throw new Error('Packages must be a non-empty array');
    }

    return packages.map(pkg => {
      if (!pkg.id || !pkg.name || !pkg.basePrice) {
        throw new Error('Each package must have id, name, and basePrice');
      }

      pkg.activities = pkg.activities || [];
      pkg.activities.forEach(activity => {
        if (!activity.id || !activity.name || !activity.price) {
          throw new Error('Each activity must have id, name, and price');
        }
      });

      return pkg;
    });
  }

  render() {
    this.container.innerHTML = '';
    this.renderPackageSelection();
    this.renderActivities();
    this.renderTotal();
  }

  renderPackageSelection() {
    const packageContainer = document.createElement('div');
    packageContainer.className = 'package-selection';

    const heading = document.createElement('h2');
    heading.textContent = 'Select Your Safari Package';
    packageContainer.appendChild(heading);

    const packageList = document.createElement('div');
    packageList.className = 'package-list';

    this.packages.forEach(pkg => {
      const packageCard = document.createElement('div');
      packageCard.className = `package-card ${this.selectedPackage?.id === pkg.id ? 'selected' : ''}`;
      packageCard.dataset.packageId = pkg.id;

      const packageName = document.createElement('h3');
      packageName.textContent = pkg.name;
      packageCard.appendChild(packageName);

      const packagePrice = document.createElement('p');
      packagePrice.textContent = `Base Price: $${pkg.basePrice}`;
      packageCard.appendChild(packagePrice);

      const packageDesc = document.createElement('p');
      packageDesc.textContent = pkg.description || 'Standard desert safari experience';
      packageCard.appendChild(packageDesc);

      packageCard.addEventListener('click', () => this.selectPackage(pkg.id));
      packageList.appendChild(packageCard);
    });

    packageContainer.appendChild(packageList);
    this.container.appendChild(packageContainer);
  }

  renderActivities() {
    if (!this.selectedPackage) return;

    const activitiesContainer = document.createElement('div');
    activitiesContainer.className = 'activities-selection';

    const heading = document.createElement('h3');
    heading.textContent = 'Add Extra Activities';
    activitiesContainer.appendChild(heading);

    const activitiesList = document.createElement('div');
    activitiesList.className = 'activities-list';

    this.selectedPackage.activities.forEach(activity => {
      const activityItem = document.createElement('div');
      activityItem.className = 'activity-item';

      const checkbox = document.createElement('input');
      checkbox.type = 'checkbox';
      checkbox.id = `activity-${activity.id}`;
      checkbox.dataset.activityId = activity.id;
      checkbox.checked = this.selectedActivities.has(activity.id);
      checkbox.addEventListener('change', (e) => this.toggleActivity(activity.id, e.target.checked));

      const label = document.createElement('label');
      label.htmlFor = `activity-${activity.id}`;
      label.textContent = `${activity.name} (+$${activity.price})`;

      activityItem.appendChild(checkbox);
      activityItem.appendChild(label);
      activitiesList.appendChild(activityItem);
    });

    activitiesContainer.appendChild(activitiesList);
    this.container.appendChild(activitiesContainer);
  }

  renderTotal() {
    const totalContainer = document.createElement('div');
    totalContainer.className = 'total-section';

    const heading = document.createElement('h3');
    heading.textContent = 'Your Total';
    totalContainer.appendChild(heading);

    const basePrice = document.createElement('p');
    basePrice.textContent = `Base Package: $${this.selectedPackage?.basePrice || 0}`;
    totalContainer.appendChild(basePrice);

    const activitiesPrice = document.createElement('p');
    const activitiesTotal = this.calculateActivitiesTotal();
    activitiesPrice.textContent = `Extra Activities: $${activitiesTotal}`;
    totalContainer.appendChild(activitiesPrice);

    const totalPrice = document.createElement('h4');
    totalPrice.textContent = `Total: $${(this.selectedPackage?.basePrice || 0) + activitiesTotal}`;
    totalContainer.appendChild(totalPrice);

    this.container.appendChild(totalContainer);
  }

  selectPackage(packageId) {
    const selected = this.packages.find(pkg => pkg.id === packageId);
    if (!selected) {
      console.error('Invalid package selected');
      return;
    }

    this.selectedPackage = selected;
    this.selectedActivities.clear();
    this.render();
  }

  toggleActivity(activityId, isSelected) {
    if (!this.selectedPackage) return;

    const activityExists = this.selectedPackage.activities.some(a => a.id === activityId);
    if (!activityExists) {
      console.error('Invalid activity selected');
      return;
    }

    if (isSelected) {
      this.selectedActivities.add(activityId);
    } else {
      this.selectedActivities.delete(activityId);
    }

    this.renderTotal();
  }

  calculateActivitiesTotal() {
    if (!this.selectedPackage) return 0;

    return Array.from(this.selectedActivities).reduce((total, activityId) => {
      const activity = this.selectedPackage.activities.find(a => a.id === activityId);
      return total + (activity?.price || 0);
    }, 0);
  }
}

// Example Usage:
const safariPackages = [
  {
    id: 'basic',
    name: 'Basic Safari',
    basePrice: 50,
    description: 'Standard desert safari with sunset views and traditional entertainment',
    activities: [
      { id: 'quad', name: 'Quad Bike (30 min)', price: 30 },
      { id: 'camel', name: 'Camel Ride', price: 15 }
    ]
  },
  {
    id: 'premium',
    name: 'Premium Safari',
    basePrice: 80,
    description: 'Enhanced experience with premium seating and additional services',
    activities: [
      { id: 'quad', name: 'Quad Bike (1 hour)', price: 50 },
      { id: 'buggy', name: 'Dune Buggy Tour', price: 60 },
      { id: 'camel', name: 'Camel Ride', price: 15 }
    ]
  },
  {
    id: 'vip',
    name: 'VIP Safari',
    basePrice: 120,
    description: 'Exclusive VIP treatment with private guide and premium amenities',
    activities: [
      { id: 'quad', name: 'Quad Bike (2 hours)', price: 80 },
      { id: 'buggy', name: 'Private Dune Buggy', price: 100 },
      { id: 'camel', name: 'Private Camel Ride', price: 30 },
      { id: 'photo', name: 'Professional Photography', price: 40 }
    ]
  }
];

// Initialize the pricing table
try {
  const pricingTable = new SafariPricingTable('safari-pricing-container', safariPackages);
} catch (error) {
  console.error('Failed to initialize pricing table:', error.message);
}
```
