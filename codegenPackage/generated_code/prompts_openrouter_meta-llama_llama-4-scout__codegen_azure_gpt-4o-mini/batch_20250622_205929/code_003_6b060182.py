"""
Generated Code Metadata:
========================
Original URL: https://www.morpo.org
Prompt: "Design a smart contract function to supply USDC into a vault on Morpho, similar to the Coinshift USDL vault, and explain the benefits of using Morpho's protocol."
Generated: DETERMINISTIC_6b060182c8ca2f74
Batch ID: 20250622_205929
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Morpho's protocol
interface IMorpho {
    function supply(address asset, uint256 amount) external;
}

// Smart contract for supplying USDC to Morpho's vault
contract USDCVault is Ownable {
    // Address of the USDC token contract
    address public usdcToken;
    // Address of the Morpho protocol contract
    IMorpho public morpho;

    // Event emitted when USDC is supplied to the vault
    event USDCSupplied(address indexed user, uint256 amount);

    // Constructor to initialize the contract with USDC and Morpho addresses
    constructor(address _usdcToken, address _morpho) {
        require(_usdcToken != address(0), "Invalid USDC address");
        require(_morpho != address(0), "Invalid Morpho address");
        
        usdcToken = _usdcToken;
        morpho = IMorpho(_morpho);
    }

    // Function to supply USDC to Morpho's vault
    function supplyUSDC(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer USDC from the user to this contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amount);

        // Approve the Morpho contract to spend the USDC
        IERC20(usdcToken).approve(address(morpho), amount);

        // Supply USDC to Morpho's vault
        morpho.supply(usdcToken, amount);

        // Emit an event for the supply action
        emit USDCSupplied(msg.sender, amount);
    }

    // Function to withdraw USDC from the contract (if needed)
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(usdcToken).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer USDC back to the owner
        IERC20(usdcToken).transfer(msg.sender, amount);
    }

    // Function to set a new Morpho contract address (onlyOwner)
    function setMorphoAddress(address _morpho) external onlyOwner {
        require(_morpho != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morpho);
    }
}
```
