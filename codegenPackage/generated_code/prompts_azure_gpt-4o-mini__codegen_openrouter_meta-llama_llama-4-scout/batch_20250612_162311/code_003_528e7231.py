"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Develop a JavaScript function that calculates the cost of various treatments (chiropractic, osteopathy, massage therapy) based on the services listed at Clinique Robin Paul & Fils.
Generated: DETERMINISTIC_528e7231620aef12
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of various treatments at Clinique Robin Paul & Fils.
 */

/**
 * Treatment costs object.
 * @typedef {Object} TreatmentCosts
 * @property {number} chiropractic - Cost of chiropractic treatment.
 * @property {number} osteopathy - Cost of osteopathy treatment.
 * @property {number} massageTherapy - Cost of massage therapy treatment.
 */

/**
 * Treatment types enum.
 * @enum {string}
 */
const TreatmentType = {
  CHIROPRACTIC: 'chiropractic',
  OSTEOPATHY: 'osteopathy',
  MASSAGE_THERAPY: 'massage therapy',
};

/**
 * Default treatment costs.
 * @type {TreatmentCosts}
 */
const defaultTreatmentCosts = {
  [TreatmentType.CHIROPRACTIC]: 60.0,
  [TreatmentType.OSTEOPATHY]: 70.0,
  [TreatmentType.MASSAGE_THERAPY]: 50.0,
};

/**
 * Calculates the total cost of treatments.
 * @param {Array<{ type: TreatmentType, duration: number }>} treatments - List of treatments.
 * @param {TreatmentCosts} [treatmentCosts=defaultTreatmentCosts] - Custom treatment costs.
 * @returns {number} Total cost of treatments.
 */
function calculateTreatmentCost(treatments, treatmentCosts = defaultTreatmentCosts) {
  if (!treatments || !Array.isArray(treatments)) {
    throw new Error('Invalid treatments list');
  }

  let totalCost = 0.0;

  treatments.forEach((treatment) => {
    if (!treatment || typeof treatment !== 'object') {
      throw new Error('Invalid treatment object');
    }

    const { type, duration } = treatment;

    if (!Object.values(TreatmentType).includes(type)) {
      throw new Error(`Invalid treatment type: ${type}`);
    }

    if (typeof duration !== 'number' || duration <= 0) {
      throw new Error(`Invalid treatment duration: ${duration}`);
    }

    const costPerUnit = treatmentCosts[type];
    if (typeof costPerUnit !== 'number' || costPerUnit <= 0) {
      throw new Error(`Invalid cost for treatment type: ${type}`);
    }

    totalCost += costPerUnit * duration;
  });

  return totalCost;
}

// Example usage:
try {
  const treatments = [
    { type: TreatmentType.CHIROPRACTIC, duration: 1 },
    { type: TreatmentType.MASSAGE_THERAPY, duration: 2 },
    { type: TreatmentType.OSTEOPATHY, duration: 1.5 },
  ];

  const totalCost = calculateTreatmentCost(treatments);
  globalThis.console.log(`Total cost: $${totalCost.toFixed(2)}`);
} catch (error) {
  globalThis.console.error(error.message);
}
```
