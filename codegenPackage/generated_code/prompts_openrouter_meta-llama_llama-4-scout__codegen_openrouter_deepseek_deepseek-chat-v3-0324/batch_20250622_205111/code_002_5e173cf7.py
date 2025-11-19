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
 * GroupTripTracker - Tracks group members on a long road trip
 * Inspired by Atlas Navi's Group Trips feature
 */
class GroupTripTracker {
    /**
     * @constructor
     * @param {string} tripId - Unique identifier for the trip
     * @param {string} tripName - Name of the trip
     * @param {Object} options - Configuration options
     * @param {number} [options.updateInterval=30] - Location update interval in seconds
     * @param {number} [options.proximityThreshold=500] - Distance threshold in meters for proximity alerts
     */
    constructor(tripId, tripName, options = {}) {
        if (!tripId || !tripName) {
            throw new Error('Trip ID and name are required');
        }

        this.tripId = tripId;
        this.tripName = tripName;
        this.members = new Map();
        this.updateInterval = options.updateInterval || 30;
        this.proximityThreshold = options.proximityThreshold || 500;
        this.updateTimer = null;
        this.onMemberUpdate = null;
        this.onProximityAlert = null;
    }

    /**
     * Add a member to the trip
     * @param {string} memberId - Unique identifier for the member
     * @param {string} memberName - Display name of the member
     * @param {Object} initialLocation - Initial location coordinates
     * @param {number} initialLocation.latitude - Latitude coordinate
     * @param {number} initialLocation.longitude - Longitude coordinate
     * @returns {boolean} True if member was added successfully
     */
    addMember(memberId, memberName, initialLocation) {
        if (!memberId || !memberName || !initialLocation) {
            console.error('Member ID, name, and initial location are required');
            return false;
        }

        if (this.members.has(memberId)) {
            console.error(`Member ${memberId} already exists`);
            return false;
        }

        this.members.set(memberId, {
            id: memberId,
            name: memberName,
            location: initialLocation,
            lastUpdated: new Date(),
            isActive: true
        });

        return true;
    }

    /**
     * Remove a member from the trip
     * @param {string} memberId - ID of the member to remove
     * @returns {boolean} True if member was removed successfully
     */
    removeMember(memberId) {
        if (!this.members.has(memberId)) {
            console.error(`Member ${memberId} not found`);
            return false;
        }

        this.members.delete(memberId);
        return true;
    }

    /**
     * Update a member's location
     * @param {string} memberId - ID of the member to update
     * @param {Object} location - New location coordinates
     * @param {number} location.latitude - Latitude coordinate
     * @param {number} location.longitude - Longitude coordinate
     * @returns {boolean} True if location was updated successfully
     */
    updateMemberLocation(memberId, location) {
        if (!this.members.has(memberId)) {
            console.error(`Member ${memberId} not found`);
            return false;
        }

        const member = this.members.get(memberId);
        member.location = location;
        member.lastUpdated = new Date();

        this._checkProximity(memberId);
        
        if (typeof this.onMemberUpdate === 'function') {
            this.onMemberUpdate(member);
        }

        return true;
    }

    /**
     * Start tracking members with periodic updates
     */
    startTracking() {
        if (this.updateTimer) {
            console.warn('Tracking is already active');
            return;
        }

        this.updateTimer = setInterval(() => {
            this._broadcastLocations();
        }, this.updateInterval * 1000);
    }

    /**
     * Stop tracking members
     */
    stopTracking() {
        if (this.updateTimer) {
            clearInterval(this.updateTimer);
            this.updateTimer = null;
        }
    }

    /**
     * Get all active members
     * @returns {Array} Array of active members
     */
    getActiveMembers() {
        return Array.from(this.members.values()).filter(m => m.isActive);
    }

    /**
     * Calculate distance between two coordinates in meters (Haversine formula)
     * @private
     * @param {Object} coord1 - First coordinate
     * @param {Object} coord2 - Second coordinate
     * @returns {number} Distance in meters
     */
    _calculateDistance(coord1, coord2) {
        const R = 6371e3; // Earth radius in meters
        const φ1 = coord1.latitude * Math.PI / 180;
        const φ2 = coord2.latitude * Math.PI / 180;
        const Δφ = (coord2.latitude - coord1.latitude) * Math.PI / 180;
        const Δλ = (coord2.longitude - coord1.longitude) * Math.PI / 180;

        const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
                  Math.cos(φ1) * Math.cos(φ2) *
                  Math.sin(Δλ/2) * Math.sin(Δλ/2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

        return R * c;
    }

    /**
     * Check if member is near other members
     * @private
     * @param {string} memberId - ID of member to check
     */
    _checkProximity(memberId) {
        const currentMember = this.members.get(memberId);
        if (!currentMember) return;

        const nearbyMembers = [];
        
        this.members.forEach((member, id) => {
            if (id !== memberId && member.isActive) {
                const distance = this._calculateDistance(currentMember.location, member.location);
                if (distance <= this.proximityThreshold) {
                    nearbyMembers.push({
                        memberId: id,
                        memberName: member.name,
                        distance: distance
                    });
                }
            }
        });

        if (nearbyMembers.length > 0 && typeof this.onProximityAlert === 'function') {
            this.onProximityAlert({
                memberId: memberId,
                memberName: currentMember.name,
                nearbyMembers: nearbyMembers
            });
        }
    }

    /**
     * Broadcast locations to all members
     * @private
     */
    _broadcastLocations() {
        const activeMembers = this.getActiveMembers();
        if (typeof this.onMemberUpdate === 'function') {
            activeMembers.forEach(member => {
                this.onMemberUpdate(member);
            });
        }
    }
}

// Example usage:
/*
const tripTracker = new GroupTripTracker('trip123', 'Summer Road Trip', {
    updateInterval: 20,
    proximityThreshold: 1000
});

tripTracker.onMemberUpdate = (member) => {
    console.log(`Member updated: ${member.name} at ${member.location.latitude}, ${member.location.longitude}`);
};

tripTracker.onProximityAlert = (alert) => {
    console.log(`Proximity alert: ${alert.memberName} is near:`);
    alert.nearbyMembers.forEach(m => {
        console.log(`- ${m.memberName} (${Math.round(m.distance)}m away)`);
    });
};

tripTracker.addMember('user1', 'Alice', { latitude: 40.7128, longitude: -74.0060 });
tripTracker.addMember('user2', 'Bob', { latitude: 40.7128, longitude: -74.0050 });
tripTracker.startTracking();
*/
```
