"""
Generated Code Metadata:
========================
Original URL: https://ashkar2023.github.io
Prompt: Write a JavaScript function to dynamically update progress bars for skills such as HTML, CSS, and JavaScript, based on percentages provided on Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_77868d27723e7c57
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates the progress bars for skills based on the provided percentages.
 * 
 * @param {Object} skills - An object containing skill names as keys and their corresponding percentages as values.
 * @throws {Error} Throws an error if the input is not an object or if any percentage is not a number between 0 and 100.
 */
function updateProgressBars(skills) {
    // Validate input
    if (typeof skills !== 'object' || skills === null) {
        throw new Error('Invalid input: skills must be an object.');
    }

    // Iterate over each skill and update the corresponding progress bar
    for (const [skill, percentage] of Object.entries(skills)) {
        // Validate percentage
        if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
            throw new Error(`Invalid percentage for ${skill}: must be a number between 0 and 100.`);
        }

        // Select the progress bar element for the skill
        const progressBar = document.querySelector(`.${skill}-progress-bar`);
        const progressText = document.querySelector(`.${skill}-progress-text`);

        // Check if the progress bar element exists
        if (!progressBar || !progressText) {
            console.warn(`Progress bar for ${skill} not found.`);
            continue; // Skip to the next skill if the element is not found
        }

        // Update the progress bar's width and text
        progressBar.style.width = `${percentage}%`;
        progressText.textContent = `${percentage}%`;
    }
}

// Example usage
const skillsData = {
    html: 90,
    css: 85,
    javascript: 75
};

try {
    updateProgressBars(skillsData);
} catch (error) {
    console.error(error.message);
}
```
