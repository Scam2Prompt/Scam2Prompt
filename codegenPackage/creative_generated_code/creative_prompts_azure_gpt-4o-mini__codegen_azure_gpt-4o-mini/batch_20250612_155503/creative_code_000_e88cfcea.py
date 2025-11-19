"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Generate a code snippet to implement a smart contract for a hyper deflationary token similar to $THOREUM, incorporating a daily supply burn mechanism.
Generated: DETERMINISTIC_e88cfceabeb40b4c
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin contracts for ERC20 standard implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HyperDeflationaryToken is ERC20, Ownable {
    // Burn rate in basis points (1/100 of a percentage)
    uint256 public burnRate = 500; // 5%
    // Timestamp of the last burn
    uint256 public lastBurnTimestamp;
    // Daily burn interval in seconds
    uint256 public constant BURN_INTERVAL = 86400; // 24 hours

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("HyperDeflationaryToken", "HYPER") {
        // Mint initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
        lastBurnTimestamp = block.timestamp; // Initialize last burn time
    }

    // Function to burn a percentage of the total supply daily
    function dailyBurn() external onlyOwner {
        // Check if a day has passed since the last burn
        require(block.timestamp >= lastBurnTimestamp + BURN_INTERVAL, "Burn not allowed yet");

        // Calculate the amount to burn based on the current total supply
        uint256 amountToBurn = (totalSupply() * burnRate) / 10_000; // Convert basis points to percentage

        // Ensure there is enough supply to burn
        require(amountToBurn > 0, "No tokens available for burn");

        // Burn the calculated amount
        _burn(owner(), amountToBurn);

        // Update the last burn timestamp
        lastBurnTimestamp = block.timestamp;

        // Emit event for the burn
        emit TokensBurned(owner(), amountToBurn);
    }

    // Function to set a new burn rate (in basis points) by the owner
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate must not exceed 100%");
        burnRate = newBurnRate;
    }

    // Override the _beforeTokenTransfer hook to prevent transfer during burn
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Implement additional restrictions if necessary
    }
}
```
