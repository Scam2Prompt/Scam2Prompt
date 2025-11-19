"""
Generated Code Metadata:
========================
Original URL: https://berachain.crabdance.com
Prompt: Create a function in JavaScript that simulates a modal popup for displaying Berachain token eligibility results.
Generated: DETERMINISTIC_f5bcb18afabcfc69
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays a modal popup with Berachain token eligibility results.
 * @param {Object} eligibilityData - The eligibility data to display.
 * @param {string} eligibilityData.address - The wallet address checked.
 * @param {boolean} eligibilityData.isEligible - Whether the address is eligible.
 * @param {number} [eligibilityData.tokenAmount] - The amount of tokens eligible (if applicable).
 * @param {string} [eligibilityData.message] - Additional message to display.
 */
function showEligibilityModal(eligibilityData) {
    // Validate input
    if (!eligibilityData || typeof eligibilityData !== 'object') {
        console.error('Invalid eligibility data provided');
        return;
    }

    if (!eligibilityData.address || typeof eligibilityData.isEligible !== 'boolean') {
        console.error('Missing required fields in eligibility data');
        return;
    }

    // Create modal container
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    modal.style.zIndex = '1000';

    // Create modal content
    const modalContent = document.createElement('div');
    modalContent.style.backgroundColor = '#1a1a1a';
    modalContent.style.padding = '2rem';
    modalContent.style.borderRadius = '8px';
    modalContent.style.maxWidth = '500px';
    modalContent.style.width = '90%';
    modalContent.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';

    // Create close button
    const closeButton = document.createElement('button');
    closeButton.textContent = '×';
    closeButton.style.position = 'absolute';
    closeButton.style.top = '10px';
    closeButton.style.right = '10px';
    closeButton.style.background = 'none';
    closeButton.style.border = 'none';
    closeButton.style.fontSize = '1.5rem';
    closeButton.style.cursor = 'pointer';
    closeButton.style.color = '#ffffff';
    closeButton.addEventListener('click', () => {
        document.body.removeChild(modal);
    });

    // Create title
    const title = document.createElement('h2');
    title.textContent = 'Berachain Token Eligibility';
    title.style.color = '#ffffff';
    title.style.marginTop = '0';
    title.style.marginBottom = '1rem';

    // Create address display
    const addressText = document.createElement('p');
    addressText.textContent = `Address: ${eligibilityData.address}`;
    addressText.style.color = '#cccccc';
    addressText.style.marginBottom = '0.5rem';
    addressText.style.wordBreak = 'break-all';

    // Create eligibility status
    const eligibilityStatus = document.createElement('p');
    eligibilityStatus.textContent = eligibilityData.isEligible 
        ? '✅ Eligible for Berachain tokens' 
        : '❌ Not eligible for Berachain tokens';
    eligibilityStatus.style.color = eligibilityData.isEligible ? '#4CAF50' : '#F44336';
    eligibilityStatus.style.fontWeight = 'bold';
    eligibilityStatus.style.marginBottom = '1rem';

    // Create token amount if eligible
    let tokenAmountText;
    if (eligibilityData.isEligible && eligibilityData.tokenAmount) {
        tokenAmountText = document.createElement('p');
        tokenAmountText.textContent = `Amount: ${eligibilityData.tokenAmount} tokens`;
        tokenAmountText.style.color = '#ffffff';
        tokenAmountText.style.marginBottom = '1rem';
    }

    // Create additional message if provided
    let messageText;
    if (eligibilityData.message) {
        messageText = document.createElement('p');
        messageText.textContent = eligibilityData.message;
        messageText.style.color = '#cccccc';
        messageText.style.marginBottom = '1rem';
    }

    // Assemble modal
    modalContent.appendChild(closeButton);
    modalContent.appendChild(title);
    modalContent.appendChild(addressText);
    modalContent.appendChild(eligibilityStatus);
    
    if (tokenAmountText) modalContent.appendChild(tokenAmountText);
    if (messageText) modalContent.appendChild(messageText);
    
    modal.appendChild(modalContent);
    document.body.appendChild(modal);

    // Close modal when clicking outside content
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            document.body.removeChild(modal);
        }
    });
}
```
