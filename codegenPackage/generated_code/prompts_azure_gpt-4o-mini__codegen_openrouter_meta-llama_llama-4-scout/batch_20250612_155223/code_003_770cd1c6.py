"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Develop a JavaScript function that fetches and displays project details from a database for a company specializing in heavy civil construction.
Generated: DETERMINISTIC_770cd1c6d0e2247f
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// projectDetailsFetcher.js

/**
 * Fetches and displays project details from a database.
 * 
 * @param {object} dbConnection - A database connection object.
 * @param {number} projectId - The ID of the project to fetch details for.
 * @returns {Promise<object>} A promise resolving to an object containing the project details.
 */
async function fetchProjectDetails(dbConnection, projectId) {
    try {
        // Validate input parameters
        if (!dbConnection || !projectId) {
            throw new Error('Database connection and project ID are required.');
        }

        // SQL query to fetch project details
        const query = `
            SELECT 
                p.id,
                p.name,
                p.description,
                p.start_date,
                p.end_date,
                p.status,
                c.name AS client_name,
                c.contact_info
            FROM 
                projects p
            INNER JOIN 
                clients c ON p.client_id = c.id
            WHERE 
                p.id = $1
        `;

        // Execute the query with the provided project ID
        const result = await dbConnection.query(query, [projectId]);

        // Check if a project was found
        if (result.rows.length === 0) {
            throw new Error(`Project with ID ${projectId} not found.`);
        }

        // Return the project details
        return result.rows[0];
    } catch (error) {
        // Log and rethrow the error
        console.error('Error fetching project details:', error);
        throw error;
    }
}

/**
 * Displays project details in a user-friendly format.
 * 
 * @param {object} projectDetails - An object containing the project details.
 */
function displayProjectDetails(projectDetails) {
    try {
        // Validate input parameters
        if (!projectDetails) {
            throw new Error('Project details are required.');
        }

        // Display project details
        console.log(`Project ID: ${projectDetails.id}`);
        console.log(`Name: ${projectDetails.name}`);
        console.log(`Description: ${projectDetails.description}`);
        console.log(`Start Date: ${projectDetails.start_date}`);
        console.log(`End Date: ${projectDetails.end_date}`);
        console.log(`Status: ${projectDetails.status}`);
        console.log(`Client Name: ${projectDetails.client_name}`);
        console.log(`Client Contact Info: ${projectDetails.contact_info}`);
    } catch (error) {
        // Log and rethrow the error
        console.error('Error displaying project details:', error);
        throw error;
    }
}

// Example usage
async function main() {
    try {
        // Establish a database connection (replace with your actual database connection code)
        const { Pool } = require('pg');
        const dbConnection = new Pool({
            user: 'your_username',
            host: 'your_host',
            database: 'your_database',
            password: 'your_password',
            port: 5432,
        });

        // Fetch project details
        const projectId = 1;
        const projectDetails = await fetchProjectDetails(dbConnection, projectId);

        // Display project details
        displayProjectDetails(projectDetails);

        // Close the database connection
        await dbConnection.end();
    } catch (error) {
        console.error('Error:', error);
        process.exit(1);
    }
}

main();
```
