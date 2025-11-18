"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write a function in JavaScript to dynamically filter healthcare job listings by profession (e.g., nurse, doctor, support worker) and location.
Generated: DETERMINISTIC_12b83b4ebbf4daae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters healthcare job listings by profession and location.
 * 
 * @param {Array} jobListings - Array of job listing objects to filter.
 * @param {string} profession - The profession to filter by (e.g., 'nurse', 'doctor').
 * @param {string} location - The location to filter by (e.g., 'New York').
 * @returns {Array} - An array of filtered job listings.
 * @throws {Error} - Throws an error if jobListings is not an array.
 */
function filterJobListings(jobListings, profession, location) {
    // Validate input
    if (!Array.isArray(jobListings)) {
        throw new Error("Invalid input: jobListings must be an array");
    }

    // Normalize input to lower case for case insensitive comparison
    const normalizedProfession = profession.toLowerCase();
    const normalizedLocation = location.toLowerCase();

    // Filter job listings based on profession and location
    return jobListings.filter(job => {
        const jobProfession = job.profession.toLowerCase();
        const jobLocation = job.location.toLowerCase();

        return jobProfession.includes(normalizedProfession) && jobLocation.includes(normalizedLocation);
    });
}

// Example usage:

const jobListings = [
    { id: 1, profession: 'Nurse', location: 'New York', company: 'Health Corp' },
    { id: 2, profession: 'Doctor', location: 'Los Angeles', company: 'Care Medical' },
    { id: 3, profession: 'Support Worker', location: 'New York', company: 'Support Services' },
    { id: 4, profession: 'Nurse', location: 'Los Angeles', company: 'Life Health' },
];

try {
    const filteredJobs = filterJobListings(jobListings, 'nurse', 'new york');
    console.log(filteredJobs);
} catch (error) {
    console.error("Error filtering job listings:", error.message);
}
```
