"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Provide an example of contributing to a Rust open-source project.
Generated: DETERMINISTIC_e98aa49a6f3de493
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use std::collections::HashMap;
use std::error::Error;
use std::fs;

// Define a struct to represent a contributor
#[derive(Debug)]
struct Contributor {
    name: String,
    contributions: u32,
}

// Implement methods for the Contributor struct
impl Contributor {
    fn new(name: String) -> Contributor {
        Contributor { name, contributions: 0 }
    }

    fn add_contribution(&mut self) {
        self.contributions += 1;
    }
}

// Define a struct to represent a project
#[derive(Debug)]
struct Project {
    name: String,
    contributors: HashMap<String, Contributor>,
}

// Implement methods for the Project struct
impl Project {
    fn new(name: String) -> Project {
        Project {
            name,
            contributors: HashMap::new(),
        }
    }

    fn add_contributor(&mut self, name: String) -> Result<(), Box<dyn Error>> {
        if self.contributors.contains_key(&name) {
            return Err("Contributor already exists".into());
        }
        self.contributors.insert(name.clone(), Contributor::new(name));
        Ok(())
    }

    fn add_contribution(&mut self, name: String) -> Result<(), Box<dyn Error>> {
        if let Some(contributor) = self.contributors.get_mut(&name) {
            contributor.add_contribution();
            Ok(())
        } else {
            Err("Contributor not found".into())
        }
    }

    fn save_to_file(&self, filename: &str) -> Result<(), Box<dyn Error>> {
        let data = serde_json::to_string(self)?;
        fs::write(filename, data)?;
        Ok(())
    }

    fn load_from_file(filename: &str) -> Result<Project, Box<dyn Error>> {
        let data = fs::read_to_string(filename)?;
        let project: Project = serde_json::from_str(&data)?;
        Ok(project)
    }
}

// Implement Serialize and Deserialize traits for Contributor and Project
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct ContributorSerializable {
    name: String,
    contributions: u32,
}

impl From<Contributor> for ContributorSerializable {
    fn from(c: Contributor) -> Self {
        ContributorSerializable {
            name: c.name,
            contributions: c.contributions,
        }
    }
}

impl From<ContributorSerializable> for Contributor {
    fn from(c: ContributorSerializable) -> Self {
        Contributor {
            name: c.name,
            contributions: c.contributions,
        }
    }
}

#[derive(Serialize, Deserialize, Debug)]
struct ProjectSerializable {
    name: String,
    contributors: Vec<ContributorSerializable>,
}

impl From<Project> for ProjectSerializable {
    fn from(p: Project) -> Self {
        ProjectSerializable {
            name: p.name,
            contributors: p.contributors.into_values().map(ContributorSerializable::from).collect(),
        }
    }
}

impl From<ProjectSerializable> for Project {
    fn from(p: ProjectSerializable) -> Self {
        let mut project = Project::new(p.name);
        for contributor in p.contributors {
            project.contributors.insert(contributor.name.clone(), contributor.into());
        }
        project
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    // Create a new project
    let mut project = Project::new("Rust Open-Source Project".to_string());

    // Add contributors
    project.add_contributor("John Doe".to_string())?;
    project.add_contributor("Jane Doe".to_string())?;

    // Add contributions
    project.add_contribution("John Doe".to_string())?;
    project.add_contribution("John Doe".to_string())?;
    project.add_contribution("Jane Doe".to_string())?;

    // Save project to file
    project.save_to_file("project.json")?;

    // Load project from file
    let loaded_project = Project::load_from_file("project.json")?;

    // Print loaded project
    println!("Loaded Project: {:?}", loaded_project);

    Ok(())
}
```
