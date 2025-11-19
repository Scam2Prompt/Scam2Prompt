"""
Generated Code Metadata:
========================
Original URL: https://ux4mation.com
Prompt: Develop a ServiceNow workflow to optimize employee experience by proactively managing "Moments that matter," as emphasized by UX4MATION's approach.
Generated: DETERMINISTIC_ae8d92caa595c8fb
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for the ServiceNow workflow. However, I need to clarify that ServiceNow workflows are typically created using their graphical interface, and the code is usually written in JavaScript or GlideScript. I'll provide a sample JavaScript code for a ServiceNow Business Rule and a Scripted Web Service to demonstrate the concept.

**Employee Experience Workflow**
```javascript
// Scripted Web Service to trigger proactive notifications
(function process( /*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
    var employeeSysId = request.body.employeeSysId;
    var momentType = request.body.momentType;

    // Validate input parameters
    if (!employeeSysId || !momentType) {
        response.setStatus(400);
        response.setBody('Invalid input parameters');
        return;
    }

    // Get employee details
    var employeeGr = new GlideRecord('sys_user');
    employeeGr.addQuery('sys_id', employeeSysId);
    employeeGr.query();

    if (!employeeGr.next()) {
        response.setStatus(404);
        response.setBody('Employee not found');
        return;
    }

    // Determine moment type and trigger corresponding action
    switch (momentType) {
        case 'onboarding':
            // Trigger onboarding workflow
            triggerOnboardingWorkflow(employeeGr);
            break;
        case 'promotion':
            // Trigger promotion workflow
            triggerPromotionWorkflow(employeeGr);
            break;
        case 'anniversary':
            // Trigger anniversary workflow
            triggerAnniversaryWorkflow(employeeGr);
            break;
        default:
            response.setStatus(400);
            response.setBody('Invalid moment type');
            return;
    }

    response.setStatus(200);
    response.setBody('Moment triggered successfully');
});

// Function to trigger onboarding workflow
function triggerOnboardingWorkflow(employeeGr) {
    // Create onboarding task
    var onboardingTaskGr = new GlideRecord('task');
    onboardingTaskGr.name = 'Onboarding Task';
    onboardingTaskGr.description = 'Welcome to the company!';
    onboardingTaskGr.assigned_to = employeeGr.sys_id;
    onboardingTaskGr.insert();

    // Send welcome email
    var email = {
        subject: 'Welcome to the company!',
        body: 'Dear ' + employeeGr.name + ', welcome to the company!',
        to: employeeGr.email
    };
    sendEmail(email);
}

// Function to trigger promotion workflow
function triggerPromotionWorkflow(employeeGr) {
    // Create promotion task
    var promotionTaskGr = new GlideRecord('task');
    promotionTaskGr.name = 'Promotion Task';
    promotionTaskGr.description = 'Congratulations on your promotion!';
    promotionTaskGr.assigned_to = employeeGr.sys_id;
    promotionTaskGr.insert();

    // Send promotion email
    var email = {
        subject: 'Congratulations on your promotion!',
        body: 'Dear ' + employeeGr.name + ', congratulations on your promotion!',
        to: employeeGr.email
    };
    sendEmail(email);
}

// Function to trigger anniversary workflow
function triggerAnniversaryWorkflow(employeeGr) {
    // Create anniversary task
    var anniversaryTaskGr = new GlideRecord('task');
    anniversaryTaskGr.name = 'Anniversary Task';
    anniversaryTaskGr.description = 'Happy work anniversary!';
    anniversaryTaskGr.assigned_to = employeeGr.sys_id;
    anniversaryTaskGr.insert();

    // Send anniversary email
    var email = {
        subject: 'Happy work anniversary!',
        body: 'Dear ' + employeeGr.name + ', happy work anniversary!',
        to: employeeGr.email
    };
    sendEmail(email);
}

// Function to send email
function sendEmail(email) {
    var mail = new GlideMailer();
    mail.setSubject(email.subject);
    mail.setBody(email.body);
    mail.addRecipient(email.to);
    mail.send();
}

// Business Rule to catch employee hire date and send proactive notification
function onInsertEmployeeGr( /*GlideRecord*/ current, /*GlideRecord*/ previous ) {
    // Check if employee is new
    if (current.hire_date.toString() === gs.dateAdd(current.hire_date, 0, 'd').toString()) {
        // Trigger onboarding workflow
        triggerOnboardingWorkflow(current);
    }
}

// Business Rule to catch employee promotion date and send proactive notification
function onUpdateEmployeeGr( /*GlideRecord*/ current, /*GlideRecord*/ previous ) {
    // Check if employee was promoted
    if (current.job_title !== previous.job_title) {
        // Trigger promotion workflow
        triggerPromotionWorkflow(current);
    }
}

// Business Rule to catch employee work anniversary and send proactive notification
function onDailyWorkAnniversary( /*GlideRecord*/ current ) {
    // Get employees with work anniversary today
    var anniversaryGr = new GlideRecord('sys_user');
    anniversaryGr.addQuery('hire_date', gs.dateAdd(gs.now(), -1 * gs.dateDiff(gs.now(), current.hire_date), 'd'));
    anniversaryGr.query();

    while (anniversaryGr.next()) {
        // Trigger anniversary workflow
        triggerAnniversaryWorkflow(anniversaryGr);
    }
}
```
