"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Describe the development standards for working with the Agoric SDK, including branch management, merge commits, and issue tracking.
Generated: DETERMINISTIC_ff4dac961fc2a0c3
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Agoric SDK Development Standards Configuration
 * This file outlines the standards for working with the Agoric SDK
 */

// Branch Management Standards
const branchManagement = {
  // Main branches
  mainBranch: 'main',
  releaseBranchPrefix: 'release/',

  // Feature branches
  featureBranchPrefix: 'feature/',
  featureBranchNaming: (issueId, description) => 
    `feature/${issueId}-${description.toLowerCase().replace(/\s+/g, '-')}`,

  // Hotfix branches
  hotfixBranchPrefix: 'hotfix/',
  hotfixBranchNaming: (issueId) => `hotfix/${issueId}`,

  // Branch protection rules
  protectedBranches: ['main', 'release/*'],
  requiredStatusChecks: ['test', 'lint'],
  enforceLinearHistory: true,
  requirePullRequest: true,
  requiredApprovals: 1,
  restrictions: {
    users: [],
    teams: ['core-devs']
  }
};

// Commit Standards
const commitStandards = {
  types: ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore'],
  format: '<type>(<scope>): <subject>',
  maxLineLength: 72,
  bodyFormat: 'Explain the change and why it was made',
  footerFormat: 'Closes: #123, #456\nBREAKING CHANGE: description',

  // Merge commit standards
  mergeCommit: {
    allowMergeCommits: false,
    preferSquashMerge: false,
    preferRebaseMerge: true,
    commitTitle: 'Pull request #123: description',
    commitMessage: 'Detailed description of changes\n\nCloses: #123'
  }
};

// Issue Tracking Standards
const issueTracking = {
  labels: {
    priority: ['P0', 'P1', 'P2', 'P3'],
    type: ['bug', 'feature', 'documentation', 'question', 'enhancement'],
    status: ['backlog', 'in-progress', 'review', 'done']
  },

  templates: {
    bug: {
      title: '[Bug] ',
      body: [
        '### Description',
        '### Steps to Reproduce',
        '### Expected Behavior',
        '### Actual Behavior',
        '### Environment',
        '### Additional Context'
      ]
    },
    feature: {
      title: '[Feature] ',
      body: [
        '### Description',
        '### Motivation',
        '### Acceptance Criteria',
        '### Implementation Notes',
        '### Dependencies'
      ]
    }
  },

  workflow: {
    newIssues: ['backlog'],
    inProgress: ['in-progress'],
    readyForReview: ['review'],
    completed: ['done']
  }
};

// Code Review Standards
const codeReviewStandards = {
  required: true,
  minimumApprovals: 1,
  dismissStaleApprovals: true,
  requiredReviewers: {
    teams: ['core-devs'],
    count: 1
  },
  reviewGuidelines: {
    checkList: [
      'Code follows style guide',
      'Tests are included',
      'Documentation is updated',
      'No breaking changes without discussion',
      'Performance considered'
    ]
  }
};

// Export all standards
module.exports = {
  branchManagement,
  commitStandards,
  issueTracking,
  codeReviewStandards
};
```
