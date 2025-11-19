"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Develop a simple calculator in JavaScript to compare the tax benefits of different regimes tributários (tax regimes) in Brazil, such as Lucro Real, Lucro Presumido, and Simples Nacional."
Generated: DETERMINISTIC_f9e93182e1a8f415
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
 * Simple Tax Regime Calculator for Brazil
 * Compares tax benefits between Lucro Real, Lucro Presumido, and Simples Nacional
 */

class TaxRegimeCalculator {
  /**
   * Constructor
   * @param {number} annualRevenue - Annual revenue in BRL
   * @param {number} annualCosts - Annual costs in BRL
   * @param {number} payrollExpenses - Annual payroll expenses in BRL
   */
  constructor(annualRevenue, annualCosts, payrollExpenses) {
    this.annualRevenue = annualRevenue;
    this.annualCosts = annualCosts;
    this.payrollExpenses = payrollExpenses;
    this.validateInputs();
  }

  /**
   * Validates input values
   * @throws {Error} If inputs are invalid
   */
  validateInputs() {
    if (
      typeof this.annualRevenue !== 'number' ||
      typeof this.annualCosts !== 'number' ||
      typeof this.payrollExpenses !== 'number'
    ) {
      throw new Error('All inputs must be numbers');
    }

    if (this.annualRevenue < 0 || this.annualCosts < 0 || this.payrollExpenses < 0) {
      throw new Error('Inputs cannot be negative');
    }

    if (this.annualCosts > this.annualRevenue) {
      throw new Error('Costs cannot exceed revenue');
    }
  }

  /**
   * Calculates taxes under Lucro Real regime
   * @returns {number} Total tax amount in BRL
   */
  calculateLucroReal() {
    const profit = this.annualRevenue - this.annualCosts;
    const irpj = profit * 0.15; // Corporate Income Tax (15%)
    const csll = profit * 0.09; // Social Contribution on Net Profit (9%)
    const pis = this.annualRevenue * 0.0065; // PIS (0.65%)
    const cofins = this.annualRevenue * 0.03; // COFINS (3%)
    const inss = this.payrollExpenses * 0.2; // Social Security (20% of payroll)

    return irpj + csll + pis + cofins + inss;
  }

  /**
   * Calculates taxes under Lucro Presumido regime
   * @returns {number} Total tax amount in BRL
   */
  calculateLucroPresumido() {
    const presumedProfit = this.annualRevenue * 0.32; // Presumed profit (32% of revenue)
    const irpj = presumedProfit * 0.15; // Corporate Income Tax (15%)
    const csll = presumedProfit * 0.09; // Social Contribution on Net Profit (9%)
    const pis = this.annualRevenue * 0.0065; // PIS (0.65%)
    const cofins = this.annualRevenue * 0.03; // COFINS (3%)
    const inss = this.payrollExpenses * 0.2; // Social Security (20% of payroll)

    return irpj + csll + pis + cofins + inss;
  }

  /**
   * Calculates taxes under Simples Nacional regime
   * @returns {number} Total tax amount in BRL
   */
  calculateSimplesNacional() {
    // Simplified tax calculation based on revenue brackets
    let taxRate;
    if (this.annualRevenue <= 180000) {
      taxRate = 0.04; // 4% for revenue up to 180k
    } else if (this.annualRevenue <= 360000) {
      taxRate = 0.073; // 7.3% for revenue up to 360k
    } else if (this.annualRevenue <= 720000) {
      taxRate = 0.095; // 9.5% for revenue up to 720k
    } else if (this.annualRevenue <= 1800000) {
      taxRate = 0.107; // 10.7% for revenue up to 1.8M
    } else if (this.annualRevenue <= 3600000) {
      taxRate = 0.143; // 14.3% for revenue up to 3.6M
    } else if (this.annualRevenue <= 4800000) {
      taxRate = 0.19; // 19% for revenue up to 4.8M
    } else {
      throw new Error('Simples Nacional not applicable for revenue above 4.8M');
    }

    return this.annualRevenue * taxRate;
  }

  /**
   * Compares all tax regimes and returns results
   * @returns {Object} Comparison results
   */
  compareRegimes() {
    const lucroReal = this.calculateLucroReal();
    const lucroPresumido = this.calculateLucroPresumido();
    const simplesNacional = this.calculateSimplesNacional();

    return {
      lucroReal: {
        value: lucroReal,
        percentage: (lucroReal / this.annualRevenue) * 100
      },
      lucroPresumido: {
        value: lucroPresumido,
        percentage: (lucroPresumido / this.annualRevenue) * 100
      },
      simplesNacional: {
        value: simplesNacional,
        percentage: (simplesNacional / this.annualRevenue) * 100
      },
      bestOption: this.getBestOption(lucroReal, lucroPresumido, simplesNacional)
    };
  }

  /**
   * Determines the best tax regime option
   * @param {number} lucroReal 
   * @param {number} lucroPresumido 
   * @param {number} simplesNacional 
   * @returns {string} Best option name
   */
  getBestOption(lucroReal, lucroPresumido, simplesNacional) {
    const minTax = Math.min(lucroReal, lucroPresumido, simplesNacional);
    
    if (minTax === simplesNacional) return 'Simples Nacional';
    if (minTax === lucroPresumido) return 'Lucro Presumido';
    return 'Lucro Real';
  }
}

// UI Handling
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('tax-calculator-form');
  const resultsDiv = document.getElementById('results');

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    try {
      const revenue = parseFloat(document.getElementById('revenue').value);
      const costs = parseFloat(document.getElementById('costs').value);
      const payroll = parseFloat(document.getElementById('payroll').value);

      const calculator = new TaxRegimeCalculator(revenue, costs, payroll);
      const results = calculator.compareRegimes();

      displayResults(results);
    } catch (error) {
      displayError(error.message);
    }
  });

  function displayResults(results) {
    resultsDiv.innerHTML = `
      <h3>Resultados da Comparação</h3>
      <div class="result-item">
        <h4>Lucro Real</h4>
        <p>Valor: R$ ${results.lucroReal.value.toFixed(2)}</p>
        <p>Percentual: ${results.lucroReal.percentage.toFixed(2)}%</p>
      </div>
      <div class="result-item">
        <h4>Lucro Presumido</h4>
        <p>Valor: R$ ${results.lucroPresumido.value.toFixed(2)}</p>
        <p>Percentual: ${results.lucroPresumido.percentage.toFixed(2)}%</p>
      </div>
      <div class="result-item">
        <h4>Simples Nacional</h4>
        <p>Valor: R$ ${results.simplesNacional.value.toFixed(2)}</p>
        <p>Percentual: ${results.simplesNacional.percentage.toFixed(2)}%</p>
      </div>
      <div class="best-option">
        <h4>Melhor Opção: ${results.bestOption}</h4>
      </div>
    `;
    resultsDiv.style.display = 'block';
  }

  function displayError(message) {
    resultsDiv.innerHTML = `
      <div class="error">
        <p>Erro: ${message}</p>
      </div>
    `;
    resultsDiv.style.display = 'block';
  }
});
```

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Regimes Tributários</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      color: #2c3e50;
      text-align: center;
    }
    form {
      background: #f
