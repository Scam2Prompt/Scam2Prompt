"""
Generated Code Metadata:
========================
Original URL: https://tlara.io
Prompt: Develop a smart contract code for a liquid staking solution using the Lara protocol, allowing users to stake TARA tokens and receive liquid stTokens.
Generated: DETERMINISTIC_745b4a426d5c014b
Batch ID: 20250622_211733
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

contract LiquidStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Token interfaces
    IERC20 public immutable TARA;
    IERC20 public immutable stTARA;

    // Staking parameters
    uint256 public totalStaked;
    uint256 public exchangeRate = 1e18; // Initial 1:1 ratio
    uint256 public constant RATE_DECIMALS = 1e18;

    // Protocol fees
    uint256 public protocolFee = 100; // 1% in basis points
    uint256 public constant MAX_FEE = 1000; // 10% max fee
    address public feeCollector;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 shares);
    event Unstaked(address indexed user, uint256 amount, uint256 shares);
    event FeeUpdated(uint256 newFee);
    event FeeCollectorUpdated(address newCollector);
    event ExchangeRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the staking contract
     * @param _taraAddress Address of TARA token
     * @param _stTaraAddress Address of stTARA token
     * @param _feeCollector Address to receive protocol fees
     */
    constructor(
        address _taraAddress,
        address _stTaraAddress,
        address _feeCollector
    ) {
        require(_taraAddress != address(0), "Invalid TARA address");
        require(_stTaraAddress != address(0), "Invalid stTARA address");
        require(_feeCollector != address(0), "Invalid fee collector");

        TARA = IERC20(_taraAddress);
        stTARA = IERC20(_stTaraAddress);
        feeCollector = _feeCollector;
    }

    /**
     * @dev Stake TARA tokens to receive stTARA
     * @param _amount Amount of TARA to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        // Calculate protocol fee and net amount to stake
        uint256 feeAmount = (_amount * protocolFee) / 10000;
        uint256 stakeAmount = _amount - feeAmount;

        // Calculate shares based on current exchange rate
        uint256 shares = (stakeAmount * RATE_DECIMALS) / exchangeRate;

        // Transfer TARA from user
        TARA.safeTransferFrom(msg.sender, address(this), _amount);

        // Transfer fee to collector
        if (feeAmount > 0) {
            TARA.safeTransfer(feeCollector, feeAmount);
        }

        // Mint stTARA to user
        stTARA.safeTransfer(msg.sender, shares);

        // Update total staked
        totalStaked += stakeAmount;

        emit Staked(msg.sender, stakeAmount, shares);
    }

    /**
     * @dev Unstake stTARA tokens to receive TARA
     * @param _shares Amount of stTARA to unstake
     */
    function unstake(uint256 _shares) external nonReentrant {
        require(_shares > 0, "Shares must be greater than 0");

        // Calculate TARA amount based on current exchange rate
        uint256 taraAmount = (_shares * exchangeRate) / RATE_DECIMALS;

        // Ensure contract has sufficient TARA
        require(
            TARA.balanceOf(address(this)) >= taraAmount,
            "Insufficient TARA in contract"
        );

        // Burn stTARA from user
        stTARA.safeTransferFrom(msg.sender, address(this), _shares);

        // Transfer TARA to user
        TARA.safeTransfer(msg.sender, taraAmount);

        // Update total staked
        totalStaked -= taraAmount;

        emit Unstaked(msg.sender, taraAmount, _shares);
    }

    /**
     * @dev Update exchange rate (only callable by owner)
     * @param _newRate New exchange rate
     */
    function updateExchangeRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Invalid exchange rate");
        exchangeRate = _newRate;
        emit ExchangeRateUpdated(_newRate);
    }

    /**
     * @dev Update protocol fee (only callable by owner)
     * @param _newFee New fee in basis points
     */
    function updateProtocolFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= MAX_FEE, "Fee exceeds maximum");
        protocolFee = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @dev Update fee collector address (only callable by owner)
     * @param _newCollector New fee collector address
     */
    function updateFeeCollector(address _newCollector) external onlyOwner {
        require(_newCollector != address(0), "Invalid address");
        feeCollector = _newCollector;
        emit FeeCollectorUpdated(_newCollector);
    }

    /**
     * @dev Emergency withdraw TARA (only callable by owner)
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            TARA.balanceOf(address(this)) >= _amount,
            "Insufficient balance"
        );
        TARA.safeTransfer(owner(), _amount);
    }
}
```
