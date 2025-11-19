"""
Generated Code Metadata:
========================
Original URL: https://welstrade.com
Prompt: Generate a smart contract code for a blockchain-based investment fund similar to Welstrade's Cryptoassets Hedge Funds.
Generated: DETERMINISTIC_b02c3fc043f65278
Batch ID: 20250622_212034
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CryptoAssetInvestmentFund
 * @dev A blockchain-based investment fund contract similar to Welstrade's Cryptoassets Hedge Funds
 */
contract CryptoAssetInvestmentFund is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Fund details
    string public fundName;
    uint256 public fundCreationDate;
    uint256 public managementFee; // Annual management fee in basis points (1% = 100 bps)
    uint256 public performanceFee; // Performance fee in basis points (20% = 2000 bps)
    uint256 public highWaterMark; // Highest NAV per share achieved
    uint256 public totalShares;
    uint256 public totalAssetsUnderManagement;

    // Token address accepted for investments
    IERC20 public investmentToken;

    // Investor information
    struct Investor {
        uint256 shares;
        uint256 lastInvestmentDate;
        uint256 lastNavPerShare;
    }

    mapping(address => Investor) public investors;

    // Events
    event InvestmentMade(address indexed investor, uint256 amount, uint256 shares);
    event WithdrawalMade(address indexed investor, uint256 amount, uint256 shares);
    event FeesCollected(uint256 managementFeeAmount, uint256 performanceFeeAmount);
    event FundRevalued(uint256 newNavPerShare);

    /**
     * @dev Constructor to initialize the fund
     * @param _fundName Name of the fund
     * @param _investmentToken Address of the ERC20 token accepted for investments
     * @param _managementFee Annual management fee in basis points
     * @param _performanceFee Performance fee in basis points
     */
    constructor(
        string memory _fundName,
        address _investmentToken,
        uint256 _managementFee,
        uint256 _performanceFee
    ) {
        require(_investmentToken != address(0), "Invalid token address");
        require(_managementFee <= 500, "Management fee too high"); // Max 5%
        require(_performanceFee <= 3000, "Performance fee too high"); // Max 30%

        fundName = _fundName;
        investmentToken = IERC20(_investmentToken);
        managementFee = _managementFee;
        performanceFee = _performanceFee;
        fundCreationDate = block.timestamp;
        highWaterMark = 1e18; // Initial NAV per share is 1.0
    }

    /**
     * @dev Invest in the fund
     * @param amount Amount of tokens to invest
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount > 0, "Investment amount must be positive");
        
        // Calculate NAV per share
        uint256 navPerShare = calculateNavPerShare();
        
        // Transfer tokens from investor
        require(
            investmentToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Calculate shares to issue
        uint256 shares = amount.mul(1e18).div(navPerShare);
        
        // Update investor's position
        investors[msg.sender].shares = investors[msg.sender].shares.add(shares);
        investors[msg.sender].lastInvestmentDate = block.timestamp;
        investors[msg.sender].lastNavPerShare = navPerShare;
        
        // Update fund totals
        totalShares = totalShares.add(shares);
        totalAssetsUnderManagement = totalAssetsUnderManagement.add(amount);
        
        emit InvestmentMade(msg.sender, amount, shares);
    }

    /**
     * @dev Withdraw from the fund
     * @param shares Amount of shares to redeem
     */
    function withdraw(uint256 shares) external nonReentrant {
        require(shares > 0, "Withdrawal amount must be positive");
        require(investors[msg.sender].shares >= shares, "Insufficient shares");
        
        // Calculate NAV per share
        uint256 navPerShare = calculateNavPerShare();
        
        // Calculate withdrawal amount
        uint256 withdrawalAmount = shares.mul(navPerShare).div(1e18);
        
        // Apply fees if applicable
        uint256 feeAmount = calculateFees(msg.sender, shares, navPerShare);
        if (feeAmount > 0) {
            withdrawalAmount = withdrawalAmount.sub(feeAmount);
            require(
                investmentToken.transfer(owner(), feeAmount),
                "Fee transfer failed"
            );
        }
        
        // Update investor's position
        investors[msg.sender].shares = investors[msg.sender].shares.sub(shares);
        investors[msg.sender].lastNavPerShare = navPerShare;
        
        // Update fund totals
        totalShares = totalShares.sub(shares);
        totalAssetsUnderManagement = totalAssetsUnderManagement.sub(withdrawalAmount.add(feeAmount));
        
        // Transfer funds to investor
        require(
            investmentToken.transfer(msg.sender, withdrawalAmount),
            "Withdrawal transfer failed"
        );
        
        emit WithdrawalMade(msg.sender, withdrawalAmount, shares);
    }

    /**
     * @dev Calculate NAV per share
     * @return NAV per share in token units
     */
    function calculateNavPerShare() public view returns (uint256) {
        if (totalShares == 0) {
            return 1e18; // Initial NAV per share
        }
        return totalAssetsUnderManagement.mul(1e18).div(totalShares);
    }

    /**
     * @dev Calculate fees for withdrawal
     * @param investor Address of the investor
     * @param shares Shares being withdrawn
     * @param currentNav Current NAV per share
     * @return Total fees to be charged
     */
    function calculateFees(address investor, uint256 shares, uint256 currentNav) internal returns (uint256) {
        Investor storage inv = investors[investor];
        
        // Management fee (pro-rated for time held)
        uint256 timeHeld = block.timestamp.sub(inv.lastInvestmentDate);
        uint256 managementFeeAmount = shares.mul(inv.lastNavPerShare)
            .mul(managementFee).mul(timeHeld)
            .div(365 days).div(10000);
        
        // Performance fee (only if above high water mark)
        uint256 performanceFeeAmount = 0;
        if (currentNav > highWaterMark) {
            uint256 profit = shares.mul(currentNav.sub(highWaterMark)).div(1e18);
            performanceFeeAmount = profit.mul(performanceFee).div(10000);
            highWaterMark = currentNav;
        }
        
        uint256 totalFees = managementFeeAmount.add(performanceFeeAmount);
        
        if (totalFees > 0) {
            emit FeesCollected(managementFeeAmount, performanceFeeAmount);
        }
        
        return totalFees;
    }

    /**
     * @dev Update fund's AUM (for external price feeds or oracle updates)
     * @param newAum New total assets under management
     */
    function updateAum(uint256 newAum) external onlyOwner {
        require(newAum > 0, "AUM must be positive");
        totalAssetsUnderManagement = newAum;
        uint256 newNav = calculateNavPerShare();
        emit FundRevalued(newNav);
    }
}
```
