"""
Generated Code Metadata:
========================
Original URL: https://cvex.pages.dev
Prompt: Write a Rust program to calculate effective leverage for a portfolio containing both futures and options positions on CVEX, using delta offsets for margin reduction.
Generated: DETERMINISTIC_d49928629f007b26
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
/// Calculates effective leverage for a portfolio containing both futures and options positions on CVEX,
/// using delta offsets for margin reduction.

use std::error::Error;

// Define a struct to represent a position in the portfolio
#[derive(Debug)]
struct Position {
    instrument: String,
    quantity: f64,
    delta: f64,
}

// Define a struct to represent the portfolio
#[derive(Debug)]
struct Portfolio {
    positions: Vec<Position>,
    cvex_price: f64,
    margin_requirement: f64,
}

impl Portfolio {
    /// Creates a new portfolio with the given positions, CVEX price, and margin requirement.
    fn new(positions: Vec<Position>, cvex_price: f64, margin_requirement: f64) -> Self {
        Portfolio {
            positions,
            cvex_price,
            margin_requirement,
        }
    }

    /// Calculates the total delta of the portfolio.
    fn total_delta(&self) -> f64 {
        self.positions.iter().map(|p| p.quantity * p.delta).sum()
    }

    /// Calculates the total margin required for the portfolio, taking into account delta offsets.
    fn total_margin(&self) -> f64 {
        let total_delta = self.total_delta();
        let mut margin = 0.0;

        for position in &self.positions {
            let position_margin = position.quantity * self.cvex_price * self.margin_requirement;
            let delta_offset = position.delta * total_delta * 0.5; // 50% delta offset
            margin += position_margin - delta_offset;
        }

        // Ensure margin is not negative
        margin.max(0.0)
    }

    /// Calculates the effective leverage of the portfolio.
    fn effective_leverage(&self) -> f64 {
        let portfolio_value = self.positions.iter().map(|p| p.quantity * self.cvex_price).sum();
        let total_margin = self.total_margin();

        if total_margin == 0.0 {
            0.0
        } else {
            portfolio_value / total_margin
        }
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    // Define positions in the portfolio
    let positions = vec![
        Position {
            instrument: "CVEX Futures".to_string(),
            quantity: 10.0,
            delta: 1.0,
        },
        Position {
            instrument: "CVEX Call Option".to_string(),
            quantity: 5.0,
            delta: 0.5,
        },
        Position {
            instrument: "CVEX Put Option".to_string(),
            quantity: -3.0,
            delta: -0.2,
        },
    ];

    // Define portfolio parameters
    let cvex_price = 100.0;
    let margin_requirement = 0.1;

    // Create a new portfolio
    let portfolio = Portfolio::new(positions, cvex_price, margin_requirement);

    // Calculate and print effective leverage
    let effective_leverage = portfolio.effective_leverage();
    println!("Effective Leverage: {}", effective_leverage);

    Ok(())
}
```
