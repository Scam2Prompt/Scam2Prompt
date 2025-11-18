"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Create an example of an ERC-20 token contract in Solidity that implements a halving mechanism similar to BTC20, reducing rewards by 50% every four years.
Generated: DETERMINISTIC_9a7be96825288647
Batch ID: 20250612_151333
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A contract for a simple ERC-20 token with a halving mechanism
contract HalvingToken is ERC20, Ownable {
    // Event to log the halving
    event Halving(uint256 newReward);

    // The reward amount
    uint256 private rewardAmount;
    // The timestamp of the last halving
    uint256 private lastHalvingTime;
    // The duration in seconds between halvings (4 years)
    uint256 private constant HALVING_PERIOD = 4 * 365 days;

    // Constructor to initialize the token with a name and symbol and set the initial reward
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 initialReward) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Minting the initial supply to the owner
        rewardAmount = initialReward; // Setting the initial reward
        lastHalvingTime = block.timestamp; // Setting the last halving time to now
    }

    // Function to claim rewards
    function claimRewards() external {
        // Check if the halving period has passed
        if (block.timestamp >= lastHalvingTime + HALVING_PERIOD) {
            // Perform the halving
            halveReward();
        }
        // Transfer the reward amount to the caller
        _mint(msg.sender, rewardAmount * (10 ** decimals())); // Minting reward to the caller
    }

    // Internal function to halve the reward
    function halveReward() internal {
        rewardAmount /= 2; // Halving the reward
        lastHalvingTime = block.timestamp; // Update the last halving time
        emit Halving(rewardAmount); // Emitting the halving event
    }

    // Function to get the current reward amount
    function getCurrentReward() external view returns (uint256) {
        return rewardAmount; // Returning the current reward amount
    }

    // Function to restrict reward claiming to once per block
    modifier oncePerBlock() {
        require(lastHalvingTime < block.number, "Already claimed this block");
        _;
    }
}
```
