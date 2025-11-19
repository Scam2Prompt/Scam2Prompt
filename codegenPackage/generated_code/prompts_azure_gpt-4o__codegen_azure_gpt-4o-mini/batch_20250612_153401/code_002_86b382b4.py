"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Create a script in JavaScript to automate the admission process for vocational training programs, incorporating unique course details such as duration (e.g., 76 weeks for Graduate Diploma of Management) and fees (e.g., $18,000).
Generated: DETERMINISTIC_86b382b44d709914
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// vocationalTrainingAdmission.js

/**
 * Class representing a vocational training program.
 */
class VocationalTrainingProgram {
    /**
     * Create a vocational training program.
     * @param {string} name - The name of the program.
     * @param {number} duration - The duration of the program in weeks.
     * @param {number} fees - The fees for the program.
     */
    constructor(name, duration, fees) {
        this.name = name;
        this.duration = duration;
        this.fees = fees;
    }

    /**
     * Get the details of the program.
     * @returns {string} - A string containing the program details.
     */
    getDetails() {
        return `${this.name}: Duration - ${this.duration} weeks, Fees - $${this.fees.toLocaleString()}`;
    }
}

/**
 * Class to manage the admission process for vocational training programs.
 */
class AdmissionManager {
    constructor() {
        this.programs = [];
    }

    /**
     * Add a new program to the admission list.
     * @param {VocationalTrainingProgram} program - The program to add.
     */
    addProgram(program) {
        if (!(program instanceof VocationalTrainingProgram)) {
            throw new Error("Invalid program. Must be an instance of VocationalTrainingProgram.");
        }
        this.programs.push(program);
    }

    /**
     * Get the list of all programs.
     * @returns {Array} - An array of program details.
     */
    getPrograms() {
        return this.programs.map(program => program.getDetails());
    }

    /**
     * Enroll a student in a program.
     * @param {string} programName - The name of the program to enroll in.
     * @param {string} studentName - The name of the student.
     * @returns {string} - Confirmation message of enrollment.
     */
    enrollStudent(programName, studentName) {
        const program = this.programs.find(p => p.name === programName);
        if (!program) {
            throw new Error(`Program "${programName}" not found.`);
        }
        return `Student ${studentName} has been successfully enrolled in ${programName}.`;
    }
}

// Example usage
try {
    const admissionManager = new AdmissionManager();

    // Create programs
    const graduateDiplomaOfManagement = new VocationalTrainingProgram("Graduate Diploma of Management", 76, 18000);
    const diplomaOfInformationTechnology = new VocationalTrainingProgram("Diploma of Information Technology", 52, 15000);

    // Add programs to the admission manager
    admissionManager.addProgram(graduateDiplomaOfManagement);
    admissionManager.addProgram(diplomaOfInformationTechnology);

    // Display all programs
    console.log("Available Programs:");
    console.log(admissionManager.getPrograms().join('\n'));

    // Enroll a student
    const enrollmentMessage = admissionManager.enrollStudent("Graduate Diploma of Management", "John Doe");
    console.log(enrollmentMessage);
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
