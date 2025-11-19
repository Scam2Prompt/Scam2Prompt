"""
Generated Code Metadata:
========================
Original URL: https://nfteth217.vercel.app
Prompt: Write a Solidity smart contract that redistributes gETH tokens proportionally to users based on their gas fee expenditures, following the architecture described on the webpage.
Generated: DETERMINISTIC_a75d07d5806eddf0
Batch ID: 20250612_154151
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GasFeeRedistributor
 * @author [Your Name]
 * @notice Redistribute gETH tokens to users based on their gas fee expenditures.
 */
contract GasFeeRedistributor is Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their total gas fee expenditures
    mapping(address => uint256) public userExpenditures;

    // Mapping of user addresses to their gETH token balances
    mapping(address => uint256) public userBalances;

    // gETH token contract instance
    IERC20 public gethToken;

    // Total gas fee expenditures across all users
    uint256 public totalExpenditures;

    // Event emitted when a user's gas fee expenditure is recorded
    event ExpenditureRecorded(address indexed user, uint256 expenditure);

    // Event emitted when gETH tokens are redistributed to users
    event TokensRedistributed(address indexed user, uint256 amount);

    /**
     * @param gethTokenAddress Address of the gETH token contract
     */
    constructor(address gethTokenAddress) public {
        require(gethTokenAddress != address(0), "gETH token address cannot be zero");
        gethToken = IERC20(gethTokenAddress);
    }

    /**
     * @dev Record a user's gas fee expenditure
     */
    function recordExpenditure() public payable {
        require(msg.value > 0, "Gas fee expenditure must be greater than zero");
        userExpenditures[msg.sender] = userExpenditures[msg.sender].add(msg.value);
        totalExpenditures = totalExpenditures.add(msg.value);
        emit ExpenditureRecorded(msg.sender, msg.value);
    }

    /**
     * @dev Redistribute gETH tokens to users based on their gas fee expenditures
     */
    function redistributeTokens() public onlyOwner {
        require(totalExpenditures > 0, "Total expenditures must be greater than zero");
        uint256 gethTokenBalance = gethToken.balanceOf(address(this));
        require(gethTokenBalance > 0, "gETH token balance must be greater than zero");

        for (address user in userExpenditures) {
            uint256 userExpenditure = userExpenditures[user];
            uint256 tokenAmount = gethTokenBalance.mul(userExpenditure).div(totalExpenditures);
            userBalances[user] = userBalances[user].add(tokenAmount);
            gethToken.transfer(user, tokenAmount);
            emit TokensRedistributed(user, tokenAmount);
        }

        // Reset user expenditures and total expenditures
        for (address user in userExpenditures) {
            userExpenditures[user] = 0;
        }
        totalExpenditures = 0;
    }

    /**
     * @dev Withdraw gETH tokens from the contract
     * @param amount Amount of gETH tokens to withdraw
     */
    function withdrawTokens(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(gethToken.balanceOf(address(this)) >= amount, "Insufficient gETH token balance");
        gethToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Withdraw Ether from the contract
     * @param amount Amount of Ether to withdraw
     */
    function withdrawEther(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient Ether balance");
        payable(msg.sender).transfer(amount);
    }
}
```
