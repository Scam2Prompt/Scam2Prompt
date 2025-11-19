"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a JavaScript function that retrieves and displays information about the different educational programs offered at I.E Politécnico Municipal Cali, including Preescolar, Básica, and Media.
Generated: DETERMINISTIC_46f71a0f0c422933
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fetches and displays educational programs information from I.E Politécnico Municipal Cali
 * @returns {Promise<void>} A promise that resolves when the data is fetched and displayed
 */
async function fetchEducationalPrograms() {
    try {
        // In a real implementation, this would be an API endpoint
        // For demonstration, we're using mock data
        const mockPrograms = [
            {
                name: "Preescolar",
                description: "Programa educativo para niños en edad preescolar, enfocado en desarrollo integral.",
                duration: "3 años",
                ageRange: "3-5 años"
            },
            {
                name: "Básica",
                description: "Educación básica primaria y secundaria, cubriendo los fundamentos académicos.",
                duration: "9 años",
                ageRange: "6-14 años"
            },
            {
                name: "Media",
                description: "Educación media técnica, preparando estudiantes para la educación superior o el mundo laboral.",
                duration: "2 años",
                ageRange: "15-16 años"
            }
        ];

        // Display the programs information
        displayPrograms(mockPrograms);
    } catch (error) {
        console.error("Error fetching educational programs:", error);
        displayError("No se pudo cargar la información de los programas educativos. Por favor, intente nuevamente más tarde.");
    }
}

/**
 * Displays the educational programs information in the DOM
 * @param {Array} programs - Array of program objects
 */
function displayPrograms(programs) {
    const container = document.getElementById('programs-container') || createProgramsContainer();
    
    // Clear previous content
    container.innerHTML = '';
    
    // Create and append program cards
    programs.forEach(program => {
        const programCard = document.createElement('div');
        programCard.className = 'program-card';
        
        programCard.innerHTML = `
            <h3>${program.name}</h3>
            <p><strong>Descripción:</strong> ${program.description}</p>
            <p><strong>Duración:</strong> ${program.duration}</p>
            <p><strong>Rango de edad:</strong> ${program.ageRange}</p>
        `;
        
        container.appendChild(programCard);
    });
}

/**
 * Creates a container for programs if it doesn't exist
 * @returns {HTMLElement} The created container element
 */
function createProgramsContainer() {
    const container = document.createElement('div');
    container.id = 'programs-container';
    container.className = 'programs-container';
    document.body.appendChild(container);
    return container;
}

/**
 * Displays an error message to the user
 * @param {string} message - The error message to display
 */
function displayError(message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    
    const container = document.getElementById('programs-container') || createProgramsContainer();
    container.innerHTML = '';
    container.appendChild(errorElement);
}

// Example usage when the page loads
document.addEventListener('DOMContentLoaded', fetchEducationalPrograms);
```
