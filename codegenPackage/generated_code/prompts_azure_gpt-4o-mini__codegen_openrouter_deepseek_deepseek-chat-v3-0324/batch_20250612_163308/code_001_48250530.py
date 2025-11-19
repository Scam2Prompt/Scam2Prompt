"""
Generated Code Metadata:
========================
Original URL: https://0xeigenlabs.github.io
Prompt: What are the steps to integrate the Eigen Prover into my existing project for zkVM functionality?
Generated: DETERMINISTIC_482505303f60a765
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready integration example for Eigen Prover in a Rust project:

```rust
//! Eigen Prover Integration for zkVM Functionality
//! 
//! This module provides integration with Eigen Prover for zero-knowledge proof
//! generation and verification in zkVM environments.

use eigen_prover_sdk::{Prover, Verifier, Proof, CircuitInput};
use thiserror::Error;
use log::{info, error};

/// Custom error type for Eigen Prover operations
#[derive(Error, Debug)]
pub enum EigenProverError {
    #[error("Initialization failed: {0}")]
    InitializationError(String),
    
    #[error("Proof generation failed: {0}")]
    ProofGenerationError(String),
    
    #[error("Verification failed: {0}")]
    VerificationError(String),
    
    #[error("Invalid input: {0}")]
    InvalidInput(String),
}

/// Configuration for Eigen Prover
#[derive(Debug, Clone)]
pub struct EigenProverConfig {
    pub prover_key_path: String,
    pub verifier_key_path: String,
    pub circuit_path: String,
}

/// Wrapper for Eigen Prover functionality
pub struct EigenProverIntegration {
    prover: Prover,
    verifier: Verifier,
}

impl EigenProverIntegration {
    /// Initialize the Eigen Prover with configuration
    pub fn new(config: EigenProverConfig) -> Result<Self, EigenProverError> {
        let prover = Prover::load(&config.prover_key_path, &config.circuit_path)
            .map_err(|e| EigenProverError::InitializationError(e.to_string()))?;
            
        let verifier = Verifier::load(&config.verifier_key_path)
            .map_err(|e| EigenProverError::InitializationError(e.to_string()))?;
            
        Ok(Self { prover, verifier })
    }
    
    /// Generate a proof for given circuit inputs
    pub fn generate_proof(&self, inputs: CircuitInput) -> Result<Proof, EigenProverError> {
        info!("Generating proof for inputs");
        
        self.validate_inputs(&inputs)?;
        
        let proof = self.prover.generate_proof(inputs)
            .map_err(|e| EigenProverError::ProofGenerationError(e.to_string()))?;
            
        info!("Proof generated successfully");
        Ok(proof)
    }
    
    /// Verify a proof with the given public inputs
    pub fn verify_proof(&self, proof: &Proof) -> Result<bool, EigenProverError> {
        info!("Verifying proof");
        
        let is_valid = self.verifier.verify(proof)
            .map_err(|e| EigenProverError::VerificationError(e.to_string()))?;
            
        if is_valid {
            info!("Proof verified successfully");
        } else {
            error!("Proof verification failed");
        }
        
        Ok(is_valid)
    }
    
    /// Validate circuit inputs before proof generation
    fn validate_inputs(&self, inputs: &CircuitInput) -> Result<(), EigenProverError> {
        // Add your input validation logic here
        // Example:
        if inputs.values.is_empty() {
            return Err(EigenProverError::InvalidInput("Empty input values".to_string()));
        }
        
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    fn test_config() -> EigenProverConfig {
        EigenProverConfig {
            prover_key_path: "path/to/prover_key".to_string(),
            verifier_key_path: "path/to/verifier_key".to_string(),
            circuit_path: "path/to/circuit".to_string(),
        }
    }
    
    #[test]
    fn test_initialization() {
        let config = test_config();
        let prover = EigenProverIntegration::new(config);
        assert!(prover.is_ok());
    }
    
    #[test]
    fn test_invalid_input() {
        let config = test_config();
        let prover = EigenProverIntegration::new(config).unwrap();
        let inputs = CircuitInput { values: vec![] };
        let result = prover.generate_proof(inputs);
        assert!(matches!(result, Err(EigenProverError::InvalidInput(_))));
    }
}
```

Add this to your Cargo.toml dependencies:
```toml
[dependencies]
eigen-prover-sdk = { version = "0.1", features = ["zkvm"] }
thiserror = "1.0"
log = "0.4"
```

Note: The actual implementation may vary based on:
1. Your specific Eigen Prover SDK version
2. Your circuit structure
3. Your project's existing architecture

The code assumes you have the Eigen Prover SDK properly installed and configured in your environment.
