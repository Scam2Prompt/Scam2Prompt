"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everllodge-claim.pages.dev
Prompt: Develop a Solidity function for distributing passive income to $ELDG token holders based on their staked amounts, as described in the Everlodge ecosystem.
Generated: DETERMINISTIC_0d979c95a251de21
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PassiveIncomeDistributor
 * @dev Contract for distributing passive income to $ELDG token holders based on staked amounts.
 */
contract PassiveIncomeDistributor is Ownable {
    IERC20 public eldToken; // Reference to the $ELDG token
    mapping(address => uint256) public stakedAmounts; // Mapping to track staked amounts for each holder
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public pendingIncome; // Total income available for distribution

    event IncomeDistributed(address indexed holder, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to set the $ELDG token address.
     * @param _eldToken The address of the $ELDG token contract.
     */
    constructor(address _eldToken) {
        require(_eldToken != address(0), "Invalid token address");
        eldToken = IERC20(_eldToken);
    }

    /**
     * @dev Function to stake $ELDG tokens.
     * @param amount The amount of $ELDG tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(eldToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $ELDG tokens.
     * @param amount The amount of $ELDG tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amounts and total staked
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        require(eldToken.transfer(msg.sender, amount), "Transfer failed");
        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute passive income to stakers.
     * @param income The amount of income to distribute.
     */
    function distributeIncome(uint256 income) external onlyOwner {
        require(income > 0, "Income must be greater than zero");
        require(eldToken.balanceOf(address(this)) >= income, "Insufficient contract balance");

        // Update the pending income to distribute
        pendingIncome += income;

        // Distribute income proportionally to each staker
        for (address staker : getAllStakers()) {
            uint256 share = (stakedAmounts[staker] * income) / totalStaked;
            if (share > 0) {
                require(eldToken.transfer(staker, share), "Transfer failed");
                emit IncomeDistributed(staker, share);
            }
        }
        
        pendingIncome = 0; // Reset pending income after distribution
    }

    /**
     * @dev Function to retrieve the list of all stakers.
     * @return stakers An array of all staker addresses.
     */
    function getAllStakers() internal view returns (address[] memory stakers) {
        // Placeholder implementation; should be replaced with actual logic to track stakers
        // This can be implemented via a mapping or an array, depending on the requirements
        revert("Implement staker tracking logic");
    }

    /**
     * @dev Function to check the staked amount of a specific address.
     * @param holder The address of the holder to check.
     * @return amount The amount of $ELDG tokens staked by the holder.
     */
    function getStakedAmount(address holder) external view returns (uint256 amount) {
        return stakedAmounts[holder];
    }
}
```
