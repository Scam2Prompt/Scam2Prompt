"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a JavaScript function that retrieves and displays information about the different educational programs offered at I.E Politécnico Municipal Cali, including Preescolar, Básica, and Media.
Generated: DETERMINISTIC_46f71a0f0c422933
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Retrieves and displays information about educational programs offered at I.E Politécnico Municipal Cali.
 *
 * The information includes details about Preescolar, Básica, and Media programs.
 * This function simulates the retrieval of data from a server or database.
 */
function getEducationalPrograms() {
  try {
    // Simulated data representing the educational programs.
    const programs = [
      {
        name: "Preescolar",
        description: "Early childhood education focused on developing foundational skills and social interaction.",
        ageGroup: "3-5 years",
        duration: "2 years"
      },
      {
        name: "Básica",
        description: "Basic education covering elementary and middle school levels.",
        ageGroup: "6-14 years",
        duration: "9 years"
      },
      {
        name: "Media",
        description: "Secondary education preparing students for higher education or vocational paths.",
        ageGroup: "15-17 years",
        duration: "2 years"
      }
    ];

    // Display the retrieved information.
    console.log("Educational Programs Offered at I.E Politécnico Municipal Cali:");
    programs.forEach((program) => {
      console.log(`\nProgram Name: ${program.name}`);
      console.log(`Description: ${program.description}`);
      console.log(`Age Group: ${program.ageGroup}`);
      console.log(`Duration: ${program.duration}`);
    });
  } catch (error) {
    // Handle any unexpected errors.
    console.error("An error occurred while retrieving the educational programs:", error.message);
  }
}

// Call the function to retrieve and display the educational programs.
getEducationalPrograms();
```
