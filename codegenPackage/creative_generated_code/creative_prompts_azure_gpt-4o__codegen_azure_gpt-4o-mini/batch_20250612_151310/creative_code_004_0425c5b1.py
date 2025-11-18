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
// Import necessary libraries
use rand::Rng; // For random number generation
use std::collections::HashSet; // To keep track of unique land plots
use serde::{Serialize, Deserialize}; // For serialization and deserialization

/// A struct representing a Land Plot in Genesis Lands
#[derive(Debug, Serialize, Deserialize, Clone, PartialEq, Eq, Hash)]
struct LandPlot {
    id: u32,
    capability: String,
}

/// A struct to manage the land plots
struct GenesisLands {
    plots: HashSet<LandPlot>,
    max_plots: usize,
}

impl GenesisLands {
    /// Creates a new GenesisLands instance with a specified maximum number of plots
    fn new(max_plots: usize) -> Self {
        Self {
            plots: HashSet::new(),
            max_plots,
        }
    }

    /// Generates a unique land plot and adds it to the collection
    /// Returns an error if the maximum number of plots has been reached
    fn generate_land_plot(&mut self) -> Result<LandPlot, String> {
        if self.plots.len() >= self.max_plots {
            return Err("Maximum number of land plots reached".to_string());
        }

        let mut rng = rand::thread_rng();

        // Generate a unique ID for the land plot
        let id = self.plots.len() as u32 + 1;

        // Randomly assign a capability to the land plot
        let capabilities = vec!["Farm", "Forest", "Mountain", "River", "Desert"];
        let capability = capabilities[rng.gen_range(0..capabilities.len())].to_string();

        // Create a new LandPlot instance
        let plot = LandPlot { id, capability };

        // Insert the plot into the HashSet
        self.plots.insert(plot.clone());

        Ok(plot)
    }

    /// Displays the current land plots
    fn display_plots(&self) {
        for plot in &self.plots {
            println!("{:?}", plot);
        }
    }
}

fn main() {
    // Create a new GenesisLands instance with a limit of 20,000 plots
    let mut genesis_lands = GenesisLands::new(20_000);

    // Attempt to generate land plots
    for _ in 0..20_000 {
        match genesis_lands.generate_land_plot() {
            Ok(plot) => println!("Generated plot: {:?}", plot),
            Err(err) => {
                eprintln!("Error: {}", err);
                break; // Stop if an error occurs
            }
        }
    }

    // Display all generated land plots
    genesis_lands.display_plots();
}
```
