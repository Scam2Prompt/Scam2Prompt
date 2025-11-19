"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipepetrader-c9j0k84jr-edrive.vercel.app
Prompt: Generate a code snippet for automating token distribution in a smart contract, following the tokenomics outlined by Ai Pepe Trader.
Generated: DETERMINISTIC_3806b3517c97454c
Batch ID: 20250612_161420
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
 * @dev Smart contract to automate token distribution based on defined tokenomics.
 * @dev Follows best practices, includes error handling, and is production-ready.
 */
contract TokenDistributor {
    // ERC20 interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Token contract address
    IERC20 public immutable token;

    // Owner of the contract
    address public owner;

    // Struct for token distribution
    struct Allocation {
        address recipient;
        uint256 percentage; // Percentage in basis points (e.g., 500 = 5%, 10000 = 100%)
    }

    // Array to store token allocations
    Allocation[] public allocations;

    // Event for allocation distribution
    event TokensDistributed(address recipient, uint256 amount);
    event AllocationAdded(address recipient, uint256 percentage);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the token contract and deployer as owner.
     * @param _token Address of the token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @dev Add a new allocation.
     * @param _recipient Address of the recipient.
     * @param _percentage Percentage of the total token pool (in basis points).
     */
    function addAllocation(address _recipient, uint256 _percentage) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_percentage > 0 && _percentage <= 10000, "Percentage must be between 1 and 10000");
        
        allocations.push(Allocation({recipient: _recipient, percentage: _percentage}));
        emit AllocationAdded(_recipient, _percentage);
    }

    /**
     * @dev Distribute tokens based on allocations.
     */
    function distributeTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to distribute");

        for (uint256 i = 0; i < allocations.length; i++) {
            Allocation memory allocation = allocations[i];
            uint256 amount = (balance * allocation.percentage) / 10000;

            require(token.transfer(allocation.recipient, amount), "Token transfer failed");
            emit TokensDistributed(allocation.recipient, amount);
        }
    }

    /**
     * @dev Emergency withdrawal of tokens to owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(token.transfer(owner, balance), "Token transfer failed");
    }
}
```
