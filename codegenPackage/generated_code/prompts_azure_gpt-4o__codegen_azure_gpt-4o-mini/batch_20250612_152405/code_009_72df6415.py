"""
Generated Code Metadata:
========================
Original URL: https://fortnite3003.pages.dev
Prompt: Create a smart contract on Polkadot that interacts with OriginTrail’s Decentralized Knowledge Graph to manage construction project data securely.
Generated: DETERMINISTIC_72df6415a00335e9
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries and modules
use ink_lang as ink;

#[ink::contract]
mod construction_project_manager {
    use ink_storage::collections::HashMap as StorageHashMap;

    /// The main contract structure
    #[ink(storage)]
    pub struct ConstructionProjectManager {
        // Mapping of project IDs to project data
        projects: StorageHashMap<u32, ProjectData>,
        // Counter for project IDs
        project_id_counter: u32,
    }

    /// Structure to hold project data
    #[derive(scale::Encode, scale::Decode, Clone, PartialEq, Eq, Debug)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub struct ProjectData {
        name: String,
        description: String,
        owner: AccountId,
        status: ProjectStatus,
    }

    /// Enum to represent project status
    #[derive(scale::Encode, scale::Decode, Clone, PartialEq, Eq, Debug)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo))]
    pub enum ProjectStatus {
        Active,
        Completed,
        Cancelled,
    }

    impl ConstructionProjectManager {
        /// Creates a new contract instance
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                projects: StorageHashMap::new(),
                project_id_counter: 0,
            }
        }

        /// Function to create a new construction project
        #[ink(message)]
        pub fn create_project(&mut self, name: String, description: String) -> Result<u32, &'static str> {
            // Validate input
            if name.is_empty() || description.is_empty() {
                return Err("Project name and description cannot be empty");
            }

            // Increment project ID counter
            self.project_id_counter += 1;

            // Create new project data
            let project_data = ProjectData {
                name,
                description,
                owner: self.env().caller(),
                status: ProjectStatus::Active,
            };

            // Store the project data
            self.projects.insert(self.project_id_counter, project_data);

            // Return the new project ID
            Ok(self.project_id_counter)
        }

        /// Function to update the status of a project
        #[ink(message)]
        pub fn update_project_status(&mut self, project_id: u32, status: ProjectStatus) -> Result<(), &'static str> {
            // Check if the project exists
            let project = self.projects.get_mut(&project_id).ok_or("Project not found")?;

            // Ensure only the owner can update the project status
            if project.owner != self.env().caller() {
                return Err("Only the project owner can update the status");
            }

            // Update the project status
            project.status = status;
            Ok(())
        }

        /// Function to retrieve project details
        #[ink(message)]
        pub fn get_project(&self, project_id: u32) -> Result<ProjectData, &'static str> {
            // Check if the project exists
            self.projects.get(&project_id).cloned().ok_or("Project not found")
        }
    }

    // Implement the default trait for the contract
    impl Default for ConstructionProjectManager {
        fn default() -> Self {
            Self::new()
        }
    }
}
```
