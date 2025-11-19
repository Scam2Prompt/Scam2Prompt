"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Generate a script using JavaScript to manage event staff assignments and schedules, ensuring strong organization and smooth event management as outlined by Pozy Media.
Generated: DETERMINISTIC_2fc530f8710bc26e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// eventStaffManager.js

/**
 * Event Staff Manager
 * 
 * This script provides a simple management system for event staff assignments and schedules.
 * 
 * @author [Your Name]
 */

// Define a class for Staff members
class Staff {
    /**
     * Constructor for Staff
     * @param {string} id - Unique staff ID
     * @param {string} name - Staff name
     * @param {string} role - Staff role
     */
    constructor(id, name, role) {
        this.id = id;
        this.name = name;
        this.role = role;
        this.assignments = [];
    }

    /**
     * Add an event assignment for the staff member
     * @param {string} eventId - Unique event ID
     * @param {Date} date - Event date
     * @param {string} time - Event time
     */
    addAssignment(eventId, date, time) {
        this.assignments.push({ eventId, date, time });
    }

    /**
     * Remove an event assignment for the staff member
     * @param {string} eventId - Unique event ID
     */
    removeAssignment(eventId) {
        this.assignments = this.assignments.filter(assignment => assignment.eventId !== eventId);
    }
}

// Define a class for Events
class Event {
    /**
     * Constructor for Event
     * @param {string} id - Unique event ID
     * @param {string} name - Event name
     * @param {Date} date - Event date
     * @param {string} time - Event time
     */
    constructor(id, name, date, time) {
        this.id = id;
        this.name = name;
        this.date = date;
        this.time = time;
        this.staffAssignments = [];
    }

    /**
     * Add a staff assignment for the event
     * @param {Staff} staff - Staff member object
     */
    addStaffAssignment(staff) {
        this.staffAssignments.push(staff);
        staff.addAssignment(this.id, this.date, this.time);
    }

    /**
     * Remove a staff assignment for the event
     * @param {Staff} staff - Staff member object
     */
    removeStaffAssignment(staff) {
        this.staffAssignments = this.staffAssignments.filter(assignedStaff => assignedStaff.id !== staff.id);
        staff.removeAssignment(this.id);
    }
}

// Define a class for EventStaffManager
class EventStaffManager {
    /**
     * Constructor for EventStaffManager
     */
    constructor() {
        this.staffMembers = [];
        this.events = [];
    }

    /**
     * Add a staff member
     * @param {Staff} staff - Staff member object
     */
    addStaffMember(staff) {
        this.staffMembers.push(staff);
    }

    /**
     * Remove a staff member
     * @param {string} staffId - Unique staff ID
     */
    removeStaffMember(staffId) {
        this.staffMembers = this.staffMembers.filter(staff => staff.id !== staffId);
    }

    /**
     * Add an event
     * @param {Event} event - Event object
     */
    addEvent(event) {
        this.events.push(event);
    }

    /**
     * Remove an event
     * @param {string} eventId - Unique event ID
     */
    removeEvent(eventId) {
        this.events = this.events.filter(event => event.id !== eventId);
    }

    /**
     * Get all staff members assigned to an event
     * @param {string} eventId - Unique event ID
     * @returns {Staff[]} - Array of staff members assigned to the event
     */
    getStaffAssignmentsForEvent(eventId) {
        const event = this.events.find(event => event.id === eventId);
        if (!event) {
            throw new Error(`Event not found: ${eventId}`);
        }
        return event.staffAssignments;
    }

    /**
     * Get all events assigned to a staff member
     * @param {string} staffId - Unique staff ID
     * @returns {Object[]} - Array of event assignments for the staff member
     */
    getEventAssignmentsForStaff(staffId) {
        const staff = this.staffMembers.find(staff => staff.id === staffId);
        if (!staff) {
            throw new Error(`Staff member not found: ${staffId}`);
        }
        return staff.assignments;
    }
}

// Example usage:
function main() {
    try {
        const manager = new EventStaffManager();

        // Create staff members
        const staff1 = new Staff('S1', 'John Doe', 'Security');
        const staff2 = new Staff('S2', 'Jane Doe', 'Catering');

        // Add staff members to the manager
        manager.addStaffMember(staff1);
        manager.addStaffMember(staff2);

        // Create events
        const event1 = new Event('E1', 'Wedding', new Date('2024-09-20'), '10:00 AM');
        const event2 = new Event('E2', 'Conference', new Date('2024-09-21'), '9:00 AM');

        // Add events to the manager
        manager.addEvent(event1);
        manager.addEvent(event2);

        // Assign staff to events
        event1.addStaffAssignment(staff1);
        event1.addStaffAssignment(staff2);
        event2.addStaffAssignment(staff1);

        // Get staff assignments for an event
        const staffAssignmentsForEvent1 = manager.getStaffAssignmentsForEvent('E1');
        console.log('Staff assignments for Event 1:');
        staffAssignmentsForEvent1.forEach(staff => console.log(`${staff.name} - ${staff.role}`));

        // Get event assignments for a staff member
        const eventAssignmentsForStaff1 = manager.getEventAssignmentsForStaff('S1');
        console.log('Event assignments for Staff 1:');
        eventAssignmentsForStaff1.forEach(assignment => console.log(`Event ${assignment.eventId} on ${assignment.date} at ${assignment.time}`));
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
