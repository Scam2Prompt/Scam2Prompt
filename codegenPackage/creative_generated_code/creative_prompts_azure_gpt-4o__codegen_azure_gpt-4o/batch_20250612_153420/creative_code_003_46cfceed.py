"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Create a Solidity function that distributes 100% of platform profits to token stakers, following the profit-sharing model outlined by Blockchain Bets.
Generated: DETERMINISTIC_46cfceed5e810ec6
Batch ID: 20250612_153420
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
 * @title ProfitDistributor
 * @dev This contract distributes platform profits to token stakers.
 */
contract ProfitDistributor {
    // State variables
    address public owner;                              // Address of the contract owner
    uint256 public totalStaked;                        // Total tokens staked
    mapping(address => uint256) public stakedAmounts;  // Mapping of staked amounts per address
    mapping(address => bool) public hasStaked;         // Tracks whether an address has staked

    // Events
    event ProfitsDistributed(uint256 amountDistributed);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external payable {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update staking data
        totalStaked += amount;
        stakedAmounts[msg.sender] += amount;
        hasStaked[msg.sender] = true;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to unstake their tokens.
     */
    function unstakeTokens() external {
        require(hasStaked[msg.sender], "No tokens staked");
        uint256 amount = stakedAmounts[msg.sender];
        require(amount > 0, "No staked amount found");

        // Update staking data
        totalStaked -= amount;
        stakedAmounts[msg.sender] = 0;
        hasStaked[msg.sender] = false;

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute 100% of platform profits to token stakers.
     * @param totalProfit The total profit to be distributed.
     */
    function distributeProfits(uint256 totalProfit) external onlyOwner {
        require(totalProfit > 0, "Profit amount must be greater than zero");
        require(totalStaked > 0, "No tokens staked to distribute profits");

        for (address staker in _getStakers()) {
            uint256 stakerShare = (stakedAmounts[staker] * totalProfit) / totalStaked;

            // Transfer profit share to the staker
            (bool success, ) = staker.call{value: stakerShare}("");
            require(success, "Profit transfer failed");
        }

        emit ProfitsDistributed(totalProfit);
    }

    /**
     * @dev Helper function to retrieve all stakers (for illustration; actual gas-efficient implementation required).
     */
    function _getStakers() private view returns (address[] memory) {
        // This is a placeholder implementation. Replace with actual logic to retrieve all stakers.
        address[] memory stakers; // This needs proper tracking in a scalable implementation.
        return stakers;
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw contract balance (owner-only).
     */
    function withdrawBalance() external onlyOwner {
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
}
```
