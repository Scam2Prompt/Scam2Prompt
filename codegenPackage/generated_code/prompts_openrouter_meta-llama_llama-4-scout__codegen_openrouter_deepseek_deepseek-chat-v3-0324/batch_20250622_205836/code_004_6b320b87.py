"""
Generated Code Metadata:
========================
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: "Develop an oracle that utilizes EigenLayer's restaked ETH to provide a trustworthy price feed on Ethereum."
Generated: DETERMINISTIC_6b320b8730d999dc
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./interfaces/IEigenLayer.sol";
import "./interfaces/IPriceFeed.sol";

/**
 * @title RestakedETHPriceOracle
 * @notice A price oracle that leverages EigenLayer's restaked ETH to provide trustworthy price feeds
 */
contract RestakedETHPriceOracle is Ownable, Pausable, IPriceFeed {
    // Struct to hold price data with timestamp
    struct PriceData {
        uint256 price;
        uint256 timestamp;
    }

    // Address of EigenLayer contract
    IEigenLayer public immutable eigenLayer;

    // Minimum stake required to submit prices
    uint256 public minStake;

    // Current price data
    PriceData private _currentPrice;

    // Mapping of staker addresses to their stake amounts
    mapping(address => uint256) public stakerBalances;

    // Events
    event PriceUpdated(uint256 price, uint256 timestamp, address updater);
    event MinStakeUpdated(uint256 newMinStake);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);

    /**
     * @dev Constructor
     * @param _eigenLayer Address of EigenLayer contract
     * @param _minStake Minimum stake required to submit prices
     */
    constructor(address _eigenLayer, uint256 _minStake) {
        require(_eigenLayer != address(0), "Invalid EigenLayer address");
        eigenLayer = IEigenLayer(_eigenLayer);
        minStake = _minStake;
    }

    /**
     * @notice Update the price feed
     * @param price New price value
     */
    function updatePrice(uint256 price) external whenNotPaused {
        require(stakerBalances[msg.sender] >= minStake, "Insufficient stake");
        require(price > 0, "Price must be positive");

        _currentPrice = PriceData({
            price: price,
            timestamp: block.timestamp
        });

        emit PriceUpdated(price, block.timestamp, msg.sender);
    }

    /**
     * @notice Stake ETH to participate in price updates
     * @param amount Amount of ETH to stake
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Amount must be positive");
        require(msg.value == amount, "Incorrect ETH amount");

        eigenLayer.deposit{value: amount}(msg.sender);
        stakerBalances[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake ETH
     * @param amount Amount of ETH to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be positive");
        require(stakerBalances[msg.sender] >= amount, "Insufficient stake");

        stakerBalances[msg.sender] -= amount;
        eigenLayer.withdraw(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Get the current price
     * @return price Current price
     * @return timestamp When the price was last updated
     */
    function getPrice() external view override returns (uint256 price, uint256 timestamp) {
        require(_currentPrice.timestamp > 0, "Price not set");
        return (_currentPrice.price, _currentPrice.timestamp);
    }

    /**
     * @notice Update the minimum stake requirement
     * @param newMinStake New minimum stake amount
     */
    function setMinStake(uint256 newMinStake) external onlyOwner {
        require(newMinStake > 0, "Min stake must be positive");
        minStake = newMinStake;
        emit MinStakeUpdated(newMinStake);
    }

    /**
     * @notice Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @notice Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @notice Get the stake amount for a given address
     * @param staker Address to query
     * @return amount Stake amount
     */
    function getStake(address staker) external view returns (uint256 amount) {
        return stakerBalances[staker];
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title IPriceFeed
 * @notice Interface for price feed contracts
 */
interface IPriceFeed {
    /**
     * @notice Get the current price
     * @return price Current price
     * @return timestamp When the price was last updated
     */
    function getPrice() external view returns (uint256 price, uint256 timestamp);
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title IEigenLayer
 * @notice Interface for EigenLayer contract
 */
interface IEigenLayer {
    /**
     * @notice Deposit ETH to stake
     * @param staker Address of the staker
     */
    function deposit(address staker) external payable;

    /**
     * @notice Withdraw staked ETH
     * @param staker Address of the staker
     * @param amount Amount to withdraw
     */
    function withdraw(address staker, uint256 amount) external;
}
```
