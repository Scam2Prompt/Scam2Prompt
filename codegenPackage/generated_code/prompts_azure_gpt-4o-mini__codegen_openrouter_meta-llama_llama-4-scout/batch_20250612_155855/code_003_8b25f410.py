"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity contract that incorporates the "B2B Booster" strategy for investing in real-world assets while ensuring token buyback and burn functionality.
Generated: DETERMINISTIC_8b25f41011fca767
Batch ID: 20250612_155855
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title B2BBoosterContract
 * @author [Your Name]
 * @notice B2B Booster strategy contract for investing in real-world assets,
 *         token buyback, and burn functionality.
 */
contract B2BBoosterContract is ReentrancyGuard, ERC20Burnable {
    using SafeMath for uint256;

    // Mapping of investors and their investment amounts
    mapping(address => uint256) public investorBalances;

    // Mapping of asset investments
    mapping(address => uint256) public assetInvestments;

    // Token buyback and burn variables
    uint256 public buybackThreshold;
    uint256 public burnPercentage;

    // Real-world asset address
    address public assetAddress;

    // Investment manager role
    address public investmentManager;

    /**
     * @dev Event emitted when an investment is made
     * @param investor Address of the investor
     * @param amount Investment amount
     */
    event InvestmentMade(address indexed investor, uint256 amount);

    /**
     * @dev Event emitted when an asset investment is made
     * @param asset Address of the asset
     * @param amount Investment amount
     */
    event AssetInvestmentMade(address indexed asset, uint256 amount);

    /**
     * @dev Event emitted when tokens are bought back and burned
     * @param amount Tokens bought back and burned
     */
    event TokensBoughtBackAndBurned(uint256 amount);

    /**
     * @dev Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param _assetAddress Real-world asset address
     * @param _investmentManager Investment manager role
     * @param _buybackThreshold Token buyback threshold
     * @param _burnPercentage Token burn percentage
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _assetAddress,
        address _investmentManager,
        uint256 _buybackThreshold,
        uint256 _burnPercentage
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        assetAddress = _assetAddress;
        investmentManager = _investmentManager;
        buybackThreshold = _buybackThreshold;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Modifier to restrict access to the investment manager
     */
    modifier onlyInvestmentManager() {
        require(msg.sender == investmentManager, "Only the investment manager can perform this action");
        _;
    }

    /**
     * @dev Function to make an investment
     * @param amount Investment amount
     */
    function makeInvestment(uint256 amount) external nonReentrant {
        require(amount > 0, "Investment amount must be greater than zero");
        investorBalances[msg.sender] = investorBalances[msg.sender].add(amount);
        emit InvestmentMade(msg.sender, amount);
    }

    /**
     * @dev Function to make an asset investment
     * @param amount Investment amount
     */
    function makeAssetInvestment(uint256 amount) external onlyInvestmentManager nonReentrant {
        require(amount > 0, "Investment amount must be greater than zero");
        assetInvestments[assetAddress] = assetInvestments[assetAddress].add(amount);
        emit AssetInvestmentMade(assetAddress, amount);
    }

    /**
     * @dev Function to buy back and burn tokens
     */
    function buyBackAndBurnTokens() external nonReentrant {
        uint256 tokenBalance = balanceOf(address(this));
        require(tokenBalance >= buybackThreshold, "Token balance must be greater than or equal to the buyback threshold");
        uint256 burnAmount = tokenBalance.mul(burnPercentage).div(100);
        _burn(address(this), burnAmount);
        emit TokensBoughtBackAndBurned(burnAmount);
    }

    /**
     * @dev Function to withdraw investment
     * @param amount Withdrawal amount
     */
    function withdrawInvestment(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(investorBalances[msg.sender] >= amount, "Insufficient investment balance");
        investorBalances[msg.sender] = investorBalances[msg.sender].sub(amount);
        payable(msg.sender).transfer(amount);
    }
}
```
