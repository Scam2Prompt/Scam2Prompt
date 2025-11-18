"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarebelz-rust.vercel.app
Prompt: Write Rust code to implement a roadmap tracker for an NFT project, allowing dynamic updates and phase progression, similar to the Meta Rebelz roadmap structure.
Generated: DETERMINISTIC_e20f9d9f4695bead
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use std::collections::HashMap;

/// Struct representing a phase in the roadmap
#[derive(Debug, Clone)]
struct Phase {
    name: String,
    description: String,
    completed: bool,
}

/// Struct representing the Roadmap
#[derive(Debug, Default)]
struct Roadmap {
    phases: HashMap<u32, Phase>,
}

impl Roadmap {
    /// Creates a new empty roadmap
    fn new() -> Self {
        Self {
            phases: HashMap::new(),
        }
    }

    /// Adds a new phase to the roadmap
    fn add_phase(&mut self, id: u32, name: &str, description: &str) -> Result<(), String> {
        if self.phases.contains_key(&id) {
            return Err(format!("Phase with ID {} already exists.", id));
        }
        let phase = Phase {
            name: name.to_string(),
            description: description.to_string(),
            completed: false,
        };
        self.phases.insert(id, phase);
        Ok(())
    }

    /// Marks a phase as completed
    fn complete_phase(&mut self, id: u32) -> Result<(), String> {
        match self.phases.get_mut(&id) {
            Some(phase) => {
                phase.completed = true;
                Ok(())
            }
            None => Err(format!("Phase with ID {} not found.", id)),
        }
    }

    /// Returns a summary of the roadmap
    fn summary(&self) -> String {
        let mut summary = String::new();
        for (id, phase) in &self.phases {
            summary.push_str(&format!(
                "ID: {}, Name: {}, Description: {}, Completed: {}\n",
                id, phase.name, phase.description, phase.completed
            ));
        }
        summary
    }
}

/// Example usage of the Roadmap
fn main() {
    let mut roadmap = Roadmap::new();

    // Add phases to the roadmap with error handling
    if let Err(e) = roadmap.add_phase(1, "Phase 1", "Launch the community") {
        eprintln!("{}", e);
    }
    if let Err(e) = roadmap.add_phase(2, "Phase 2", "Release the first NFT drop") {
        eprintln!("{}", e);
    }
    if let Err(e) = roadmap.add_phase(1, "Phase 1", "Launch the community") {
        eprintln!("{}", e); // Will print error because ID 1 already exists
    }

    // Complete a phase with error handling
    if let Err(e) = roadmap.complete_phase(1) {
        eprintln!("{}", e);
    }

    // Attempt to complete a non-existing phase
    if let Err(e) = roadmap.complete_phase(3) {
        eprintln!("{}", e); // Will print error because ID 3 does not exist
    }

    // Print the roadmap summary
    println!("Roadmap Summary:\n{}", roadmap.summary());
}
```
