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
use std::error::Error;

/// Struct to represent a position in the portfolio
#[derive(Debug)]
struct Position {
    asset: String,
    quantity: f64,
    delta: f64,
}

impl Position {
    /// Create a new position with the specified asset, quantity, and delta
    fn new(asset: &str, quantity: f64, delta: f64) -> Self {
        Position {
            asset: asset.to_string(),
            quantity,
            delta,
        }
    }
}

/// Calculates the effective leverage for the portfolio
/// 
/// # Arguments
/// 
/// * `positions` - A vector of positions in the portfolio
/// * `total_margin` - The total margin available
///
/// # Returns
///
/// The effective leverage as a f64 value
fn calculate_effective_leverage(positions: &[Position], total_margin: f64) -> Result<f64, Box<dyn Error>> {
    if total_margin <= 0.0 {
        return Err("Total margin must be greater than zero".into());
    }

    let mut total_delta = 0.0;
    let mut total_value = 0.0;

    // Calculate total delta and total portfolio value
    for position in positions {
        total_delta += position.delta * position.quantity;
        total_value += position.quantity; // Assuming quantity represents monetary value for simplification
    }

    // Effective leverage calculation
    if total_value == 0.0 {
        return Err("Total portfolio value cannot be zero".into());
    }

    let effective_leverage = (total_value - total_delta).abs() / total_margin;

    Ok(effective_leverage)
}

fn main() -> Result<(), Box<dyn Error>> {
    // Example positions in the portfolio
    let positions = vec![
        Position::new("Futures_A", 10.0, 0.5),
        Position::new("Options_B", 5.0, 0.3),
    ];

    // Total margin available for the portfolio
    let total_margin = 20000.0;

    // Calculate the effective leverage
    match calculate_effective_leverage(&positions, total_margin) {
        Ok(leverage) => println!("Effective Leverage: {:.2}", leverage),
        Err(e) => eprintln!("Error calculating leverage: {}", e),
    }

    Ok(())
}
```
