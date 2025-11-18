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
// Function to dynamically update progress bars based on percentages
function updateSkillProgress(skillData) {
    /**
     * skillData: Array of objects in the following format:
     * [
     *   { skill: "HTML", percentage: 90 },
     *   { skill: "CSS", percentage: 80 },
     *   { skill: "JavaScript", percentage: 70 }
     * ]
     */

    // Validate input
    if (!Array.isArray(skillData)) {
        console.error("Invalid input: skillData must be an array");
        return;
    }

    skillData.forEach((item) => {
        try {
            // Destructure skill and percentage
            const { skill, percentage } = item;

            // Ensure skill is a string and percentage is a valid number
            if (typeof skill !== "string" || typeof percentage !== "number" || percentage < 0 || percentage > 100) {
                throw new Error(`Invalid data for skill: ${JSON.stringify(item)}`);
            }

            // Select the progress bar element for the skill
            const progressBar = document.querySelector(`.progress-bar[data-skill="${skill}"]`);

            if (!progressBar) {
                console.warn(`No progress bar found for skill: ${skill}`);
                return;
            }

            // Update progress bar width and aria-label for accessibility
            progressBar.style.width = `${percentage}%`;
            progressBar.setAttribute("aria-valuenow", percentage);
            progressBar.textContent = `${percentage}%`; // Optional: Display percentage inside the bar
        } catch (error) {
            console.error(error.message);
        }
    });
}

// Example usage
document.addEventListener("DOMContentLoaded", () => {
    // Example skill data
    const skills = [
        { skill: "HTML", percentage: 90 },
        { skill: "CSS", percentage: 80 },
        { skill: "JavaScript", percentage: 70 },
    ];

    // Call the function to update progress bars
    updateSkillProgress(skills);
});
```

**HTML Example for Progress Bars:**
```html
<div class="skills">
    <div class="skill">
        <label for="html-skill">HTML</label>
        <div class="progress">
            <div class="progress-bar" id="html-skill" data-skill="HTML" role="progressbar" aria-valuemin="0" aria-valuemax="100">0%</div>
        </div>
    </div>
    <div class="skill">
        <label for="css-skill">CSS</label>
        <div class="progress">
            <div class="progress-bar" id="css-skill" data-skill="CSS" role="progressbar" aria-valuemin="0" aria-valuemax="100">0%</div>
        </div>
    </div>
    <div class="skill">
        <label for="js-skill">JavaScript</label>
        <div class="progress">
            <div class="progress-bar" id="js-skill" data-skill="JavaScript" role="progressbar" aria-valuemin="0" aria-valuemax="100">0%</div>
        </div>
    </div>
</div>
```

**CSS Example for Styling:**
```css
.skills {
    max-width: 600px;
    margin: 0 auto;
}

.skill {
    margin-bottom: 1.5em;
}

.progress {
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
    height: 20px;
    position: relative;
}

.progress-bar {
    background-color: #4caf50;
    height: 100%;
    text-align: center;
    line-height: 20px;
    color: white;
    font-size: 14px;
    transition: width 0.4s ease;
}
```
