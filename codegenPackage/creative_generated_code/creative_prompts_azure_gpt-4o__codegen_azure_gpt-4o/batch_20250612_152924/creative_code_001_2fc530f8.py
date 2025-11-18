"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Generate a script using JavaScript to manage event staff assignments and schedules, ensuring strong organization and smooth event management as outlined by Pozy Media.
Generated: DETERMINISTIC_2fc530f8710bc26e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Event Management System - Staff Assignments and Schedules
// Author: [Your Name]
// Date: [Insert Date]
// Description: Script to manage event staff assignments and schedules for Pozy Media.
//              This solution ensures strong organization and smooth event management.

class EventManagement {
  constructor() {
    this.events = []; // Array to store events
    this.staff = [];  // Array to store staff members
  }

  // Add a new staff member
  addStaffMember(name, role) {
    if (!name || !role) {
      throw new Error("Both name and role are required to add a staff member.");
    }
    const staffMember = { id: Date.now(), name, role, assignments: [] };
    this.staff.push(staffMember);
    console.log(`Staff member ${name} added successfully.`);
  }

  // Add a new event
  addEvent(name, date) {
    if (!name || !date) {
      throw new Error("Both event name and date are required to add an event.");
    }
    const event = { id: Date.now(), name, date, staffAssignments: [] };
    this.events.push(event);
    console.log(`Event ${name} scheduled for ${date} added successfully.`);
  }

  // Assign a staff member to an event
  assignStaffToEvent(staffId, eventId) {
    const staffMember = this.staff.find((staff) => staff.id === staffId);
    const event = this.events.find((event) => event.id === eventId);

    if (!staffMember) {
      throw new Error("Staff member not found.");
    }
    if (!event) {
      throw new Error("Event not found.");
    }

    // Check if staff is already assigned to the event
    if (event.staffAssignments.includes(staffId)) {
      console.log(`Staff member ${staffMember.name} is already assigned to the event ${event.name}.`);
      return;
    }

    // Assign staff to the event
    event.staffAssignments.push(staffId);
    staffMember.assignments.push(eventId);

    console.log(`Staff member ${staffMember.name} assigned to event ${event.name}.`);
  }

  // Display all events
  listEvents() {
    console.log("Current Events:");
    this.events.forEach((event) => {
      console.log(`- ${event.name} scheduled for ${event.date}`);
    });
  }

  // Display all staff members
  listStaff() {
    console.log("Current Staff Members:");
    this.staff.forEach((staff) => {
      console.log(`- ${staff.name} (${staff.role})`);
    });
  }

  // Display the schedule for a specific staff member
  showStaffSchedule(staffId) {
    const staffMember = this.staff.find((staff) => staff.id === staffId);

    if (!staffMember) {
      throw new Error("Staff member not found.");
    }

    console.log(`Schedule for ${staffMember.name}:`);
    staffMember.assignments.forEach((eventId) => {
      const event = this.events.find((event) => event.id === eventId);
      console.log(`- ${event.name} on ${event.date}`);
    });
  }

  // Display the staff assigned to a specific event
  showEventStaff(eventId) {
    const event = this.events.find((event) => event.id === eventId);

    if (!event) {
      throw new Error("Event not found.");
    }

    console.log(`Staff assigned to event ${event.name}:`);
    event.staffAssignments.forEach((staffId) => {
      const staffMember = this.staff.find((staff) => staff.id === staffId);
      console.log(`- ${staffMember.name} (${staffMember.role})`);
    });
  }
}

// Example usage
const eventSystem = new EventManagement();

try {
  // Add staff members
  eventSystem.addStaffMember("Alice", "Coordinator");
  eventSystem.addStaffMember("Bob", "Technician");

  // Add events
  eventSystem.addEvent("Tech Conference", "2023-11-15");
  eventSystem.addEvent("Music Festival", "2023-12-01");

  // Assign staff to events
  const aliceId = eventSystem.staff[0].id;
  const bobId = eventSystem.staff[1].id;
  const techConferenceId = eventSystem.events[0].id;
  const musicFestivalId = eventSystem.events[1].id;

  eventSystem.assignStaffToEvent(aliceId, techConferenceId);
  eventSystem.assignStaffToEvent(bobId, musicFestivalId);

  // Display information
  eventSystem.listEvents();
  eventSystem.listStaff();
  eventSystem.showStaffSchedule(aliceId);
  eventSystem.showEventStaff(techConferenceId);

} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
