"""
Generated Code Metadata:
========================
Original URL: https://gavasilva.adv.br
Prompt: Develop a JavaScript application that helps users understand the steps involved in legal consultations at Gava & Silva Advogados, highlighting the consultation, strategy, and action phases.
Generated: DETERMINISTIC_7239cdf8f8ceb7ac
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Legal Consultation Application for Gava & Silva Advogados

// Define a class to represent the Legal Consultation process
class LegalConsultation {
    constructor() {
        this.phases = {
            consultation: "Consultation Phase: Initial meeting to understand the client's needs.",
            strategy: "Strategy Phase: Developing a tailored legal strategy based on the client's situation.",
            action: "Action Phase: Implementing the legal strategy and taking necessary actions."
        };
    }

    // Method to get the description of all phases
    getPhases() {
        return Object.values(this.phases);
    }

    // Method to get a specific phase description
    getPhase(phase) {
        if (this.phases[phase]) {
            return this.phases[phase];
        } else {
            throw new Error("Invalid phase requested. Please choose 'consultation', 'strategy', or 'action'.");
        }
    }
}

// Function to display the phases in the console
function displayPhases() {
    const consultation = new LegalConsultation();
    console.log("Legal Consultation Phases:\n");

    // Get all phases and display them
    const phases = consultation.getPhases();
    phases.forEach((phase, index) => {
        console.log(`${index + 1}. ${phase}`);
    });
}

// Function to display a specific phase based on user input
function displaySpecificPhase(phase) {
    const consultation = new LegalConsultation();
    try {
        const phaseDescription = consultation.getPhase(phase);
        console.log(`\n${phaseDescription}`);
    } catch (error) {
        console.error(error.message);
    }
}

// Main function to run the application
function main() {
    // Display all phases
    displayPhases();

    // Example of displaying a specific phase
    const userRequestedPhase = 'strategy'; // This can be dynamically set based on user input
    displaySpecificPhase(userRequestedPhase);
}

// Run the application
main();
```
