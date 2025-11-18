"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Develop a ServiceNow workflow to optimize employee experience by proactively managing "Moments that matter," as emphasized by UX4MATION's approach.
Generated: DETERMINISTIC_ae8d92caa595c8fb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// ServiceNow Scripted Workflow: Optimize Employee Experience for "Moments that Matter"
// This script initializes and automates proactive management of employee "Moments that Matter".
// Follows UX4MATION's approach for enhancing employee experience.
// Ensure this script is added to a ServiceNow workflow in a scoped application.

(function executeWorkflow(current, workflow) {
    try {
        // Step 1: Initialize variables and constants
        const momentsTable = 'x_ux4mation_moments'; // Table to store "Moments that Matter"
        const employeeTable = 'sys_user'; // ServiceNow User table
        const notificationTemplate = 'x_ux4mation_moment_notification'; // Notification template name

        // Step 2: Fetch the current user and their moments
        var currentUserSysId = current.getValue('sys_created_by');
        var momentsQuery = new GlideRecord(momentsTable); // GlideRecord for moments table
        momentsQuery.addQuery('user', currentUserSysId);
        momentsQuery.query();

        // Step 3: Process each "Moment that Matters" for the employee
        while (momentsQuery.next()) {
            var momentType = momentsQuery.getValue('moment_type'); // Type of the moment
            var momentDate = momentsQuery.getValue('moment_date'); // Scheduled or expected date
            var momentStatus = momentsQuery.getValue('status'); // Current status of the moment

            // Step 4: Check if the moment requires proactive action
            if (momentStatus === 'pending' && isDateApproaching(momentDate)) {
                // Send notification to the employee about the upcoming moment
                sendNotification(currentUserSysId, momentType, notificationTemplate);
                
                // Update the status to "notified"
                momentsQuery.setValue('status', 'notified');
                momentsQuery.update();
            }
        }

        // Step 5: Log workflow execution
        workflow.debug('Moments that Matter workflow executed successfully for user: ' + currentUserSysId);

    } catch (error) {
        // Error handling
        workflow.error('Error in Moments that Matter workflow: ' + error.message);
    }

    /**
     * Helper Function: Check if a date is within the next 7 days.
     * @param {string} dateString - Date string in GlideDateTime format.
     * @returns {boolean} - True if the date is approaching, false otherwise.
     */
    function isDateApproaching(dateString) {
        var currentDate = new GlideDateTime();
        var momentDate = new GlideDateTime(dateString);
        var difference = GlideDateTime.subtract(momentDate, currentDate); // Difference in milliseconds
        return difference < (7 * 24 * 60 * 60 * 1000); // Check if within 7 days
    }

    /**
     * Helper Function: Send a notification to the user.
     * @param {string} userSysId - Sys ID of the user.
     * @param {string} momentType - Type of the moment.
     * @param {string} templateName - Name of the notification template.
     */
    function sendNotification(userSysId, momentType, templateName) {
        var notification = new GlideRecord('sys_notification');
        notification.initialize();
        notification.setValue('recipient', userSysId);
        notification.setValue('subject', 'Upcoming "Moment that Matters": ' + momentType);
        notification.setValue('template', templateName);
        notification.insert();
    }

})(current, workflow);
```
