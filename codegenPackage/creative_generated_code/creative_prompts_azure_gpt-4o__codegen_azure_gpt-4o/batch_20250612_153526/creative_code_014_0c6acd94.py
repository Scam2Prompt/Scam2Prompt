"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Write a Solidity function to distribute protocol token incentives (e.g., CRV, CVX, COMP) earned by OUSD across its yield strategies.
Generated: DETERMINISTIC_0c6acd94929e8b14
Batch ID: 20250612_153526
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
 * @title TokenDistributor
 * @dev Contract to distribute protocol token incentives earned by OUSD across its yield strategies.
 */
contract TokenDistributor {
    // Mapping to track the share percentage for each strategy
    mapping(address => uint256) public strategyShare;
    
    // List of strategies
    address[] public strategies;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed token, uint256 totalAmount);

    // Modifier to check if the caller is the contract owner
    address public owner;
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the initial owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Update strategy shares. Only owner can call this function.
     * @param _strategies List of strategy addresses
     * @param _shares List of share percentages for the given strategies
     */
    function updateStrategyShares(address[] calldata _strategies, uint256[] calldata _shares) external onlyOwner {
        require(_strategies.length == _shares.length, "Strategies and shares length mismatch");
        uint256 totalShare = 0;

        for (uint256 i = 0; i < _shares.length; i++) {
            totalShare += _shares[i];
        }
        require(totalShare == 100, "Total share must be 100%");

        strategies = _strategies;

        for (uint256 i = 0; i < _strategies.length; i++) {
            strategyShare[_strategies[i]] = _shares[i];
        }
    }

    /**
     * @dev Distribute earned tokens across the strategies based on their share.
     * @param _token Address of the token to distribute
     * @param _totalAmount Total amount of tokens to distribute
     */
    function distributeTokens(address _token, uint256 _totalAmount) external {
        require(_totalAmount > 0, "Total amount must be greater than zero");

        // Transfer tokens to each strategy based on their share
        for (uint256 i = 0; i < strategies.length; i++) {
            address strategy = strategies[i];
            uint256 sharePercentage = strategyShare[strategy];

            // Calculate the amount for the strategy
            uint256 amount = (_totalAmount * sharePercentage) / 100;

            // Ensure the transfer succeeds
            require(
                IERC20(_token).transfer(strategy, amount),
                "Token transfer failed"
            );
        }

        emit TokensDistributed(_token, _totalAmount);
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
