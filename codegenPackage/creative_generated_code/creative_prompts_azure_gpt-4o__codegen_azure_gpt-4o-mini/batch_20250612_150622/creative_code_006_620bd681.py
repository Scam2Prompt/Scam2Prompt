"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-route.pages.dev
Prompt: Provide an example of how to use Chainlink price oracles to calculate the value of collateral deposited into the Origin vault for minting OUSD.
Generated: DETERMINISTIC_620bd681ff67a14b
Batch ID: 20250612_150622
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

// Importing OpenZeppelin contracts for safe math operations and ERC20 interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract OriginVault {
    // State variables
    AggregatorV3Interface internal priceFeed; // Chainlink price feed
    IERC20 public collateralToken; // Token that will be used as collateral
    mapping(address => uint256) public collateralBalance; // User collateral balances

    // Events
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    
    // Constructor to set the collateral token and price feed address
    constructor(address _collateralToken, address _priceFeed) {
        collateralToken = IERC20(_collateralToken);
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    // Function to deposit collateral into the vault
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer collateral tokens from user to this contract
        collateralToken.transferFrom(msg.sender, address(this), amount);
        collateralBalance[msg.sender] += amount;

        emit CollateralDeposited(msg.sender, amount);
    }

    // Function to withdraw collateral from the vault
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(collateralBalance[msg.sender] >= amount, "Insufficient balance");

        // Update the user's collateral balance
        collateralBalance[msg.sender] -= amount;

        // Transfer tokens back to the user
        collateralToken.transfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    // Function to get the latest price of the collateral in USD
    function getLatestPrice() public view returns (int) {
        // Fetch the latest price from the Chainlink price feed
        (
            , 
            int price, 
            , 
            , 
        ) = priceFeed.latestRoundData();
        return price;
    }

    // Function to calculate the USD value of the collateral deposited
    function calculateCollateralValue(address user) external view returns (uint256) {
        uint256 balance = collateralBalance[user];
        int price = getLatestPrice();

        // Calculate the USD value (assuming price is in 8 decimals)
        require(price > 0, "Invalid price from oracle");
        return balance * uint256(price) / 1e8; // Adjust for 8 decimal places
    }
}
```
