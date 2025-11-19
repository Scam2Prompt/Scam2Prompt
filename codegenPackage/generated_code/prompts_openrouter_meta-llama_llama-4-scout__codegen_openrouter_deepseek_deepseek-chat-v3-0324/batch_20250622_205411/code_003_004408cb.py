"""
Generated Code Metadata:
========================
Original URL: https://justicetree-mint.com
Prompt: "Design a library for tracking and reporting social justice issues using JavaScript."
Generated: DETERMINISTIC_004408cbb8967837
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Social Justice Tracker Library
 * A library for tracking and reporting social justice issues.
 */

class SocialJusticeTracker {
  constructor() {
    this.issues = [];
    this.categories = new Set();
    this.statistics = {
      totalReports: 0,
      byCategory: {},
      bySeverity: {
        low: 0,
        medium: 0,
        high: 0
      }
    };
  }

  /**
   * Add a new social justice issue
   * @param {string} title - Title of the issue
   * @param {string} description - Description of the issue
   * @param {string} category - Category of the issue
   * @param {string} severity - Severity level (low, medium, high)
   * @param {Object} location - Location data {latitude, longitude, address}
   * @param {Date} date - Date of occurrence
   * @returns {Object} The created issue
   */
  addIssue(title, description, category, severity, location, date = new Date()) {
    if (!title || !description || !category || !severity || !location) {
      throw new Error('Missing required fields');
    }

    if (!['low', 'medium', 'high'].includes(severity)) {
      throw new Error('Invalid severity level');
    }

    const issue = {
      id: this._generateId(),
      title,
      description,
      category,
      severity,
      location,
      date,
      status: 'reported',
      createdAt: new Date(),
      updatedAt: new Date()
    };

    this.issues.push(issue);
    this.categories.add(category);
    this._updateStatistics(issue);
    return issue;
  }

  /**
   * Update an existing issue
   * @param {string} id - Issue ID
   * @param {Object} updates - Fields to update
   * @returns {Object} The updated issue
   */
  updateIssue(id, updates) {
    const issueIndex = this.issues.findIndex(issue => issue.id === id);
    if (issueIndex === -1) {
      throw new Error('Issue not found');
    }

    const updatedIssue = {
      ...this.issues[issueIndex],
      ...updates,
      updatedAt: new Date()
    };

    if (updates.severity && !['low', 'medium', 'high'].includes(updates.severity)) {
      throw new Error('Invalid severity level');
    }

    this.issues[issueIndex] = updatedIssue;
    this._updateStatistics(updatedIssue, true);
    return updatedIssue;
  }

  /**
   * Get all issues
   * @param {Object} filters - Optional filters
   * @returns {Array} Filtered issues
   */
  getIssues(filters = {}) {
    let filteredIssues = [...this.issues];

    if (filters.category) {
      filteredIssues = filteredIssues.filter(issue => issue.category === filters.category);
    }

    if (filters.severity) {
      filteredIssues = filteredIssues.filter(issue => issue.severity === filters.severity);
    }

    if (filters.status) {
      filteredIssues = filteredIssues.filter(issue => issue.status === filters.status);
    }

    if (filters.startDate) {
      const startDate = new Date(filters.startDate);
      filteredIssues = filteredIssues.filter(issue => new Date(issue.date) >= startDate);
    }

    if (filters.endDate) {
      const endDate = new Date(filters.endDate);
      filteredIssues = filteredIssues.filter(issue => new Date(issue.date) <= endDate);
    }

    return filteredIssues;
  }

  /**
   * Get issue by ID
   * @param {string} id - Issue ID
   * @returns {Object} The issue
   */
  getIssueById(id) {
    const issue = this.issues.find(issue => issue.id === id);
    if (!issue) {
      throw new Error('Issue not found');
    }
    return issue;
  }

  /**
   * Get all categories
   * @returns {Array} List of categories
   */
  getCategories() {
    return Array.from(this.categories);
  }

  /**
   * Get statistics
   * @returns {Object} Statistics object
   */
  getStatistics() {
    return this.statistics;
  }

  /**
   * Generate a report
   * @param {Object} options - Report options
   * @returns {Object} Report data
   */
  generateReport(options = {}) {
    const { format = 'summary' } = options;
    
    if (format === 'summary') {
      return {
        totalIssues: this.statistics.totalReports,
        categories: this.getCategories(),
        severityBreakdown: this.statistics.bySeverity,
        recentIssues: this.getIssues().slice(-5).reverse()
      };
    } else if (format === 'detailed') {
      return {
        statistics: this.getStatistics(),
        issues: this.getIssues(),
        categories: this.getCategories()
      };
    } else {
      throw new Error('Invalid report format');
    }
  }

  /**
   * Export issues to JSON
   * @returns {string} JSON string
   */
  exportToJSON() {
    return JSON.stringify({
      issues: this.issues,
      statistics: this.statistics,
      categories: this.getCategories()
    }, null, 2);
  }

  /**
   * Import issues from JSON
   * @param {string} json - JSON string
   */
  importFromJSON(json) {
    const data = JSON.parse(json);
    if (!data.issues || !Array.isArray(data.issues)) {
      throw new Error('Invalid JSON format');
    }

    this.issues = data.issues;
    this.statistics = data.statistics || {
      totalReports: 0,
      byCategory: {},
      bySeverity: {
        low: 0,
        medium: 0,
        high: 0
      }
    };
    this.categories = new Set(data.categories || []);
  }

  // Private methods
  _generateId() {
    return Math.random().toString(36).substring(2, 15) + 
           Math.random().toString(36).substring(2, 15);
  }

  _updateStatistics(issue, isUpdate = false) {
    if (!isUpdate) {
      this.statistics.totalReports++;
      this.statistics.bySeverity[issue.severity]++;
      
      if (!this.statistics.byCategory[issue.category]) {
        this.statistics.byCategory[issue.category] = 0;
      }
      this.statistics.byCategory[issue.category]++;
    } else {
      // For updates, we would need to track previous state to adjust statistics
      // This is simplified for demonstration
    }
  }
}

// Export the class for use in other modules
module.exports = SocialJusticeTracker;
```
