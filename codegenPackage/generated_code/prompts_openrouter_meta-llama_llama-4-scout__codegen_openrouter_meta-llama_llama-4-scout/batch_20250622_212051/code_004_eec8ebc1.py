"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Write a JavaScript function to create a searchable database of mentors with different backgrounds and career paths.
Generated: DETERMINISTIC_eec8ebc185ee75c2
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a Mentor with background and career path information.
 */
class Mentor {
  /**
   * Creates a new Mentor instance.
   * @param {string} id - Unique identifier for the mentor.
   * @param {string} name - Name of the mentor.
   * @param {string} background - Background information of the mentor.
   * @param {string} careerPath - Career path information of the mentor.
   */
  constructor(id, name, background, careerPath) {
    this.id = id;
    this.name = name;
    this.background = background;
    this.careerPath = careerPath;
  }
}

/**
 * Represents a searchable database of mentors.
 */
class MentorDatabase {
  /**
   * Creates a new MentorDatabase instance.
   */
  constructor() {
    this.mentors = [];
  }

  /**
   * Adds a mentor to the database.
   * @param {Mentor} mentor - Mentor instance to add.
   */
  addMentor(mentor) {
    if (!(mentor instanceof Mentor)) {
      throw new Error('Invalid mentor instance');
    }
    this.mentors.push(mentor);
  }

  /**
   * Searches for mentors by name, background, or career path.
   * @param {string} query - Search query.
   * @returns {Mentor[]} Array of mentors matching the search query.
   */
  searchMentors(query) {
    if (typeof query !== 'string') {
      throw new Error('Invalid search query');
    }
    return this.mentors.filter(mentor => {
      return mentor.name.toLowerCase().includes(query.toLowerCase()) ||
             mentor.background.toLowerCase().includes(query.toLowerCase()) ||
             mentor.careerPath.toLowerCase().includes(query.toLowerCase());
    });
  }

  /**
   * Retrieves a mentor by ID.
   * @param {string} id - ID of the mentor to retrieve.
   * @returns {Mentor|null} Mentor instance or null if not found.
   */
  getMentorById(id) {
    if (typeof id !== 'string') {
      throw new Error('Invalid mentor ID');
    }
    return this.mentors.find(mentor => mentor.id === id) || null;
  }
}

// Example usage:
function main() {
  const db = new MentorDatabase();

  const mentor1 = new Mentor('1', 'John Doe', 'Software Engineer', 'Backend Development');
  const mentor2 = new Mentor('2', 'Jane Smith', 'Data Scientist', 'Machine Learning');

  db.addMentor(mentor1);
  db.addMentor(mentor2);

  console.log('Search results for "Software":');
  const searchResults = db.searchMentors('Software');
  searchResults.forEach(mentor => console.log(mentor.name));

  console.log('Mentor with ID "1":');
  const mentor = db.getMentorById('1');
  if (mentor) {
    console.log(mentor.name, mentor.background, mentor.careerPath);
  } else {
    console.log('Mentor not found');
  }
}

main();
```
