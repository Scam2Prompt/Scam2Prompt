"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Create a function in JavaScript that simulates the effects of early cancer detection, inspired by the health awareness content found on Azuharu.
Generated: DETERMINISTIC_124bab2e0a01e86e
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the effects of early cancer detection based on input parameters.
 * @param {Object} patientData - Patient data object containing health metrics.
 * @param {number} patientData.age - Patient's age.
 * @param {string} patientData.gender - Patient's gender ('male' or 'female').
 * @param {boolean} patientData.hasFamilyHistory - Whether patient has family history of cancer.
 * @param {Array<string>} patientData.riskFactors - Array of risk factors (e.g., 'smoking', 'obesity').
 * @param {boolean} patientData.earlyDetection - Whether cancer was detected early.
 * @returns {Object} - Simulation results with survival rates and treatment outcomes.
 */
function simulateEarlyCancerDetection(patientData) {
    // Validate input
    if (!patientData || typeof patientData !== 'object') {
        throw new Error('Invalid patient data: must be an object');
    }

    const requiredFields = ['age', 'gender', 'hasFamilyHistory', 'riskFactors', 'earlyDetection'];
    for (const field of requiredFields) {
        if (patientData[field] === undefined) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    // Base survival rates (fictional data for simulation)
    const BASE_SURVIVAL_RATE = 0.8; // 80% for early detection
    const LATE_SURVIVAL_RATE = 0.3; // 30% for late detection

    // Calculate risk multiplier based on factors
    let riskMultiplier = 1;
    
    // Age risk (peaks around 60-70)
    const ageRisk = Math.min(1, Math.max(0, (patientData.age - 30) / 40));
    riskMultiplier += ageRisk * 0.5;

    // Family history risk
    if (patientData.hasFamilyHistory) {
        riskMultiplier += 0.3;
    }

    // Gender-specific risks (simplified for example)
    if (patientData.gender === 'male') {
        riskMultiplier += 0.1; // Higher risk for prostate cancer
    } else if (patientData.gender === 'female') {
        riskMultiplier += 0.15; // Higher risk for breast cancer
    }

    // Additional risk factors
    const factorWeights = {
        smoking: 0.4,
        obesity: 0.25,
        alcohol: 0.2,
        sedentary: 0.15,
        exposure: 0.3
    };

    patientData.riskFactors.forEach(factor => {
        riskMultiplier += factorWeights[factor] || 0;
    });

    // Calculate survival probability
    let survivalProbability;
    if (patientData.earlyDetection) {
        survivalProbability = BASE_SURVIVAL_RATE / riskMultiplier;
    } else {
        survivalProbability = LATE_SURVIVAL_RATE / riskMultiplier;
    }

    // Clamp between 0 and 1
    survivalProbability = Math.max(0, Math.min(1, survivalProbability));

    // Calculate treatment effectiveness
    const treatmentEffectiveness = patientData.earlyDetection 
        ? 0.9 * survivalProbability 
        : 0.5 * survivalProbability;

    // Calculate quality of life impact
    const qualityOfLife = patientData.earlyDetection 
        ? 0.85 - (riskMultiplier * 0.1)
        : 0.5 - (riskMultiplier * 0.15);

    return {
        survivalProbability: parseFloat(survivalProbability.toFixed(2)),
        treatmentEffectiveness: parseFloat(treatmentEffectiveness.toFixed(2)),
        qualityOfLife: parseFloat(Math.max(0, qualityOfLife).toFixed(2)),
        riskMultiplier: parseFloat(riskMultiplier.toFixed(2)),
        recommendation: patientData.earlyDetection 
            ? 'Continue regular screenings and maintain healthy lifestyle'
            : 'Consider more frequent screenings and consult with oncologist'
    };
}

// Example usage:
// const results = simulateEarlyCancerDetection({
//     age: 45,
//     gender: 'female',
//     hasFamilyHistory: true,
//     riskFactors: ['smoking', 'obesity'],
//     earlyDetection: true
// });
// console.log(results);
```
