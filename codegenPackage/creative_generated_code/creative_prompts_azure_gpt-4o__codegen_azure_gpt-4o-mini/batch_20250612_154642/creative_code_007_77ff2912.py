"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoonmeme.com
Prompt: Generate code to allow users to copy the SafeMoon Meme contract address `ELPrcU7qRV3DUz8AP6siTE7GkR3gkkBvGmgBRiLnC19Y` directly into their clipboard using JavaScript.
Generated: DETERMINISTIC_77ff291299544ccf
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to copy the SafeMoon Meme contract address to the clipboard
function copyContractAddress() {
    // Define the SafeMoon Meme contract address
    const contractAddress = 'ELPrcU7qRV3DUz8AP6siTE7GkR3gkkBvGmgBRiLnC19Y';

    // Create a temporary textarea element to facilitate the copy action
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = contractAddress; // Set the value to the contract address
    document.body.appendChild(tempTextArea); // Append the textarea to the document

    // Select the text in the textarea
    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices

    try {
        // Execute the copy command
        const successful = document.execCommand('copy');

        // Provide feedback to the user based on the success of the copy action
        if (successful) {
            console.log('Contract address copied to clipboard: ' + contractAddress);
            alert('Contract address copied to clipboard!');
        } else {
            console.error('Failed to copy the contract address.');
            alert('Failed to copy the contract address. Please try again.');
        }
    } catch (err) {
        console.error('Error executing copy command: ', err);
        alert('An error occurred while trying to copy the contract address. Please try again.');
    } finally {
        // Clean up by removing the temporary textarea
        document.body.removeChild(tempTextArea);
    }
}

// Example usage: Bind the function to a button click event
document.getElementById('copyButton').addEventListener('click', copyContractAddress);
```

<!-- HTML for the button to trigger the copy functionality -->
```html
<button id="copyButton">Copy SafeMoon Contract Address</button>
```
