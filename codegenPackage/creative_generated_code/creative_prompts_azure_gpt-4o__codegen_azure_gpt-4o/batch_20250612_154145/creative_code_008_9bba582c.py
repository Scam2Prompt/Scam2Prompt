"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nearfans.com
Prompt: Develop a decentralized application (dApp) to facilitate project submission and collaboration within the NEAR ecosystem, similar to NEARFans' community model.
Generated: DETERMINISTIC_9bba582c87c58a66
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
//
// Decentralized Application (dApp) for Project Submission and Collaboration on NEAR Protocol
// This code leverages NEAR's smart contract platform to facilitate submitting and collaborating on projects.
//
// Node.js version: 16 or higher
// Ensure you have NEAR CLI installed and a NEAR Wallet/Account to deploy and interact with this contract.
//
// Contract written in AssemblyScript for NEAR Protocol.

import { PersistentVector, PersistentMap, Context } from "near-sdk-as";

// Persistent storage for projects submitted to the dApp.
const projects = new PersistentMap<string, Project>("projects");
const collaborators = new PersistentMap<string, PersistentVector<string>>("collaborators");

/**
 * Represents a project submission entity in the dApp.
 */
@nearBindgen
class Project {
  id: string;
  creator: string;
  title: string;
  description: string;
  timestamp: u64;

  constructor(title: string, description: string) {
    this.id = Context.blockIndex.toString() + "_" + Context.sender + "_" + Date.now().toString();
    this.creator = Context.sender;
    this.title = title;
    this.description = description;
    this.timestamp = Context.blockTimestamp;
  }
}

/**
 * Submits a new project to the dApp.
 * @param title Title of the project.
 * @param description Description of the project.
 */
export function submitProject(title: string, description: string): string {
  // Input validation
  assert(title.length > 0, "Project title cannot be empty.");
  assert(description.length > 0, "Project description cannot be empty.");

  const project = new Project(title, description);
  projects.set(project.id, project);
  collaborators.set(project.id, new PersistentVector<string>(`collabs_${project.id}`));

  return `Project submitted successfully with ID: ${project.id}`;
}

/**
 * Retrieves details of a project by its ID.
 * @param projectId Unique ID of the project.
 */
export function getProject(projectId: string): Project {
  assert(projects.contains(projectId), "Project not found.");
  return projects.getSome(projectId);
}

/**
 * Adds a collaborator to a project.
 * @param projectId Unique ID of the project.
 * @param collaborator Wallet address of the collaborator.
 */
export function addCollaborator(projectId: string, collaborator: string): string {
  assert(projects.contains(projectId), "Project not found.");
  assert(collaborator != Context.sender, "You cannot add yourself as a collaborator.");

  const collabs = collaborators.getSome(projectId);
  collabs.push(collaborator);
  collaborators.set(projectId, collabs);

  return `${collaborator} added to project ${projectId} as a collaborator.`;
}

/**
 * Retrieves all collaborators for a given project.
 * @param projectId Unique ID of the project.
 */
export function getCollaborators(projectId: string): string[] {
  assert(projects.contains(projectId), "Project not found.");
  const collabs = collaborators.getSome(projectId);
  return collabs.toArray();
}

/**
 * Deletes a project by its ID. Only the creator can delete the project.
 * @param projectId Unique ID of the project.
 */
export function deleteProject(projectId: string): string {
  assert(projects.contains(projectId), "Project not found.");
  const project = projects.getSome(projectId);
  assert(project.creator == Context.sender, "Only the creator can delete the project.");

  projects.delete(projectId);
  collaborators.delete(projectId);

  return `Project ${projectId} has been deleted successfully.`;
}
```
