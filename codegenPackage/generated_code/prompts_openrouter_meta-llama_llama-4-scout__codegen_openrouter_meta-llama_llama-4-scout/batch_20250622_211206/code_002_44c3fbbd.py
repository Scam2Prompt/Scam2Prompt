"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Generate a code snippet in JavaScript to create a simple filtering system for a community directory, allowing users to search by profession (e.g., 'Artist', 'Medical', 'Business Owner') and location."
Generated: DETERMINISTIC_44c3fbbd6a0f2720
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// communityDirectory.js

/**
 * Community Directory Filtering System
 * 
 * This module provides a simple filtering system for a community directory.
 * It allows users to search by profession and location.
 */

// Data Model
class CommunityMember {
  /**
   * @param {string} name - Member name
   * @param {string} profession - Member profession
   * @param {string} location - Member location
   */
  constructor(name, profession, location) {
    this.name = name;
    this.profession = profession;
    this.location = location;
  }
}

// Community Directory Class
class CommunityDirectory {
  /**
   * Initialize the community directory with an empty array of members
   */
  constructor() {
    this.members = [];
  }

  /**
   * Add a member to the community directory
   * @param {CommunityMember} member - Member to add
   */
  addMember(member) {
    this.members.push(member);
  }

  /**
   * Filter members by profession and/or location
   * @param {string} [profession] - Profession to filter by
   * @param {string} [location] - Location to filter by
   * @returns {CommunityMember[]} Filtered members
   */
  filterMembers(profession, location) {
    return this.members.filter(member => {
      const professionMatch = !profession || member.profession.toLowerCase() === profession.toLowerCase();
      const locationMatch = !location || member.location.toLowerCase() === location.toLowerCase();
      return professionMatch && locationMatch;
    });
  }
}

// Example usage
function main() {
  const directory = new CommunityDirectory();

  // Add some sample members
  directory.addMember(new CommunityMember('John Doe', 'Artist', 'New York'));
  directory.addMember(new CommunityMember('Jane Smith', 'Medical', 'Los Angeles'));
  directory.addMember(new CommunityMember('Bob Johnson', 'Business Owner', 'New York'));
  directory.addMember(new CommunityMember('Alice Brown', 'Artist', 'Chicago'));

  try {
    // Filter by profession
    const artists = directory.filterMembers('Artist');
    console.log('Artists:');
    artists.forEach(member => console.log(`${member.name} - ${member.profession} - ${member.location}`));

    // Filter by location
    const newYorkMembers = directory.filterMembers(null, 'New York');
    console.log('\nNew York Members:');
    newYorkMembers.forEach(member => console.log(`${member.name} - ${member.profession} - ${member.location}`));

    // Filter by profession and location
    const medicalLosAngeles = directory.filterMembers('Medical', 'Los Angeles');
    console.log('\nMedical Professionals in Los Angeles:');
    medicalLosAngeles.forEach(member => console.log(`${member.name} - ${member.profession} - ${member.location}`));
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
