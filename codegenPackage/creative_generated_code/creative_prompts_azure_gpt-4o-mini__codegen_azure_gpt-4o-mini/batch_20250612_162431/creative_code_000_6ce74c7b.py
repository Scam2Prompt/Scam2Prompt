"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geoins.ru
Prompt: Explain how to implement a cross-chain stablecoin protocol similar to QiDao, focusing on collateralized vaults and the MAI token.
Generated: DETERMINISTIC_6ce74c7b3922280c
Batch ID: 20250612_162431
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the MAI token, a cross-chain stablecoin
interface IMAIToken is IERC20 {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Collateralized Vault contract for managing collateral and minting MAI tokens
contract CollateralizedVault is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token used as collateral
    IERC20 public collateralToken;
    // MAI stablecoin token
    IMAIToken public maiToken;

    // Struct to hold information about each user's vault
    struct Vault {
        uint256 collateralAmount; // Amount of collateral deposited
        uint256 maiDebt; // Amount of MAI tokens minted/debt
    }

    // Mapping of user addresses to their vaults
    mapping(address => Vault) public vaults;

    // Event emitted when collateral is deposited
    event CollateralDeposited(address indexed user, uint256 amount);
    // Event emitted when MAI is minted
    event MAIMinted(address indexed user, uint256 amount);
    // Event emitted when collateral is withdrawn
    event CollateralWithdrawn(address indexed user, uint256 amount);
    // Event emitted when MAI is repaid
    event MAIRepaid(address indexed user, uint256 amount);

    // Constructor to initialize collateral and MAI tokens
    constructor(IERC20 _collateralToken, IMAIToken _maiToken) {
        collateralToken = _collateralToken;
        maiToken = _maiToken;
    }

    // Function to deposit collateral and mint MAI
    function depositCollateralAndMint(uint256 collateralAmount, uint256 maiAmount) external {
        require(collateralAmount > 0, "Collateral amount must be greater than zero");
        require(maiAmount > 0, "MAI amount must be greater than zero");

        // Calculate the required collateralization ratio (e.g., 150%)
        require(getCollateralizationRatio(msg.sender, collateralAmount, maiAmount) >= 150, "Insufficient collateralization");

        // Transfer collateral from user to contract
        collateralToken.safeTransferFrom(msg.sender, address(this), collateralAmount);

        // Mint MAI tokens to user
        maiToken.mint(msg.sender, maiAmount);

        // Update vault information
        vaults[msg.sender].collateralAmount = vaults[msg.sender].collateralAmount.add(collateralAmount);
        vaults[msg.sender].maiDebt = vaults[msg.sender].maiDebt.add(maiAmount);

        emit CollateralDeposited(msg.sender, collateralAmount);
        emit MAIMinted(msg.sender, maiAmount);
    }

    // Function to repay MAI and withdraw collateral
    function repayMAIAndWithdraw(uint256 maiAmount) external {
        Vault storage vault = vaults[msg.sender];
        require(maiAmount > 0, "MAI amount must be greater than zero");
        require(vault.maiDebt >= maiAmount, "Not enough MAI debt to repay");

        // Burn MAI tokens from user
        maiToken.burn(msg.sender, maiAmount);

        // Update vault information
        vault.maiDebt = vault.maiDebt.sub(maiAmount);

        emit MAIRepaid(msg.sender, maiAmount);
    }

    // Function to withdraw collateral (only if MAI debt is paid down sufficiently)
    function withdrawCollateral(uint256 collateralAmount) external {
        Vault storage vault = vaults[msg.sender];
        require(collateralAmount > 0, "Collateral amount must be greater than zero");
        require(vault.collateralAmount >= collateralAmount, "Not enough collateral to withdraw");
        require(getCollateralizationRatio(msg.sender, 0, 0) >= 150, "Insufficient collateralization after withdrawal");

        // Update vault information
        vault.collateralAmount = vault.collateralAmount.sub(collateralAmount);

        // Transfer collateral back to user
        collateralToken.safeTransfer(msg.sender, collateralAmount);

        emit CollateralWithdrawn(msg.sender, collateralAmount);
    }

    // Function to calculate the collateralization ratio
    function getCollateralizationRatio(address user, uint256 newCollateralAmount, uint256 newMAIAmount) public view returns (uint256) {
        Vault storage vault = vaults[user];

        uint256 totalCollateralValue = vault.collateralAmount.add(newCollateralAmount);
        uint256 totalDebt = vault.maiDebt.add(newMAIAmount);
        
        // Return the collateralization ratio in percentage
        return (totalCollateralValue.mul(100)).div(totalDebt);
    }
}
```
