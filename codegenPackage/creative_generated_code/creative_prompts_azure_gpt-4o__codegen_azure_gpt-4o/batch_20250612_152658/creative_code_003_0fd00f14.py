"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Generate a Solidity smart contract for a bonding mechanism like Thoreum Bond, where 20% of bonding funds are used for market buying and 80% are allocated to liquidity creation.
Generated: DETERMINISTIC_0fd00f14e8ec84e7
Batch ID: 20250612_152658
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
 * @title BondingMechanism
 * @dev A smart contract for bonding funds and allocating them for market buying and liquidity creation.
 */
contract BondingMechanism {
    address public owner;
    address public marketWallet; // Wallet address for market buying
    address public liquidityWallet; // Wallet address for liquidity creation

    uint256 public totalFunds; // Total funds contributed via bonding
    uint256 public marketAllocation = 20; // Percentage allocated to market buying (20%)
    uint256 public liquidityAllocation = 80; // Percentage allocated to liquidity creation (80%)

    event Bonded(address indexed user, uint256 amount);
    event FundsDistributed(uint256 marketAmount, uint256 liquidityAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    constructor(address _marketWallet, address _liquidityWallet) {
        require(_marketWallet != address(0), "Invalid market wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");

        owner = msg.sender;
        marketWallet = _marketWallet;
        liquidityWallet = _liquidityWallet;
    }

    /**
     * @dev Allows users to bond funds to the contract.
     */
    function bond() external payable {
        require(msg.value > 0, "Bond amount must be greater than zero");

        totalFunds += msg.value;

        emit Bonded(msg.sender, msg.value);
    }

    /**
     * @dev Distributes the bonded funds based on allocation percentages.
     * Can only be called by the contract owner.
     */
    function distributeFunds() external onlyOwner {
        require(totalFunds > 0, "No funds to distribute");
        
        // Calculate allocation amounts
        uint256 marketAmount = (totalFunds * marketAllocation) / 100;
        uint256 liquidityAmount = (totalFunds * liquidityAllocation) / 100;

        // Reset totalFunds to avoid double distribution
        totalFunds = 0;

        // Transfer funds to respective wallets
        (bool marketSuccess, ) = marketWallet.call{value: marketAmount}("");
        require(marketSuccess, "Market fund transfer failed");

        (bool liquiditySuccess, ) = liquidityWallet.call{value: liquidityAmount}("");
        require(liquiditySuccess, "Liquidity fund transfer failed");

        emit FundsDistributed(marketAmount, liquidityAmount);
    }

    /**
     * @dev Allows the owner to update the market wallet address.
     * @param _marketWallet The new market wallet address.
     */
    function updateMarketWallet(address _marketWallet) external onlyOwner {
        require(_marketWallet != address(0), "Invalid market wallet address");
        marketWallet = _marketWallet;
    }

    /**
     * @dev Allows the owner to update the liquidity wallet address.
     * @param _liquidityWallet The new liquidity wallet address.
     */
    function updateLiquidityWallet(address _liquidityWallet) external onlyOwner {
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        liquidityWallet = _liquidityWallet;
    }

    /**
     * @dev Fallback function to accept ether directly.
     */
    receive() external payable {
        bond();
    }
}
```
