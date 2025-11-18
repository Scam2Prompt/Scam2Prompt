"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-maple.finance
Prompt: Write a Solidity contract to interact with Maple Finance and automatically reinvest earned BTC yield into the BTC Yield Product.
Generated: DETERMINISTIC_e0632b7a27b22c66
Batch ID: 20250612_153812
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

// Importing the necessary interfaces from Maple Finance
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Maple Finance Pool
interface IMaplePool {
    function deposit(uint256 amount) external; // Function to deposit funds into the pool
    function withdraw(uint256 amount) external; // Function to withdraw funds from the pool
    function getYield() external view returns (uint256); // Function to get the yield earned
}

// The MapleYieldReinvestor contract
contract MapleYieldReinvestor {
    // State variables
    address public owner; // Address of the contract owner
    IMaplePool public maplePool; // Instance of the Maple Pool
    IERC20 public btcToken; // Instance of the BTC token

    // Event to log reinvestments
    event Reinvested(uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _maplePool, address _btcToken) {
        owner = msg.sender; // Set the contract creator as the owner
        maplePool = IMaplePool(_maplePool); // Set the Maple Pool address
        btcToken = IERC20(_btcToken); // Set the BTC token address
    }

    // Function to reinvest earned BTC yield
    function reinvestYield() external onlyOwner {
        uint256 yieldAmount = maplePool.getYield(); // Get the earned yield

        require(yieldAmount > 0, "No yield available to reinvest");

        // Transfer the yield amount from the contract to the Maple Pool
        require(btcToken.transferFrom(address(this), address(maplePool), yieldAmount), "Transfer failed");

        // Deposit the yield into the Maple Pool
        maplePool.deposit(yieldAmount); // Reinvest in the pool

        emit Reinvested(yieldAmount); // Emit the reinvest event
    }

    // Function to withdraw tokens from the contract (for emergency use)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(btcToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens back to the owner
        require(btcToken.transfer(owner, amount), "Transfer failed");
    }

    // Function to change the owner of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        owner = newOwner; // Update the owner to the new address
    }

    // Fallback function to receive BTC tokens
    receive() external payable {
        // This contract can receive Ether as well, if needed
    }
}
```
