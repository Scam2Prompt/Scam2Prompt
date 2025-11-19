"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate a smart contract for a decentralized betting platform that allows users to stake $BCB tokens and receive rewards in stable coins.
Generated: DETERMINISTIC_b7a11231a0d2b817
Batch ID: 20250612_163616
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

/**
 * @title Decentralized Betting Platform
 * @dev This smart contract allows users to stake $BCB tokens and receive rewards in stable coins.
 */
contract BettingPlatform {
    // ERC20 interface for interacting with $BCB token and stable coin
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Address of the $BCB token contract
    IERC20 public bcbToken;

    // Address of the stable coin contract
    IERC20 public stableCoin;

    // Owner of the contract
    address public owner;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _bcbToken Address of the $BCB token contract.
     * @param _stableCoin Address of the stable coin contract.
     */
    constructor(IERC20 _bcbToken, IERC20 _stableCoin) {
        bcbToken = _bcbToken;
        stableCoin = _stableCoin;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $BCB tokens.
     * @param amount Amount of $BCB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer $BCB tokens from the user to the contract
        require(bcbToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake balance
        stakes[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Distributes rewards to a user in stable coins.
     * @param user Address of the user to distribute rewards to.
     * @param reward Amount of stable coins to distribute as reward.
     */
    function distributeReward(address user, uint256 reward) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(reward > 0, "Reward amount must be greater than zero");
        require(stakes[user] > 0, "User has no stakes");

        // Transfer stable coins to the user
        require(stableCoin.transfer(user, reward), "Reward transfer failed");

        emit RewardDistributed(user, reward);
    }

    /**
     * @dev Allows the owner to withdraw $BCB tokens from the contract.
     * @param amount Amount of $BCB tokens to withdraw.
     */
    function withdrawBCB(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(bcbToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer $BCB tokens to the owner
        require(bcbToken.transfer(owner, amount), "Withdraw transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw stable coins from the contract.
     * @param amount Amount of stable coins to withdraw.
     */
    function withdrawStableCoin(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(stableCoin.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer stable coins to the owner
        require(stableCoin.transfer(owner, amount), "Withdraw transfer failed");
    }
}
```
