"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Create a smart contract in Solidity that integrates with Belt Finance to automate reinvestment of earned tokens into liquidity pools.
Generated: DETERMINISTIC_3a81589629fafe2b
Batch ID: 20250612_155024
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

// Import interfaces for ERC20 token and the Belt Finance protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Smart Contract
contract BeltReinvestment is Ownable {
    // Define state variables
    IERC20 public beltToken; // Belt token contract
    address public beltFinance; // Address of Belt Finance pool

    // Event to log reinvestment actions
    event Reinvested(address indexed user, uint256 amount);

    // Constructor to initialize the contract with Belt token and Belt Finance pool address
    constructor(address _beltToken, address _beltFinance) {
        beltToken = IERC20(_beltToken);
        beltFinance = _beltFinance;
    }

    // Function to reinvest earned tokens back into the liquidity pool
    function reinvest() external onlyOwner {
        uint256 balance = beltToken.balanceOf(address(this));

        require(balance > 0, "No tokens to reinvest");

        // Approve the Belt Finance contract to spend the tokens
        beltToken.approve(beltFinance, balance);

        // Call the reinvest function from the Belt Finance contract
        (bool success, ) = beltFinance.call(abi.encodeWithSignature("reinvest()"));

        // Check if the reinvest call was successful
        require(success, "Reinvestment failed");

        emit Reinvested(msg.sender, balance);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(beltToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        beltToken.transfer(_to, _amount);
    }

    // Function to set a new Belt Finance address (if necessary)
    function setBeltFinanceAddress(address _beltFinance) external onlyOwner {
        beltFinance = _beltFinance;
    }

    // Function to receive Ether (if needed)
    receive() external payable {}
}
```
