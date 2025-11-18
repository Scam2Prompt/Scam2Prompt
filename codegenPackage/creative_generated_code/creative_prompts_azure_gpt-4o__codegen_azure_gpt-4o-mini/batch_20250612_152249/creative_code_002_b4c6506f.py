"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cvex.pages.dev
Prompt: Using the CVEX documentation, write a function in Rust to calculate margin requirements for a cross-margin portfolio with correlated futures and options positions.
Generated: DETERMINISTIC_b4c6506fd8bb5c9f
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

/// Represents a position in the portfolio.
#[derive(Debug)]
struct Position {
    /// The notional value of the position.
    notional: f64,
    /// The correlation coefficient with another position.
    correlation: f64,
}

/// Calculates the margin requirements for a cross-margin portfolio.
/// 
/// # Arguments
/// 
/// * `positions` - A vector of positions in the portfolio.
/// 
/// # Returns
/// 
/// * The total margin requirement for the portfolio.
/// 
/// # Errors
///
/// Returns an error if any position's notional value is negative or 
/// if the correlation coefficient is outside the range [-1, 1].
fn calculate_margin(positions: &[Position]) -> Result<f64, Box<dyn Error>> {
    let mut total_margin: f64 = 0.0;

    for position in positions {
        if position.notional < 0.0 {
            return Err("Notional value cannot be negative".into());
        }
        if position.correlation < -1.0 || position.correlation > 1.0 {
            return Err("Correlation coefficient must be between -1 and 1".into());
        }
        
        // Calculate margin for each position using a simple approach
        // Placeholder margin calculation: notional * correlation
        let margin = position.notional * (1.0 - position.correlation);
        total_margin += margin;
    }
    
    Ok(total_margin)
}

fn main() -> Result<(), Box<dyn Error>> {
    // Example usage of calculate_margin function
    let positions = vec![
        Position {
            notional: 100_000.0,
            correlation: 0.5,
        },
        Position {
            notional: 150_000.0,
            correlation: 0.3,
        },
        Position {
            notional: 200_000.0,
            correlation: -0.2,
        },
    ];

    match calculate_margin(&positions) {
        Ok(margin) => println!("Total margin requirement: ${:.2}", margin),
        Err(e) => eprintln!("Error calculating margin: {}", e),
    }

    Ok(())
}
```
