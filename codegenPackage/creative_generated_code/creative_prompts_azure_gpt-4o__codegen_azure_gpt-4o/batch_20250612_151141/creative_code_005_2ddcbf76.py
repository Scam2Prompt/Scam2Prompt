"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hellohosting.pages.dev
Prompt: Write a function in Solidity to distribute Wealth Coin from a Treasury Reserve to charities, ensuring compliance with the rules outlined in the Wealth Coin whitepaper.
Generated: DETERMINISTIC_2ddcbf761cfe88ce
Batch ID: 20250612_151141
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
 * @title WealthCoinTreasury
 * @dev This contract handles the distribution of Wealth Coin from the treasury reserve to approved charities.
 */
contract WealthCoinTreasury {
    // State variables
    address public owner; // Contract owner
    IERC20 public wealthCoin; // ERC20 token (Wealth Coin) contract
    uint256 public totalDistributed; // Tracks total distributed Wealth Coins

    struct Charity {
        bool approved;
        uint256 allocatedAmount;
    }

    mapping(address => Charity) public charities; // Mapping of charities

    event CharityApproved(address charity, uint256 allocation);
    event CharityRemoved(address charity);
    event WealthDistributed(address charity, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _wealthCoin) {
        require(_wealthCoin != address(0), "Invalid Wealth Coin contract address");
        owner = msg.sender;
        wealthCoin = IERC20(_wealthCoin);
    }

    /**
     * @dev Approves a charity for allocation, specifying the amount of Wealth Coin they can receive.
     * @param _charity Address of the charity to approve.
     * @param _allocation Allocation of Wealth Coins for the charity.
     */
    function approveCharity(address _charity, uint256 _allocation) external onlyOwner {
        require(_charity != address(0), "Invalid charity address");
        require(_allocation > 0, "Allocation must be greater than zero");

        charities[_charity] = Charity({
            approved: true,
            allocatedAmount: _allocation
        });

        emit CharityApproved(_charity, _allocation);
    }

    /**
     * @dev Removes a charity from the approved list.
     * @param _charity Address of the charity to remove.
     */
    function removeCharity(address _charity) external onlyOwner {
        require(charities[_charity].approved, "Charity not found");

        delete charities[_charity]; // Remove charity from mapping

        emit CharityRemoved(_charity);
    }

    /**
     * @dev Distributes Wealth Coins to an approved charity.
     * @param _charity Address of the charity to distribute to.
     */
    function distributeWealth(address _charity) external onlyOwner {
        Charity storage charity = charities[_charity];
        require(charity.approved, "Charity not approved");
        require(charity.allocatedAmount > 0, "No allocation for this charity");
        require(wealthCoin.balanceOf(address(this)) >= charity.allocatedAmount, "Insufficient balance in treasury");

        uint256 amountToDistribute = charity.allocatedAmount;

        // Transfer Wealth Coins to the charity
        require(wealthCoin.transfer(_charity, amountToDistribute), "Token transfer failed");

        totalDistributed += amountToDistribute;
        charity.allocatedAmount = 0; // Mark allocation as distributed

        emit WealthDistributed(_charity, amountToDistribute);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract in case of emergency.
     * @param _to Address to withdraw tokens to.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address to withdraw to");
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(wealthCoin.balanceOf(address(this)) >= _amount, "Insufficient balance");

        require(wealthCoin.transfer(_to, _amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
