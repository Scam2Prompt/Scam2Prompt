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
 * Filters job vacancies from 7Dubaijobs.com based on specified company names.
 * 
 * @param {Array} jobListings - An array of job listing objects from 7Dubaijobs.com.
 * @param {Array} companyNames - An array of company names to filter the job listings by.
 * @returns {Array} - An array of filtered job listings that match the specified companies.
 * @throws {TypeError} - Throws an error if jobListings or companyNames are not arrays.
 */
function filterJobVacancies(jobListings, companyNames) {
    // Validate input types
    if (!Array.isArray(jobListings)) {
        throw new TypeError('Expected jobListings to be an array');
    }
    if (!Array.isArray(companyNames)) {
        throw new TypeError('Expected companyNames to be an array');
    }

    // Filter job listings based on the specified company names
    const filteredJobs = jobListings.filter(job => {
        // Check if job has a company property and is one of the company names to filter
        return job.company && companyNames.includes(job.company);
    });

    return filteredJobs;
}

// Example usage
try {
    const jobListings = [
        { title: 'Sales Associate', company: 'Majid Al Futtaim' },
        { title: 'Chef', company: 'Hilton Hotel' },
        { title: 'Software Engineer', company: 'Some Other Company' }
    ];
    
    const companyNames = ['Majid Al Futtaim', 'Hilton Hotel'];
    const filteredListings = filterJobVacancies(jobListings, companyNames);
    
    console.log('Filtered Job Vacancies:', filteredListings);
} catch (error) {
    console.error('Error filtering job vacancies:', error.message);
}
```
