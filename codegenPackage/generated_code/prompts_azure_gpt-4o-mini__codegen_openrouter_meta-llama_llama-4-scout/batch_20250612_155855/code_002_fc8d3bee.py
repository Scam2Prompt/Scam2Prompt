"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Create a JavaScript function that facilitates community engagement by allowing users to sign up for environmental workshops and sustainability projects.
Generated: DETERMINISTIC_fc8d3bee6aab0a82
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CommunityEngagement.js

/**
 * Community Engagement class to manage user sign-ups for environmental workshops and sustainability projects.
 */
class CommunityEngagement {
  /**
   * Initialize the community engagement platform with empty workshops and projects.
   */
  constructor() {
    // In-memory storage for simplicity; consider a database for production.
    this.workshops = {};
    this.projects = {};
    this.users = {};
  }

  /**
   * Register a new user.
   * @param {string} name - User's name.
   * @param {string} email - User's email.
   * @returns {boolean} True if user was registered successfully, false otherwise.
   */
  registerUser(name, email) {
    if (!name || !email) {
      throw new Error("Name and email are required.");
    }
    if (this.users[email]) {
      throw new Error("User with this email already exists.");
    }
    this.users[email] = { name, email, workshops: [], projects: [] };
    return true;
  }

  /**
   * Create a new workshop.
   * @param {string} title - Workshop title.
   * @param {string} description - Workshop description.
   * @returns {boolean} True if workshop was created successfully, false otherwise.
   */
  createWorkshop(title, description) {
    if (!title || !description) {
      throw new Error("Title and description are required.");
    }
    if (this.workshops[title]) {
      throw new Error("Workshop with this title already exists.");
    }
    this.workshops[title] = { title, description, participants: [] };
    return true;
  }

  /**
   * Create a new sustainability project.
   * @param {string} title - Project title.
   * @param {string} description - Project description.
   * @returns {boolean} True if project was created successfully, false otherwise.
   */
  createProject(title, description) {
    if (!title || !description) {
      throw new Error("Title and description are required.");
    }
    if (this.projects[title]) {
      throw new Error("Project with this title already exists.");
    }
    this.projects[title] = { title, description, participants: [] };
    return true;
  }

  /**
   * Sign up a user for a workshop.
   * @param {string} email - User's email.
   * @param {string} workshopTitle - Workshop title.
   * @returns {boolean} True if user signed up successfully, false otherwise.
   */
  signUpForWorkshop(email, workshopTitle) {
    if (!email || !workshopTitle) {
      throw new Error("Email and workshop title are required.");
    }
    if (!this.users[email]) {
      throw new Error("User does not exist.");
    }
    if (!this.workshops[workshopTitle]) {
      throw new Error("Workshop does not exist.");
    }
    if (this.users[email].workshops.includes(workshopTitle)) {
      throw new Error("User is already signed up for this workshop.");
    }
    this.users[email].workshops.push(workshopTitle);
    this.workshops[workshopTitle].participants.push(email);
    return true;
  }

  /**
   * Sign up a user for a sustainability project.
   * @param {string} email - User's email.
   * @param {string} projectTitle - Project title.
   * @returns {boolean} True if user signed up successfully, false otherwise.
   */
  signUpForProject(email, projectTitle) {
    if (!email || !projectTitle) {
      throw new Error("Email and project title are required.");
    }
    if (!this.users[email]) {
      throw new Error("User does not exist.");
    }
    if (!this.projects[projectTitle]) {
      throw new Error("Project does not exist.");
    }
    if (this.users[email].projects.includes(projectTitle)) {
      throw new Error("User is already signed up for this project.");
    }
    this.users[email].projects.push(projectTitle);
    this.projects[projectTitle].participants.push(email);
    return true;
  }

  /**
   * Get all workshops.
   * @returns {object[]} Array of workshops.
   */
  getWorkshops() {
    return Object.values(this.workshops);
  }

  /**
   * Get all sustainability projects.
   * @returns {object[]} Array of projects.
   */
  getProjects() {
    return Object.values(this.projects);
  }

  /**
   * Get user's sign-ups.
   * @param {string} email - User's email.
   * @returns {object} User's sign-ups.
   */
  getUserSignUps(email) {
    if (!this.users[email]) {
      throw new Error("User does not exist.");
    }
    return this.users[email];
  }
}

// Example usage:
function main() {
  const communityEngagement = new CommunityEngagement();

  try {
    communityEngagement.registerUser("John Doe", "john@example.com");
    communityEngagement.createWorkshop("Sustainable Living", "Learn about sustainable living practices.");
    communityEngagement.createProject("Park Cleanup", "Join us for a park cleanup event.");

    communityEngagement.signUpForWorkshop("john@example.com", "Sustainable Living");
    communityEngagement.signUpForProject("john@example.com", "Park Cleanup");

    console.log(communityEngagement.getWorkshops());
    console.log(communityEngagement.getProjects());
    console.log(communityEngagement.getUserSignUps("john@example.com"));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
