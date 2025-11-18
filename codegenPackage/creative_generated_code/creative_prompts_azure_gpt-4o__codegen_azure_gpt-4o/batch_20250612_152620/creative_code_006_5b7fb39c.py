"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Implement a function in Rust to calculate the dynamic rewards rate for $SCOTTY tokens based on the provided staking parameters and ETH block data.
Generated: DETERMINISTIC_5b7fb39c6fa32beb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use std::error::Error;

/// Represents staking parameters for SCOTTY tokens.
#[derive(Debug)]
struct StakingParams {
    base_rate: f64,         // Base rewards rate (e.g., 0.05 -> 5%)
    multiplier: f64,        // Multiplier for rewards rate based on staking tier
    max_rate: f64,          // Maximum rewards rate cap
    min_rate: f64,          // Minimum rewards rate cap
}

/// Represents Ethereum block data relevant to reward calculations.
#[derive(Debug)]
struct EthBlockData {
    block_time: u64,        // Time in seconds since the last block
    network_utilization: f64, // Network utilization percentage (0.0 to 1.0)
}

/// Calculates the dynamic rewards rate for SCOTTY tokens.
///
/// # Arguments
/// * `staking_params` - Staking parameters for SCOTTY tokens.
/// * `eth_block_data` - Ethereum block data relevant to reward calculations.
///
/// # Returns
/// * `Result<f64, Box<dyn Error>>` - The calculated rewards rate or an error if the input is invalid.
///
/// # Example
/// ```
/// let staking_params = StakingParams {
///     base_rate: 0.05,
///     multiplier: 1.2,
///     max_rate: 0.15,
///     min_rate: 0.01,
/// };
/// let eth_block_data = EthBlockData {
///     block_time: 12,
///     network_utilization: 0.8,
/// };
/// let rewards_rate = calculate_rewards_rate(&staking_params, &eth_block_data)?;
/// println!("Rewards rate: {}", rewards_rate);
/// ```
fn calculate_rewards_rate(
    staking_params: &StakingParams,
    eth_block_data: &EthBlockData,
) -> Result<f64, Box<dyn Error>> {
    // Validate input parameters
    if staking_params.base_rate <= 0.0 || staking_params.multiplier <= 0.0 {
        return Err("Invalid staking parameters: base_rate and multiplier must be positive.".into());
    }
    if staking_params.max_rate <= staking_params.min_rate {
        return Err("Invalid staking parameters: max_rate must be greater than min_rate.".into());
    }
    if eth_block_data.network_utilization < 0.0 || eth_block_data.network_utilization > 1.0 {
        return Err("Invalid Ethereum block data: network_utilization must be between 0.0 and 1.0.".into());
    }

    // Dynamic adjustment based on block time (e.g., faster blocks increase rewards slightly)
    let time_adjustment = 1.0 + (eth_block_data.block_time as f64 / 100.0);

    // Dynamic adjustment based on network utilization
    let utilization_adjustment = 1.0 + eth_block_data.network_utilization;

    // Calculate the raw rewards rate
    let raw_rate = staking_params.base_rate * staking_params.multiplier 
                   * time_adjustment * utilization_adjustment;

    // Clamp the rewards rate within min_rate and max_rate
    let clamped_rate = raw_rate.clamp(staking_params.min_rate, staking_params.max_rate);

    // Return the calculated rewards rate
    Ok(clamped_rate)
}

fn main() {
    // Example usage
    let staking_params = StakingParams {
        base_rate: 0.05,
        multiplier: 1.2,
        max_rate: 0.15,
        min_rate: 0.01,
    };
    let eth_block_data = EthBlockData {
        block_time: 12,
        network_utilization: 0.8,
    };

    match calculate_rewards_rate(&staking_params, &eth_block_data) {
        Ok(rewards_rate) => println!("Calculated rewards rate: {:.4}", rewards_rate),
        Err(e) => eprintln!("Error calculating rewards rate: {}", e),
    }
}
```
