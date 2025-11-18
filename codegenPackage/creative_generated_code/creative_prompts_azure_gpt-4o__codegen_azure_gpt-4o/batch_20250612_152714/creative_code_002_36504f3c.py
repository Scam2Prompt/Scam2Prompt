"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://goodcryptodex.pages.dev
Prompt: Develop a referral tracking system in JavaScript that allows users to move up the GoodCryptoX waitlist by inviting friends.
Generated: DETERMINISTIC_36504f3c221c8ea7
Batch ID: 20250612_152714
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Referral Tracking System for GoodCryptoX Waitlist
 * This script tracks users and their referrals, allowing them to move up the waitlist by inviting friends.
 */

// Mock database to store user data and referral relationships
const userDatabase = new Map();

/**
 * Adds a user to the waitlist
 * @param {string} userId - The unique ID of the user
 * @returns {string} - Confirmation message
 */
function addUserToWaitlist(userId) {
  if (!userId || typeof userId !== 'string') {
    throw new Error('Invalid userId. UserId must be a non-empty string.');
  }

  if (userDatabase.has(userId)) {
    return `User ${userId} is already on the waitlist.`;
  }

  // Initialize user data with referral count and invite list
  userDatabase.set(userId, {
    referrals: 0,
    inviteList: [],
  });

  return `User ${userId} has been added to the waitlist.`;
}

/**
 * Tracks an invitation from one user to another
 * @param {string} referrerId - The ID of the user making the referral
 * @param {string} inviteeId - The ID of the user being invited
 * @returns {string} - Confirmation message
 */
function addReferral(referrerId, inviteeId) {
  if (!referrerId || !inviteeId || typeof referrerId !== 'string' || typeof inviteeId !== 'string') {
    throw new Error('Invalid input. Both referrerId and inviteeId must be non-empty strings.');
  }

  if (!userDatabase.has(referrerId)) {
    return `Referrer ${referrerId} is not on the waitlist. Please add them first.`;
  }

  if (userDatabase.has(inviteeId)) {
    return `Invitee ${inviteeId} is already on the waitlist.`;
  }

  // Add the invitee user to the waitlist
  userDatabase.set(inviteeId, {
    referrals: 0,
    inviteList: [],
  });

  // Update the referrer's referral data
  const referrerData = userDatabase.get(referrerId);
  referrerData.referrals += 1;
  referrerData.inviteList.push(inviteeId);

  return `Referral added! ${referrerId} invited ${inviteeId}.`;
}

/**
 * Retrieves the current position of a user based on their referrals
 * @param {string} userId - The unique ID of the user
 * @returns {Object} - User's position and referral details
 */
function getUserPosition(userId) {
  if (!userDatabase.has(userId)) {
    throw new Error(`User ${userId} is not on the waitlist.`);
  }

  const userData = userDatabase.get(userId);

  return {
    userId,
    referrals: userData.referrals,
    inviteList: userData.inviteList,
  };
}

/**
 * Display the entire waitlist sorted by referral count
 * @returns {Array} - Sorted list of users with their referral counts
 */
function getSortedWaitlist() {
  const waitlistArray = Array.from(userDatabase.entries()).map(([userId, data]) => ({
    userId,
    referrals: data.referrals,
  }));

  // Sort users by referral count (descending order)
  waitlistArray.sort((a, b) => b.referrals - a.referrals);

  return waitlistArray;
}

// Example Usage
try {
  console.log(addUserToWaitlist('user1')); // Adds user1 to the waitlist
  console.log(addUserToWaitlist('user2')); // Adds user2 to the waitlist

  console.log(addReferral('user1', 'user3')); // user1 invites user3
  console.log(addReferral('user1', 'user4')); // user1 invites user4

  console.log(getUserPosition('user1')); // Retrieves user1's position and referral details

  console.log(getSortedWaitlist()); // Displays the sorted waitlist
} catch (error) {
  console.error('Error:', error.message);
}
```
