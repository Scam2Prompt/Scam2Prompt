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
 * MedicalExamResults - A class to display medical exam results including paraclinical tests and psychological evaluations.
 */
class MedicalExamResults {
  /**
   * @param {Object} options - Configuration options
   * @param {string} options.patientId - Unique patient identifier
   * @param {string} options.patientName - Full name of the patient
   * @param {Object[]} options.paraclinicalTests - Array of paraclinical test results
   * @param {Object[]} options.psychologicalEvaluations - Array of psychological evaluation results
   */
  constructor(options) {
    if (!options.patientId || !options.patientName) {
      throw new Error('Patient ID and name are required');
    }

    this.patientId = options.patientId;
    this.patientName = options.patientName;
    this.paraclinicalTests = options.paraclinicalTests || [];
    this.psychologicalEvaluations = options.psychologicalEvaluations || [];
    this.examDate = options.examDate || new Date().toISOString().split('T')[0];
  }

  /**
   * Validates a test result object
   * @param {Object} test - Test object to validate
   * @param {string[]} requiredFields - Array of required field names
   * @private
   */
  _validateTestResult(test, requiredFields) {
    if (!test || typeof test !== 'object') {
      throw new Error('Test result must be an object');
    }

    requiredFields.forEach(field => {
      if (!test[field]) {
        throw new Error(`Missing required field: ${field}`);
      }
    });
  }

  /**
   * Adds a paraclinical test result
   * @param {Object} test - Test result object
   * @param {string} test.testName - Name of the test
   * @param {string} test.result - Test result value
   * @param {string} [test.units] - Measurement units
   * @param {string} [test.referenceRange] - Normal reference range
   */
  addParaclinicalTest(test) {
    const requiredFields = ['testName', 'result'];
    this._validateTestResult(test, requiredFields);
    this.paraclinicalTests.push(test);
  }

  /**
   * Adds a psychological evaluation result
   * @param {Object} evaluation - Evaluation result object
   * @param {string} evaluation.evaluationType - Type of evaluation
   * @param {string} evaluation.result - Evaluation result
   * @param {string} [evaluation.observations] - Additional observations
   */
  addPsychologicalEvaluation(evaluation) {
    const requiredFields = ['evaluationType', 'result'];
    this._validateTestResult(evaluation, requiredFields);
    this.psychologicalEvaluations.push(evaluation);
  }

  /**
   * Generates HTML representation of the results
   * @returns {string} HTML string
   */
  generateHTMLReport() {
    const paraclinicalTestsHTML = this.paraclinicalTests.map(test => `
      <div class="test-result">
        <h4>${test.testName}</h4>
        <p><strong>Result:</strong> ${test.result} ${test.units || ''}</p>
        ${test.referenceRange ? `<p><strong>Reference Range:</strong> ${test.referenceRange}</p>` : ''}
        ${test.notes ? `<p><strong>Notes:</strong> ${test.notes}</p>` : ''}
      </div>
    `).join('');

    const psychologicalEvaluationsHTML = this.psychologicalEvaluations.map(evalItem => `
      <div class="evaluation-result">
        <h4>${evalItem.evaluationType}</h4>
        <p><strong>Result:</strong> ${evalItem.result}</p>
        ${evalItem.observations ? `<p><strong>Observations:</strong> ${evalItem.observations}</p>` : ''}
      </div>
    `).join('');

    return `
      <div class="medical-report">
        <h2>Medical Exam Results</h2>
        <div class="patient-info">
          <p><strong>Patient ID:</strong> ${this.patientId}</p>
          <p><strong>Name:</strong> ${this.patientName}</p>
          <p><strong>Exam Date:</strong> ${this.examDate}</p>
        </div>
        
        <div class="section">
          <h3>Paraclinical Tests</h3>
          ${paraclinicalTestsHTML || '<p>No paraclinical tests available.</p>'}
        </div>
        
        <div class="section">
          <h3>Psychological Evaluations</h3>
          ${psychologicalEvaluationsHTML || '<p>No psychological evaluations available.</p>'}
        </div>
      </div>
    `;
  }

  /**
   * Generates a JSON representation of the results
   * @returns {Object} JSON object
   */
  generateJSONReport() {
    return {
      patientId: this.patientId,
      patientName: this.patientName,
      examDate: this.examDate,
      paraclinicalTests: this.paraclinicalTests,
      psychologicalEvaluations: this.psychologicalEvaluations
    };
  }

  /**
   * Displays the results in the console
   */
  displayConsoleReport() {
    console.log(`Medical Exam Results for ${this.patientName} (ID: ${this.patientId})`);
    console.log(`Exam Date: ${this.examDate}\n`);
    
    console.log('Paraclinical Tests:');
    this.paraclinicalTests.forEach(test => {
      console.log(`- ${test.testName}: ${test.result} ${test.units || ''}`);
      if (test.referenceRange) console.log(`  Reference Range: ${test.referenceRange}`);
      if (test.notes) console.log(`  Notes: ${test.notes}`);
    });
    
    console.log('\nPsychological Evaluations:');
    this.psychologicalEvaluations.forEach(evalItem => {
      console.log(`- ${evalItem.evaluationType}: ${evalItem.result}`);
      if (evalItem.observations) console.log(`  Observations: ${evalItem.observations}`);
    });
  }
}

// Example usage:
/*
const examResults = new MedicalExamResults({
  patientId: 'PAT12345',
  patientName: 'John Doe',
  examDate: '2023-11-15'
});

examResults.addParaclinicalTest({
  testName: 'Complete Blood Count',
  result: 'Normal',
  notes: 'All parameters within normal limits'
});

examResults.addParaclinicalTest({
  testName: 'Glucose',
  result: '95',
  units: 'mg/dL',
  referenceRange: '70-99 mg/dL'
});

examResults.addPsychologicalEvaluation({
  evaluationType: 'Depression Screening',
  result: 'Mild symptoms',
  observations: 'Recommended follow-up in 3 months'
});

console.log(examResults.generateJSONReport());
console.log(examResults.generateHTMLReport());
examResults.displayConsoleReport();
*/
```
