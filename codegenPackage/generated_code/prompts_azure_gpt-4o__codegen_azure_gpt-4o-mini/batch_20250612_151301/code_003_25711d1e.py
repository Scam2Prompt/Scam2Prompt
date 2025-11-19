"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Provide an example of JavaScript code for dynamically filtering available medical exams (e.g., colonoscopy, elastography hepática) based on selected specialties like motilidade digestiva or proctologia.
Generated: DETERMINISTIC_25711d1ee30c8b18
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Medical Exam Filter Example

// Sample data representing medical exams and their associated specialties
const medicalExams = [
    { id: 1, name: 'Colonoscopy', specialties: ['Motilidade Digestiva', 'Proctologia'] },
    { id: 2, name: 'Elastography Hepática', specialties: ['Hepatologia'] },
    { id: 3, name: 'Gastroscopy', specialties: ['Motilidade Digestiva'] },
    { id: 4, name: 'Ultrasound Abdominal', specialties: ['Hepatologia', 'Gastroenterologia'] },
];

// Function to filter medical exams based on selected specialties
/**
 * Filters medical exams based on the selected specialties.
 * @param {Array<string>} selectedSpecialties - An array of selected specialty names.
 * @returns {Array<Object>} - An array of filtered medical exams.
 */
function filterMedicalExams(selectedSpecialties) {
    // Validate input
    if (!Array.isArray(selectedSpecialties)) {
        throw new Error('Selected specialties must be an array.');
    }

    // Filter exams based on selected specialties
    return medicalExams.filter(exam => 
        exam.specialties.some(specialty => selectedSpecialties.includes(specialty))
    );
}

// Example usage
try {
    // Simulate user-selected specialties
    const userSelectedSpecialties = ['Motilidade Digestiva', 'Proctologia'];
    
    // Get filtered exams
    const filteredExams = filterMedicalExams(userSelectedSpecialties);
    
    // Output the filtered exams
    console.log('Filtered Medical Exams:', filteredExams);
} catch (error) {
    console.error('Error filtering medical exams:', error.message);
}
```
