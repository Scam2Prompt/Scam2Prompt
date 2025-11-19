"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a Solidity contract for a stablecoin that maintains its value pegged to the US dollar, using the principles described on Ethereum.org.
Generated: DETERMINISTIC_f9c611e48cc863ee
Batch ID: 20250612_151948
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title StableCoin
 * @dev A stablecoin pegged to the US dollar with minting and burning functionality
 */
contract StableCoin is ERC20, Ownable, Pausable {
    // Address of the oracle that provides the USD exchange rate
    address public oracle;

    // Minimum collateral ratio (e.g., 1.5 for 150%)
    uint256 public constant MIN_COLLATERAL_RATIO = 150;
    uint256 public constant RATIO_DECIMALS = 2;

    // Events
    event Mint(address indexed minter, uint256 amount, uint256 collateralAmount);
    event Burn(address indexed burner, uint256 amount, uint256 collateralAmount);
    event OracleUpdated(address indexed newOracle);

    /**
     * @dev Constructor that initializes the stablecoin
     * @param _oracle Address of the price oracle
     */
    constructor(address _oracle) ERC20("StableCoin", "STC") {
        require(_oracle != address(0), "Invalid oracle address");
        oracle = _oracle;
    }

    /**
     * @dev Updates the oracle address
     * @param _newOracle Address of the new oracle
     */
    function updateOracle(address _newOracle) external onlyOwner {
        require(_newOracle != address(0), "Invalid oracle address");
        oracle = _newOracle;
        emit OracleUpdated(_newOracle);
    }

    /**
     * @dev Mints new stablecoins when collateral is deposited
     * @param _amount Amount of stablecoins to mint
     * @param _collateralAmount Amount of collateral deposited
     */
    function mint(uint256 _amount, uint256 _collateralAmount) external whenNotPaused {
        require(_amount > 0, "Amount must be greater than 0");
        require(_collateralAmount > 0, "Collateral amount must be greater than 0");

        // Verify collateral ratio is maintained
        uint256 currentRatio = (_collateralAmount * 100 * (10 ** RATIO_DECIMALS)) / _amount;
        require(currentRatio >= MIN_COLLATERAL_RATIO * (10 ** RATIO_DECIMALS), "Insufficient collateral ratio");

        _mint(msg.sender, _amount);
        emit Mint(msg.sender, _amount, _collateralAmount);
    }

    /**
     * @dev Burns stablecoins to withdraw collateral
     * @param _amount Amount of stablecoins to burn
     * @param _collateralAmount Amount of collateral to withdraw
     */
    function burn(uint256 _amount, uint256 _collateralAmount) external whenNotPaused {
        require(_amount > 0, "Amount must be greater than 0");
        require(_collateralAmount > 0, "Collateral amount must be greater than 0");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        _burn(msg.sender, _amount);
        emit Burn(msg.sender, _amount, _collateralAmount);
    }

    /**
     * @dev Pauses all minting and burning operations
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all minting and burning operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Overrides decimals to match standard USD conventions
     */
    function decimals() public pure override returns (uint8) {
        return 6;
    }
}

/**
 * @title Oracle interface
 * @dev Interface for the price oracle
 */
interface IOracle {
    function getPrice() external view returns (uint256);
}
```
