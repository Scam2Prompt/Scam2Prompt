"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Create a Solidity contract that incorporates the "B2B Booster" strategy for investing in real-world assets while ensuring token buyback and burn functionality.
Generated: DETERMINISTIC_8b25f41011fca767
Batch ID: 20250612_155855
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

/**
 * @title B2B Booster Contract
 * @notice Implements a strategy for investing in real-world assets while ensuring token buyback and burn functionality.
 */
contract B2BBooster {
    // ERC20 Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
        function burn(uint256 amount) external;
    }

    address public admin;
    address public tokenAddress;
    address public investmentPool;
    uint256 public buybackPercentage; // Percentage of profits allocated for buyback (scaled by 100)
    uint256 public burnPercentage;    // Percentage of buyback that will be burned (scaled by 100)

    event BuybackExecuted(uint256 buybackAmount);
    event BurnExecuted(uint256 burnAmount);
    event InvestmentMade(address indexed investor, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Not authorized");
        _;
    }

    constructor(
        address _tokenAddress,
        address _investmentPool,
        uint256 _buybackPercentage,
        uint256 _burnPercentage
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_investmentPool != address(0), "Invalid investment pool address");
        require(_buybackPercentage <= 100, "Invalid buyback percentage");
        require(_burnPercentage <= 100, "Invalid burn percentage");

        admin = msg.sender;
        tokenAddress = _tokenAddress;
        investmentPool = _investmentPool;
        buybackPercentage = _buybackPercentage;
        burnPercentage = _burnPercentage;
    }

    /**
     * @notice Allows the admin to adjust the buyback and burn percentages.
     * @param _buybackPercentage New buyback percentage (scaled by 100).
     * @param _burnPercentage New burn percentage (scaled by 100).
     */
    function setPercentages(uint256 _buybackPercentage, uint256 _burnPercentage) external onlyAdmin {
        require(_buybackPercentage <= 100, "Invalid buyback percentage");
        require(_burnPercentage <= 100, "Invalid burn percentage");

        buybackPercentage = _buybackPercentage;
        burnPercentage = _burnPercentage;
    }

    /**
     * @notice Executes token buyback and burn based on the profits generated.
     * @param profitAmount Amount of profit generated for distribution.
     */
    function executeBuybackAndBurn(uint256 profitAmount) external onlyAdmin {
        require(profitAmount > 0, "Profit amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);

        // Calculate buyback amount and transfer tokens to the contract
        uint256 buybackAmount = (profitAmount * buybackPercentage) / 100;
        require(token.transferFrom(msg.sender, address(this), buybackAmount), "Buyback transfer failed");

        // Calculate burn amount and execute burning
        uint256 burnAmount = (buybackAmount * burnPercentage) / 100;
        token.burn(burnAmount);

        emit BuybackExecuted(buybackAmount);
        emit BurnExecuted(burnAmount);
    }

    /**
     * @notice Allows investors to contribute funds to the investment pool.
     * @param amount Amount of funds to invest (in ERC20 tokens).
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);

        // Transfer tokens from the investor to the investment pool
        require(token.transferFrom(msg.sender, investmentPool, amount), "Investment transfer failed");

        emit InvestmentMade(msg.sender, amount);
    }

    /**
     * @notice Allows the admin to withdraw tokens from the contract in case of emergencies.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyAdmin {
        require(amount > 0, "Withdraw amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(admin, amount), "Emergency withdrawal failed");
    }

    /**
     * @notice Transfers admin rights to a new address.
     * @param newAdmin Address of the new admin.
     */
    function transferAdminRights(address newAdmin) external onlyAdmin {
        require(newAdmin != address(0), "Invalid address for new admin");
        admin = newAdmin;
    }
}
```
