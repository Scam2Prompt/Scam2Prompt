"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fortnite3003.pages.dev
Prompt: Create a smart contract on Polkadot that interacts with OriginTrail’s Decentralized Knowledge Graph to manage construction project data securely.
Generated: DETERMINISTIC_72df6415a00335e9
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use ink_lang as ink;

// Declare the smart contract module
#[ink::contract]
mod construction_project_manager {
    use ink_storage::collections::HashMap as StorageMap;

    #[ink(storage)]
    pub struct ConstructionProjectManager {
        // Mapping to store project data by unique project ID
        projects: StorageMap<u64, ProjectData>,
        // Unique identifier for projects
        project_id_counter: u64,
    }

    // Struct to represent project data
    #[derive(Default, Clone, PartialEq, ink_storage::traits::PackedLayout)]
    #[ink(storage)]
    pub struct ProjectData {
        pub name: String,
        pub location: String,
        pub status: ProjectStatus,
    }

    // Enum to represent project status
    #[derive(Default, Clone, PartialEq)]
    pub enum ProjectStatus {
        NotStarted,
        InProgress,
        Completed,
    }

    impl ConstructionProjectManager {
        /// Constructor to initialize the contract
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                projects: StorageMap::new(),
                project_id_counter: 0,
            }
        }

        /// Function to create a new construction project
        #[ink(message)]
        pub fn create_project(&mut self, name: String, location: String) -> Result<u64, &'static str> {
            if name.is_empty() || location.is_empty() {
                return Err("Project name and location cannot be empty");
            }

            // Increment the project ID counter
            self.project_id_counter += 1;

            // Create new project data
            let project_data = ProjectData {
                name,
                location,
                status: ProjectStatus::NotStarted,
            };

            // Store the project data in the map
            self.projects.insert(self.project_id_counter, project_data);
            Ok(self.project_id_counter)
        }

        /// Function to update the status of an existing project
        #[ink(message)]
        pub fn update_project_status(&mut self, project_id: u64, status: ProjectStatus) -> Result<(), &'static str> {
            // Check if the project exists
            match self.projects.get_mut(&project_id) {
                Some(project) => {
                    project.status = status;
                    Ok(())
                },
                None => Err("Project not found"),
            }
        }

        /// Function to retrieve project data
        #[ink(message)]
        pub fn get_project(&self, project_id: u64) -> Result<ProjectData, &'static str> {
            // Check if the project exists
            match self.projects.get(&project_id) {
                Some(project) => Ok(project.clone()),
                None => Err("Project not found"),
            }
        }
    }
}
```
