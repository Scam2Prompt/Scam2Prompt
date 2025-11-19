"""
Generated Code Metadata:
========================
Original URL: https://ff-info-online.com
Prompt: Develop a sample application in Rust that uses FixedFloat for handling exchange rates, detailing the storage efficiency and precision advantages it offers.
Generated: DETERMINISTIC_9530027cfe0c1820
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A sample Rust application demonstrating FixedFloat for exchange rate handling.
//! Showcases storage efficiency and precision advantages over floating-point types.

use fixed::types::I32F32; // 32-bit fixed-point number with 32 fractional bits
use std::error::Error;
use std::fmt;

/// Custom error type for exchange rate operations
#[derive(Debug)]
pub enum ExchangeRateError {
    InvalidRate,
    ConversionOverflow,
}

impl fmt::Display for ExchangeRateError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            ExchangeRateError::InvalidRate => write!(f, "Invalid exchange rate provided"),
            ExchangeRateError::ConversionOverflow => write!(f, "Conversion would overflow"),
        }
    }
}

impl Error for ExchangeRateError {}

/// Exchange rate handler using fixed-point arithmetic
pub struct ExchangeRateHandler {
    rate: I32F32,
}

impl ExchangeRateHandler {
    /// Creates a new ExchangeRateHandler with the given rate
    /// # Arguments
    /// * `rate` - Exchange rate as a string (e.g., "1.2345")
    pub fn new(rate: &str) -> Result<Self, ExchangeRateError> {
        let parsed_rate = rate.parse::<f64>()
            .map_err(|_| ExchangeRateError::InvalidRate)?;
        
        if parsed_rate <= 0.0 {
            return Err(ExchangeRateError::InvalidRate);
        }

        Ok(ExchangeRateHandler {
            rate: I32F32::from_num(parsed_rate),
        })
    }

    /// Converts an amount from one currency to another
    /// # Arguments
    /// * `amount` - Amount to convert (in source currency)
    pub fn convert(&self, amount: f64) -> Result<f64, ExchangeRateError> {
        let fixed_amount = I32F32::from_num(amount);
        let result = fixed_amount * self.rate;
        
        result.to_num::<f64>()
            .ok_or(ExchangeRateError::ConversionOverflow)
    }

    /// Gets the current exchange rate with full precision
    pub fn get_rate(&self) -> String {
        format!("{:.8}", self.rate.to_num::<f64>())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use approx::assert_relative_eq;

    #[test]
    fn test_valid_conversion() {
        let handler = ExchangeRateHandler::new("1.23456789").unwrap();
        let converted = handler.convert(100.0).unwrap();
        assert_relative_eq!(converted, 123.456789, max_relative = 1e-8);
    }

    #[test]
    fn test_precision_preservation() {
        let handler = ExchangeRateHandler::new("1.00000001").unwrap();
        let converted = handler.convert(1_000_000.0).unwrap();
        assert_relative_eq!(converted, 1_000_000.01, max_relative = 1e-8);
    }

    #[test]
    fn test_invalid_rate() {
        assert!(ExchangeRateHandler::new("0.0").is_err());
        assert!(ExchangeRateHandler::new("-1.0").is_err());
        assert!(ExchangeRateHandler::new("invalid").is_err());
    }

    #[test]
    fn test_overflow_handling() {
        let handler = ExchangeRateHandler::new("2.0").unwrap();
        assert!(handler.convert(f64::MAX).is_err());
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    // Example usage
    let rate = "1.23456789";
    let amount = 100.0;
    
    let handler = ExchangeRateHandler::new(rate)?;
    let converted = handler.convert(amount)?;
    
    println!("Exchange rate: {}", handler.get_rate());
    println!("Converted {} {} to {:.8} {}", 
        amount, "USD", converted, "EUR");
    
    Ok(())
}
```
