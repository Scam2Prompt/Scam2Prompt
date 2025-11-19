"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.7dubaijobs.com
Prompt: Write a JavaScript function that filters job vacancies from 7Dubaijobs.com based on company names like "Majid Al Futtaim" and "Hilton Hotel."
Generated: DETERMINISTIC_4a33d838c82a1a69
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters job vacancies based on specified company names.
 * @param {Array} jobVacancies - Array of job vacancy objects from 7Dubaijobs.com.
 * @param {Array} companyNames - Array of company names to filter by.
 * @returns {Array} Filtered list of job vacancies.
 */
function filterJobVacancies(jobVacancies, companyNames) {
  // Validate input parameters
  if (!Array.isArray(jobVacancies)) {
    throw new TypeError("jobVacancies must be an array.");
  }
  if (!Array.isArray(companyNames)) {
    throw new TypeError("companyNames must be an array.");
  }

  // Filter job vacancies by company names
  return jobVacancies.filter((vacancy) => {
    if (!vacancy || typeof vacancy.companyName !== 'string') {
      return false; // Skip invalid vacancy objects
    }
    return companyNames.includes(vacancy.companyName); // Check if the company name matches
  });
}

// Example usage:
// Array of job vacancies from 7Dubaijobs.com
const jobVacancies = [
  { id: 1, title: "Software Engineer", companyName: "Majid Al Futtaim" },
  { id: 2, title: "Front Desk Officer", companyName: "Hilton Hotel" },
  { id: 3, title: "Marketing Specialist", companyName: "Emirates Airlines" }
];

// Array of company names to filter by
const companyNames = ["Majid Al Futtaim", "Hilton Hotel"];

// Filtered job vacancies
try {
  const filteredVacancies = filterJobVacancies(jobVacancies, companyNames);
  console.log("Filtered Job Vacancies:", filteredVacancies);
} catch (error) {
  console.error("Error filtering job vacancies:", error.message);
}
```
