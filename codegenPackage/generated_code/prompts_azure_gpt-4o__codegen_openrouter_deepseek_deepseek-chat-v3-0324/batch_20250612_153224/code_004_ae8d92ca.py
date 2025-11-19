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

```javascript
// ServiceNow Workflow Script for Employee Experience Optimization
// This workflow proactively manages "Moments that Matter" based on UX4MATION's approach

(function execute(current, previous /*null when async*/) {
    try {
        // Define moments that matter with their respective triggers and actions
        var moments = {
            'Onboarding': {
                trigger: 'onboarding_started',
                actions: [
                    scheduleWelcomeMeeting,
                    assignMentor,
                    provisionEquipment
                ]
            },
            'Promotion': {
                trigger: 'promotion_approved',
                actions: [
                    updateRoleInformation,
                    scheduleCareerPathDiscussion,
                    notifyTeam
                ]
            },
            'Performance Review': {
                trigger: 'review_period_started',
                actions: [
                    sendSelfEvaluationReminder,
                    scheduleReviewMeeting,
                    collectPeerFeedback
                ]
            },
            'Offboarding': {
                trigger: 'offboarding_requested',
                actions: [
                    scheduleExitInterview,
                    initiateKnowledgeTransfer,
                    processAssetReturn
                ]
            }
        };

        // Get the current moment based on the triggering event
        var currentMoment = getCurrentMoment(current, moments);
        
        if (!currentMoment) {
            gs.info('No matching moment found for current event');
            return;
        }

        // Execute all actions for the current moment
        executeMomentActions(current, currentMoment);

    } catch (e) {
        gs.error('Error in Employee Experience Workflow: ' + e.message);
        logError(current, e);
    }

    function getCurrentMoment(currentRecord, momentsConfig) {
        // Determine which moment is being triggered
        var eventName = currentRecord.getValue('event_name');
        
        for (var moment in momentsConfig) {
            if (momentsConfig[moment].trigger === eventName) {
                return momentsConfig[moment];
            }
        }
        return null;
    }

    function executeMomentActions(currentRecord, moment) {
        gs.info('Executing actions for moment: ' + moment);
        
        moment.actions.forEach(function(action) {
            try {
                action(currentRecord);
            } catch (e) {
                gs.error('Failed to execute action for moment: ' + e.message);
            }
        });
    }

    // Action Functions
    function scheduleWelcomeMeeting(record) {
        var meeting = new GlideRecord('meeting');
        meeting.initialize();
        meeting.setValue('topic', 'Welcome Meeting for ' + record.employee_name);
        meeting.setValue('start_date', new GlideDateTime().addDays(3).getDate());
        meeting.setValue('attendees', record.manager);
        meeting.insert();
    }

    function assignMentor(record) {
        var mentorAssignment = new GlideRecord('mentor_assignment');
        mentorAssignment.initialize();
        mentorAssignment.setValue('employee', record.sys_id);
        mentorAssignment.setValue('mentor', findSuitableMentor(record.department));
        mentorAssignment.insert();
    }

    function findSuitableMentor(department) {
        // Implementation would query for suitable mentors in the same department
        return '12345'; // Sample mentor sys_id
    }

    function provisionEquipment(record) {
        var task = new GlideRecord('procurement_task');
        task.initialize();
        task.setValue('requested_for', record.sys_id);
        task.setValue('items', 'Laptop, Access Card, Welcome Kit');
        task.insert();
    }

    function updateRoleInformation(record) {
        var employee = new GlideRecord('sys_user');
        if (employee.get(record.employee)) {
            employee.title = record.new_title;
            employee.department = record.new_department;
            employee.update();
        }
    }

    function scheduleCareerPathDiscussion(record) {
        var meeting = new GlideRecord('meeting');
        meeting.initialize();
        meeting.setValue('topic', 'Career Path Discussion for ' + record.employee_name);
        meeting.setValue('start_date', new GlideDateTime().addDays(7).getDate());
        meeting.setValue('attendees', record.manager + ',' + record.hr_partner);
        meeting.insert();
    }

    function notifyTeam(record) {
        var notification = new GlideRecord('notification');
        notification.initialize();
        notification.setValue('message', 'Please congratulate ' + record.employee_name + ' on their promotion to ' + record.new_title);
        notification.setValue('recipients', record.team_members);
        notification.insert();
    }

    function sendSelfEvaluationReminder(record) {
        var email = new GlideEmailOutbound();
        email.setRecipient(record.employee_email);
        email.setSubject('Performance Review: Self-Evaluation Reminder');
        email.setBody('Please complete your self-evaluation by ' + record.review_deadline);
        email.send();
    }

    function scheduleReviewMeeting(record) {
        var meeting = new GlideRecord('meeting');
        meeting.initialize();
        meeting.setValue('topic', 'Performance Review for ' + record.employee_name);
        meeting.setValue('start_date', record.review_deadline);
        meeting.setValue('attendees', record.manager);
        meeting.insert();
    }

    function collectPeerFeedback(record) {
        var feedbackTask = new GlideRecord('feedback_task');
        feedbackTask.initialize();
        feedbackTask.setValue('employee', record.sys_id);
        feedbackTask.setValue('review_period', record.review_period);
        feedbackTask.setValue('peers', record.peers);
        feedbackTask.insert();
    }

    function scheduleExitInterview(record) {
        var meeting = new GlideRecord('meeting');
        meeting.initialize();
        meeting.setValue('topic', 'Exit Interview for ' + record.employee_name);
        meeting.setValue('start_date', new GlideDateTime().addDays(2).getDate());
        meeting.setValue('attendees', record.hr_partner);
        meeting.insert();
    }

    function initiateKnowledgeTransfer(record) {
        var ktTask = new GlideRecord('knowledge_transfer');
        ktTask.initialize();
        ktTask.setValue('employee', record.sys_id);
        ktTask.setValue('successor', record.successor);
        ktTask.setValue('priority', 'High');
        ktTask.insert();
    }

    function processAssetReturn(record) {
        var assetTask = new GlideRecord('asset_return');
        assetTask.initialize();
        assetTask.setValue('employee', record.sys_id);
        assetTask.setValue('assets', record.assets);
        assetTask.insert();
    }

    function logError(record, error) {
        var errorLog = new GlideRecord('error_log');
        errorLog.initialize();
        errorLog.setValue('source', 'Employee Experience Workflow');
        errorLog.setValue('record', record.getRecordClassName() + ':' + record.sys_id);
        errorLog.setValue('message', error.message);
        errorLog.setValue('stack_trace', error.stack);
        errorLog.insert();
    }
})(current, previous);
```
