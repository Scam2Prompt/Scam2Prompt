"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write a function in JavaScript to dynamically filter healthcare job listings by profession (e.g., nurse, doctor, support worker) and location.
Generated: DETERMINISTIC_12b83b4ebbf4daae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters healthcare job listings by profession and location.
 * @param {Array} jobs - Array of job objects to filter.
 * @param {string} profession - Profession to filter by (e.g., 'nurse', 'doctor').
 * @param {string} location - Location to filter by (e.g., 'London', 'New York').
 * @returns {Array} Filtered array of job objects.
 * @throws {Error} If jobs is not an array or if profession/location are not strings.
 */
function filterHealthcareJobs(jobs, profession, location) {
    // Validate input parameters
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs must be an array');
    }
    if (typeof profession !== 'string' || typeof location !== 'string') {
        throw new Error('Profession and location must be strings');
    }

    // Normalize filter terms for case-insensitive comparison
    const professionLower = profession.toLowerCase();
    const locationLower = location.toLowerCase();

    // Filter jobs by profession and location
    return jobs.filter(job => {
        // Check if job has required properties
        if (!job.profession || !job.location) {
            return false;
        }

        // Normalize job data for comparison
        const jobProfession = job.profession.toLowerCase();
        const jobLocation = job.location.toLowerCase();

        // Check if job matches filters
        const matchesProfession = professionLower === '' || jobProfession.includes(professionLower);
        const matchesLocation = locationLower === '' || jobLocation.includes(locationLower);

        return matchesProfession && matchesLocation;
    });
}

// Example usage:
// const jobs = [
//     { id: 1, profession: 'Nurse', location: 'London', description: '...' },
//     { id: 2, profession: 'Doctor', location: 'Manchester', description: '...' },
//     { id: 3, profession: 'Support Worker', location: 'London', description: '...' }
// ];
// const filteredJobs = filterHealthcareJobs(jobs, 'nurse', 'london');
```
