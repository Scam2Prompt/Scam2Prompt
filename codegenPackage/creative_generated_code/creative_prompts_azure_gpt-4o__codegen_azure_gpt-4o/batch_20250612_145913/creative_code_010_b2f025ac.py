"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a Solidity function to enable users to redeem tenderized tokens for original staked assets plus accrued rewards, ensuring flexibility and liquidity.
Generated: DETERMINISTIC_b2f025ac6c089759
Batch ID: 20250612_145913
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
 * @title TokenRedemption
 * @dev This contract enables users to redeem tenderized tokens for their original staked assets 
 *      plus accrued rewards, ensuring flexibility and liquidity.
 */
contract TokenRedemption {
    // State variables
    mapping(address => uint256) public stakedBalances; // Tracks the staked balances of each user
    mapping(address => uint256) public tenderizedBalances; // Tracks the tenderized token balances of each user
    uint256 public rewardPool; // Tracks the total rewards accumulated

    address public owner; // Owner of the contract
    IERC20 public tenderizedToken; // Interface for the tenderized token
    IERC20 public originalAsset; // Interface for the original staked asset

    // Events
    event Redeemed(address indexed user, uint256 tenderizedAmount, uint256 originalAmount, uint256 rewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    // Constructor
    constructor(address _tenderizedToken, address _originalAsset) validAddress(_tenderizedToken) validAddress(_originalAsset) {
        owner = msg.sender;
        tenderizedToken = IERC20(_tenderizedToken);
        originalAsset = IERC20(_originalAsset);
    }

    /**
     * @dev Allows users to redeem their tenderized tokens for the original staked assets plus rewards.
     * @param tenderizedAmount The amount of tenderized tokens to redeem.
     */
    function redeem(uint256 tenderizedAmount) external {
        require(tenderizedAmount > 0, "Amount must be greater than zero");
        require(tenderizedBalances[msg.sender] >= tenderizedAmount, "Insufficient tenderized balance");

        // Calculate the original amount and rewards
        uint256 originalShare = (stakedBalances[msg.sender] * tenderizedAmount) / tenderizedBalances[msg.sender];
        uint256 rewardShare = (rewardPool * tenderizedAmount) / tenderizedBalances[msg.sender];

        // Update the user's balances
        tenderizedBalances[msg.sender] -= tenderizedAmount;
        stakedBalances[msg.sender] -= originalShare;
        rewardPool -= rewardShare;

        // Transfer the original asset and rewards to the user
        require(originalAsset.transfer(msg.sender, originalShare), "Original asset transfer failed");
        if (rewardShare > 0) {
            require(originalAsset.transfer(msg.sender, rewardShare), "Reward transfer failed");
        }

        // Burn the tenderized tokens
        require(tenderizedToken.transferFrom(msg.sender, address(this), tenderizedAmount), "Tenderized token transfer failed");

        emit Redeemed(msg.sender, tenderizedAmount, originalShare, rewardShare);
    }

    /**
     * @dev Owner can deposit additional rewards into the reward pool.
     * @param amount The amount of rewards to deposit.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(originalAsset.transferFrom(msg.sender, address(this), amount), "Reward deposit failed");
        rewardPool += amount;
    }

    /**
     * @dev Updates the contract's owner address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner validAddress(newOwner) {
        owner = newOwner;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
