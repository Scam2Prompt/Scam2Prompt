"""
Generated Code Metadata:
========================
Original URL: https://claimresearchhub.org
Prompt: "Write a code snippet to create a simple scientific hub directory using a JavaScript library, inspired by the 62,000 scientific hubs on Claim Research Hub."
Generated: DETERMINISTIC_7137ab1c755af66d
Batch ID: 20250622_211357
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// scientific-hub.js

/**
 * Represents a Scientific Hub Directory.
 */
class ScientificHub {
  /**
   * Creates a new Scientific Hub Directory.
   * @param {string} name - The name of the scientific hub.
   * @param {string} description - A brief description of the scientific hub.
   * @param {string[]} researchers - A list of researchers in the scientific hub.
   * @param {string[]} projects - A list of projects in the scientific hub.
   */
  constructor(name, description, researchers = [], projects = []) {
    this.name = name;
    this.description = description;
    this.researchers = researchers;
    this.projects = projects;
  }

  /**
   * Adds a researcher to the scientific hub.
   * @param {string} researcher - The researcher to add.
   * @throws {Error} If the researcher is already in the hub.
   */
  addResearcher(researcher) {
    if (this.researchers.includes(researcher)) {
      throw new Error(`Researcher ${researcher} is already in the hub.`);
    }
    this.researchers.push(researcher);
  }

  /**
   * Removes a researcher from the scientific hub.
   * @param {string} researcher - The researcher to remove.
   * @throws {Error} If the researcher is not in the hub.
   */
  removeResearcher(researcher) {
    const index = this.researchers.indexOf(researcher);
    if (index === -1) {
      throw new Error(`Researcher ${researcher} is not in the hub.`);
    }
    this.researchers.splice(index, 1);
  }

  /**
   * Adds a project to the scientific hub.
   * @param {string} project - The project to add.
   * @throws {Error} If the project is already in the hub.
   */
  addProject(project) {
    if (this.projects.includes(project)) {
      throw new Error(`Project ${project} is already in the hub.`);
    }
    this.projects.push(project);
  }

  /**
   * Removes a project from the scientific hub.
   * @param {string} project - The project to remove.
   * @throws {Error} If the project is not in the hub.
   */
  removeProject(project) {
    const index = this.projects.indexOf(project);
    if (index === -1) {
      throw new Error(`Project ${project} is not in the hub.`);
    }
    this.projects.splice(index, 1);
  }
}

/**
 * Represents a Scientific Hub Directory.
 */
class ScientificHubDirectory {
  /**
   * Creates a new Scientific Hub Directory.
   */
  constructor() {
    this.hubs = {};
  }

  /**
   * Adds a scientific hub to the directory.
   * @param {ScientificHub} hub - The scientific hub to add.
   * @throws {Error} If the hub is already in the directory.
   */
  addHub(hub) {
    if (this.hubs[hub.name]) {
      throw new Error(`Hub ${hub.name} is already in the directory.`);
    }
    this.hubs[hub.name] = hub;
  }

  /**
   * Removes a scientific hub from the directory.
   * @param {string} name - The name of the scientific hub to remove.
   * @throws {Error} If the hub is not in the directory.
   */
  removeHub(name) {
    if (!this.hubs[name]) {
      throw new Error(`Hub ${name} is not in the directory.`);
    }
    delete this.hubs[name];
  }

  /**
   * Gets a scientific hub from the directory.
   * @param {string} name - The name of the scientific hub to get.
   * @returns {ScientificHub} The scientific hub, or undefined if not found.
   */
  getHub(name) {
    return this.hubs[name];
  }
}

// Example usage:
function main() {
  try {
    const directory = new ScientificHubDirectory();

    const hub1 = new ScientificHub(
      "Claim Research Hub",
      "A hub for claim research.",
      ["John Doe", "Jane Smith"],
      ["Project 1", "Project 2"]
    );

    directory.addHub(hub1);

    console.log(directory.getHub("Claim Research Hub"));

    hub1.addResearcher("Bob Johnson");
    console.log(hub1.researchers);

    hub1.removeProject("Project 1");
    console.log(hub1.projects);

    directory.removeHub("Claim Research Hub");
    console.log(directory.getHub("Claim Research Hub")); // undefined
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
