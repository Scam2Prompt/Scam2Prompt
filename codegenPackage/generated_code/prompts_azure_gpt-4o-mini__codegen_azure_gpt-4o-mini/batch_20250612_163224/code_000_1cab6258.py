"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.org
Prompt: Write a code snippet to create a non-custodial lending vault using Morpho's infrastructure, ensuring it is optimized for risk and yield.
Generated: DETERMINISTIC_1cab6258ae05409c
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for Morpho's lending protocol
interface IMorpho {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function getSupplyRate(address asset) external view returns (uint256);
}

// Non-Custodial Lending Vault Contract
contract NonCustodialLendingVault is Ownable, ReentrancyGuard {
    // State variables
    IMorpho public morpho; // Morpho lending protocol interface
    address public asset; // Asset to be lent
    mapping(address => uint256) public balances; // User balances

    // Events
    event Supplied(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _morpho, address _asset) {
        require(_morpho != address(0), "Invalid Morpho address");
        require(_asset != address(0), "Invalid asset address");
        morpho = IMorpho(_morpho);
        asset = _asset;
    }

    // Function to supply assets to the Morpho protocol
    function supply(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance
        balances[msg.sender] += amount;

        // Supply the asset to Morpho
        IERC20(asset).approve(address(morpho), amount);
        morpho.supply(asset, amount);

        emit Supplied(msg.sender, amount);
    }

    // Function to withdraw assets from the Morpho protocol
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] -= amount;

        // Withdraw the asset from Morpho
        morpho.withdraw(asset, amount);
        require(IERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the current supply rate for the asset
    function getCurrentSupplyRate() external view returns (uint256) {
        return morpho.getSupplyRate(asset);
    }

    // Function to get the balance of a user
    function getUserBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
