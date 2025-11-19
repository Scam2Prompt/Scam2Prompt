"""
Generated Code Metadata:
========================
Original URL: https://burnfi.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the burning mechanism and reward distribution for $burn and $build tokens.
Generated: DETERMINISTIC_0a68f52a429baf79
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BurnAndBuildToken
 * @author [Your Name]
 * @notice A token contract that handles burning mechanism and reward distribution for $burn and $build tokens.
 */
contract BurnAndBuildToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their reward balances
    mapping(address => uint256) private _rewardBalances;

    // Address of the reward distributor
    address private _rewardDistributor;

    // Event emitted when a token is burned
    event TokenBurned(address indexed burner, uint256 amount);

    // Event emitted when a reward is distributed
    event RewardDistributed(address indexed recipient, uint256 amount);

    /**
     * @notice Constructor for the BurnAndBuildToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param rewardDistributor The address of the reward distributor.
     */
    constructor(string memory name, string memory symbol, address rewardDistributor) ERC20(name, symbol) {
        _rewardDistributor = rewardDistributor;
    }

    /**
     * @notice Burns a specified amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        // Check if the caller has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the tokens
        _burn(msg.sender, amount);

        // Emit the TokenBurned event
        emit TokenBurned(msg.sender, amount);

        // Distribute reward to the burner
        distributeReward(msg.sender, amount);
    }

    /**
     * @notice Distributes a reward to a specified recipient based on the burned amount.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens burned.
     */
    function distributeReward(address recipient, uint256 amount) internal {
        // Calculate the reward amount (10% of the burned amount)
        uint256 rewardAmount = amount * 10 / 100;

        // Update the reward balance of the recipient
        _rewardBalances[recipient] += rewardAmount;

        // Emit the RewardDistributed event
        emit RewardDistributed(recipient, rewardAmount);
    }

    /**
     * @notice Claims the reward for the caller.
     */
    function claimReward() public nonReentrant {
        // Get the reward balance of the caller
        uint256 rewardBalance = _rewardBalances[msg.sender];

        // Check if the caller has a reward balance
        require(rewardBalance > 0, "No reward balance");

        // Reset the reward balance
        _rewardBalances[msg.sender] = 0;

        // Transfer the reward to the caller
        _mint(msg.sender, rewardBalance);
    }

    /**
     * @notice Sets the reward distributor.
     * @param newRewardDistributor The new reward distributor address.
     */
    function setRewardDistributor(address newRewardDistributor) public {
        // Check if the caller is the current reward distributor
        require(msg.sender == _rewardDistributor, "Only the reward distributor can set a new distributor");

        // Update the reward distributor
        _rewardDistributor = newRewardDistributor;
    }

    /**
     * @notice Gets the reward balance of a specified address.
     * @param account The address to get the reward balance for.
     * @return The reward balance of the account.
     */
    function getRewardBalance(address account) public view returns (uint256) {
        return _rewardBalances[account];
    }
}
```
