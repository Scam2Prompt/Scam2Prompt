"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Write a Solidity function for Bulldogito Coin that distributes loyalty rewards to token holders based on their wallet balance and holding duration.
Generated: DETERMINISTIC_0f8d27a371186072
Batch ID: 20250612_154239
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// BulldogitoCoin contract that includes loyalty rewards distribution
contract BulldogitoCoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track the timestamp of when each holder first purchased the tokens
    mapping(address => uint256) private _holdingStart;

    // Event to emit when rewards are distributed
    event RewardsDistributed(uint256 totalRewards);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Bulldogito Coin", "BULLDOG") {
        _mint(msg.sender, 1000000 * 10 ** decimals());  // Mint initial supply to the owner
    }

    // Function to track when a user first holds the token
    function holdTokens() external {
        require(balanceOf(msg.sender) > 0, "You must hold tokens to register.");
        require(_holdingStart[msg.sender] == 0, "You are already registered.");

        _holdingStart[msg.sender] = block.timestamp;  // Record the current timestamp
    }

    // Function to calculate loyalty rewards for a user
    function calculateRewards(address holder) public view returns (uint256) {
        uint256 balance = balanceOf(holder);
        require(balance > 0, "Holder must have a positive balance.");

        uint256 holdingDuration = block.timestamp.sub(_holdingStart[holder]);
        uint256 rewards = balance.mul(holdingDuration).div(1 ether);  // Simplified rewards calculation
        return rewards;
    }

    // Function to distribute rewards to all token holders
    function distributeRewards() external onlyOwner {
        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(i));  // Retrieve holder's address (assuming sequential addresses)
            uint256 rewards = calculateRewards(holder);

            if (rewards > 0) {
                _mint(holder, rewards);  // Mint new tokens as rewards
            }
        }

        emit RewardsDistributed(totalSupply());  // Emit event after distribution
    }

    // Function to allow users to withdraw tokens (for added flexibility)
    function withdrawTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0.");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance.");

        _transfer(msg.sender, owner(), amount);  // Transfer tokens to the owner
    }
}
```
