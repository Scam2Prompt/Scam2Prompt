"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Create a smart contract on Injective that supports structured DeFi products like liquid staking derivatives and real-world asset tokenization, as described in the Black Panther project.
Generated: DETERMINISTIC_de0a6fc6be9f373e
Batch ID: 20250612_150018
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
 * @title BlackPantherDeFiProduct
 * @dev Smart contract for supporting structured DeFi products such as liquid staking derivatives
 *      and real-world asset tokenization on Injective.
 */
contract BlackPantherDeFiProduct {
    // State variables
    address public admin; // Admin address for contract management
    uint256 public totalAssetsTokenized; // Tracks the total amount of tokenized real-world assets
    
    mapping(address => uint256) public stakedBalances; // Staking balances
    mapping(address => uint256) public realWorldTokenizedAssets; // Tokenized asset balances

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event AssetTokenized(address indexed user, string assetDetails, uint256 value);
    event TokenizedAssetWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes contract with admin as the deployer.
     */
    constructor() {
        admin = msg.sender;
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    /**
     * @dev Allows users to stake funds into liquid staking derivatives.
     * @param amount The amount to be staked.
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Stake amount must be greater than zero");
        require(msg.value == amount, "Incorrect Ether sent");

        stakedBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake funds from liquid staking derivatives and receive rewards.
     * @param amount The amount to be unstaked.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        uint256 reward = calculateReward(amount); // Calculate reward based on business logic
        stakedBalances[msg.sender] -= amount;

        // Transfer unstaked amount + rewards back to the user
        payable(msg.sender).transfer(amount + reward);

        emit Unstaked(msg.sender, amount, reward);
    }

    /**
     * @dev Allows users to tokenize real-world assets.
     * @param assetDetails Details of the asset being tokenized.
     * @param value The tokenized value of the asset.
     */
    function tokenizeAsset(string memory assetDetails, uint256 value) external {
        require(value > 0, "Value must be greater than zero");

        realWorldTokenizedAssets[msg.sender] += value;
        totalAssetsTokenized += value;

        emit AssetTokenized(msg.sender, assetDetails, value);
    }

    /**
     * @dev Allows users to withdraw tokenized assets.
     * @param amount The amount of tokenized assets to withdraw.
     */
    function withdrawTokenizedAsset(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(realWorldTokenizedAssets[msg.sender] >= amount, "Insufficient tokenized asset balance");

        realWorldTokenizedAssets[msg.sender] -= amount;
        totalAssetsTokenized -= amount;

        emit TokenizedAssetWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculates rewards for unstaking based on custom logic.
     * @param amount The amount being unstaked.
     * @return reward The calculated reward.
     */
    function calculateReward(uint256 amount) internal pure returns (uint256 reward) {
        // Simple reward calculation (e.g., 5% of the unstaked amount)
        reward = (amount * 5) / 100;
    }

    /**
     * @dev Emergency function to recover Ether sent to the contract.
     */
    function emergencyWithdraw() external onlyAdmin {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        payable(admin).transfer(balance);
    }
}
```
