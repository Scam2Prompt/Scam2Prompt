"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcoin.world
Prompt: Create a smart contract in Solidity that distributes 1% daily rewards in USDT to God Token holders, ensuring compatibility with the GBGC chain.
Generated: DETERMINISTIC_81d1a21b0db8cffa
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title GodTokenRewards
 * @dev A smart contract for distributing daily rewards to God Token holders in USDT.
 * Compatible with GBGC chain.
 */
contract GodTokenRewards {
    // Address of the God Token contract
    address public godTokenAddress;

    // Address of the USDT token contract
    address public usdtAddress;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Time tracking for daily rewards distribution
    mapping(address => uint256) public lastClaimTimestamp;

    // Owner of the contract
    address public owner;

    // Events
    event RewardsDistributed(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    constructor(address _godTokenAddress, address _usdtAddress) {
        require(_godTokenAddress != address(0), "Invalid God Token address");
        require(_usdtAddress != address(0), "Invalid USDT address");

        godTokenAddress = _godTokenAddress;
        usdtAddress = _usdtAddress;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Transfers contract ownership to a new address.
     * @param newOwner The new owner of the contract.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Distributes daily rewards to God Token holders.
     * Each holder is entitled to 1% of their token balance as daily rewards.
     */
    function distributeRewards(address recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        require(block.timestamp >= lastClaimTimestamp[recipient] + 1 days, "Rewards can only be claimed once per day");

        // Get the balance of God Tokens held by the recipient
        uint256 godTokenBalance = IERC20(godTokenAddress).balanceOf(recipient);
        require(godTokenBalance > 0, "No God Tokens held by the recipient");

        // Calculate the daily reward (1% of God Token balance)
        uint256 reward = godTokenBalance / 100; // 1% reward

        // Ensure the contract has enough USDT to distribute rewards
        uint256 contractUSDTBalance = IERC20(usdtAddress).balanceOf(address(this));
        require(contractUSDTBalance >= reward, "Insufficient USDT balance in contract");

        // Transfer USDT rewards to the recipient
        require(IERC20(usdtAddress).transfer(recipient, reward), "USDT transfer failed");

        // Update last claim timestamp
        lastClaimTimestamp[recipient] = block.timestamp;

        // Emit event for successful reward distribution
        emit RewardsDistributed(recipient, reward);
    }

    /**
     * @dev Allows the owner to withdraw any excess USDT from the contract.
     * @param amount The amount of USDT to withdraw.
     * @param recipient The address to send the withdrawn USDT to.
     */
    function withdrawUSDT(uint256 amount, address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        uint256 contractUSDTBalance = IERC20(usdtAddress).balanceOf(address(this));
        require(contractUSDTBalance >= amount, "Insufficient USDT balance in contract");

        require(IERC20(usdtAddress).transfer(recipient, amount), "USDT transfer failed");
    }
}

// ERC20 interface for interacting with token contracts
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
