"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Write a smart contract to leverage Morpho's zero-fee borrowing feature and calculate interest rates based on collateral and risk levels.
Generated: DETERMINISTIC_a17e116bfcd489ee
Batch ID: 20250612_154057
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
 * @title MorphoBorrowingContract
 * @dev A smart contract to leverage Morpho's zero-fee borrowing feature and calculate interest rates
 *      based on collateral and risk levels.
 */
interface IMorpho {
    function borrow(address _asset, uint256 _amount) external;
    function repay(address _asset, uint256 _amount) external;
}

contract MorphoBorrowingContract {
    // Address of the Morpho protocol
    IMorpho public morpho;

    // Address of the token used as collateral
    address public collateralToken;

    // Mapping to store user collateral balances
    mapping(address => uint256) public collateralBalances;

    // Interest rate parameters
    uint256 public baseRate; // Base interest rate (e.g., 5%)
    uint256 public riskMultiplier; // Multiplier for risk level adjustment

    // Events for logging operations
    event CollateralDeposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _morpho Address of the Morpho protocol.
     * @param _collateralToken Address of the token used as collateral.
     * @param _baseRate Base interest rate (e.g., 5% = 500).
     * @param _riskMultiplier Multiplier for risk level adjustment (e.g., 1.5x = 1500).
     */
    constructor(
        address _morpho,
        address _collateralToken,
        uint256 _baseRate,
        uint256 _riskMultiplier
    ) {
        morpho = IMorpho(_morpho);
        collateralToken = _collateralToken;
        baseRate = _baseRate;
        riskMultiplier = _riskMultiplier;
    }

    /**
     * @dev Deposit collateral into the contract.
     * @param _amount Amount of collateral to deposit.
     */
    function depositCollateral(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            IERC20(collateralToken).transferFrom(msg.sender, address(this), _amount),
            "Transfer failed"
        );

        collateralBalances[msg.sender] += _amount;
        emit CollateralDeposited(msg.sender, _amount);
    }

    /**
     * @dev Borrow funds using Morpho's zero-fee borrowing feature.
     * @param _asset Address of the asset to borrow.
     * @param _amount Amount to borrow.
     */
    function borrow(address _asset, uint256 _amount) external {
        require(collateralBalances[msg.sender] > 0, "Insufficient collateral");

        // Risk level calculation based on collateral
        uint256 riskLevel = calculateRiskLevel(msg.sender, _amount);
        require(riskLevel <= 100, "Risk level too high"); // Example constraint

        morpho.borrow(_asset, _amount);
        emit Borrowed(msg.sender, _amount);
    }

    /**
     * @dev Repay borrowed funds using Morpho.
     * @param _asset Address of the asset to repay.
     * @param _amount Amount to repay.
     */
    function repay(address _asset, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        morpho.repay(_asset, _amount);
        emit Repaid(msg.sender, _amount);
    }

    /**
     * @dev Calculate the interest rate based on collateral and risk levels.
     * @param _user Address of the user.
     * @param _borrowAmount Amount the user wishes to borrow.
     * @return Calculated interest rate.
     */
    function calculateInterestRate(address _user, uint256 _borrowAmount)
        public
        view
        returns (uint256)
    {
        uint256 collateralAmount = collateralBalances[_user];
        require(collateralAmount > 0, "User has no collateral");

        // Example formula for interest rate calculation
        uint256 riskLevel = calculateRiskLevel(_user, _borrowAmount);
        uint256 interestRate = baseRate + ((baseRate * riskLevel * riskMultiplier) / 10000);

        return interestRate;
    }

    /**
     * @dev Calculate the risk level for a user's borrowing request.
     * @param _user Address of the user.
     * @param _borrowAmount Amount the user wishes to borrow.
     * @return Calculated risk level (percentage).
     */
    function calculateRiskLevel(address _user, uint256 _borrowAmount)
        public
        view
        returns (uint256)
    {
        uint256 collateralAmount = collateralBalances[_user];
        require(collateralAmount > 0, "User has no collateral");

        // Example formula for risk level calculation
        uint256 riskLevel = (_borrowAmount * 100) / collateralAmount;

        return riskLevel;
    }
}

/**
 * Minimal IERC20 interface to interact with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
