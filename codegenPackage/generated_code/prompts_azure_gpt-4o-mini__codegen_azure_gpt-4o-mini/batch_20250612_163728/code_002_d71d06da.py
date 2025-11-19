"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: Create a JavaScript function that dynamically generates a list of extracurricular clubs available at Unidad Educativa Bilingüe de la Inmaculada, highlighting their focus on cognitive and socio-emotional skills.
Generated: DETERMINISTIC_d71d06dacc0fe143
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a list of extracurricular clubs available at Unidad Educativa Bilingüe de la Inmaculada.
 * Each club focuses on enhancing cognitive and socio-emotional skills.
 * 
 * @returns {HTMLElement} The unordered list element containing the clubs.
 */
function generateExtracurricularClubs() {
    // Define the clubs and their descriptions
    const clubs = [
        {
            name: "Robotics Club",
            description: "Enhances problem-solving and critical thinking skills through hands-on robotics projects."
        },
        {
            name: "Drama Club",
            description: "Develops emotional intelligence and teamwork through theatrical performances."
        },
        {
            name: "Debate Club",
            description: "Fosters cognitive skills and public speaking abilities through structured debates."
        },
        {
            name: "Art Club",
            description: "Encourages creativity and self-expression while building social skills through collaborative projects."
        },
        {
            name: "Music Band",
            description: "Promotes teamwork and discipline while enhancing cognitive skills through music education."
        }
    ];

    // Create an unordered list element
    const ul = document.createElement('ul');

    // Iterate over the clubs array and create list items
    clubs.forEach(club => {
        // Create a list item for each club
        const li = document.createElement('li');
        li.textContent = `${club.name}: ${club.description}`;
        
        // Append the list item to the unordered list
        ul.appendChild(li);
    });

    // Return the generated list
    return ul;
}

// Example usage: Append the generated clubs list to a specific element in the DOM
try {
    const clubsList = generateExtracurricularClubs();
    document.getElementById('clubs-container').appendChild(clubsList);
} catch (error) {
    console.error("An error occurred while generating the clubs list:", error);
}
```

Make sure to have an HTML element with the ID `clubs-container` in your HTML file for the code to work correctly.
