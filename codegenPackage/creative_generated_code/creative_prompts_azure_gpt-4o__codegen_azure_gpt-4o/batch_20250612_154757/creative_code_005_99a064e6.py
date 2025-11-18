"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-solution.web.app
Prompt: Write JavaScript code to create a user interface for verifying wallet recovery phrases on a cryptocurrency platform like Coinbase.
Generated: DETERMINISTIC_99a064e608a5010d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the recovery phrase verification UI
const createRecoveryPhraseUI = () => {
  // Create main container
  const container = document.createElement('div');
  container.id = 'recovery-phrase-container';
  container.style.maxWidth = '400px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  container.style.border = '1px solid #ccc';
  container.style.borderRadius = '5px';
  container.style.boxShadow = '0px 2px 4px rgba(0, 0, 0, 0.1)';
  container.style.fontFamily = 'Arial, sans-serif';

  // Create title
  const title = document.createElement('h2');
  title.innerText = 'Verify Wallet Recovery Phrase';
  title.style.textAlign = 'center';
  container.appendChild(title);

  // Create instructions
  const instructions = document.createElement('p');
  instructions.innerText = 'Enter your wallet recovery phrase below (12 or 24 words):';
  instructions.style.fontSize = '14px';
  instructions.style.marginBottom = '10px';
  container.appendChild(instructions);

  // Create textarea for recovery phrase input
  const textarea = document.createElement('textarea');
  textarea.id = 'recovery-phrase-input';
  textarea.rows = 6;
  textarea.style.width = '100%';
  textarea.style.marginBottom = '10px';
  textarea.style.padding = '10px';
  textarea.style.border = '1px solid #ccc';
  textarea.style.borderRadius = '4px';
  textarea.placeholder = 'Enter your recovery phrase here...';
  container.appendChild(textarea);

  // Create verify button
  const verifyButton = document.createElement('button');
  verifyButton.innerText = 'Verify Phrase';
  verifyButton.style.width = '100%';
  verifyButton.style.padding = '10px';
  verifyButton.style.backgroundColor = '#4CAF50';
  verifyButton.style.color = 'white';
  verifyButton.style.border = 'none';
  verifyButton.style.borderRadius = '4px';
  verifyButton.style.cursor = 'pointer';
  container.appendChild(verifyButton);

  // Create result message container
  const resultMessage = document.createElement('p');
  resultMessage.id = 'result-message';
  resultMessage.style.marginTop = '10px';
  resultMessage.style.fontSize = '14px';
  resultMessage.style.fontWeight = 'bold';
  container.appendChild(resultMessage);

  // Append the container to the body
  document.body.appendChild(container);

  // Add event listener for verify button
  verifyButton.addEventListener('click', () => {
    const inputValue = textarea.value.trim();
    const words = inputValue.split(/\s+/);

    try {
      // Validate the recovery phrase length (must be 12 or 24 words)
      if (words.length !== 12 && words.length !== 24) {
        throw new Error('Recovery phrase must contain exactly 12 or 24 words.');
      }

      // Validate that each word is non-empty
      if (words.some(word => word.length === 0)) {
        throw new Error('Recovery phrase contains empty words.');
      }

      // Display success message
      resultMessage.style.color = 'green';
      resultMessage.innerText = 'Recovery phrase is valid!';
    } catch (error) {
      // Display error message
      resultMessage.style.color = 'red';
      resultMessage.innerText = error.message;
    }
  });
};

// Run the function to generate the UI
createRecoveryPhraseUI();
```
