"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashkar2023.github.io
Prompt: Write a JavaScript function to dynamically update progress bars for skills such as HTML, CSS, and JavaScript, based on percentages provided on Muhammed Ashkar's portfolio.
Generated: DETERMINISTIC_77868d27723e7c57
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates the progress bars for specified skills based on the provided percentages.
 * The function assumes that progress bars are represented by HTML elements with IDs corresponding to the skill names.
 *
 * @param {Object} skillPercentages - An object containing skill names as keys and their respective percentages as values.
 * @example
 * const skills = {
 *   html: 80,
 *   css: 70,
 *   javascript: 90
 * };
 * updateProgressBars(skills);
 */
function updateProgressBars(skillPercentages) {
    // Ensure skillPercentages is an object
    if (typeof skillPercentages !== 'object' || skillPercentages === null) {
        console.error('Invalid input: skillPercentages must be an object');
        return;
    }

    // Iterate over each skill in the provided object
    for (const [skill, percentage] of Object.entries(skillPercentages)) {
        // Validate that each percentage is a number between 0 and 100
        if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
            console.error(`Invalid percentage for ${skill}: ${percentage}. Must be a number between 0 and 100.`);
            continue; // Skip invalid skill
        }

        // Create the selector for the skill's progress bar
        const progressBar = document.getElementById(`${skill}-progress`);

        // Check if the progress bar element exists
        if (!progressBar) {
            console.error(`Progress bar element not found for skill: ${skill}`);
            continue; // Skip if the progress bar does not exist
        }

        // Update the width of the progress bar based on the percentage
        progressBar.style.width = `${percentage}%`;
        progressBar.setAttribute('aria-valuenow', percentage); // Improve accessibility
        progressBar.innerText = `${percentage}%`; // Optional: Display percentage inside the bar
    }
}

// Example usage
const skills = {
    html: 80,
    css: 70,
    javascript: 90
};

// Update progress bars with provided skill percentages
updateProgressBars(skills);
```

```html
<!-- Example HTML structure for progress bars -->
<div>
    <div id="html-progress" class="progress-bar"></div>
    <div id="css-progress" class="progress-bar"></div>
    <div id="javascript-progress" class="progress-bar"></div>
</div>
```

```css
/* Example CSS for styling progress bars */
.progress-bar {
    width: 0;
    height: 30px;
    background-color: #4caf50; /* Green */
    transition: width 0.5s ease; /* Smooth transition */
    text-align: center; /* Center text inside the bar */
    color: white; /* Text color */
}
```
