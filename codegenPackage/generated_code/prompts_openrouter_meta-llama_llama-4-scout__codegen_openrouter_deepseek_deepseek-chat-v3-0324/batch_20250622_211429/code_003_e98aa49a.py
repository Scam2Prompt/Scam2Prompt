"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Provide an example of contributing to a Rust open-source project.
Generated: DETERMINISTIC_e98aa49a6f3de493
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Example of contributing to a Rust open-source project
//! This demonstrates a simple contribution by adding a utility function to a hypothetical `math-utils` crate.

use std::error::Error;
use std::fmt;

/// Custom error type for mathematical operations
#[derive(Debug)]
pub enum MathError {
    DivisionByZero,
    NegativeLogarithm,
    InvalidInput(String),
}

impl fmt::Display for MathError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            MathError::DivisionByZero => write!(f, "Division by zero error"),
            MathError::NegativeLogarithm => write!(f, "Logarithm of negative number"),
            MathError::InvalidInput(msg) => write!(f, "Invalid input: {}", msg),
        }
    }
}

impl Error for MathError {}

/// Calculates the harmonic mean of two numbers
///
/// # Arguments
/// * `a` - First number
/// * `b` - Second number
///
/// # Returns
/// Result with harmonic mean or MathError
///
/// # Examples
/// ```
/// use math_utils::harmonic_mean;
/// 
/// let result = harmonic_mean(2.0, 4.0).unwrap();
/// assert_eq!(result, 2.6666666666666665);
/// ```
pub fn harmonic_mean(a: f64, b: f64) -> Result<f64, MathError> {
    if a == 0.0 || b == 0.0 {
        return Err(MathError::DivisionByZero);
    }

    if a.is_nan() || b.is_nan() {
        return Err(MathError::InvalidInput("NaN input".to_string()));
    }

    if a.is_infinite() || b.is_infinite() {
        return Err(MathError::InvalidInput("Infinite input".to_string()));
    }

    Ok(2.0 * a * b / (a + b))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_harmonic_mean_valid() {
        assert_eq!(harmonic_mean(2.0, 4.0).unwrap(), 2.6666666666666665);
        assert_eq!(harmonic_mean(1.0, 1.0).unwrap(), 1.0);
    }

    #[test]
    fn test_harmonic_mean_zero() {
        assert!(harmonic_mean(0.0, 4.0).is_err());
        assert!(harmonic_mean(2.0, 0.0).is_err());
    }

    #[test]
    fn test_harmonic_mean_invalid() {
        assert!(harmonic_mean(f64::NAN, 1.0).is_err());
        assert!(harmonic_mean(1.0, f64::INFINITY).is_err());
    }
}
```
