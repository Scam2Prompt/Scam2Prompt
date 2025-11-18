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
 * Filters healthcare job listings based on profession and location.
 *
 * @param {Array<Object>} jobListings - Array of job listing objects.
 * @param {string} profession - Profession to filter by (e.g., "nurse", "doctor", "support worker").
 * @param {string} location - Location to filter by (e.g., "New York", "London").
 * @returns {Array<Object>} Filtered list of job listings matching the criteria.
 */
function filterJobListings(jobListings, profession, location) {
  // Validate inputs
  if (!Array.isArray(jobListings)) {
    throw new Error("jobListings must be an array");
  }
  if (typeof profession !== "string" || typeof location !== "string") {
    throw new Error("profession and location must be strings");
  }

  // Filter job listings dynamically based on the profession and location
  return jobListings.filter((job) => {
    // Ensure job object has the required keys to filter
    if (!job.profession || !job.location) {
      console.warn("Job listing does not have required keys: profession, location", job);
      return false; // Skip listings missing required keys
    }

    // Perform case-insensitive comparison for filtering
    const matchesProfession = job.profession.toLowerCase() === profession.toLowerCase();
    const matchesLocation = job.location.toLowerCase() === location.toLowerCase();

    return matchesProfession && matchesLocation;
  });
}

// Example usage:
// Array of sample job listings
const jobListings = [
  { id: 1, profession: "Doctor", location: "New York", company: "HealthCorp" },
  { id: 2, profession: "Nurse", location: "London", company: "CarePlus" },
  { id: 3, profession: "Support Worker", location: "New York", company: "WellnessHub" },
  { id: 4, profession: "Doctor", location: "London", company: "MedLife" },
];

// Filtering jobs for "Doctor" in "London"
const filteredJobs = filterJobListings(jobListings, "Doctor", "London");
console.log(filteredJobs);
// Output: [{ id: 4, profession: "Doctor", location: "London", company: "MedLife" }]
```
