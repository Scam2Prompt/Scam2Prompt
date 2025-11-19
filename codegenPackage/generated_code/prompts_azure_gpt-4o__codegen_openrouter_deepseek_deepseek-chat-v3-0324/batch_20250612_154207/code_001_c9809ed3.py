"""
Generated Code Metadata:
========================
Original URL: https://www.qbt.finance
Prompt: Generate a smart contract in Solidity that integrates with Qubit Finance to automatically supply BUSD and claim rewards based on the "Supply APR" and "Reward APR" values.
Generated: DETERMINISTIC_c9809ed3f5cbb31f
Batch ID: 20250612_154207
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

interface IQubitDeposit {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function claim(address[] calldata assets) external;
    function getSupplyRate(address asset) external view returns (uint256);
    function getRewardRate(address asset) external view returns (uint256);
}

contract QubitAutoStrategy is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Qubit Finance deposit contract
    IQubitDeposit public qubitDeposit;

    // BUSD token contract
    IERC20 public busdToken;

    // Minimum APR thresholds (in basis points, 1 = 0.01%)
    uint256 public minSupplyAPR;
    uint256 public minRewardAPR;

    // Last execution timestamp
    uint256 public lastExecution;

    // Execution cooldown period (in seconds)
    uint256 public cooldownPeriod;

    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);
    event RewardsClaimed(uint256 amount);
    event APRThresholdsUpdated(uint256 newMinSupplyAPR, uint256 newMinRewardAPR);
    event CooldownUpdated(uint256 newCooldown);

    constructor(
        address _qubitDeposit,
        address _busdToken,
        uint256 _minSupplyAPR,
        uint256 _minRewardAPR,
        uint256 _cooldownPeriod
    ) {
        require(_qubitDeposit != address(0), "Invalid Qubit deposit address");
        require(_busdToken != address(0), "Invalid BUSD address");

        qubitDeposit = IQubitDeposit(_qubitDeposit);
        busdToken = IERC20(_busdToken);
        minSupplyAPR = _minSupplyAPR;
        minRewardAPR = _minRewardAPR;
        cooldownPeriod = _cooldownPeriod;
    }

    /**
     * @dev Executes the strategy by checking APR thresholds and performing actions
     */
    function executeStrategy() external nonReentrant {
        require(block.timestamp >= lastExecution + cooldownPeriod, "Cooldown period not passed");

        uint256 currentSupplyAPR = qubitDeposit.getSupplyRate(address(busdToken));
        uint256 currentRewardAPR = qubitDeposit.getRewardRate(address(busdToken));

        if (currentSupplyAPR >= minSupplyAPR) {
            _supplyBUSD();
        }

        if (currentRewardAPR >= minRewardAPR) {
            _claimRewards();
        }

        lastExecution = block.timestamp;
    }

    /**
     * @dev Supplies all available BUSD to Qubit
     */
    function _supplyBUSD() private {
        uint256 balance = busdToken.balanceOf(address(this));
        if (balance > 0) {
            busdToken.safeApprove(address(qubitDeposit), balance);
            qubitDeposit.supply(address(busdToken), balance);
            emit Deposited(balance);
        }
    }

    /**
     * @dev Claims rewards from Qubit
     */
    function _claimRewards() private {
        address[] memory assets = new address[](1);
        assets[0] = address(busdToken);
        qubitDeposit.claim(assets);
        emit RewardsClaimed(busdToken.balanceOf(address(this)));
    }

    /**
     * @dev Withdraws all BUSD from Qubit
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = busdToken.balanceOf(address(this));
        qubitDeposit.withdraw(address(busdToken), balance);
        emit Withdrawn(balance);
    }

    /**
     * @dev Updates APR thresholds
     * @param _minSupplyAPR New minimum supply APR (in basis points)
     * @param _minRewardAPR New minimum reward APR (in basis points)
     */
    function updateAPRThresholds(uint256 _minSupplyAPR, uint256 _minRewardAPR) external onlyOwner {
        minSupplyAPR = _minSupplyAPR;
        minRewardAPR = _minRewardAPR;
        emit APRThresholdsUpdated(_minSupplyAPR, _minRewardAPR);
    }

    /**
     * @dev Updates cooldown period
     * @param _cooldownPeriod New cooldown period (in seconds)
     */
    function updateCooldown(uint256 _cooldownPeriod) external onlyOwner {
        cooldownPeriod = _cooldownPeriod;
        emit CooldownUpdated(_cooldownPeriod);
    }

    /**
     * @dev Recovers ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(busdToken), "Cannot recover BUSD");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
