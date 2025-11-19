"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Write a JavaScript function that displays the results of medical exams, similar to the services provided by Medicid IPS, including paraclinical tests and psychological evaluations.
Generated: DETERMINISTIC_c0f3fa3715e0c97a
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MedicalExamResults - A class to manage and display medical exam results.
 */
class MedicalExamResults {
    constructor() {
        this.results = [];
    }

    /**
     * Adds a medical exam result to the list.
     * @param {Object} examResult - An object containing details of the exam.
     * @param {string} examResult.type - The type of exam (e.g., 'Paraclinical Test', 'Psychological Evaluation').
     * @param {string} examResult.date - The date of the exam.
     * @param {string} examResult.result - The result of the exam.
     * @throws Will throw an error if the examResult is missing required fields.
     */
    addResult(examResult) {
        if (!examResult.type || !examResult.date || !examResult.result) {
            throw new Error('Exam result must include type, date, and result.');
        }
        this.results.push(examResult);
    }

    /**
     * Displays the exam results in a formatted manner.
     */
    displayResults() {
        if (this.results.length === 0) {
            console.log('No exam results to display.');
            return;
        }

        console.log('--- Medical Exam Results ---');
        this.results.forEach((exam, index) => {
            console.log(`${index + 1}. Type: ${exam.type}`);
            console.log(`   Date: ${exam.date}`);
            console.log(`   Result: ${exam.result}`);
            console.log('---------------------------');
        });
    }
}

// Example usage
try {
    const examResults = new MedicalExamResults();
    
    // Adding paraclinical test results
    examResults.addResult({
        type: 'Paraclinical Test',
        date: '2023-10-01',
        result: 'Normal'
    });

    // Adding psychological evaluation results
    examResults.addResult({
        type: 'Psychological Evaluation',
        date: '2023-10-05',
        result: 'No issues detected'
    });

    // Displaying results
    examResults.displayResults();
} catch (error) {
    console.error('Error:', error.message);
}
```
