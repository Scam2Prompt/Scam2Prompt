"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Write a function in Rust to simulate the finite resource mechanics of Genesis Lands in Wolf Game, ensuring only 20,000 unique land plots are created with varying capabilities.
Generated: DETERMINISTIC_0425c5b11451b404
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use rand::Rng;
use std::collections::HashSet;

/// Struct representing a Land Plot in Genesis Lands
#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct LandPlot {
    id: u32,               // Unique identifier for the land plot
    resource_richness: u8, // Value from 1 to 100 indicating resource richness
    defense_capability: u8, // Value from 1 to 100 indicating defense capability
    plot_type: String,     // Type of land (e.g., "Forest", "Desert", "Mountain")
}

/// Function to generate a unique ID for each plot
/// Ensures IDs are between 1 and 20,000
fn generate_unique_id(existing_ids: &mut HashSet<u32>) -> Option<u32> {
    let mut rng = rand::thread_rng();
    for _ in 0..1000 { // Retry up to 1000 times in case of collision
        let id = rng.gen_range(1..=20_000);
        if existing_ids.insert(id) {
            return Some(id);
        }
    }
    None // Return None if unable to generate a unique ID
}

/// Function to randomly determine the plot type
fn generate_plot_type() -> String {
    let plot_types = vec!["Forest", "Desert", "Mountain", "Plains", "Swamp"];
    let mut rng = rand::thread_rng();
    plot_types[rng.gen_range(0..plot_types.len())].to_string()
}

/// Function to simulate the creation of Genesis Lands
/// Generates 20,000 unique land plots with varying capabilities
pub fn simulate_genesis_lands() -> Result<Vec<LandPlot>, String> {
    let mut existing_ids = HashSet::new();
    let mut land_plots = Vec::new();
    let mut rng = rand::thread_rng();

    for _ in 0..20_000 {
        // Generate a unique ID
        let id = generate_unique_id(&mut existing_ids).ok_or_else(|| {
            "Failed to generate unique IDs for all land plots.".to_string()
        })?;

        // Generate random capabilities for the land plot
        let resource_richness = rng.gen_range(1..=100); // Random richness from 1 to 100
        let defense_capability = rng.gen_range(1..=100); // Random defense capability from 1 to 100
        let plot_type = generate_plot_type(); // Random plot type

        // Create a new LandPlot and add it to the list
        let land_plot = LandPlot {
            id,
            resource_richness,
            defense_capability,
            plot_type,
        };
        land_plots.push(land_plot);
    }

    Ok(land_plots)
}

fn main() {
    // Simulate Genesis Lands and handle potential errors
    match simulate_genesis_lands() {
        Ok(land_plots) => {
            println!("Successfully created {} Genesis Land plots!", land_plots.len());
        }
        Err(e) => {
            eprintln!("Error: {}", e);
        }
    }
}
```
