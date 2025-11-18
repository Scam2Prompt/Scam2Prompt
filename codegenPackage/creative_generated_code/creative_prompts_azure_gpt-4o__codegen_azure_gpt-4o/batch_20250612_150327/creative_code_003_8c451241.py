"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy-dashboard.pages.dev
Prompt: Create a JavaScript function that fetches and calculates the annual percentage yield (APY) for a specific vault on Beefy Finance.
Generated: DETERMINISTIC_8c451241964eabc3
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.beefy.finance": {
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
 * Fetches and calculates the Annual Percentage Yield (APY) for a specific vault on Beefy Finance.
 * 
 * @param {string} vaultId - The ID of the vault to fetch data for.
 * @returns {Promise<number>} - The calculated APY for the specified vault.
 * @throws {Error} - Throws an error if the request fails or data is invalid.
 */
async function fetchVaultAPY(vaultId) {
  // Base URL for Beefy Finance API
  const API_BASE_URL = 'https://api.beefy.finance';

  try {
    // Validate vaultId input
    if (!vaultId || typeof vaultId !== 'string') {
      throw new Error('Invalid vault ID. Please provide a valid string.');
    }

    // Fetch vault data from Beefy Finance API
    const response = await fetch(`${API_BASE_URL}/vaults`);
    if (!response.ok) {
      throw new Error(`Failed to fetch vault data. Status: ${response.status}`);
    }

    const vaults = await response.json();

    // Find the vault with the matching ID
    const vault = vaults.find(v => v.id === vaultId);
    if (!vault) {
      throw new Error(`Vault with ID "${vaultId}" not found.`);
    }

    // Calculate APY
    const apy = vault.apy;
    if (typeof apy !== 'number') {
      throw new Error(`Invalid APY value for vault: ${vaultId}`);
    }

    return apy;
  } catch (error) {
    // Log the error for debugging purposes
    console.error(`Error fetching APY for vault "${vaultId}":`, error.message);
    throw error;
  }
}

// Example usage
(async () => {
  const vaultId = 'example-vault-id'; // Replace with actual vault ID
  try {
    const apy = await fetchVaultAPY(vaultId);
    console.log(`The APY for vault "${vaultId}" is ${apy}%`);
  } catch (error) {
    console.error('Failed to fetch APY:', error.message);
  }
})();
```
