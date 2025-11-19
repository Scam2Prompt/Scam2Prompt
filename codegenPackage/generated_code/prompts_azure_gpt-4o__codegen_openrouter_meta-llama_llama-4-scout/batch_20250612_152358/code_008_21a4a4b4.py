"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Write a Solidity function that allows users to deposit institutional-grade collateral to mint USD0, ensuring compliance with the protocol's risk policies.
Generated: DETERMINISTIC_21a4a4b453452746
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title USD0 Collateral Manager
 * @author [Your Name]
 * @notice This contract manages the deposit of institutional-grade collateral to mint USD0.
 */
contract CollateralManager {
    using SafeMath for uint256;

    // Mapping of collateral assets to their respective risk parameters
    mapping(address => RiskParams) public collateralParams;

    // Mapping of user collateral balances
    mapping(address => mapping(address => uint256)) public userCollateralBalances;

    // Mapping of user debt balances (USD0 minted)
    mapping(address => uint256) public userDebtBalances;

    // USD0 token contract
    IERC20 public usd0Token;

    /**
     * @dev Event emitted when a user deposits collateral
     * @param user User address
     * @param collateralAsset Collateral asset address
     * @param amount Amount deposited
     */
    event CollateralDeposited(address indexed user, address indexed collateralAsset, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws collateral
     * @param user User address
     * @param collateralAsset Collateral asset address
     * @param amount Amount withdrawn
     */
    event CollateralWithdrawn(address indexed user, address indexed collateralAsset, uint256 amount);

    /**
     * @dev Event emitted when a user mints USD0
     * @param user User address
     * @param amount Amount minted
     */
    event Usd0Minted(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user burns USD0
     * @param user User address
     * @param amount Amount burned
     */
    event Usd0Burned(address indexed user, uint256 amount);

    /**
     * @dev Struct representing risk parameters for a collateral asset
     */
    struct RiskParams {
        uint256 collateralFactor; // Collateral factor (e.g. 0.5 for 50%)
        uint256 liquidationPenalty; // Liquidation penalty (e.g. 0.1 for 10%)
    }

    /**
     * @dev Constructor
     * @param _usd0Token USD0 token contract address
     */
    constructor(address _usd0Token) public {
        require(_usd0Token != address(0), "USD0 token address cannot be zero");
        usd0Token = IERC20(_usd0Token);
    }

    /**
     * @dev Add collateral asset with risk parameters
     * @param collateralAsset Collateral asset address
     * @param _collateralFactor Collateral factor
     * @param _liquidationPenalty Liquidation penalty
     */
    function addCollateralAsset(address collateralAsset, uint256 _collateralFactor, uint256 _liquidationPenalty) public onlyOwner {
        require(collateralAsset != address(0), "Collateral asset address cannot be zero");
        require(_collateralFactor > 0 && _collateralFactor <= 1 ether, "Collateral factor must be between 0 and 1");
        require(_liquidationPenalty > 0 && _liquidationPenalty <= 1 ether, "Liquidation penalty must be between 0 and 1");

        collateralParams[collateralAsset] = RiskParams(_collateralFactor, _liquidationPenalty);
    }

    /**
     * @dev Deposit collateral asset
     * @param collateralAsset Collateral asset address
     * @param amount Amount to deposit
     */
    function depositCollateral(address collateralAsset, uint256 amount) public {
        require(collateralParams[collateralAsset].collateralFactor > 0, "Collateral asset not supported");
        require(amount > 0, "Deposit amount must be greater than zero");

        userCollateralBalances[msg.sender][collateralAsset] = userCollateralBalances[msg.sender][collateralAsset].add(amount);

        emit CollateralDeposited(msg.sender, collateralAsset, amount);
    }

    /**
     * @dev Withdraw collateral asset
     * @param collateralAsset Collateral asset address
     * @param amount Amount to withdraw
     */
    function withdrawCollateral(address collateralAsset, uint256 amount) public {
        require(userCollateralBalances[msg.sender][collateralAsset] >= amount, "Insufficient collateral balance");

        userCollateralBalances[msg.sender][collateralAsset] = userCollateralBalances[msg.sender][collateralAsset].sub(amount);

        emit CollateralWithdrawn(msg.sender, collateralAsset, amount);
    }

    /**
     * @dev Mint USD0
     * @param amount Amount to mint
     */
    function mintUsd0(uint256 amount) public {
        require(amount > 0, "Mint amount must be greater than zero");

        // Calculate collateral requirement
        uint256 collateralRequirement = amount.mul(1 ether).div(collateralParams[address(usd0Token)].collateralFactor);

        require(userCollateralBalances[msg.sender][address(usd0Token)] >= collateralRequirement, "Insufficient collateral balance");

        userDebtBalances[msg.sender] = userDebtBalances[msg.sender].add(amount);

        emit Usd0Minted(msg.sender, amount);
    }

    /**
     * @dev Burn USD0
     * @param amount Amount to burn
     */
    function burnUsd0(uint256 amount) public {
        require(userDebtBalances[msg.sender] >= amount, "Insufficient debt balance");

        userDebtBalances[msg.sender] = userDebtBalances[msg.sender].sub(amount);

        emit Usd0Burned(msg.sender, amount);
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        // Return the owner address (e.g. a multisig wallet)
        return 0x...;
    }
}
```
