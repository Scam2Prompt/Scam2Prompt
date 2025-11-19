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
 * Development Standards for Agoric SDK
 * ======================================
 * 
 * This document outlines the development standards for working with the Agoric SDK.
 * 
 * @author [Your Name]
 */

// Import required modules
const { exec } = require('child_process');
const { promisify } = require('util');

// Define constants
const BRANCH_PREFIX = 'feature/';
const MERGE_COMMIT_MESSAGE = 'Merge branch %s into %s';

/**
 * Create a new branch for a feature
 * @param {string} branchName - Name of the branch
 */
function createBranch(branchName) {
  // Create a new branch with the given name
  const command = `git checkout -b ${BRANCH_PREFIX}${branchName}`;
  return promisify(exec)(command);
}

/**
 * Make a merge commit
 * @param {string} sourceBranch - Source branch
 * @param {string} targetBranch - Target branch
 */
function makeMergeCommit(sourceBranch, targetBranch) {
  // Checkout the target branch
  const checkoutCommand = `git checkout ${targetBranch}`;
  return promisify(exec)(checkoutCommand)
    .then(() => {
      // Merge the source branch into the target branch
      const mergeCommand = `git merge ${sourceBranch}`;
      return promisify(exec)(mergeCommand);
    })
    .then(() => {
      // Create a merge commit message
      const commitMessage = MERGE_COMMIT_MESSAGE.replace('%s', sourceBranch).replace('%s', targetBranch);
      const commitCommand = `git commit --amend -m "${commitMessage}"`;
      return promisify(exec)(commitCommand);
    });
}

/**
 * Track issues
 * @param {string} issueNumber - Issue number
 * @param {string} branchName - Branch name
 */
function trackIssue(issueNumber, branchName) {
  // Create a comment on the issue with the branch name
  const comment = `Branch created: ${BRANCH_PREFIX}${branchName}`;
  // Use a GitHub API or similar to create a comment on the issue
  // For demonstration purposes, just log the comment
  // console.log(comment); // Commented out to avoid the error
  return Promise.resolve();
}

// Example usage
async function main() {
  try {
    // Create a new branch
    const branchName = 'example-feature';
    await createBranch(branchName);
    console.log(`Branch created: ${BRANCH_PREFIX}${branchName}`);

    // Make a merge commit
    const sourceBranch = `${BRANCH_PREFIX}${branchName}`;
    const targetBranch = 'main';
    await makeMergeCommit(sourceBranch, targetBranch);
    console.log(`Merge commit made: ${sourceBranch} into ${targetBranch}`);

    // Track issues
    const issueNumber = '123';
    await trackIssue(issueNumber, branchName);
    console.log(`Issue tracked: ${issueNumber}`);
  } catch (error) {
    console.error(error);
  }
}

main();
```
