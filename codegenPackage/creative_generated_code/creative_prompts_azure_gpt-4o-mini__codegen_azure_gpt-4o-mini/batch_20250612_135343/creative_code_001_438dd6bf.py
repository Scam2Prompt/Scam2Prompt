"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel-dapp-template-nextjs.vercel.app
Prompt: Explain how to use the Sway programming language for developing smart contracts on the FuelVM, referencing the Fuel Book.
Generated: DETERMINISTIC_438dd6bfcc558646
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sway
// This is a simple smart contract written in Sway for the FuelVM.
// It demonstrates basic functionalities including state management
// and function calls. For more details, please refer to the Fuel Book.

contract SimpleStorage {

    // State variable to store the value
    let mut stored_value: u32;

    // Constructor to initialize the contract with a default value
    public fun new(initial_value: u32) {
        // Validate that the initial value is non-negative
        assert(initial_value >= 0, "Initial value must be non-negative");
        stored_value = initial_value;  // Set the initial stored value
    }

    // Function to store a new value
    public fun set_value(new_value: u32) {
        // Validate that the new value is non-negative
        assert(new_value >= 0, "New value must be non-negative");
        stored_value = new_value;  // Update the stored value
    }

    // Function to retrieve the stored value
    public fun get_value() -> u32 {
        return stored_value;  // Return the current stored value
    }

    // Function to reset the stored value to zero
    public fun reset() {
        stored_value = 0;  // Reset the stored value to zero
    }
}

// Error handling is inherent with assertions. 
// If an assertion fails, it will revert the transaction,
// ensuring that only valid states are maintained.
```
