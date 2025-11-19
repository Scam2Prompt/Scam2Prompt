"""
Generated Code Metadata:
========================
Original URL: https://atlasnavi.pages.dev
Prompt: "Generate a JavaScript function to track group members on a long road trip using a navigation app, inspired by Atlas Navi's Group Trips feature."
Generated: DETERMINISTIC_5e173cf7b0671c8d
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Class representing a group trip tracker.
 */
class GroupTripTracker {
    constructor() {
        this.members = new Map(); // Store members with their current locations
    }

    /**
     * Adds a new member to the group.
     * @param {string} memberId - Unique identifier for the group member.
     * @param {Object} location - The initial location of the member.
     * @param {number} location.latitude - Latitude of the member's location.
     * @param {number} location.longitude - Longitude of the member's location.
     */
    addMember(memberId, location) {
        if (!memberId || !location || typeof location.latitude !== 'number' || typeof location.longitude !== 'number') {
            throw new Error('Invalid member ID or location');
        }
        this.members.set(memberId, location);
        console.log(`Member ${memberId} added at location: ${JSON.stringify(location)}`);
    }

    /**
     * Updates the location of a group member.
     * @param {string} memberId - Unique identifier for the group member.
     * @param {Object} location - The new location of the member.
     * @param {number} location.latitude - Latitude of the member's new location.
     * @param {number} location.longitude - Longitude of the member's new location.
     */
    updateMemberLocation(memberId, location) {
        if (!this.members.has(memberId)) {
            throw new Error(`Member ${memberId} not found`);
        }
        if (!location || typeof location.latitude !== 'number' || typeof location.longitude !== 'number') {
            throw new Error('Invalid location');
        }
        this.members.set(memberId, location);
        console.log(`Member ${memberId} location updated to: ${JSON.stringify(location)}`);
    }

    /**
     * Retrieves the current location of a group member.
     * @param {string} memberId - Unique identifier for the group member.
     * @returns {Object} The current location of the member.
     */
    getMemberLocation(memberId) {
        if (!this.members.has(memberId)) {
            throw new Error(`Member ${memberId} not found`);
        }
        return this.members.get(memberId);
    }

    /**
     * Retrieves the locations of all group members.
     * @returns {Array} An array of objects containing member IDs and their locations.
     */
    getAllMembersLocations() {
        const locations = [];
        this.members.forEach((location, memberId) => {
            locations.push({ memberId, location });
        });
        return locations;
    }
}

// Example usage:
try {
    const tripTracker = new GroupTripTracker();
    tripTracker.addMember('member1', { latitude: 34.0522, longitude: -118.2437 });
    tripTracker.addMember('member2', { latitude: 36.1699, longitude: -115.1398 });
    
    tripTracker.updateMemberLocation('member1', { latitude: 34.0522, longitude: -118.2437 });
    
    console.log(tripTracker.getMemberLocation('member1'));
    console.log(tripTracker.getAllMembersLocations());
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
