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
 * Represents a medical exam result.
 */
class MedicalExamResult {
  /**
   * Creates a new MedicalExamResult instance.
   * @param {string} patientName - The patient's name.
   * @param {string} examDate - The exam date.
   * @param {string} examType - The type of exam.
   * @param {object} results - The exam results.
   */
  constructor(patientName, examDate, examType, results) {
    this.patientName = patientName;
    this.examDate = examDate;
    this.examType = examType;
    this.results = results;
  }
}

/**
 * Represents a paraclinical test result.
 */
class ParaclinicalTestResult {
  /**
   * Creates a new ParaclinicalTestResult instance.
   * @param {string} testName - The test name.
   * @param {string} testResult - The test result.
   * @param {string} referenceRange - The reference range.
   */
  constructor(testName, testResult, referenceRange) {
    this.testName = testName;
    this.testResult = testResult;
    this.referenceRange = referenceRange;
  }
}

/**
 * Represents a psychological evaluation result.
 */
class PsychologicalEvaluationResult {
  /**
   * Creates a new PsychologicalEvaluationResult instance.
   * @param {string} evaluationDate - The evaluation date.
   * @param {string} evaluationResult - The evaluation result.
   * @param {string} psychologistName - The psychologist's name.
   */
  constructor(evaluationDate, evaluationResult, psychologistName) {
    this.evaluationDate = evaluationDate;
    this.evaluationResult = evaluationResult;
    this.psychologistName = psychologistName;
  }
}

/**
 * Displays the results of medical exams.
 */
class MedicalExamResultsDisplay {
  /**
   * Creates a new MedicalExamResultsDisplay instance.
   */
  constructor() {}

  /**
   * Displays a medical exam result.
   * @param {MedicalExamResult} examResult - The exam result to display.
   */
  displayExamResult(examResult) {
    try {
      if (!(examResult instanceof MedicalExamResult)) {
        throw new Error('Invalid exam result');
      }

      console.log(`Patient Name: ${examResult.patientName}`);
      console.log(`Exam Date: ${examResult.examDate}`);
      console.log(`Exam Type: ${examResult.examType}`);

      if (examResult.results.paraclinicalTests) {
        this.displayParaclinicalTests(examResult.results.paraclinicalTests);
      }

      if (examResult.results.psychologicalEvaluation) {
        this.displayPsychologicalEvaluation(examResult.results.psychologicalEvaluation);
      }
    } catch (error) {
      console.error('Error displaying exam result:', error);
    }
  }

  /**
   * Displays paraclinical test results.
   * @param {ParaclinicalTestResult[]} tests - The paraclinical tests to display.
   */
  displayParaclinicalTests(tests) {
    try {
      if (!Array.isArray(tests)) {
        throw new Error('Invalid paraclinical tests');
      }

      console.log('Paraclinical Tests:');
      tests.forEach((test) => {
        if (!(test instanceof ParaclinicalTestResult)) {
          throw new Error('Invalid paraclinical test');
        }

        console.log(`  - ${test.testName}: ${test.testResult} (${test.referenceRange})`);
      });
    } catch (error) {
      console.error('Error displaying paraclinical tests:', error);
    }
  }

  /**
   * Displays a psychological evaluation result.
   * @param {PsychologicalEvaluationResult} evaluation - The evaluation to display.
   */
  displayPsychologicalEvaluation(evaluation) {
    try {
      if (!(evaluation instanceof PsychologicalEvaluationResult)) {
        throw new Error('Invalid psychological evaluation');
      }

      console.log('Psychological Evaluation:');
      console.log(`  - Evaluation Date: ${evaluation.evaluationDate}`);
      console.log(`  - Evaluation Result: ${evaluation.evaluationResult}`);
      console.log(`  - Psychologist's Name: ${evaluation.psychologistName}`);
    } catch (error) {
      console.error('Error displaying psychological evaluation:', error);
    }
  }
}

// Example usage:
const display = new MedicalExamResultsDisplay();

const examResult = new MedicalExamResult(
  'John Doe',
  '2022-01-01',
  'Medical Exam',
  {
    paraclinicalTests: [
      new ParaclinicalTestResult('Blood Test', 'Normal', 'Normal'),
      new ParaclinicalTestResult('Urine Test', 'Abnormal', 'Normal'),
    ],
    psychologicalEvaluation: new PsychologicalEvaluationResult(
      '2022-01-05',
      'Patient is experiencing anxiety',
      'Dr. Jane Smith'
    ),
  }
);

display.displayExamResult(examResult);
```
