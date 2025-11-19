"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Write Rust code to implement a roadmap tracker for an NFT project, allowing dynamic updates and phase progression, similar to the Meta Rebelz roadmap structure.
Generated: DETERMINISTIC_e20f9d9f4695bead
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// roadmap_tracker.rs

use std::collections::HashMap;
use std::error::Error;
use std::fmt;

// Define a custom error type for the roadmap tracker
#[derive(Debug)]
enum RoadmapError {
    PhaseNotFound,
    InvalidPhaseProgression,
    DuplicatePhase,
}

impl fmt::Display for RoadmapError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            RoadmapError::PhaseNotFound => write!(f, "Phase not found"),
            RoadmapError::InvalidPhaseProgression => write!(f, "Invalid phase progression"),
            RoadmapError::DuplicatePhase => write!(f, "Duplicate phase"),
        }
    }
}

impl Error for RoadmapError {}

// Define a struct to represent a phase in the roadmap
#[derive(Debug, PartialEq, Eq, Clone)]
struct Phase {
    name: String,
    description: String,
    completed: bool,
}

// Define a struct to represent the roadmap tracker
pub struct RoadmapTracker {
    phases: HashMap<String, Phase>,
    phase_order: Vec<String>,
    current_phase_index: usize,
}

impl RoadmapTracker {
    // Create a new roadmap tracker
    pub fn new() -> Self {
        RoadmapTracker {
            phases: HashMap::new(),
            phase_order: Vec::new(),
            current_phase_index: 0,
        }
    }

    // Add a new phase to the roadmap
    pub fn add_phase(&mut self, name: String, description: String) -> Result<(), RoadmapError> {
        if self.phases.contains_key(&name) {
            return Err(RoadmapError::DuplicatePhase);
        }
        self.phases.insert(name.clone(), Phase {
            name,
            description,
            completed: false,
        });
        self.phase_order.push(name);
        Ok(())
    }

    // Mark a phase as completed and progress to the next phase
    pub fn complete_phase(&mut self, phase_name: &str) -> Result<(), RoadmapError> {
        let phase = self.phases.get_mut(phase_name);
        if phase.is_none() {
            return Err(RoadmapError::PhaseNotFound);
        }
        let phase = phase.unwrap();
        if phase.completed {
            return Err(RoadmapError::InvalidPhaseProgression);
        }
        phase.completed = true;

        // Update the current phase index
        let current_phase = &self.phase_order[self.current_phase_index];
        if current_phase == phase_name {
            self.current_phase_index += 1;
            if self.current_phase_index >= self.phase_order.len() {
                self.current_phase_index = self.phase_order.len() - 1;
            }
        }
        Ok(())
    }

    // Get the current phase
    pub fn get_current_phase(&self) -> Option<&Phase> {
        if self.current_phase_index < self.phase_order.len() {
            let current_phase_name = &self.phase_order[self.current_phase_index];
            self.phases.get(current_phase_name)
        } else {
            None
        }
    }

    // Get the next phase
    pub fn get_next_phase(&self) -> Option<&Phase> {
        if self.current_phase_index + 1 < self.phase_order.len() {
            let next_phase_name = &self.phase_order[self.current_phase_index + 1];
            self.phases.get(next_phase_name)
        } else {
            None
        }
    }
}

fn main() -> Result<(), RoadmapError> {
    let mut tracker = RoadmapTracker::new();

    tracker.add_phase("Phase 1".to_string(), "Description for phase 1".to_string())?;
    tracker.add_phase("Phase 2".to_string(), "Description for phase 2".to_string())?;
    tracker.add_phase("Phase 3".to_string(), "Description for phase 3".to_string())?;

    println!("Current phase: {:?}", tracker.get_current_phase());

    tracker.complete_phase("Phase 1")?;
    println!("Current phase: {:?}", tracker.get_current_phase());

    tracker.complete_phase("Phase 2")?;
    println!("Current phase: {:?}", tracker.get_current_phase());

    Ok(())
}
```
