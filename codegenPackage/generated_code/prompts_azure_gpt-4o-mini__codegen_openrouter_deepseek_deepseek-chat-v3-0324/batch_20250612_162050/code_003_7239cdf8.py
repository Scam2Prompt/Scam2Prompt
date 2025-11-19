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
/**
 * Legal Consultation Process Application for Gava & Silva Advogados
 * This application outlines the steps involved in legal consultations:
 * 1. Consultation Phase
 * 2. Strategy Phase
 * 3. Action Phase
 */

class LegalConsultationApp {
  constructor() {
    this.phases = {
      consultation: {
        title: "Consultation Phase",
        steps: [
          "Initial client meeting",
          "Case assessment and documentation review",
          "Identification of legal issues",
          "Preliminary advice and options"
        ]
      },
      strategy: {
        title: "Strategy Phase",
        steps: [
          "Development of legal strategy",
          "Risk assessment and mitigation planning",
          "Client approval of proposed strategy",
          "Preparation of necessary legal documents"
        ]
      },
      action: {
        title: "Action Phase",
        steps: [
          "Implementation of legal strategy",
          "Representation in legal proceedings",
          "Regular client updates",
          "Case resolution and follow-up"
        ]
      }
    };
  }

  /**
   * Display all phases and their steps
   */
  displayAllPhases() {
    try {
      console.log("Gava & Silva Advogados - Legal Consultation Process\n");
      for (const phase in this.phases) {
        this.displayPhase(phase);
      }
    } catch (error) {
      console.error("Error displaying phases:", error.message);
    }
  }

  /**
   * Display a specific phase and its steps
   * @param {string} phaseName - Name of the phase to display
   */
  displayPhase(phaseName) {
    try {
      if (!this.phases[phaseName]) {
        throw new Error(`Phase '${phaseName}' not found`);
      }

      const phase = this.phases[phaseName];
      console.log(`\n${phase.title}:`);
      phase.steps.forEach((step, index) => {
        console.log(`${index + 1}. ${step}`);
      });
    } catch (error) {
      console.error(`Error displaying phase '${phaseName}':`, error.message);
    }
  }

  /**
   * Get phase information as an object
   * @param {string} phaseName - Name of the phase to retrieve
   * @returns {Object} Phase information
   */
  getPhase(phaseName) {
    try {
      if (!this.phases[phaseName]) {
        throw new Error(`Phase '${phaseName}' not found`);
      }
      return this.phases[phaseName];
    } catch (error) {
      console.error(`Error getting phase '${phaseName}':`, error.message);
      return null;
    }
  }

  /**
   * Add a new step to a phase
   * @param {string} phaseName - Name of the phase to modify
   * @param {string} step - New step to add
   */
  addStepToPhase(phaseName, step) {
    try {
      if (!this.phases[phaseName]) {
        throw new Error(`Phase '${phaseName}' not found`);
      }
      if (!step || typeof step !== "string") {
        throw new Error("Step must be a non-empty string");
      }
      this.phases[phaseName].steps.push(step);
    } catch (error) {
      console.error(`Error adding step to phase '${phaseName}':`, error.message);
    }
  }
}

// Example usage
const app = new LegalConsultationApp();

// Display all phases
app.displayAllPhases();

// Display a specific phase
app.displayPhase("strategy");

// Get phase information
const consultationPhase = app.getPhase("consultation");
console.log("\nConsultation Phase Info:", consultationPhase);

// Add a new step to a phase
app.addStepToPhase("action", "Post-case evaluation and client feedback");
app.displayPhase("action");
```
