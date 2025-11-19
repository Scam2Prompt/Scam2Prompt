"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Generate a code snippet in JavaScript to implement a simple Agile project management tool that integrates with Crestagile’s expert-led courses.
Generated: DETERMINISTIC_8a67362c5dc6fe84
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// AgileProject.js

/**
 * Represents an Agile project.
 */
class AgileProject {
  /**
   * Creates a new Agile project.
   * @param {string} name - The project's name.
   * @param {string} description - The project's description.
   */
  constructor(name, description) {
    this.name = name;
    this.description = description;
    this.tasks = [];
  }

  /**
   * Adds a task to the project.
   * @param {string} taskName - The task's name.
   * @param {string} taskDescription - The task's description.
   * @param {string} taskStatus - The task's status (e.g., "To-Do", "In Progress", "Done").
   */
  addTask(taskName, taskDescription, taskStatus) {
    const task = {
      name: taskName,
      description: taskDescription,
      status: taskStatus,
    };
    this.tasks.push(task);
  }

  /**
   * Updates a task's status.
   * @param {string} taskName - The task's name.
   * @param {string} newStatus - The task's new status.
   */
  updateTaskStatus(taskName, newStatus) {
    const taskIndex = this.tasks.findIndex((task) => task.name === taskName);
    if (taskIndex !== -1) {
      this.tasks[taskIndex].status = newStatus;
    } else {
      throw new Error(`Task '${taskName}' not found.`);
    }
  }

  /**
   * Removes a task from the project.
   * @param {string} taskName - The task's name.
   */
  removeTask(taskName) {
    this.tasks = this.tasks.filter((task) => task.name !== taskName);
  }

  /**
   * Gets all tasks in the project.
   * @returns {Object[]} An array of tasks.
   */
  getTasks() {
    return this.tasks;
  }
}

// CrestagileCourse.js

/**
 * Represents a Crestagile course.
 */
class CrestagileCourse {
  /**
   * Creates a new Crestagile course.
   * @param {string} name - The course's name.
   * @param {string} description - The course's description.
   */
  constructor(name, description) {
    this.name = name;
    this.description = description;
  }

  /**
   * Integrates with an Agile project.
   * @param {AgileProject} project - The Agile project to integrate with.
   */
  integrateWithProject(project) {
    // Simulate integration by logging a message
    // In a real-world scenario, this would involve API calls or data exchange
    // eslint-disable-next-line no-console
    console.log(`Integrating ${this.name} with ${project.name}...`);
  }
}

// AgileProjectManagementTool.js

/**
 * Represents an Agile project management tool.
 */
class AgileProjectManagementTool {
  /**
   * Creates a new Agile project management tool.
   */
  constructor() {
    this.projects = [];
    this.courses = [];
  }

  /**
   * Creates a new Agile project.
   * @param {string} projectName - The project's name.
   * @param {string} projectDescription - The project's description.
   */
  createProject(projectName, projectDescription) {
    const project = new AgileProject(projectName, projectDescription);
    this.projects.push(project);
    return project;
  }

  /**
   * Adds a Crestagile course.
   * @param {string} courseName - The course's name.
   * @param {string} courseDescription - The course's description.
   */
  addCourse(courseName, courseDescription) {
    const course = new CrestagileCourse(courseName, courseDescription);
    this.courses.push(course);
    return course;
  }

  /**
   * Integrates a course with a project.
   * @param {string} courseName - The course's name.
   * @param {string} projectName - The project's name.
   */
  integrateCourseWithProject(courseName, projectName) {
    const course = this.courses.find((course) => course.name === courseName);
    const project = this.projects.find((project) => project.name === projectName);
    if (course && project) {
      course.integrateWithProject(project);
    } else {
      throw new Error(`Course or project not found.`);
    }
  }
}

// Example usage:

function main() {
  try {
    const tool = new AgileProjectManagementTool();

    // Create a new Agile project
    const project = tool.createProject("My Agile Project", "This is a sample Agile project.");

    // Add tasks to the project
    project.addTask("Task 1", "This is task 1.", "To-Do");
    project.addTask("Task 2", "This is task 2.", "In Progress");

    // Create a new Crestagile course
    const course = tool.addCourse("Crestagile Course", "This is a sample Crestagile course.");

    // Integrate the course with the project
    tool.integrateCourseWithProject("Crestagile Course", "My Agile Project");

    // Log tasks in the project
    // eslint-disable-next-line no-console
    console.log("Tasks in the project:");
    project.getTasks().forEach((task) => {
      // eslint-disable-next-line no-console
      console.log(`- ${task.name} (${task.status})`);
    });
  } catch (error) {
    // eslint-disable-next-line no-console
    console.error(error.message);
  }
}

main();
```
