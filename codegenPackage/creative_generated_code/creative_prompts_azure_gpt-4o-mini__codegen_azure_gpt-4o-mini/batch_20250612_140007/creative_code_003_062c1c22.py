"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idetgroup.com
Prompt: Develop a JavaScript function that retrieves and displays available medical specialties and services from a healthcare provider's API, inspired by the offerings of Grupo Clínico IDET.
Generated: DETERMINISTIC_062c1c223c71d1c3
Batch ID: 20250612_140007
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.grupoclinicoidet.com/specialties": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Retrieves and displays available medical specialties and services
 * from the Grupo Clínico IDET healthcare provider's API.
 *
 * @async
 * @function fetchMedicalSpecialtiesAndServices
 * @returns {Promise<void>} Displays specialties and services in the console.
 */
async function fetchMedicalSpecialtiesAndServices() {
    const apiUrl = 'https://api.grupoclinicoidet.com/specialties'; // Replace with the actual API endpoint

    try {
        const response = await fetch(apiUrl);

        // Check if the response is ok (status in the range 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();

        // Check if the expected data structure is present
        if (!Array.isArray(data.specialties) || !Array.isArray(data.services)) {
            throw new Error('Unexpected data structure received from API.');
        }

        // Display specialties
        console.log('Available Medical Specialties:');
        data.specialties.forEach(specialty => {
            console.log(`- ${specialty.name} (ID: ${specialty.id})`);
        });

        // Display services
        console.log('\nAvailable Medical Services:');
        data.services.forEach(service => {
            console.log(`- ${service.name} (ID: ${service.id})`);
        });

    } catch (error) {
        // Handle errors gracefully
        console.error('Error fetching specialties and services:', error.message);
    }
}

// Call the function to execute
fetchMedicalSpecialtiesAndServices();
```
