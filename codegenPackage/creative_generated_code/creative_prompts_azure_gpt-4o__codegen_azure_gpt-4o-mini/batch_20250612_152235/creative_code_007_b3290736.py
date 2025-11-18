"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokita-dashboard.pages.dev
Prompt: Write a Solidity smart contract that implements staking functionality for Flokita tokens, ensuring compatibility with both Binance Smart Chain (BSC) and Solana (SOL), as mentioned on the Flokita website.
Generated: DETERMINISTIC_b3290736329e40ff
Batch ID: 20250612_152235
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

// Import OpenZeppelin contracts for ERC20 token and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FlokitaStaking
 * @dev A smart contract for staking Flokita tokens on the Ethereum compatible chains.
 */
contract FlokitaStaking is Ownable {
    // The Flokita token interface
    IERC20 public flokitaToken;

    // Struct to track user stakes
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging stake and unstake actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _flokitaToken) {
        flokitaToken = _flokitaToken;
    }

    /**
     * @dev Stakes a specified amount of Flokita tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(
            flokitaToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed."
        );

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes the entire amount of Flokita tokens staked by the user.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked.");

        // Transfer the staked tokens back to the user
        require(
            flokitaToken.transfer(msg.sender, userStake.amount),
            "Token transfer failed."
        );

        // Reset the user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Returns the total amount of tokens staked by a user.
     * @param user The address of the user.
     * @return The amount of tokens staked.
     */
    function getStakeAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
