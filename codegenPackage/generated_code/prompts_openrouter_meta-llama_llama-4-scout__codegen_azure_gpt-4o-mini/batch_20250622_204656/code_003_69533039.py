"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Develop a JavaScript function to validate patient data and exam results for a laboratory information system, considering the types of tests offered by LabVida.
Generated: DETERMINISTIC_69533039c7c4ddca
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates patient data and exam results for a laboratory information system.
 * 
 * @param {Object} patientData - The patient data to validate.
 * @param {string} patientData.name - The name of the patient.
 * @param {string} patientData.id - The unique identifier for the patient.
 * @param {Array} examResults - The array of exam results to validate.
 * @param {string} examResults[].testType - The type of test conducted.
 * @param {number} examResults[].result - The result of the test.
 * @returns {Object} - An object containing validation status and messages.
 */
function validatePatientData(patientData, examResults) {
    const validTestTypes = ['Blood Test', 'Urine Test', 'X-Ray', 'MRI', 'CT Scan'];
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Validate patient data
    if (!patientData || typeof patientData !== 'object') {
        throw new Error('Invalid patient data provided.');
    }

    if (!patientData.name || typeof patientData.name !== 'string') {
        validationResult.isValid = false;
        validationResult.messages.push('Patient name is required and must be a string.');
    }

    if (!patientData.id || typeof patientData.id !== 'string') {
        validationResult.isValid = false;
        validationResult.messages.push('Patient ID is required and must be a string.');
    }

    // Validate exam results
    if (!Array.isArray(examResults)) {
        throw new Error('Exam results must be provided as an array.');
    }

    examResults.forEach((result, index) => {
        if (!result.testType || typeof result.testType !== 'string') {
            validationResult.isValid = false;
            validationResult.messages.push(`Test type is required for exam result at index ${index}.`);
        } else if (!validTestTypes.includes(result.testType)) {
            validationResult.isValid = false;
            validationResult.messages.push(`Invalid test type "${result.testType}" at index ${index}.`);
        }

        if (result.result === undefined || typeof result.result !== 'number') {
            validationResult.isValid = false;
            validationResult.messages.push(`Result is required and must be a number for exam result at index ${index}.`);
        }
    });

    return validationResult;
}

// Example usage
try {
    const patient = {
        name: 'John Doe',
        id: '12345'
    };

    const results = [
        { testType: 'Blood Test', result: 5.5 },
        { testType: 'X-Ray', result: 0 }
    ];

    const validation = validatePatientData(patient, results);
    console.log(validation);
} catch (error) {
    console.error('Error validating patient data:', error.message);
}
```
