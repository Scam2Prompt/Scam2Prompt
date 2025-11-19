"""
Generated Code Metadata:
========================
Original URL: https://marvinonbase.pages.dev
Prompt: Write a Solidity function that implements a giveaway mechanism, distributing tokens to the top 1000 holders based on their holdings, similar to Marvin's $1M giveaway plan.
Generated: DETERMINISTIC_977cec357d6012aa
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Giveaway {
    // Mapping of user balances
    mapping(address => uint256) public balances;

    // IERC20 token instance
    IERC20 public token;

    // Total tokens to be distributed
    uint256 public totalTokens;

    // Maximum number of holders to receive tokens
    uint256 public constant MAX_HOLDERS = 1000;

    // Event emitted when giveaway is executed
    event GiveawayExecuted(address[] holders, uint256[] amounts);

    /**
     * Constructor
     * @param _token IERC20 token instance
     * @param _totalTokens Total tokens to be distributed
     */
    constructor(IERC20 _token, uint256 _totalTokens) {
        require(address(_token) != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than 0");

        token = _token;
        totalTokens = _totalTokens;
    }

    /**
     * Update user balance
     * @param _user User address
     * @param _amount New balance
     */
    function updateBalance(address _user, uint256 _amount) public {
        require(_user != address(0), "Invalid user address");
        require(_amount >= 0, "Invalid balance");

        balances[_user] = _amount;
    }

    /**
     * Execute giveaway
     */
    function executeGiveaway() public {
        // Get all holders and their balances
        address[] memory holders = getHolders();
        uint256[] memory amounts = new uint256[](holders.length);

        // Calculate total balance of all holders
        uint256 totalBalance = 0;
        for (uint256 i = 0; i < holders.length; i++) {
            totalBalance = SafeMath.add(totalBalance, balances[holders[i]]);
        }

        // Distribute tokens to top MAX_HOLDERS holders
        uint256 distributedTokens = 0;
        for (uint256 i = 0; i < MAX_HOLDERS && i < holders.length; i++) {
            // Calculate token amount for current holder
            uint256 holderBalance = balances[holders[i]];
            uint256 tokenAmount = SafeMath.mul(totalTokens, holderBalance) / totalBalance;

            // Update distributed tokens
            distributedTokens = SafeMath.add(distributedTokens, tokenAmount);

            // Update holder's balance
            amounts[i] = tokenAmount;
        }

        // Ensure not more tokens than totalTokens are distributed
        require(distributedTokens <= totalTokens, "Too many tokens distributed");

        // Transfer tokens to holders
        for (uint256 i = 0; i < MAX_HOLDERS && i < holders.length; i++) {
            require(token.transfer(holders[i], amounts[i]), "Token transfer failed");
        }

        emit GiveawayExecuted(holders, amounts);
    }

    /**
     * Get all holders
     * @return address[] All holders
     */
    function getHolders() internal view returns (address[] memory) {
        // In a real-world scenario, use a more efficient data structure like a mapping with enumeration.
        // For simplicity, assume all addresses with non-zero balances are holders.
        address[] memory holders = new address[](address(this).balance == 0 ? 1 : 10000); // placeholder capacity
        uint256 holderCount;

        for (address user in balances) {
            if (balances[user] > 0) {
                holders[holderCount++] = user;
            }
        }

        // Trim array to actual holder count
        assembly {
            mstore(holders, holderCount)
        }

        return holders;
    }
}
```
