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
 * Updates progress bars dynamically based on provided skill percentages.
 * @param {Object} skills - An object containing skill names as keys and percentages as values.
 * @param {string} [containerId='skills-container'] - The ID of the container holding progress bars.
 */
function updateSkillProgressBars(skills, containerId = 'skills-container') {
    try {
        // Validate inputs
        if (!skills || typeof skills !== 'object' || Object.keys(skills).length === 0) {
            throw new Error('Invalid skills object provided');
        }

        const container = document.getElementById(containerId);
        if (!container) {
            throw new Error(`Container element with ID '${containerId}' not found`);
        }

        // Create or update progress bars for each skill
        Object.entries(skills).forEach(([skillName, percentage]) => {
            // Validate percentage
            const numericPercentage = Number(percentage);
            if (isNaN(numericPercentage) || numericPercentage < 0 || numericPercentage > 100) {
                console.warn(`Invalid percentage (${percentage}) for skill ${skillName}`);
                return;
            }

            // Find or create progress bar element
            let progressBar = container.querySelector(`.progress-bar[data-skill="${skillName}"]`);
            if (!progressBar) {
                progressBar = document.createElement('div');
                progressBar.className = 'progress-bar';
                progressBar.setAttribute('data-skill', skillName);
                
                const label = document.createElement('span');
                label.className = 'skill-label';
                label.textContent = skillName;
                
                const bar = document.createElement('div');
                bar.className = 'bar';
                
                const fill = document.createElement('div');
                fill.className = 'fill';
                
                const percentageText = document.createElement('span');
                percentageText.className = 'percentage';
                
                bar.appendChild(fill);
                bar.appendChild(percentageText);
                progressBar.appendChild(label);
                progressBar.appendChild(bar);
                container.appendChild(progressBar);
            }

            // Update progress bar
            const fill = progressBar.querySelector('.fill');
            const percentageText = progressBar.querySelector('.percentage');
            
            fill.style.width = `${numericPercentage}%`;
            percentageText.textContent = `${numericPercentage}%`;
            
            // Add animation class
            fill.classList.add('animate');
            setTimeout(() => fill.classList.remove('animate'), 1000);
        });

    } catch (error) {
        console.error('Error updating skill progress bars:', error.message);
    }
}

// Example usage:
// updateSkillProgressBars({
//     'HTML': 90,
//     'CSS': 85,
//     'JavaScript': 80,
//     'React': 75
// });
```
