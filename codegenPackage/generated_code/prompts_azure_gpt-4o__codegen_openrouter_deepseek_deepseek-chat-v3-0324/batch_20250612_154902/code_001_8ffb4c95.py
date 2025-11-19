"""
Generated Code Metadata:
========================
Original URL: https://mixer-novostei.ru
Prompt: Generate Solidity code for a smart contract that mimics Ribbon Finance's automated covered call strategy, ensuring risk minimization and passive income generation.
Generated: DETERMINISTIC_8ffb4c950b231253
Batch ID: 20250612_154902
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Automated Covered Call Strategy
 * @dev Mimics Ribbon Finance's automated covered call strategy
 */
contract CoveredCallStrategy is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store option details
    struct Option {
        uint256 strikePrice;
        uint256 expiry;
        uint256 premium;
        bool isSold;
    }

    // Asset token (e.g., WBTC, WETH)
    IERC20 public assetToken;
    // Stablecoin token (e.g., USDC)
    IERC20 public stablecoinToken;

    // Mapping from epoch to Option
    mapping(uint256 => Option) public options;
    // Current epoch
    uint256 public currentEpoch;
    // Minimum strike price percentage (e.g., 105% for 5% above current price)
    uint256 public minStrikePercentage;
    // Minimum premium percentage
    uint256 public minPremiumPercentage;
    // Option duration in seconds (e.g., 1 week)
    uint256 public optionDuration;

    // Events
    event OptionSold(uint256 indexed epoch, uint256 strikePrice, uint256 premium, uint256 expiry);
    event OptionExercised(uint256 indexed epoch, uint256 amount);
    event OptionExpired(uint256 indexed epoch);
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _assetToken Address of the asset token
     * @param _stablecoinToken Address of the stablecoin token
     * @param _minStrikePercentage Minimum strike price percentage (e.g., 10500 for 105%)
     * @param _minPremiumPercentage Minimum premium percentage (e.g., 200 for 2%)
     * @param _optionDuration Option duration in seconds
     */
    constructor(
        address _assetToken,
        address _stablecoinToken,
        uint256 _minStrikePercentage,
        uint256 _minPremiumPercentage,
        uint256 _optionDuration
    ) {
        require(_assetToken != address(0), "Invalid asset token");
        require(_stablecoinToken != address(0), "Invalid stablecoin token");
        require(_minStrikePercentage >= 10000, "Strike must be >= 100%");
        require(_minPremiumPercentage > 0, "Premium must be > 0");
        require(_optionDuration > 0, "Duration must be > 0");

        assetToken = IERC20(_assetToken);
        stablecoinToken = IERC20(_stablecoinToken);
        minStrikePercentage = _minStrikePercentage;
        minPremiumPercentage = _minPremiumPercentage;
        optionDuration = _optionDuration;
        currentEpoch = 1;
    }

    /**
     * @dev Deposit assets into the strategy
     * @param amount Amount of assets to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        
        assetToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw assets from the strategy
     * @param amount Amount of assets to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(assetToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        assetToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Sell covered call options (only owner)
     * @param strikePrice Strike price of the option
     * @param premium Premium received for the option
     */
    function sellOption(uint256 strikePrice, uint256 premium) external onlyOwner {
        require(strikePrice >= (assetToken.balanceOf(address(this)) * minStrikePercentage) / 10000, "Strike too low");
        require(premium >= (assetToken.balanceOf(address(this)) * minPremiumPercentage) / 10000, "Premium too low");
        require(!options[currentEpoch].isSold, "Option already sold");

        options[currentEpoch] = Option({
            strikePrice: strikePrice,
            expiry: block.timestamp + optionDuration,
            premium: premium,
            isSold: true
        });

        stablecoinToken.safeTransferFrom(msg.sender, address(this), premium);
        emit OptionSold(currentEpoch, strikePrice, premium, options[currentEpoch].expiry);
    }

    /**
     * @dev Exercise the option if conditions are met
     * @param epoch Epoch of the option to exercise
     */
    function exerciseOption(uint256 epoch) external nonReentrant {
        Option storage option = options[epoch];
        require(option.isSold, "Option not sold");
        require(block.timestamp <= option.expiry, "Option expired");
        
        uint256 assetBalance = assetToken.balanceOf(address(this));
        require(assetBalance > 0, "No assets to exercise");

        stablecoinToken.safeTransfer(msg.sender, option.strikePrice * assetBalance / 1e18);
        assetToken.safeTransfer(msg.sender, assetBalance);

        option.isSold = false;
        emit OptionExercised(epoch, assetBalance);
    }

    /**
     * @dev Handle expired options
     * @param epoch Epoch of the expired option
     */
    function handleExpiredOption(uint256 epoch) external nonReentrant {
        Option storage option = options[epoch];
        require(option.isSold, "Option not sold");
        require(block.timestamp > option.expiry, "Option not expired");

        option.isSold = false;
        currentEpoch++;
        emit OptionExpired(epoch);
    }

    /**
     * @dev Update strategy parameters (only owner)
     * @param _minStrikePercentage New minimum strike percentage
     * @param _minPremiumPercentage New minimum premium percentage
     * @param _optionDuration New option duration
     */
    function updateParameters(
        uint256 _minStrikePercentage,
        uint256 _minPremiumPercentage,
        uint256 _optionDuration
    ) external onlyOwner {
        require(_minStrikePercentage >= 10000, "Strike must be >= 100%");
        require(_minPremiumPercentage > 0, "Premium must be > 0");
        require(_optionDuration > 0, "Duration must be > 0");

        minStrikePercentage = _minStrikePercentage;
        minPremiumPercentage = _minPremiumPercentage;
        optionDuration = _optionDuration;
    }

    /**
     * @dev Emergency withdraw all assets (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 assetBalance = assetToken.balanceOf(address(this));
        uint256 stablecoinBalance = stablecoinToken.balanceOf(address(this));

        if (assetBalance > 0) {
            assetToken.safeTransfer(owner(), assetBalance);
        }
        if (stablecoinBalance > 0) {
            stablecoinToken.safeTransfer(owner(), stablecoinBalance);
        }
    }
}
```
