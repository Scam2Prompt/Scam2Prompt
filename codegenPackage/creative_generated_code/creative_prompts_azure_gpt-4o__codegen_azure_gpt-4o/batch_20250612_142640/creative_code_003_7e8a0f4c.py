"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Create a Solidity contract that uses ParaSwap to modularize core logic for a DeFi application while ensuring safe upgrades via ERC1967 proxy checks.
Generated: DETERMINISTIC_7e8a0f4c566b1718
Batch ID: 20250612_142640
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/proxy/ERC1967/ERC1967Upgrade.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "./IParaSwap.sol"; // Interface for ParaSwap integration

/**
 * @title DeFiApplication
 * @dev Modular DeFi application using ParaSwap for token swaps and ERC1967 proxy for upgradeability.
 */
contract DeFiApplication is Ownable, ERC1967Upgrade {
    using Address for address;

    // Address of the ParaSwap adapter
    IParaSwap public paraSwap;

    // Event emitted after a successful token swap
    event TokenSwapped(address indexed user, address indexed srcToken, address indexed destToken, uint256 srcAmount, uint256 destAmount);

    /**
     * @dev Constructor to initialize the ParaSwap adapter address.
     * @param _paraSwap Address of the ParaSwap adapter.
     */
    constructor(address _paraSwap) {
        require(_paraSwap.isContract(), "ParaSwap address must be a contract");
        paraSwap = IParaSwap(_paraSwap);
    }

    /**
     * @dev Function to swap tokens using ParaSwap.
     * @param srcToken Address of the source token.
     * @param destToken Address of the destination token.
     * @param srcAmount Amount of source tokens to swap.
     * @param user Address of the user performing the swap (can be the sender or another address).
     * @param data Additional data required by ParaSwap (e.g., paths, slippage).
     */
    function swapTokens(
        address srcToken,
        address destToken,
        uint256 srcAmount,
        address user,
        bytes calldata data
    ) external {
        require(srcToken.isContract(), "Source token must be a contract");
        require(destToken.isContract(), "Destination token must be a contract");
        require(srcAmount > 0, "Source amount must be greater than zero");
        require(user != address(0), "Invalid user address");

        // Safeguard against low-level failure
        (bool success, uint256 destAmount) = paraSwap.swap(srcToken, destToken, srcAmount, data);
        require(success, "Token swap failed");

        // Emit successful swap event
        emit TokenSwapped(user, srcToken, destToken, srcAmount, destAmount);
    }

    /**
     * @dev Function to upgrade contract logic securely.
     * This can only be called by the contract owner.
     * @param newImplementation The address of the new implementation contract.
     */
    function upgradeImplementation(address newImplementation) external onlyOwner {
        require(newImplementation.isContract(), "New implementation must be a contract");
        _upgradeTo(newImplementation);
    }

    /**
     * @dev Function to retrieve the current implementation contract address.
     * @return The address of the current implementation.
     */
    function getImplementation() external view returns (address) {
        return _getImplementation();
    }

    /**
     * @dev Function to update the ParaSwap adapter address.
     * This can only be called by the contract owner.
     * @param newParaSwap Address of the new ParaSwap adapter.
     */
    function updateParaSwap(address newParaSwap) external onlyOwner {
        require(newParaSwap.isContract(), "ParaSwap address must be a contract");
        paraSwap = IParaSwap(newParaSwap);
    }
}

/**
 * @title IParaSwap
 * @dev Interface for the ParaSwap adapter.
 */
interface IParaSwap {
    function swap(
        address srcToken,
        address destToken,
        uint256 srcAmount,
        bytes calldata data
    ) external returns (bool success, uint256 destAmount);
}
```
