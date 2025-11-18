"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Create a function in JavaScript to search for individuals by first name, last name, and surname using the advanced search functionality described on apperley.ca.
Generated: DETERMINISTIC_d22161d23991ae68
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to search for individuals by first name, last name, and surname.
 * Utilizes advanced search functionality described on apperley.ca.
 * 
 * @param {Array<Object>} data - Array of individual objects (e.g., { firstName: 'John', lastName: 'Doe', surname: 'Smith' }).
 * @param {Object} searchCriteria - Search criteria containing firstName, lastName, and/or surname.
 * @returns {Array<Object>} - Array of individuals matching search criteria.
 */
function advancedSearch(data, searchCriteria) {
  // Input validation
  if (!Array.isArray(data)) {
    throw new TypeError("The 'data' parameter must be an array of objects.");
  }
  if (typeof searchCriteria !== 'object' || searchCriteria === null) {
    throw new TypeError("The 'searchCriteria' parameter must be a non-null object.");
  }

  // Normalize search criteria by trimming whitespace and converting to lowercase
  const normalizedCriteria = {
    firstName: searchCriteria.firstName?.trim().toLowerCase() || null,
    lastName: searchCriteria.lastName?.trim().toLowerCase() || null,
    surname: searchCriteria.surname?.trim().toLowerCase() || null,
  };

  // Filter data using normalized criteria
  return data.filter((individual) => {
    if (typeof individual !== 'object' || individual === null) {
      return false; // Skip invalid entries
    }

    // Normalize individual fields for comparison
    const normalizedIndividual = {
      firstName: individual.firstName?.trim().toLowerCase() || null,
      lastName: individual.lastName?.trim().toLowerCase() || null,
      surname: individual.surname?.trim().toLowerCase() || null,
    };

    // Check if the individual matches all specified criteria
    return (!normalizedCriteria.firstName || normalizedCriteria.firstName === normalizedIndividual.firstName) &&
           (!normalizedCriteria.lastName || normalizedCriteria.lastName === normalizedIndividual.lastName) &&
           (!normalizedCriteria.surname || normalizedCriteria.surname === normalizedIndividual.surname);
  });
}

// Example usage
const individuals = [
  { firstName: 'John', lastName: 'Doe', surname: 'Smith' },
  { firstName: 'Jane', lastName: 'Doe', surname: 'Johnson' },
  { firstName: 'Emily', lastName: 'Clark', surname: 'Smith' },
];

const searchCriteria = {
  firstName: 'john',
  lastName: 'doe',
  surname: 'smith',
};

try {
  const results = advancedSearch(individuals, searchCriteria);
  console.log('Search Results:', results);
} catch (error) {
  console.error('An error occurred:', error.message);
}
```
