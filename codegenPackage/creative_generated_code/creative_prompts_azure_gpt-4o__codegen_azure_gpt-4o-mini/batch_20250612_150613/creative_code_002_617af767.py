"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Create a Solidity function that enables a smart contract to opt-in for receiving stablecoin yield from OUSD, as outlined in the documentation. Ensure compatibility with Safe contracts.
Generated: DETERMINISTIC_617af7672a968f8e
Batch ID: 20250612_150613
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for OUSD stablecoin
interface IOUSD {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

// Contract to manage OUSD yield
contract OUSDYieldManager is Ownable {
    using Address for address;

    // OUSD token contract address
    IOUSD public ousd;

    // Event emitted when a deposit is made
    event YieldDeposited(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event YieldWithdrawn(address indexed user, uint256 amount);

    // Constructor to set OUSD contract address
    constructor(address _ousdAddress) {
        require(_ousdAddress.isContract(), "OUSD address must be a contract");
        ousd = IOUSD(_ousdAddress);
    }

    // Function to deposit stablecoins into OUSD for yield
    function depositYield(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer the specified amount of stablecoin to this contract
        IERC20(address(ousd)).transferFrom(msg.sender, address(this), amount);

        // Deposit the stablecoin into OUSD
        ousd.deposit(amount);

        emit YieldDeposited(msg.sender, amount);
    }

    // Function to withdraw stablecoins from OUSD
    function withdrawYield(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(ousd.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Withdraw the specified amount of stablecoin from OUSD
        ousd.withdraw(amount);

        // Transfer the stablecoin back to the owner
        IERC20(address(ousd)).transfer(msg.sender, amount);

        emit YieldWithdrawn(msg.sender, amount);
    }

    // Function to check the contract's OUSD balance
    function getOUSDBalance() external view returns (uint256) {
        return ousd.balanceOf(address(this));
    }
}
```
