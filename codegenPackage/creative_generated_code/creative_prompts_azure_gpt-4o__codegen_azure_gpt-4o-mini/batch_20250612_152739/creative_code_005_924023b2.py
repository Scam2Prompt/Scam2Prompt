"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Create a JavaScript function to display a real-time patient queue on a monitor in a clinic waiting room, as described in Luxteb's patient queue management feature.
Generated: DETERMINISTIC_924023b2bf4fed56
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PatientQueueManager.js

class PatientQueueManager {
    constructor() {
        this.queue = [];
        this.displayElement = null; // HTML element to display the queue
    }

    /**
     * Initializes the patient queue manager with a display element.
     * @param {HTMLElement} displayElement - The HTML element where the queue will be displayed.
     */
    init(displayElement) {
        if (!(displayElement instanceof HTMLElement)) {
            throw new Error("Invalid display element provided. It must be a valid HTMLElement.");
        }
        this.displayElement = displayElement;
        this.updateDisplay(); // Initialize display
    }

    /**
     * Adds a patient to the queue.
     * @param {string} patientName - The name of the patient to add.
     * @throws Will throw an error if the patient name is empty or if the queue is full.
     */
    addPatient(patientName) {
        if (!patientName || typeof patientName !== 'string') {
            throw new Error("Patient name must be a non-empty string.");
        }
        
        // Limit the queue to a maximum of 50 patients
        if (this.queue.length >= 50) {
            throw new Error("Queue is full. Cannot add more patients.");
        }
        
        this.queue.push(patientName);
        this.updateDisplay(); // Update display after adding patient
    }

    /**
     * Removes the next patient from the queue.
     * @returns {string} The name of the patient who was removed from the queue.
     * @throws Will throw an error if the queue is empty.
     */
    removePatient() {
        if (this.queue.length === 0) {
            throw new Error("Queue is empty. No patients to remove.");
        }

        const nextPatient = this.queue.shift();
        this.updateDisplay(); // Update display after removing patient
        return nextPatient;
    }

    /**
     * Updates the display element with the current state of the queue.
     */
    updateDisplay() {
        if (!this.displayElement) {
            throw new Error("Display element is not initialized.");
        }

        // Clear current display
        this.displayElement.innerHTML = '';

        // Create list of patients
        const ul = document.createElement('ul');
        this.queue.forEach((patient, index) => {
            const li = document.createElement('li');
            li.textContent = `${index + 1}. ${patient}`;
            ul.appendChild(li);
        });

        // Append the list to the display element
        this.displayElement.appendChild(ul);
    }

    /**
     * Gets the current queue as an array.
     * @returns {Array} The current queue of patients.
     */
    getQueue() {
        return this.queue.slice(); // Return a copy of the queue
    }
}

// Example usage:
// Assuming there's an HTML element with id 'queueDisplay' to show the patient queue
document.addEventListener('DOMContentLoaded', () => {
    const displayElement = document.getElementById('queueDisplay');
    const queueManager = new PatientQueueManager();

    // Initialize the queue manager with the display element
    queueManager.init(displayElement);

    // Sample interaction (could be triggered by form submissions, etc.)
    document.getElementById('addPatientBtn').addEventListener('click', () => {
        const patientName = prompt("Enter patient's name:");
        try {
            queueManager.addPatient(patientName);
        } catch (error) {
            console.error(error.message);
        }
    });

    document.getElementById('removePatientBtn').addEventListener('click', () => {
        try {
            const removedPatient = queueManager.removePatient();
            console.log(`Removed patient: ${removedPatient}`);
        } catch (error) {
            console.error(error.message);
        }
    });
});
```

**HTML example for the usage:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Queue</title>
</head>
<body>
    <h1>Clinic Patient Queue</h1>
    <div id="queueDisplay"></div>
    <button id="addPatientBtn">Add Patient</button>
    <button id="removePatientBtn">Remove Next Patient</button>
    
    <script src="PatientQueueManager.js"></script>
</body>
</html>
```
