"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wazfnynow.com
Prompt: Write a script in JavaScript to filter and display job postings from "وظفني الان" for Oman-based roles in universities, including qualifications and salary details.
Generated: DETERMINISTIC_63655642bbc8e790
Batch ID: 20250612_151811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wazfni-alan.com/jobs": {
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
 * Script to fetch, filter, and display job postings from "وظفني الان" 
 * for Oman-based roles in universities, including qualifications and salary details.
 * 
 * Assumptions:
 * - The API endpoint for "وظفني الان" provides job data in JSON format.
 * - Each job object contains fields: location, companyType, qualifications, salary, and other relevant details.
 * - Modify the API URL or request format as necessary to match actual API structure.
 */

const axios = require('axios'); // Dependency for HTTP requests

// Base URL for "وظفني الان" API (replace with actual URL)
const API_URL = 'https://api.wazfni-alan.com/jobs';

/**
 * Fetch job postings from the API.
 * @returns {Promise<Array>} List of job postings.
 */
async function fetchJobPostings() {
  try {
    const response = await axios.get(API_URL);
    return response.data; // Assuming the API returns a JSON array of job postings
  } catch (error) {
    console.error('Error fetching job postings:', error.message);
    throw new Error('Failed to fetch job postings from the API.');
  }
}

/**
 * Filter job postings for Oman-based university roles.
 * @param {Array} jobs - List of job postings.
 * @returns {Array} Filtered list of job postings.
 */
function filterJobPostings(jobs) {
  return jobs.filter(job => 
    job.location.includes('Oman') && 
    job.companyType.toLowerCase() === 'university'
  );
}

/**
 * Display filtered job postings in a readable format.
 * @param {Array} jobs - List of filtered job postings.
 */
function displayJobPostings(jobs) {
  if (jobs.length === 0) {
    console.log('No university job postings found in Oman.');
    return;
  }

  console.log('University Job Postings in Oman:');
  jobs.forEach((job, index) => {
    console.log(`\nJob #${index + 1}:`);
    console.log(`Title: ${job.title}`);
    console.log(`Location: ${job.location}`);
    console.log(`Qualifications: ${job.qualifications || 'N/A'}`);
    console.log(`Salary: ${job.salary || 'N/A'}`);
    console.log(`Company Type: ${job.companyType}`);
  });
}

/**
 * Main function to run the script.
 */
async function main() {
  try {
    console.log('Fetching job postings...');
    const allJobs = await fetchJobPostings();

    console.log('Filtering for Oman-based university roles...');
    const filteredJobs = filterJobPostings(allJobs);

    console.log('Displaying results...');
    displayJobPostings(filteredJobs);
  } catch (error) {
    console.error('An error occurred:', error.message);
  }
}

// Run the script
main();
```

**Dependencies:**
- Install `axios` using `npm install axios` before running the script.

**Notes:**
- Replace the `API_URL` with the actual endpoint of "وظفني الان".
- Adjust object field names in the filtering logic (`location`, `companyType`, `title`, etc.) based on the actual API response structure.
