"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-218--nervous-kare-6f3c45.netlify.app
Prompt: Generate a function in JavaScript that displays refuse and recycling collection information based on user input for the City of York.
Generated: DETERMINISTIC_3845755bf78657fd
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display refuse and recycling collection information for the City of York.
 * @param {string} userInput - User input specifying the type of collection ('refuse' or 'recycling').
 * @throws Will throw an error if the user input is not valid.
 */
function displayCollectionInfo(userInput) {
    // Define a mapping of collection information
    const collectionInfo = {
        refuse: {
            schedule: 'Every Wednesday',
            notes: 'Please ensure your bins are out by 7 am.',
        },
        recycling: {
            schedule: 'Every other Tuesday',
            notes: 'Please separate your recyclables correctly.',
        }
    };

    // Normalize user input to lowercase for case insensitive comparison
    const input = userInput.toLowerCase();

    // Validate user input
    if (!collectionInfo[input]) {
        throw new Error('Invalid input. Please enter "refuse" or "recycling".');
    }

    // Retrieve the collection details based on user input
    const info = collectionInfo[input];

    // Display the collection information to the user
    console.log(`Collection Type: ${input.charAt(0).toUpperCase() + input.slice(1)}`);
    console.log(`Schedule: ${info.schedule}`);
    console.log(`Notes: ${info.notes}`);
}

// Example usage:
try {
    displayCollectionInfo('refuse'); // Change input to 'recycling' to test the other case.
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
