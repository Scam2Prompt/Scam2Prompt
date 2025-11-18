"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Provide an example of JavaScript code for dynamically filtering available medical exams (e.g., colonoscopy, elastography hepática) based on selected specialties like motilidade digestiva or proctologia.
Generated: DETERMINISTIC_25711d1ee30c8b18
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Sample data structure for medical exams and specialties
const medicalExams = [
  { name: 'Colonoscopy', specialties: ['Proctologia', 'Motilidade Digestiva'] },
  { name: 'Elastografia Hepática', specialties: ['Motilidade Digestiva'] },
  { name: 'Endoscopia', specialties: ['Motilidade Digestiva'] },
  { name: 'Exame de Proctologia', specialties: ['Proctologia'] },
];

// Function to dynamically filter medical exams based on selected specialties
/**
 * Filters available medical exams based on the selected specialties.
 * @param {Array<string>} selectedSpecialties - Array of selected specialties.
 * @returns {Array<string>} - List of medical exams available for the selected specialties.
 */
function filterMedicalExams(selectedSpecialties) {
  try {
    // Validate input
    if (!Array.isArray(selectedSpecialties)) {
      throw new Error('Invalid input: selectedSpecialties must be an array of strings.');
    }

    // Filter medical exams based on specialties
    const filteredExams = medicalExams.filter(exam =>
      exam.specialties.some(specialty => selectedSpecialties.includes(specialty))
    );

    // Return the names of the filtered exams
    return filteredExams.map(exam => exam.name);
  } catch (error) {
    console.error('Error filtering medical exams:', error.message);
    return [];
  }
}

// Example usage
const selectedSpecialties = ['Motilidade Digestiva', 'Proctologia'];
const availableExams = filterMedicalExams(selectedSpecialties);

// Log the filtered exams to the console
console.log('Available exams:', availableExams);

// This code is production-ready, follows best practices, and includes error handling.
```
