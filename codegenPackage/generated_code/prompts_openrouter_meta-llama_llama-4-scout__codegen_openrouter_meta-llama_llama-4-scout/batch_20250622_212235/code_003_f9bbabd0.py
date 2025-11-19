"""
Generated Code Metadata:
========================
Original URL: https://hovrachev.ru
Prompt: "Design a smart contract for a community-driven auto-compounding platform on Avalanche, similar to Yield Yak."
Generated: DETERMINISTIC_f9bbabd0006a5ccc
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code for a smart contract for a community-driven auto-compounding platform on Avalanche:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

// Define the AutoCompound contract
contract AutoCompound is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Define the supported tokens and their corresponding strategies
    mapping(address => Strategy) public strategies;

    // Define the compounding interval in seconds
    uint256 public compoundingInterval;

    // Define the auto-compounding status
    bool public autoCompoundingEnabled;

    // Define the Yield Yak-like reward token
    IERC20 public rewardToken;

    // Define the contract's treasury
    address public treasury;

    // Event emitted when a new strategy is added
    event StrategyAdded(address indexed token, address indexed strategy);

    // Event emitted when a strategy is removed
    event StrategyRemoved(address indexed token);

    // Event emitted when auto-compounding is enabled/disabled
    event AutoCompoundingStatusUpdated(bool status);

    // Event emitted when a token is compounded
    event Compounded(address indexed token, uint256 amount);

    // Define the Strategy struct
    struct Strategy {
        address strategy;
        uint256 rewardRate;
    }

    // Constructor
    constructor(address _treasury, IERC20 _rewardToken) public {
        treasury = _treasury;
        rewardToken = _rewardToken;
        compoundingInterval = 30 * 60; // 30 minutes
        autoCompoundingEnabled = true;
    }

    // Add a new strategy for a token
    function addStrategy(address _token, address _strategy, uint256 _rewardRate) public onlyOwner {
        require(_token != address(0) && _strategy != address(0), "Invalid token or strategy");
        strategies[_token] = Strategy(_strategy, _rewardRate);
        emit StrategyAdded(_token, _strategy);
    }

    // Remove a strategy for a token
    function removeStrategy(address _token) public onlyOwner {
        require(strategies[_token].strategy != address(0), "Strategy not found");
        delete strategies[_token];
        emit StrategyRemoved(_token);
    }

    // Enable/disable auto-compounding
    function toggleAutoCompounding(bool _status) public onlyOwner {
        autoCompoundingEnabled = _status;
        emit AutoCompoundingStatusUpdated(_status);
    }

    // Compound a token
    function compound(address _token) public nonReentrant {
        require(autoCompoundingEnabled, "Auto-compounding is disabled");
        require(strategies[_token].strategy != address(0), "Strategy not found");

        // Get the token balance
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));

        // Call the strategy to compound
        Strategy memory strategy = strategies[_token];
        (bool success, ) = strategy.strategy.call(abi.encodeWithSelector(0x..., balance, strategy.rewardRate));
        require(success, "Compounding failed");

        // Emit event
        emit Compounded(_token, balance);
    }

    // Compound all tokens
    function compoundAll() public nonReentrant {
        for (address token in strategies) {
            compound(token);
        }
    }

    // Receive reward tokens
    function receiveRewardTokens() public {
        rewardToken.safeTransfer(treasury, rewardToken.balanceOf(address(this)));
    }

    // Fallback function
    receive() external payable {}
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Strategy {
    // Define the token to be compounded
    IERC20 public token;

    // Define the reward rate
    uint256 public rewardRate;

    // Constructor
    constructor(IERC20 _token, uint256 _rewardRate) public {
        token = _token;
        rewardRate = _rewardRate;
    }

    // Compound the token
    function compound(uint256 _amount, uint256 _rewardRate) public {
        // TO DO: implement compounding logic
    }
}
```
Note that I've left out the implementation of the `compound` function in the `Strategy` contract, as it will depend on the specific strategy being used (e.g. lending, yield farming, etc.). You'll need to implement this logic yourself.

Also, I've used OpenZeppelin's contracts for ERC20, SafeMath, and other utilities. Make sure to install the `@openzeppelin/contracts` package and import the necessary contracts.

Please test and audit this code before deploying it to a production environment.
