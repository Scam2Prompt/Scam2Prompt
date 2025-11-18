"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbull.io
Prompt: Implement a token burn mechanism in Solidity that automatically burns a percentage of $BTCBULL supply whenever Bitcoin's price increases by $25K, following the milestones described on the BTC Bull roadmap.
Generated: DETERMINISTIC_48efd5ccc1b303d5
Batch ID: 20250612_154757
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

interface IPriceFeed {
    function getLatestPrice() external view returns (int256);
}

contract BTCBullToken {
    // Token metadata
    string public name = "BTCBull";
    string public symbol = "BTCBULL";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token balances
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // Milestones for automatic burns
    uint256 public nextMilestone = 25000 * 1e18; // First milestone ($25K in wei)
    uint256 public burnPercentage = 2; // Percentage of total supply to burn (e.g., 2%)

    // Price feed for Bitcoin price
    IPriceFeed public priceFeed;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(uint256 amountBurned, uint256 newTotalSupply);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(uint256 _initialSupply, address _priceFeedAddress) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** decimals;
        balances[owner] = totalSupply;
        priceFeed = IPriceFeed(_priceFeedAddress);
    }

    // Transfer function
    function transfer(address _to, uint256 _amount) public returns (bool) {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        require(_to != address(0), "Invalid recipient");

        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);

        // Check if milestone is reached after transfer
        checkMilestone();

        return true;
    }

    // Check if the Bitcoin price has crossed the next milestone
    function checkMilestone() internal {
        int256 currentPrice = priceFeed.getLatestPrice();
        require(currentPrice > 0, "Invalid price from feed");

        if (uint256(currentPrice) >= nextMilestone) {
            burnTokens();
            nextMilestone += 25000 * 1e18; // Increment milestone by $25K in wei
        }
    }

    // Burn a percentage of the total supply
    function burnTokens() internal {
        uint256 amountToBurn = (totalSupply * burnPercentage) / 100;
        require(amountToBurn > 0, "Burn amount must be greater than zero");

        balances[owner] -= amountToBurn;
        totalSupply -= amountToBurn;

        emit Burn(amountToBurn, totalSupply);
    }

    // Owner can set a new burn percentage
    function setBurnPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Invalid percentage");
        burnPercentage = _newPercentage;
    }

    // Owner can set a new price feed contract
    function setPriceFeed(address _newPriceFeed) external onlyOwner {
        require(_newPriceFeed != address(0), "Invalid price feed address");
        priceFeed = IPriceFeed(_newPriceFeed);
    }
}
```
