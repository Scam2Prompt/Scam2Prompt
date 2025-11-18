"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ttrumpwallet.com
Prompt: Generate a smart contract in Solidity that distributes rewards in a custom token, such as "$TRUMP," to referrers based on successful referrals.
Generated: DETERMINISTIC_e10e38aa1e4e2e51
Batch ID: 20250612_145114
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

/**
 * @title ReferralRewardDistributor
 * @dev This smart contract distributes rewards in a custom token ($TRUMP) to referrers for successful referrals.
 */
contract ReferralRewardDistributor {
    // Address of the custom token ($TRUMP) contract
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Mapping to track referrer balances
    mapping(address => uint256) public referrerBalances;

    /**
     * @dev Emitted when rewards are distributed to a referrer.
     * @param referrer Address of the referrer receiving the reward.
     * @param amount Amount of reward tokens distributed.
     */
    event RewardDistributed(address indexed referrer, uint256 amount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the $TRUMP token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Distribute rewards to a referrer.
     * @param referrer Address of the referrer to receive the reward.
     * @param amount Amount of reward tokens to distribute.
     */
    function distributeReward(address referrer, uint256 amount) external onlyOwner {
        require(referrer != address(0), "Referrer address cannot be zero");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update referrer balance
        referrerBalances[referrer] += amount;

        // Transfer $TRUMP tokens to the referrer
        require(token.transfer(referrer, amount), "Token transfer failed");

        // Emit event for reward distribution
        emit RewardDistributed(referrer, amount);
    }

    /**
     * @dev Withdraw tokens from the contract (only owner).
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        require(token.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Change ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
