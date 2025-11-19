"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: Generate a JavaScript function that displays the schedule of events for the India (Bengal) Cultural Association Japan, highlighting the upcoming Saraswati Puja and other cultural celebrations.
Generated: DETERMINISTIC_358664d825df23c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Event class representing a cultural event
class Event {
    /**
     * @param {string} name - Name of the event
     * @param {Date} date - Date of the event
     * @param {string} description - Brief description of the event
     */
    constructor(name, date, description) {
        this.name = name;
        this.date = date;
        this.description = description;
    }
}

// IndiaBengalCulturalAssociation class to manage events
class IndiaBengalCulturalAssociation {
    /**
     * Initialize events array
     */
    constructor() {
        this.events = [];
    }

    /**
     * Add an event to the schedule
     * @param {Event} event - Event to be added
     */
    addEvent(event) {
        this.events.push(event);
    }

    /**
     * Display upcoming events
     */
    displayUpcomingEvents() {
        // Sort events by date
        this.events.sort((a, b) => a.date - b.date);

        console.log("Upcoming Events:");
        this.events.forEach((event) => {
            console.log(`Event: ${event.name}, Date: ${event.date.toLocaleDateString('en-GB')}, Description: ${event.description}`);
        });
    }

    /**
     * Highlight Saraswati Puja event
     */
    highlightSaraswatiPuja() {
        const saraswatiPuja = this.events.find((event) => event.name.toLowerCase().includes("saraswati puja"));
        if (saraswatiPuja) {
            console.log(`\n**Saraswati Puja Details:**`);
            console.log(`Event: ${saraswatiPuja.name}, Date: ${saraswatiPuja.date.toLocaleDateString('en-GB')}, Description: ${saraswatiPuja.description}`);
        } else {
            console.log("\nSaraswati Puja event not found in the schedule.");
        }
    }
}

// Main function to demonstrate usage
function main() {
    try {
        const association = new IndiaBengalCulturalAssociation();

        // Adding events
        association.addEvent(new Event("Saraswati Puja", new Date('2024-09-20'), "Celebration of Goddess Saraswati"));
        association.addEvent(new Event("Diwali", new Date('2024-11-12'), "Festival of Lights"));
        association.addEvent(new Event("Holi", new Date('2025-03-20'), "Festival of Colors"));

        // Display all upcoming events
        association.displayUpcomingEvents();

        // Highlight Saraswati Puja
        association.highlightSaraswatiPuja();
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
}

// Run the main function
main();
```
