"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Create a JavaScript function that displays a proposal for solar installation options, including financing and incentives, inspired by the offerings of PowerFive Solar Consulting.
Generated: DETERMINISTIC_18c8d2b183ab13e2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Solar Installation Proposal Generator
 * Inspired by PowerFive Solar Consulting offerings
 * 
 * This function generates a solar installation proposal with various options,
 * including financing plans and available incentives.
 * 
 * @param {Object} customerDetails - Customer information
 * @param {Object} systemDetails - Solar system specifications
 * @param {Array} financingOptions - Available financing plans
 * @param {Array} incentives - Available incentives/rebates
 * @returns {Object} Complete solar proposal
 */
function generateSolarProposal(customerDetails, systemDetails, financingOptions, incentives) {
    // Validate input parameters
    if (!customerDetails || typeof customerDetails !== 'object') {
        throw new Error('Invalid customer details provided');
    }
    if (!systemDetails || typeof systemDetails !== 'object') {
        throw new Error('Invalid system details provided');
    }
    if (!Array.isArray(financingOptions) || financingOptions.length === 0) {
        throw new Error('Invalid financing options provided');
    }
    if (!Array.isArray(incentives)) {
        throw new Error('Invalid incentives provided');
    }

    // Calculate system cost and savings estimates
    const calculateSystemCost = () => {
        const baseCost = systemDetails.sizeKW * 3000; // $3,000 per kW as baseline
        const incentivesTotal = incentives.reduce((sum, incentive) => sum + incentive.amount, 0);
        const netCost = baseCost - incentivesTotal;
        
        return {
            baseCost: baseCost,
            incentivesTotal: incentivesTotal,
            netCost: netCost
        };
    };

    // Calculate annual savings estimate
    const calculateAnnualSavings = () => {
        const averageElectricityRate = 0.15; // $0.15 per kWh as national average
        const productionFactor = 1400; // kWh per kW per year (varies by location)
        return systemDetails.sizeKW * productionFactor * averageElectricityRate;
    };

    // Generate financing options with monthly payments
    const generateFinancingPlans = () => {
        const { netCost } = calculateSystemCost();
        
        return financingOptions.map(option => {
            if (option.termMonths <= 0 || option.interestRate < 0) {
                throw new Error('Invalid financing option parameters');
            }

            const monthlyInterestRate = option.interestRate / 100 / 12;
            const monthlyPayment = netCost * 
                (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, option.termMonths)) / 
                (Math.pow(1 + monthlyInterestRate, option.termMonths) - 1);
            
            return {
                name: option.name,
                termMonths: option.termMonths,
                interestRate: option.interestRate,
                monthlyPayment: monthlyPayment.toFixed(2),
                totalCost: (monthlyPayment * option.termMonths).toFixed(2)
            };
        });
    };

    // Generate the complete proposal
    try {
        const costBreakdown = calculateSystemCost();
        const annualSavings = calculateAnnualSavings();
        const financingPlans = generateFinancingPlans();
        
        return {
            customer: {
                name: customerDetails.name || 'Not provided',
                address: customerDetails.address || 'Not provided',
                email: customerDetails.email || 'Not provided',
                phone: customerDetails.phone || 'Not provided'
            },
            system: {
                sizeKW: systemDetails.sizeKW,
                panelType: systemDetails.panelType || 'Premium Efficiency',
                warrantyYears: systemDetails.warrantyYears || 25,
                estimatedProductionKWh: systemDetails.sizeKW * 1400 // kWh per year
            },
            financials: {
                baseCost: costBreakdown.baseCost,
                incentives: incentives,
                netCost: costBreakdown.netCost,
                annualSavings: annualSavings,
                paybackYears: (costBreakdown.netCost / annualSavings).toFixed(1),
                financingOptions: financingPlans
            },
            disclaimer: 'Estimates are based on average conditions and may vary. Actual savings depend on system performance, utility rates, and other factors.',
            generatedDate: new Date().toISOString()
        };
    } catch (error) {
        console.error('Error generating solar proposal:', error);
        throw new Error('Failed to generate solar proposal');
    }
}

// Example usage:
/*
const customer = {
    name: 'John Doe',
    address: '123 Solar St, Sun City',
    email: 'john@example.com',
    phone: '555-123-4567'
};

const system = {
    sizeKW: 6.5,
    panelType: 'High Efficiency',
    warrantyYears: 30
};

const financing = [
    { name: '10-Year Loan', termMonths: 120, interestRate: 3.99 },
    { name: '15-Year Loan', termMonths: 180, interestRate: 4.49 },
    { name: '20-Year Loan', termMonths: 240, interestRate: 4.99 }
];

const incentives = [
    { name: 'Federal Tax Credit', amount: 1950, description: '26% of system cost' },
    { name: 'State Rebate', amount: 1000, description: 'State solar incentive program' }
];

const proposal = generateSolarProposal(customer, system, financing, incentives);
console.log(proposal);
*/
```
