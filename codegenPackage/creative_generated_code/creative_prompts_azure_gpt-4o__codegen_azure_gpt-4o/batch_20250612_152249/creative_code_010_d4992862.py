"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Write a Rust program to calculate effective leverage for a portfolio containing both futures and options positions on CVEX, using delta offsets for margin reduction.
Generated: DETERMINISTIC_d49928629f007b26
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use std::collections::HashMap;

/// Represents a position in the portfolio
#[derive(Debug)]
struct Position {
    instrument: String,        // Name of the instrument
    notional: f64,             // Notional value of the position (in USD)
    delta: f64,                // Delta of the position (0.0 - 1.0 for options)
    margin_requirement: f64,   // Margin requirement percentage (as a fraction, e.g., 0.1 for 10%)
}

/// Represents the portfolio containing various positions
#[derive(Debug)]
struct Portfolio {
    positions: Vec<Position>, // List of positions
}

impl Portfolio {
    /// Calculates the total margin requirement for the portfolio, accounting for delta offsets
    fn calculate_total_margin(&self) -> f64 {
        let mut total_margin = 0.0;
        let mut delta_offset = 0.0;

        for pos in &self.positions {
            // Calculate the raw margin for the position
            let position_margin = pos.notional * pos.margin_requirement;

            // Apply delta offset for options
            if pos.delta > 0.0 && pos.delta < 1.0 {
                delta_offset += pos.delta * pos.notional;
            }

            total_margin += position_margin;
        }

        // Adjust the total margin using the delta offset (CVEX rules for margin reduction)
        total_margin -= delta_offset;
        if total_margin < 0.0 {
            total_margin = 0.0; // Ensure margin is never negative
        }

        total_margin
    }

    /// Calculates the effective leverage of the portfolio
    fn calculate_effective_leverage(&self) -> f64 {
        let total_notional: f64 = self.positions.iter().map(|pos| pos.notional).sum();
        let total_margin = self.calculate_total_margin();

        if total_margin == 0.0 {
            return 0.0; // Avoid division by zero, leverage is zero if no margin
        }

        total_notional / total_margin
    }
}

fn main() {
    // Example positions in the portfolio
    let positions = vec![
        Position {
            instrument: "Futures 1".to_string(),
            notional: 100_000.0,
            delta: 1.0, // Futures have delta of 1
            margin_requirement: 0.1, // 10% margin requirement
        },
        Position {
            instrument: "Option 1".to_string(),
            notional: 50_000.0,
            delta: 0.5, // Option delta
            margin_requirement: 0.2, // 20% margin requirement
        },
        Position {
            instrument: "Option 2".to_string(),
            notional: 30_000.0,
            delta: 0.7, // Option delta
            margin_requirement: 0.15, // 15% margin requirement
        },
    ];

    let portfolio = Portfolio { positions };

    // Calculate effective leverage
    let effective_leverage = portfolio.calculate_effective_leverage();

    println!("Effective Leverage: {:.2}", effective_leverage);
}
```
