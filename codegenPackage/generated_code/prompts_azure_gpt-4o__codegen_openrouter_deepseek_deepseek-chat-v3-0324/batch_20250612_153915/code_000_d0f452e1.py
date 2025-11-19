"""
Generated Code Metadata:
========================
Original URL: https://spark.fiddler-pkg.com
Prompt: Write a Solidity smart contract that integrates with Spark's Savings USDS protocol to deposit stablecoins and withdraw rewards in USDC, USDS, or DAI. Ensure the contract includes functionality to track savings rates determined by Sky governance.
Generated: DETERMINISTIC_d0f452e1de9be628
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ISparkSavings {
    function deposit(uint256 assets, address receiver) external returns (uint256);
    function withdraw(uint256 assets, address receiver, address owner) external returns (uint256);
    function convertToAssets(uint256 shares) external view returns (uint256);
    function convertToShares(uint256 assets) external view returns (uint256);
    function totalAssets() external view returns (uint256);
    function getRewards() external view returns (uint256);
}

contract SparkSavingsIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Supported stablecoins
    IERC20 public immutable usdc;
    IERC20 public immutable usds;
    IERC20 public immutable dai;
    
    // Spark Savings protocol
    ISparkSavings public immutable sparkSavings;
    
    // Governance address for savings rate updates
    address public governance;
    
    // Current savings rate (in basis points, e.g. 500 = 5%)
    uint256 public savingsRateBps;
    
    // Track user deposits
    mapping(address => uint256) public userShares;
    
    // Events
    event Deposited(address indexed user, address indexed token, uint256 amount, uint256 shares);
    event Withdrawn(address indexed user, address indexed token, uint256 amount, uint256 shares);
    event SavingsRateUpdated(uint256 newRateBps);
    event GovernanceUpdated(address newGovernance);
    
    constructor(
        address _usdc,
        address _usds,
        address _dai,
        address _sparkSavings,
        address _governance,
        uint256 _initialSavingsRateBps
    ) {
        require(_usdc != address(0), "Invalid USDC address");
        require(_usds != address(0), "Invalid USDS address");
        require(_dai != address(0), "Invalid DAI address");
        require(_sparkSavings != address(0), "Invalid Spark Savings address");
        require(_governance != address(0), "Invalid governance address");
        
        usdc = IERC20(_usdc);
        usds = IERC20(_usds);
        dai = IERC20(_dai);
        sparkSavings = ISparkSavings(_sparkSavings);
        governance = _governance;
        savingsRateBps = _initialSavingsRateBps;
    }
    
    /**
     * @dev Deposit stablecoins into Spark Savings
     * @param token Address of the stablecoin to deposit (USDC, USDS, or DAI)
     * @param amount Amount of tokens to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(
            token == address(usdc) || token == address(usds) || token == address(dai),
            "Unsupported token"
        );
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        IERC20(token).safeApprove(address(sparkSavings), amount);
        
        uint256 shares = sparkSavings.deposit(amount, address(this));
        userShares[msg.sender] += shares;
        
        emit Deposited(msg.sender, token, amount, shares);
    }
    
    /**
     * @dev Withdraw from Spark Savings in specified token
     * @param token Address of the stablecoin to withdraw (USDC, USDS, or DAI)
     * @param shares Amount of shares to withdraw
     */
    function withdraw(address token, uint256 shares) external nonReentrant {
        require(
            token == address(usdc) || token == address(usds) || token == address(dai),
            "Unsupported token"
        );
        require(shares > 0, "Shares must be greater than 0");
        require(userShares[msg.sender] >= shares, "Insufficient shares");
        
        userShares[msg.sender] -= shares;
        
        uint256 amount = sparkSavings.withdraw(shares, address(this), address(this));
        IERC20(token).safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, token, amount, shares);
    }
    
    /**
     * @dev Get estimated assets for given shares
     * @param shares Amount of shares to convert
     * @return Estimated asset amount
     */
    function getEstimatedAssets(uint256 shares) external view returns (uint256) {
        return sparkSavings.convertToAssets(shares);
    }
    
    /**
     * @dev Get estimated shares for given assets
     * @param assets Amount of assets to convert
     * @return Estimated share amount
     */
    function getEstimatedShares(uint256 assets) external view returns (uint256) {
        return sparkSavings.convertToShares(assets);
    }
    
    /**
     * @dev Get current rewards available
     * @return Current rewards amount
     */
    function getCurrentRewards() external view returns (uint256) {
        return sparkSavings.getRewards();
    }
    
    /**
     * @dev Update savings rate (only callable by governance)
     * @param newRateBps New savings rate in basis points
     */
    function updateSavingsRate(uint256 newRateBps) external {
        require(msg.sender == governance, "Only governance can update rate");
        require(newRateBps <= 10000, "Rate cannot exceed 100%");
        
        savingsRateBps = newRateBps;
        emit SavingsRateUpdated(newRateBps);
    }
    
    /**
     * @dev Update governance address (only callable by owner)
     * @param newGovernance New governance address
     */
    function updateGovernance(address newGovernance) external onlyOwner {
        require(newGovernance != address(0), "Invalid governance address");
        governance = newGovernance;
        emit GovernanceUpdated(newGovernance);
    }
    
    /**
     * @dev Emergency withdraw all funds (only callable by owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 totalAssets = sparkSavings.totalAssets();
        if (totalAssets > 0) {
            sparkSavings.withdraw(totalAssets, address(this), address(this));
        }
        
        uint256 usdcBalance = usdc.balanceOf(address(this));
        if (usdcBalance > 0) {
            usdc.safeTransfer(owner(), usdcBalance);
        }
        
        uint256 usdsBalance = usds.balanceOf(address(this));
        if (usdsBalance > 0) {
            usds.safeTransfer(owner(), usdsBalance);
        }
        
        uint256 daiBalance = dai.balanceOf(address(this));
        if (daiBalance > 0) {
            dai.safeTransfer(owner(), daiBalance);
        }
    }
}
```
