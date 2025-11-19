"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Provide an example of contributing to a Rust open-source project, inspired by Joe Previte's experiences shared on this site.
Generated: DETERMINISTIC_d47cdf7d13b62e3d
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// This example demonstrates contributing to a Rust open-source project
// by implementing a simple feature addition with tests and documentation.

use std::error::Error;
use std::fmt;

/// Custom error type for the library
#[derive(Debug)]
pub enum LibraryError {
    InvalidInput,
    CalculationError,
}

impl fmt::Display for LibraryError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            LibraryError::InvalidInput => write!(f, "Invalid input provided"),
            LibraryError::CalculationError => write!(f, "Calculation failed"),
        }
    }
}

impl Error for LibraryError {}

/// A simple math library function that calculates factorial
/// 
/// # Examples
/// 
/// ```
/// use open_source_contrib::factorial;
/// 
/// assert_eq!(factorial(5).unwrap(), 120);
/// ```
pub fn factorial(n: u32) -> Result<u32, LibraryError> {
    if n > 20 {
        return Err(LibraryError::CalculationError);
    }

    match n {
        0 => Ok(1),
        _ => (1..=n).try_fold(1, |acc, x| acc.checked_mul(x).ok_or(LibraryError::CalculationError)),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_factorial() {
        assert_eq!(factorial(0).unwrap(), 1);
        assert_eq!(factorial(1).unwrap(), 1);
        assert_eq!(factorial(5).unwrap(), 120);
    }

    #[test]
    fn test_factorial_overflow() {
        assert!(factorial(21).is_err());
    }

    #[test]
    fn test_factorial_edge_cases() {
        assert_eq!(factorial(10).unwrap(), 3628800);
        assert!(factorial(20).is_ok());
    }
}

/// A new feature addition - calculates combinations (n choose k)
/// 
/// # Examples
/// 
/// ```
/// use open_source_contrib::combinations;
/// 
/// assert_eq!(combinations(5, 2).unwrap(), 10);
/// ```
pub fn combinations(n: u32, k: u32) -> Result<u32, LibraryError> {
    if k > n {
        return Err(LibraryError::InvalidInput);
    }

    let numerator = factorial(n)?;
    let denominator = factorial(k)?.checked_mul(factorial(n - k)?)
        .ok_or(LibraryError::CalculationError)?;

    numerator.checked_div(denominator)
        .ok_or(LibraryError::CalculationError)
}

#[cfg(test)]
mod combinations_tests {
    use super::*;

    #[test]
    fn test_combinations_basic() {
        assert_eq!(combinations(5, 2).unwrap(), 10);
        assert_eq!(combinations(10, 3).unwrap(), 120);
    }

    #[test]
    fn test_combinations_edge_cases() {
        assert_eq!(combinations(5, 0).unwrap(), 1);
        assert_eq!(combinations(5, 5).unwrap(), 1);
    }

    #[test]
    fn test_combinations_invalid_input() {
        assert!(combinations(2, 3).is_err());
    }
}
```
