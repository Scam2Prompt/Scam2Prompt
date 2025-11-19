"""
Generated Code Metadata:
========================
Original URL: https://iteamworldwide.com
Prompt: "Generate a code snippet in JavaScript to create a pricing table for USANA's business plans, including Silver, Gold, and Platinum options."
Generated: DETERMINISTIC_6621d07f6a3114aa
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * USANA Business Plans Pricing Table
 * This script creates a responsive pricing table for USANA's Silver, Gold, and Platinum business plans.
 */

// Pricing data for USANA business plans
const pricingPlans = [
  {
    name: 'Silver',
    price: 99,
    features: [
      'Basic product discounts',
      'Access to marketing materials',
      'Personal website',
      'Monthly training sessions'
    ],
    bestValue: false
  },
  {
    name: 'Gold',
    price: 199,
    features: [
      'All Silver benefits',
      'Higher product discounts',
      'Advanced marketing tools',
      'Weekly training sessions',
      'Business coaching'
    ],
    bestValue: true
  },
  {
    name: 'Platinum',
    price: 299,
    features: [
      'All Gold benefits',
      'Highest product discounts',
      'Priority support',
      'Exclusive events access',
      'Mentorship program',
      'Leadership training'
    ],
    bestValue: false
  }
];

/**
 * Creates a pricing table element
 * @param {HTMLElement} container - The DOM element to append the pricing table to
 */
function createPricingTable(container) {
  if (!container || !(container instanceof HTMLElement)) {
    console.error('Invalid container element provided');
    return;
  }

  try {
    const pricingTable = document.createElement('div');
    pricingTable.className = 'pricing-table';

    pricingPlans.forEach(plan => {
      const planCard = document.createElement('div');
      planCard.className = `plan-card ${plan.bestValue ? 'highlighted' : ''}`;

      const header = document.createElement('div');
      header.className = 'plan-header';
      header.innerHTML = `<h3>${plan.name}</h3>`;

      const price = document.createElement('div');
      price.className = 'plan-price';
      price.innerHTML = `<span class="currency">$</span><span class="amount">${plan.price}</span><span class="period">/mo</span>`;

      const featuresList = document.createElement('ul');
      featuresList.className = 'plan-features';
      plan.features.forEach(feature => {
        const li = document.createElement('li');
        li.textContent = feature;
        featuresList.appendChild(li);
      });

      const button = document.createElement('button');
      button.className = 'plan-button';
      button.textContent = 'Join Now';

      if (plan.bestValue) {
        const badge = document.createElement('div');
        badge.className = 'best-value-badge';
        badge.textContent = 'Best Value';
        header.appendChild(badge);
      }

      planCard.appendChild(header);
      planCard.appendChild(price);
      planCard.appendChild(featuresList);
      planCard.appendChild(button);

      pricingTable.appendChild(planCard);
    });

    container.appendChild(pricingTable);
  } catch (error) {
    console.error('Error creating pricing table:', error);
  }
}

// Example usage when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('pricing-container');
  if (container) {
    createPricingTable(container);
  } else {
    console.error('Could not find pricing container element');
  }
});
```

```html
<!-- Example HTML structure for the pricing table -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>USANA Business Plans</title>
  <style>
    .pricing-table {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 20px;
      padding: 20px;
      font-family: Arial, sans-serif;
    }
    .plan-card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 20px;
      width: 300px;
      background: white;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
      position: relative;
    }
    .plan-card.highlighted {
      border: 2px solid #ffcc00;
      transform: scale(1.05);
    }
    .plan-header {
      text-align: center;
      margin-bottom: 20px;
    }
    .plan-header h3 {
      margin: 0;
      color: #333;
      font-size: 24px;
    }
    .plan-price {
      text-align: center;
      margin-bottom: 20px;
    }
    .plan-price .amount {
      font-size: 36px;
      font-weight: bold;
      color: #2a5c8c;
    }
    .plan-price .currency {
      font-size: 20px;
      vertical-align: super;
    }
    .plan-price .period {
      font-size: 16px;
      color: #666;
    }
    .plan-features {
      list-style: none;
      padding: 0;
      margin-bottom: 20px;
    }
    .plan-features li {
      padding: 8px 0;
      border-bottom: 1px solid #eee;
    }
    .plan-button {
      width: 100%;
      padding: 12px;
      background-color: #2a5c8c;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
      transition: background-color 0.3s;
    }
    .plan-button:hover {
      background-color: #1e456e;
    }
    .best-value-badge {
      position: absolute;
      top: -10px;
      right: 20px;
      background-color: #ffcc00;
      color: #333;
      padding: 5px 10px;
      border-radius: 20px;
      font-weight: bold;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div id="pricing-container"></div>
  <script src="pricing-table.js"></script>
</body>
</html>
```
