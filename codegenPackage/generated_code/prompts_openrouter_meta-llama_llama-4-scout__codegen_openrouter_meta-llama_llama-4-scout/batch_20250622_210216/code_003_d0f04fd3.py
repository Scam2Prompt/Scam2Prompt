"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Generate a JavaScript code snippet to create a simple dashboard for tracking project progress and performance metrics, inspired by the services offered by SEGREPIN sarl.
Generated: DETERMINISTIC_d0f04fd398d36b32
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ProjectDashboard.js

/**
 * Represents a project dashboard for tracking progress and performance metrics.
 */
class ProjectDashboard {
  /**
   * Initializes a new instance of the ProjectDashboard class.
   * @param {Object} config - Configuration object containing project data.
   */
  constructor(config) {
    this.config = config;
    this.projects = {};
  }

  /**
   * Adds a new project to the dashboard.
   * @param {String} projectId - Unique identifier for the project.
   * @param {String} projectName - Name of the project.
   * @param {Number} targetProgress - Target progress percentage.
   */
  addProject(projectId, projectName, targetProgress) {
    this.projects[projectId] = {
      name: projectName,
      targetProgress: targetProgress,
      currentProgress: 0,
      metrics: {}
    };
  }

  /**
   * Updates the progress of a project.
   * @param {String} projectId - Unique identifier for the project.
   * @param {Number} progress - Current progress percentage.
   */
  updateProgress(projectId, progress) {
    if (this.projects[projectId]) {
      this.projects[projectId].currentProgress = progress;
    } else {
      throw new Error(`Project ${projectId} not found.`);
    }
  }

  /**
   * Adds a performance metric to a project.
   * @param {String} projectId - Unique identifier for the project.
   * @param {String} metricName - Name of the metric.
   * @param {Number} metricValue - Value of the metric.
   */
  addMetric(projectId, metricName, metricValue) {
    if (this.projects[projectId]) {
      this.projects[projectId].metrics[metricName] = metricValue;
    } else {
      throw new Error(`Project ${projectId} not found.`);
    }
  }

  /**
   * Gets the project dashboard data.
   * @returns {Object} - Project dashboard data.
   */
  getDashboardData() {
    return Object.keys(this.projects).map(projectId => {
      return {
        id: projectId,
        name: this.projects[projectId].name,
        targetProgress: this.projects[projectId].targetProgress,
        currentProgress: this.projects[projectId].currentProgress,
        metrics: this.projects[projectId].metrics
      };
    });
  }
}

// Example usage:
try {
  const dashboard = new ProjectDashboard({});

  dashboard.addProject('proj1', 'Project 1', 100);
  dashboard.addProject('proj2', 'Project 2', 100);

  dashboard.updateProgress('proj1', 50);
  dashboard.addMetric('proj1', 'velocity', 20);

  const dashboardData = dashboard.getDashboardData();
  console.log(dashboardData);
} catch (error) {
  console.error(error.message);
}
```
