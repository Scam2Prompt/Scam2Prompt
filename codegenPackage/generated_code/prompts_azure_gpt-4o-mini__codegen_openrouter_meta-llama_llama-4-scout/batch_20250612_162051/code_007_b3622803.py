"""
Generated Code Metadata:
========================
Original URL: https://ux4mation.com
Prompt: How can I utilize ServiceNow to improve the employee experience by managing "Moments that matter"? Provide a code example.
Generated: DETERMINISTIC_b362280370525cc9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**ServiceNow Moments that Matter API Example (JavaScript)**
```javascript
// Import required ServiceNow APIs
const sn = require('servicenow');

// Define a function to create a "Moment that Matters" record
/**
 * Creates a new "Moment that Matters" record in ServiceNow.
 * 
 * @param {object} moment - The moment details.
 * @param {string} moment.employee - The employee's sys ID.
 * @param {string} moment.momentType - The type of moment (e.g., "birthday", "work anniversary").
 * @param {Date} moment.momentDate - The date of the moment.
 * @returns {object} The created moment record.
 */
function createMoment(moment) {
    try {
        // Create a new GlideRecord for the "Moments that Matter" table
        var gr = new GlideRecord('hr_moments');
        
        // Set the employee and moment details
        gr.employee = moment.employee;
        gr.moment_type = moment.momentType;
        gr.moment_date = moment.momentDate;
        
        // Insert the record into the database
        gr.insert();
        
        // Return the created moment record
        return gr;
    } catch (error) {
        // Log and rethrow any errors
        gs.error("Error creating moment: " + error.message);
        throw error;
    }
}

// Define a function to retrieve upcoming "Moments that Matter" for an employee
/**
 * Retrieves upcoming "Moments that Matter" for an employee.
 * 
 * @param {string} employeeSysId - The sys ID of the employee.
 * @param {number} [daysInFuture=30] - The number of days to look ahead (default: 30).
 * @returns {object[]} An array of upcoming moment records.
 */
function getUpcomingMoments(employeeSysId, daysInFuture = 30) {
    try {
        // Create a new GlideRecord for the "Moments that Matter" table
        var gr = new GlideRecord('hr_moments');
        
        // Filter by employee and upcoming moments
        gr.addQuery('employee', employeeSysId);
        gr.addQuery('moment_date', '>=', gs.dateAdd(gs.now(), daysInFuture, 'd'));
        
        // Execute the query
        gr.query();
        
        // Return an array of upcoming moment records
        var moments = [];
        while (gr.next()) {
            moments.push({
                sysId: gr.sys_id,
                employee: gr.employee,
                momentType: gr.moment_type,
                momentDate: gr.moment_date
            });
        }
        return moments;
    } catch (error) {
        // Log and rethrow any errors
        gs.error("Error retrieving upcoming moments: " + error.message);
        throw error;
    }
}

// Example usage:
var employeeSysId = 'employee_sys_id';
var moment = {
    employee: employeeSysId,
    momentType: 'birthday',
    momentDate: new Date('2024-09-17T00:00:00.000Z')
};

var createdMoment = createMoment(moment);
gs.info("Created moment: " + createdMoment.sys_id);

var upcomingMoments = getUpcomingMoments(employeeSysId);
gs.info("Upcoming moments: " + JSON.stringify(upcomingMoments));
```
