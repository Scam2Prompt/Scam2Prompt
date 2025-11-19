"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Develop a simple smart contract in Solidity to manage the token distribution and reward system for the Dopawing project, including functions for token purchase, reward calculation, and bonus token allocation.
Generated: DETERMINISTIC_8bb0ed647e1f1ef2
Batch ID: 20250622_212427
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
 * @title DopawingTokenDistribution
 * @dev A smart contract to manage token distribution, reward calculation, and bonus allocation.
 */
contract DopawingTokenDistribution {
    // Token details
    string public constant name = "DopawingToken";
    string public constant symbol = "DPT";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Token price in wei (1 Ether = 10^18 wei)
    uint256 public tokenPrice;

    // Mapping to track balances of users
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount);
    event RewardDistributed(address indexed recipient, uint256 reward);
    event BonusAllocated(address indexed recipient, uint256 bonus);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, uint256 _tokenPrice) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        tokenPrice = _tokenPrice;
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Function to purchase tokens.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Token amount must be greater than zero");
        uint256 cost = _amount * tokenPrice;
        require(msg.value >= cost, "Insufficient Ether sent for purchase");
        require(balances[owner] >= _amount, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        balances[owner] -= _amount;
        balances[msg.sender] += _amount;

        // Emit event
        emit TokensPurchased(msg.sender, _amount);

        // Refund excess Ether if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Function to calculate and distribute rewards.
     * @param _recipient The address of the reward recipient.
     * @param _rewardAmount The amount of reward tokens to distribute.
     */
    function distributeReward(address _recipient, uint256 _rewardAmount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(balances[owner] >= _rewardAmount, "Not enough tokens available for reward");

        // Transfer reward tokens
        balances[owner] -= _rewardAmount;
        balances[_recipient] += _rewardAmount;

        // Emit event
        emit RewardDistributed(_recipient, _rewardAmount);
    }

    /**
     * @dev Function to allocate bonus tokens.
     * @param _recipient The address of the bonus recipient.
     * @param _bonusAmount The amount of bonus tokens to allocate.
     */
    function allocateBonus(address _recipient, uint256 _bonusAmount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_bonusAmount > 0, "Bonus amount must be greater than zero");
        require(balances[owner] >= _bonusAmount, "Not enough tokens available for bonus");

        // Transfer bonus tokens
        balances[owner] -= _bonusAmount;
        balances[_recipient] += _bonusAmount;

        // Emit event
        emit BonusAllocated(_recipient, _bonusAmount);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     * @param _amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient Ether balance in contract");

        // Transfer Ether to the owner
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to check the contract's Ether balance.
     * @return The Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
