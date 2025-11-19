"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Write a JavaScript function that displays the results of medical exams, similar to the services provided by Medicid IPS, including paraclinical tests and psychological evaluations.
Generated: DETERMINISTIC_c0f3fa3715e0c97a
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MedicalExamResults class to manage and display medical exam results.
 */
class MedicalExamResults {
    constructor() {
        this.results = [];
    }

    /**
     * Adds a new exam result to the list.
     * @param {string} examType - The type of the exam (e.g., 'Paraclinical', 'Psychological').
     * @param {string} patientName - The name of the patient.
     * @param {string} result - The result of the exam.
     * @throws Will throw an error if any parameter is missing or invalid.
     */
    addResult(examType, patientName, result) {
        if (!examType || !patientName || !result) {
            throw new Error('All parameters (examType, patientName, result) are required.');
        }

        const examResult = {
            examType,
            patientName,
            result,
            date: new Date().toISOString()
        };

        this.results.push(examResult);
    }

    /**
     * Displays all exam results in a formatted manner.
     */
    displayResults() {
        if (this.results.length === 0) {
            console.log('No exam results available.');
            return;
        }

        console.log('--- Medical Exam Results ---');
        this.results.forEach((exam, index) => {
            console.log(`Result #${index + 1}:`);
            console.log(`  Exam Type: ${exam.examType}`);
            console.log(`  Patient Name: ${exam.patientName}`);
            console.log(`  Result: ${exam.result}`);
            console.log(`  Date: ${exam.date}`);
            console.log('-----------------------------');
        });
    }
}

// Example usage:
try {
    const medicalExamResults = new MedicalExamResults();
    medicalExamResults.addResult('Paraclinical', 'John Doe', 'Normal');
    medicalExamResults.addResult('Psychological', 'Jane Smith', 'Anxiety diagnosed');
    medicalExamResults.displayResults();
} catch (error) {
    console.error('Error:', error.message);
}
```
