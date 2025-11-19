"""
Generated Code Metadata:
========================
Original URL: https://chaintether.web.app
Prompt: Generate a smart contract template for launching high-quality blockchain projects on a decentralized IDO platform like ChainTether.
Generated: DETERMINISTIC_fcc20de07104746b
Batch ID: 20250612_151659
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ChainTetherIDO
 * @dev A smart contract for decentralized IDO launches on ChainTether platform
 */
contract ChainTetherIDO is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token being sold
    IERC20 public token;

    // Token price in base currency (e.g., USDT)
    uint256 public tokenPrice;

    // Minimum and maximum investment amounts
    uint256 public minInvestment;
    uint256 public maxInvestment;

    // IDO start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Total tokens available for sale
    uint256 public totalTokensForSale;

    // Total tokens sold
    uint256 public totalTokensSold;

    // Base currency (e.g., USDT)
    IERC20 public baseCurrency;

    // Whitelist functionality
    mapping(address => bool) public whitelist;
    bool public whitelistEnabled;

    // Vesting parameters
    struct VestingSchedule {
        uint256 percentage;
        uint256 unlockTime;
    }
    VestingSchedule[] public vestingSchedules;

    // Investor tracking
    struct Investor {
        uint256 investedAmount;
        uint256 tokenAmount;
        uint256 claimedAmount;
        uint256 lastClaimTime;
    }
    mapping(address => Investor) public investors;

    // Events
    event TokensPurchased(address indexed investor, uint256 amount, uint256 tokenAmount);
    event TokensClaimed(address indexed investor, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    event VestingScheduleAdded(uint256 percentage, uint256 unlockTime);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _token Address of the token being sold
     * @param _tokenPrice Price of each token in base currency
     * @param _minInvestment Minimum investment amount
     * @param _maxInvestment Maximum investment amount
     * @param _startTime IDO start time
     * @param _endTime IDO end time
     * @param _totalTokensForSale Total tokens available for sale
     * @param _baseCurrency Address of the base currency (e.g., USDT)
     */
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _minInvestment,
        uint256 _maxInvestment,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _totalTokensForSale,
        address _baseCurrency
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_baseCurrency != address(0), "Base currency address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_minInvestment > 0, "Min investment must be greater than zero");
        require(_maxInvestment > _minInvestment, "Max investment must be greater than min");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        minInvestment = _minInvestment;
        maxInvestment = _maxInvestment;
        startTime = _startTime;
        endTime = _endTime;
        totalTokensForSale = _totalTokensForSale;
        baseCurrency = IERC20(_baseCurrency);
    }

    /**
     * @dev Modifier to check if IDO is active
     */
    modifier isIDOActive() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "IDO is not active");
        _;
    }

    /**
     * @dev Modifier to check if investor is whitelisted (if whitelist is enabled)
     */
    modifier isWhitelisted(address _investor) {
        require(!whitelistEnabled || whitelist[_investor], "Investor is not whitelisted");
        _;
    }

    /**
     * @dev Buy tokens during IDO
     * @param _amount Amount of base currency to invest
     */
    function buyTokens(uint256 _amount) external isIDOActive isWhitelisted(msg.sender) nonReentrant {
        require(_amount >= minInvestment, "Amount is below minimum investment");
        require(_amount <= maxInvestment, "Amount exceeds maximum investment");
        
        uint256 tokenAmount = _amount.mul(1e18).div(tokenPrice);
        require(totalTokensSold.add(tokenAmount) <= totalTokensForSale, "Not enough tokens left");

        // Transfer base currency from investor to contract
        require(baseCurrency.transferFrom(msg.sender, address(this), _amount), "Base currency transfer failed");

        // Update investor data
        Investor storage investor = investors[msg.sender];
        investor.investedAmount = investor.investedAmount.add(_amount);
        investor.tokenAmount = investor.tokenAmount.add(tokenAmount);
        investor.lastClaimTime = block.timestamp;

        // Update total tokens sold
        totalTokensSold = totalTokensSold.add(tokenAmount);

        emit TokensPurchased(msg.sender, _amount, tokenAmount);
    }

    /**
     * @dev Claim vested tokens
     */
    function claimTokens() external nonReentrant {
        require(vestingSchedules.length > 0, "No vesting schedule set");
        require(block.timestamp > endTime, "IDO has not ended yet");

        Investor storage investor = investors[msg.sender];
        require(investor.tokenAmount > 0, "No tokens to claim");

        uint256 claimableAmount = 0;
        uint256 lastClaimTime = investor.lastClaimTime;

        for (uint256 i = 0; i < vestingSchedules.length; i++) {
            VestingSchedule memory schedule = vestingSchedules[i];
            if (block.timestamp >= schedule.unlockTime && lastClaimTime < schedule.unlockTime) {
                claimableAmount = claimableAmount.add(
                    investor.tokenAmount.mul(schedule.percentage).div(100)
                );
            }
        }

        require(claimableAmount > 0, "No tokens available for claim at this time");

        investor.claimedAmount = investor.claimedAmount.add(claimableAmount);
        investor.lastClaimTime = block.timestamp;

        require(token.transfer(msg.sender, claimableAmount), "Token transfer failed");
        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Add a vesting schedule
     * @param _percentage Percentage of tokens to unlock
     * @param _unlockTime Timestamp when tokens unlock
     */
    function addVestingSchedule(uint256 _percentage, uint256 _unlockTime) external onlyOwner {
        require(_percentage > 0 && _percentage <= 100, "Invalid percentage");
        require(_unlockTime > endTime, "Unlock time must be after IDO ends");

        vestingSchedules.push(VestingSchedule({
            percentage: _percentage,
            unlockTime: _unlockTime
        }));

        emit VestingScheduleAdded(_percentage, _unlockTime);
    }

    /**
     * @dev Toggle whitelist status
     */
    function toggleWhitelist() external onlyOwner {
        whitelistEnabled = !whitelistEnabled;
    }

    /**
     * @dev Add/remove addresses from whitelist
     * @param _accounts Array of addresses to update
     * @param _status New whitelist status
     */
    function updateWhitelist(address[] calldata _accounts, bool _status) external onlyOwner {
        for (uint256 i = 0; i < _accounts.length; i++) {
            whitelist[_accounts[i]] = _status;
            emit WhitelistUpdated(_accounts[i], _status);
        }
    }

    /**
     * @dev Withdraw raised funds
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > endTime, "IDO has not ended yet");
        
        uint256 balance = baseCurrency.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");

        require(baseCurrency.transfer(owner(), balance), "Withdrawal failed");
        emit FundsWithdrawn(owner(), balance);
    }

    /**
     * @dev Emergency withdraw remaining tokens after IDO ends
     */
    function emergencyWithdrawTokens() external onlyOwner {
        require(block.timestamp > endTime, "IDO has not ended yet");
        
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(token.transfer(owner(), balance), "Token withdrawal failed");
