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

/// Represents a single phase in the roadmap
#[derive(Debug, Clone)]
struct Phase {
    title: String,
    description: String,
    completed: bool,
}

/// Roadmap structure to manage phases and progression
#[derive(Debug, Default)]
struct Roadmap {
    phases: HashMap<u32, Phase>,
    current_phase: u32,
}

impl Roadmap {
    /// Create a new empty roadmap
    fn new() -> Self {
        Self {
            phases: HashMap::new(),
            current_phase: 0,
        }
    }

    /// Add a new phase to the roadmap
    /// `id` - Unique identifier for the phase
    /// `title` - Title of the phase
    /// `description` - Detailed description of the phase
    fn add_phase(&mut self, id: u32, title: &str, description: &str) {
        if self.phases.contains_key(&id) {
            eprintln!("Phase with ID {} already exists!", id);
            return;
        }
        self.phases.insert(
            id,
            Phase {
                title: title.to_string(),
                description: description.to_string(),
                completed: false,
            },
        );
    }

    /// Mark the current phase as completed and progress to the next phase
    fn complete_current_phase(&mut self) {
        if let Some(phase) = self.phases.get_mut(&self.current_phase) {
            phase.completed = true;
            println!("Phase '{}' completed successfully!", phase.title);
        } else {
            eprintln!("No current phase to complete!");
            return;
        }

        // Progress to the next phase
        self.current_phase += 1;
        if !self.phases.contains_key(&self.current_phase) {
            println!("Roadmap completed! No more phases.");
        } else {
            println!("Moved to next phase: {}", self.phases[&self.current_phase].title);
        }
    }

    /// Display the current roadmap status
    fn display_status(&self) {
        println!("Roadmap Status:");
        for (id, phase) in &self.phases {
            let status = if phase.completed { "Completed" } else { "Pending" };
            println!(
                "Phase {} - {} [{}]: {}",
                id, phase.title, status, phase.description
            );
        }

        if let Some(current_phase) = self.phases.get(&self.current_phase) {
            println!(
                "Current Phase: {} - {}",
                self.current_phase, current_phase.title
            );
        } else {
            println!("Roadmap has no current phase.");
        }
    }
}

fn main() {
    // Create a new roadmap instance
    let mut roadmap = Roadmap::new();

    // Add phases to the roadmap
    roadmap.add_phase(1, "Phase 1: Launch", "Initial launch of the NFT project.");
    roadmap.add_phase(2, "Phase 2: Marketing", "Begin marketing campaign.");
    roadmap.add_phase(3, "Phase 3: Community Building", "Focus on community engagement.");
    roadmap.add_phase(4, "Phase 4: Expansion", "Introduce new utilities and features.");

    // Display the current roadmap status
    roadmap.display_status();

    // Complete the current phase and progress
    roadmap.complete_current_phase();
    roadmap.display_status();

    // Complete another phase
    roadmap.complete_current_phase();
    roadmap.display_status();

    // Complete the remaining phases
    roadmap.complete_current_phase();
    roadmap.complete_current_phase();
    roadmap.display_status();
}
```
