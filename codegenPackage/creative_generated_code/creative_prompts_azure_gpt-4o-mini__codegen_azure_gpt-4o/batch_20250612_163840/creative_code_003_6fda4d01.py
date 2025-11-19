"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Provide a code example that enhances user experience on a site that requires JavaScript, similar to ETH Pledge.
Generated: DETERMINISTIC_6fda4d01779b6b5a
Batch ID: 20250612_163840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ETH Pledge Example - Interactive Donation Widget
 * Enhances user experience for a donation system
 */

/**
 * Functionality:
 * - Users can enter an ETH amount they wish to pledge.
 * - Real-time validation of the input.
 * - Dynamic conversion of ETH to USD based on live exchange rates.
 * - Interactive confirmation modal before submitting the pledge.
 */

document.addEventListener('DOMContentLoaded', () => {
  // HTML Elements
  const pledgeInput = document.getElementById('eth-pledge-input');
  const usdValueDisplay = document.getElementById('usd-value-display');
  const submitButton = document.getElementById('submit-pledge');
  const confirmationModal = document.getElementById('confirmation-modal');
  const modalPledgeValue = document.getElementById('modal-pledge-value');
  const confirmButton = document.getElementById('confirm-pledge');
  const cancelButton = document.getElementById('cancel-pledge');

  let ethToUsdRate = 0;

  /**
   * Fetch live ETH to USD exchange rate from an API
   * Replace URL with a valid API endpoint for production use.
   */
  async function fetchExchangeRate() {
    try {
      const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd');
      const data = await response.json();
      ethToUsdRate = data.ethereum.usd;
    } catch (error) {
      console.error('Failed to fetch ETH to USD rate:', error);
      ethToUsdRate = 0;
      usdValueDisplay.textContent = 'Error fetching exchange rate';
    }
  }

  // Validate ETH input and display corresponding USD value
  function updateUsdValue() {
    const ethAmount = parseFloat(pledgeInput.value);
    if (isNaN(ethAmount) || ethAmount <= 0) {
      usdValueDisplay.textContent = 'Enter a valid ETH amount';
      submitButton.disabled = true;
    } else {
      const usdValue = (ethAmount * ethToUsdRate).toFixed(2);
      usdValueDisplay.textContent = `≈ $${usdValue} USD`;
      submitButton.disabled = false;
    }
  }

  // Open confirmation modal
  function openConfirmationModal() {
    const ethAmount = parseFloat(pledgeInput.value);
    const usdEquivalent = (ethAmount * ethToUsdRate).toFixed(2);
    modalPledgeValue.textContent = `You are pledging ${ethAmount} ETH (≈ $${usdEquivalent} USD). Proceed?`;
    confirmationModal.style.display = 'block';
  }

  // Close confirmation modal
  function closeConfirmationModal() {
    confirmationModal.style.display = 'none';
  }

  // Handle pledge confirmation
  function confirmPledge() {
    const ethAmount = parseFloat(pledgeInput.value);
    alert(`Thank you for pledging ${ethAmount} ETH!`);
    closeConfirmationModal();
    pledgeInput.value = ''; // Reset input
    usdValueDisplay.textContent = ''; // Reset display
    submitButton.disabled = true; // Disable button
  }

  // Event Listeners
  pledgeInput.addEventListener('input', updateUsdValue);
  submitButton.addEventListener('click', openConfirmationModal);
  cancelButton.addEventListener('click', closeConfirmationModal);
  confirmButton.addEventListener('click', confirmPledge);

  // Initial Setup
  fetchExchangeRate();
});

/**
 * Example HTML Structure (for context):
 * 
 * <div>
 *   <h1>ETH Pledge</h1>
 *   <input type="number" id="eth-pledge-input" placeholder="Enter ETH amount">
 *   <p id="usd-value-display"></p>
 *   <button id="submit-pledge" disabled>Submit Pledge</button>
 * </div>
 * <div id="confirmation-modal" style="display: none;">
 *   <p id="modal-pledge-value"></p>
 *   <button id="confirm-pledge">Confirm</button>
 *   <button id="cancel-pledge">Cancel</button>
 * </div>
 *
 * CSS (optional for style): Ensure modal styling for visibility and usability.
 */
```
