"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Create a function in JavaScript to search for individuals by first name, last name, and surname using the advanced search functionality described on apperley.ca.
Generated: DETERMINISTIC_d22161d23991ae68
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents an individual with first name, last name, and surname.
 */
class Individual {
    /**
     * Creates an instance of Individual.
     * 
     * @param {string} firstName - The first name of the individual.
     * @param {string} lastName - The last name of the individual.
     * @param {string} surname - The surname of the individual.
     */
    constructor(firstName, lastName, surname) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.surname = surname;
    }
}

/**
 * Advanced search functionality to find individuals by first name, last name, and surname.
 */
class AdvancedSearch {
    /**
     * Creates an instance of AdvancedSearch.
     * 
     * @param {Individual[]} individuals - The list of individuals to search through.
     */
    constructor(individuals) {
        this.individuals = individuals;
    }

    /**
     * Searches for individuals by first name, last name, and surname.
     * 
     * @param {string} [firstName] - The first name to search for.
     * @param {string} [lastName] - The last name to search for.
     * @param {string} [surname] - The surname to search for.
     * @returns {Individual[]} The list of individuals matching the search criteria.
     */
    search({ firstName, lastName, surname } = {}) {
        if (!this.individuals) {
            throw new Error("No individuals to search through.");
        }

        return this.individuals.filter(individual => {
            const firstNameMatch = !firstName || individual.firstName.toLowerCase().includes(firstName.toLowerCase());
            const lastNameMatch = !lastName || individual.lastName.toLowerCase().includes(lastName.toLowerCase());
            const surnameMatch = !surname || individual.surname.toLowerCase().includes(surname.toLowerCase());

            return firstNameMatch && lastNameMatch && surnameMatch;
        });
    }
}

// Example usage:
function main() {
    try {
        const individuals = [
            new Individual("John", "Doe", "Smith"),
            new Individual("Jane", "Doe", "Johnson"),
            new Individual("Bob", "Smith", "Williams")
        ];

        const advancedSearch = new AdvancedSearch(individuals);

        const results1 = advancedSearch.search({ firstName: "John" });
        console.log("Search results for first name 'John':");
        console.log(results1);

        const results2 = advancedSearch.search({ lastName: "Doe" });
        console.log("Search results for last name 'Doe':");
        console.log(results2);

        const results3 = advancedSearch.search({ surname: "Smith" });
        console.log("Search results for surname 'Smith':");
        console.log(results3);
    } catch (error) {
        console.error("Error:", error.message);
    }
}

main();
```
