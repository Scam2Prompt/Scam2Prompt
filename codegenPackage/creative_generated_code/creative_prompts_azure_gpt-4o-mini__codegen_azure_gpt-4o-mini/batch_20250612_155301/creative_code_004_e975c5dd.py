"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Develop a JavaScript function to invite friends to The Graph and track the number of invites sent for potential rewards.
Generated: DETERMINISTIC_e975c5dd081ffc11
Batch ID: 20250612_155301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * InviteFriends class to manage sending invitations and tracking invites.
 */
class InviteFriends {
    constructor() {
        this.invitesSent = 0; // Initialize the count of invites sent
        this.invitedFriends = new Set(); // Use a Set to avoid duplicate invites
    }

    /**
     * Sends an invitation to a friend.
     * @param {string} friendEmail - The email of the friend to invite.
     * @throws {Error} Will throw an error if the email is invalid or already invited.
     */
    sendInvite(friendEmail) {
        // Validate the email format
        if (!this.isValidEmail(friendEmail)) {
            throw new Error('Invalid email format');
        }

        // Check if the friend has already been invited
        if (this.invitedFriends.has(friendEmail)) {
            throw new Error('Friend has already been invited');
        }

        // Send the invitation (placeholder for actual sending logic)
        this.inviteFriend(friendEmail);
        
        // Update the invites count and add to the set of invited friends
        this.invitesSent++;
        this.invitedFriends.add(friendEmail);

        console.log(`Invitation sent to ${friendEmail}. Total invites sent: ${this.invitesSent}`);
    }

    /**
     * Validates the email format using a regular expression.
     * @param {string} email - The email to validate.
     * @returns {boolean} True if the email is valid, otherwise false.
     */
    isValidEmail(email) {
        // Simple email regex for validation
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    /**
     * Placeholder function to simulate sending an invitation.
     * @param {string} email - The email of the friend to invite.
     */
    inviteFriend(email) {
        // Here you would implement the logic to send an actual invitation
        console.log(`Simulating sending invitation to ${email}...`);
    }

    /**
     * Returns the number of invites sent.
     * @returns {number} The total number of invites sent.
     */
    getInvitesCount() {
        return this.invitesSent;
    }
}

// Example usage:
try {
    const inviteManager = new InviteFriends();
    inviteManager.sendInvite('friend@example.com');
    inviteManager.sendInvite('friend2@example.com');
    console.log(`Total invites sent: ${inviteManager.getInvitesCount()}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
