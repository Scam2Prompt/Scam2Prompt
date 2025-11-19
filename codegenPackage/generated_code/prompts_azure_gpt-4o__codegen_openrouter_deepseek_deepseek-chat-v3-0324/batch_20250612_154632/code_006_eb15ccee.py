"""
Generated Code Metadata:
========================
Original URL: https://levei.money
Prompt: Provide code examples for integrating lvlUSD into a lending protocol to earn yield while maintaining dollar peg stability.
Generated: DETERMINISTIC_eb15cceeb0f2d2c9
Batch ID: 20250612_154632
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

interface ILvlUSD {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

interface ILendingProtocol {
    function deposit(address token, uint256 amount) external returns (uint256);
    function withdraw(address token, uint256 amount) external returns (uint256);
    function getYield(address token) external view returns (uint256);
}

contract LvlUSDIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    ILvlUSD public immutable lvlUSD;
    IERC20 public immutable stablecoin;
    ILendingProtocol public lendingProtocol;

    uint256 public totalDeposits;
    uint256 public yieldEarned;
    uint256 public lastYieldUpdate;

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event YieldClaimed(address indexed user, uint256 amount);
    event LendingProtocolUpdated(address newProtocol);

    constructor(
        address _lvlUSD,
        address _stablecoin,
        address _lendingProtocol
    ) {
        require(_lvlUSD != address(0), "Invalid lvlUSD address");
        require(_stablecoin != address(0), "Invalid stablecoin address");
        require(_lendingProtocol != address(0), "Invalid lending protocol address");

        lvlUSD = ILvlUSD(_lvlUSD);
        stablecoin = IERC20(_stablecoin);
        lendingProtocol = ILendingProtocol(_lendingProtocol);
        lastYieldUpdate = block.timestamp;
    }

    /**
     * @notice Deposit stablecoin and mint lvlUSD
     * @param amount Amount of stablecoin to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer stablecoin from user
        stablecoin.safeTransferFrom(msg.sender, address(this), amount);

        // Deposit into lending protocol
        stablecoin.safeApprove(address(lendingProtocol), amount);
        uint256 shares = lendingProtocol.deposit(address(stablecoin), amount);

        // Mint lvlUSD to user
        lvlUSD.mint(msg.sender, amount);

        totalDeposits += amount;
        emit Deposited(msg.sender, amount);
    }

    /**
     * @notice Withdraw stablecoin by burning lvlUSD
     * @param amount Amount of lvlUSD to burn
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lvlUSD.balanceOf(msg.sender) >= amount, "Insufficient lvlUSD balance");

        // Calculate share of total deposits
        uint256 share = (amount * totalDeposits) / lvlUSD.totalSupply();

        // Withdraw from lending protocol
        uint256 withdrawn = lendingProtocol.withdraw(address(stablecoin), share);

        // Burn lvlUSD from user
        lvlUSD.burn(msg.sender, amount);

        // Transfer stablecoin to user
        stablecoin.safeTransfer(msg.sender, withdrawn);

        totalDeposits -= share;
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim yield earned from lending protocol
     */
    function claimYield() external nonReentrant onlyOwner {
        _updateYield();
        uint256 availableYield = yieldEarned;
        require(availableYield > 0, "No yield to claim");

        // Withdraw yield from lending protocol
        uint256 withdrawn = lendingProtocol.withdraw(address(stablecoin), availableYield);

        // Transfer yield to owner
        stablecoin.safeTransfer(owner(), withdrawn);

        yieldEarned = 0;
        emit YieldClaimed(owner(), withdrawn);
    }

    /**
     * @notice Update the lending protocol address
     * @param newProtocol Address of new lending protocol
     */
    function updateLendingProtocol(address newProtocol) external onlyOwner {
        require(newProtocol != address(0), "Invalid protocol address");
        lendingProtocol = ILendingProtocol(newProtocol);
        emit LendingProtocolUpdated(newProtocol);
    }

    /**
     * @notice Internal function to update yield earned
     */
    function _updateYield() internal {
        uint256 currentYield = lendingProtocol.getYield(address(stablecoin));
        if (currentYield > 0) {
            yieldEarned += currentYield;
        }
        lastYieldUpdate = block.timestamp;
    }

    /**
     * @notice Get current yield information
     * @return Current yield available
     */
    function getCurrentYield() external view returns (uint256) {
        return yieldEarned + lendingProtocol.getYield(address(stablecoin));
    }
}
```
