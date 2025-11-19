"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Write a code snippet for a decentralized application that allows users to stake QI tokens and manage collateral for MAI issuance.
Generated: DETERMINISTIC_bf49b63286fecc68
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title QI Staking and MAI Collateral Manager
 * @author [Your Name]
 * @notice Allows users to stake QI tokens and manage collateral for MAI issuance
 */
contract QiStakingMaiCollateralManager is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user collateral balances
    mapping(address => uint256) public collateralBalances;

    // Mapping of user MAI issuance
    mapping(address => uint256) public maiIssuance;

    // QI token contract
    IERC20 public qiToken;

    // MAI token contract
    IERC20 public maiToken;

    // Collateralization ratio (e.g. 150% = 1.5)
    uint256 public collateralizationRatio;

    // Event emitted when user stakes QI tokens
    event StakedQi(address indexed user, uint256 amount);

    // Event emitted when user unstakes QI tokens
    event UnstakedQi(address indexed user, uint256 amount);

    // Event emitted when user adds collateral
    event AddedCollateral(address indexed user, uint256 amount);

    // Event emitted when user removes collateral
    event RemovedCollateral(address indexed user, uint256 amount);

    // Event emitted when MAI is issued
    event MaiIssued(address indexed user, uint256 amount);

    /**
     * @param _qiToken QI token contract address
     * @param _maiToken MAI token contract address
     * @param _collateralizationRatio Collateralization ratio (e.g. 150% = 1.5)
     */
    constructor(
        address _qiToken,
        address _maiToken,
        uint256 _collateralizationRatio
    ) public {
        require(_qiToken != address(0), "QI token address cannot be zero");
        require(_maiToken != address(0), "MAI token address cannot be zero");
        require(_collateralizationRatio > 0, "Collateralization ratio must be greater than 0");

        qiToken = IERC20(_qiToken);
        maiToken = IERC20(_maiToken);
        collateralizationRatio = _collateralizationRatio;
    }

    /**
     * @dev Stake QI tokens
     * @param amount Amount of QI tokens to stake
     */
    function stakeQi(uint256 amount) public {
        require(amount > 0, "Stake amount must be greater than 0");
        require(qiToken.transferFrom(msg.sender, address(this), amount), "QI token transfer failed");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        emit StakedQi(msg.sender, amount);
    }

    /**
     * @dev Unstake QI tokens
     * @param amount Amount of QI tokens to unstake
     */
    function unstakeQi(uint256 amount) public {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked QI tokens");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        require(qiToken.transfer(msg.sender, amount), "QI token transfer failed");

        emit UnstakedQi(msg.sender, amount);
    }

    /**
     * @dev Add collateral
     * @param amount Amount of collateral to add
     */
    function addCollateral(uint256 amount) public {
        require(amount > 0, "Collateral amount must be greater than 0");
        require(maiToken.transferFrom(msg.sender, address(this), amount), "MAI token transfer failed");

        collateralBalances[msg.sender] = collateralBalances[msg.sender].add(amount);

        emit AddedCollateral(msg.sender, amount);
    }

    /**
     * @dev Remove collateral
     * @param amount Amount of collateral to remove
     */
    function removeCollateral(uint256 amount) public {
        require(amount > 0, "Collateral amount must be greater than 0");
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral");

        collateralBalances[msg.sender] = collateralBalances[msg.sender].sub(amount);
        require(maiToken.transfer(msg.sender, amount), "MAI token transfer failed");

        emit RemovedCollateral(msg.sender, amount);
    }

    /**
     * @dev Issue MAI tokens
     * @param amount Amount of MAI tokens to issue
     */
    function issueMai(uint256 amount) public {
        require(amount > 0, "Issue amount must be greater than 0");
        require(collateralBalances[msg.sender] >= amount.mul(collateralizationRatio).div(100), "Insufficient collateral");

        maiIssuance[msg.sender] = maiIssuance[msg.sender].add(amount);
        require(maiToken.transfer(msg.sender, amount), "MAI token transfer failed");

        emit MaiIssued(msg.sender, amount);
    }

    /**
     * @dev Repay MAI tokens
     * @param amount Amount of MAI tokens to repay
     */
    function repayMai(uint256 amount) public {
        require(amount > 0, "Repay amount must be greater than 0");
        require(maiIssuance[msg.sender] >= amount, "Insufficient MAI issuance");

        maiIssuance[msg.sender] = maiIssuance[msg.sender].sub(amount);
        require(maiToken.transferFrom(msg.sender, address(this), amount), "MAI token transfer failed");

        emit MaiIssued(msg.sender, amount);
    }
}
```
