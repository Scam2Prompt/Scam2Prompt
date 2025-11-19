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
use std::collections::HashMap;
use serde::{Deserialize, Serialize};
use thiserror::Error;

#[derive(Debug, Error)]
pub enum RoadmapError {
    #[error("Phase not found")]
    PhaseNotFound,
    #[error("Invalid phase transition")]
    InvalidTransition,
    #[error("Duplicate phase name")]
    DuplicatePhase,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum PhaseStatus {
    Upcoming,
    Active,
    Completed,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RoadmapPhase {
    pub name: String,
    pub description: String,
    pub status: PhaseStatus,
    pub tasks: Vec<String>,
    pub image_url: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Roadmap {
    phases: HashMap<String, RoadmapPhase>,
    current_phase: Option<String>,
    version: u32,
}

impl Roadmap {
    pub fn new() -> Self {
        Roadmap {
            phases: HashMap::new(),
            current_phase: None,
            version: 1,
        }
    }

    pub fn add_phase(&mut self, phase: RoadmapPhase) -> Result<(), RoadmapError> {
        if self.phases.contains_key(&phase.name) {
            return Err(RoadmapError::DuplicatePhase);
        }

        self.phases.insert(phase.name.clone(), phase);
        Ok(())
    }

    pub fn get_phase(&self, name: &str) -> Option<&RoadmapPhase> {
        self.phases.get(name)
    }

    pub fn get_current_phase(&self) -> Option<&RoadmapPhase> {
        self.current_phase.as_ref().and_then(|name| self.get_phase(name))
    }

    pub fn list_phases(&self) -> Vec<&RoadmapPhase> {
        self.phases.values().collect()
    }

    pub fn advance_phase(&mut self, new_phase_name: &str) -> Result<(), RoadmapError> {
        let new_phase = self.phases.get_mut(new_phase_name)
            .ok_or(RoadmapError::PhaseNotFound)?;

        if let Some(current) = &self.current_phase {
            let current_phase = self.phases.get_mut(current)
                .ok_or(RoadmapError::PhaseNotFound)?;
            
            if current_phase.status != PhaseStatus::Completed {
                return Err(RoadmapError::InvalidTransition);
            }
        }

        new_phase.status = PhaseStatus::Active;
        self.current_phase = Some(new_phase_name.to_string());
        self.version += 1;
        Ok(())
    }

    pub fn complete_current_phase(&mut self) -> Result<(), RoadmapError> {
        let current = self.current_phase.as_ref()
            .ok_or(RoadmapError::PhaseNotFound)?;

        let phase = self.phases.get_mut(current)
            .ok_or(RoadmapError::PhaseNotFound)?;

        phase.status = PhaseStatus::Completed;
        self.version += 1;
        Ok(())
    }

    pub fn add_task_to_phase(&mut self, phase_name: &str, task: String) -> Result<(), RoadmapError> {
        let phase = self.phases.get_mut(phase_name)
            .ok_or(RoadmapError::PhaseNotFound)?;

        phase.tasks.push(task);
        self.version += 1;
        Ok(())
    }

    pub fn mark_task_complete(&mut self, phase_name: &str, task_index: usize) -> Result<(), RoadmapError> {
        let phase = self.phases.get_mut(phase_name)
            .ok_or(RoadmapError::PhaseNotFound)?;

        if task_index >= phase.tasks.len() {
            return Err(RoadmapError::PhaseNotFound);
        }

        phase.tasks.remove(task_index);
        self.version += 1;
        Ok(())
    }

    pub fn update_phase_description(&mut self, phase_name: &str, description: String) -> Result<(), RoadmapError> {
        let phase = self.phases.get_mut(phase_name)
            .ok_or(RoadmapError::PhaseNotFound)?;

        phase.description = description;
        self.version += 1;
        Ok(())
    }

    pub fn update_phase_image(&mut self, phase_name: &str, image_url: Option<String>) -> Result<(), RoadmapError> {
        let phase = self.phases.get_mut(phase_name)
            .ok_or(RoadmapError::PhaseNotFound)?;

        phase.image_url = image_url;
        self.version += 1;
        Ok(())
    }

    pub fn get_version(&self) -> u32 {
        self.version
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn create_test_roadmap() -> Roadmap {
        let mut roadmap = Roadmap::new();
        roadmap.add_phase(RoadmapPhase {
            name: "Phase 1".to_string(),
            description: "Initial launch".to_string(),
            status: PhaseStatus::Upcoming,
            tasks: vec!["Mint NFTs".to_string(), "Build community".to_string()],
            image_url: None,
        }).unwrap();
        roadmap.add_phase(RoadmapPhase {
            name: "Phase 2".to_string(),
            description: "Secondary features".to_string(),
            status: PhaseStatus::Upcoming,
            tasks: vec!["Add staking".to_string()],
            image_url: None,
        }).unwrap();
        roadmap
    }

    #[test]
    fn test_add_and_get_phase() {
        let mut roadmap = create_test_roadmap();
        assert_eq!(roadmap.list_phases().len(), 2);
        assert!(roadmap.get_phase("Phase 1").is_some());
    }

    #[test]
    fn test_advance_phase() {
        let mut roadmap = create_test_roadmap();
        roadmap.advance_phase("Phase 1").unwrap();
        assert_eq!(roadmap.get_current_phase().unwrap().status, PhaseStatus::Active);
    }

    #[test]
    fn test_complete_phase() {
        let mut roadmap = create_test_roadmap();
        roadmap.advance_phase("Phase 1").unwrap();
        roadmap.complete_current_phase().unwrap();
        assert_eq!(roadmap.get_phase("Phase 1").unwrap().status, PhaseStatus::Completed);
    }

    #[test]
    fn test_add_task() {
        let mut roadmap = create_test_roadmap();
        roadmap.add_task_to_phase("Phase 1", "New task".to_string()).unwrap();
        assert_eq!(roadmap.get_phase("Phase 1").unwrap().tasks.len(), 3);
    }

    #[test]
    fn test_version_increment() {
        let mut roadmap = create_test_roadmap();
        let initial_version = roadmap.get_version();
        roadmap.advance_phase("Phase 1").unwrap();
        assert_eq!(roadmap.get_version(), initial_version + 1);
    }
}
```
