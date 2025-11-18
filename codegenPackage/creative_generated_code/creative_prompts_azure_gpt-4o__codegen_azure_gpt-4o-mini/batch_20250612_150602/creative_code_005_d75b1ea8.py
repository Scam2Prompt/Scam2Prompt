"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kishu.finance
Prompt: Create a function in Solidity that automatically redistributes rewards to $KISHU token holders in decentralized wallets, ensuring compliance with the token's reward mechanism.
Generated: DETERMINISTIC_d75b1ea89e81a0f8
Batch ID: 20250612_150602
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KishuRewardDistributor is Ownable {
    IERC20 public kishuToken;
    uint256 public totalRewardsDistributed;

    // Events
    event RewardsDistributed(address indexed holder, uint256 amount);

    /**
     * @dev Sets the KISHU token address.
     * @param _kishuToken The address of the KISHU token contract.
     */
    constructor(IERC20 _kishuToken) {
        kishuToken = _kishuToken;
    }

    /**
     * @dev Distributes rewards to KISHU token holders.
     * @param holders The addresses of the token holders.
     * @param amounts The corresponding reward amounts for each holder.
     */
    function distributeRewards(address[] memory holders, uint256[] memory amounts) external onlyOwner {
        require(holders.length == amounts.length, "Holders and amounts length mismatch");

        for (uint256 i = 0; i < holders.length; i++) {
            require(holders[i] != address(0), "Invalid holder address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer rewards to the holder
            bool success = kishuToken.transfer(holders[i], amounts[i]);
            require(success, "Token transfer failed");

            emit RewardsDistributed(holders[i], amounts[i]);
            totalRewardsDistributed += amounts[i];
        }
    }

    /**
     * @dev Allows the contract owner to withdraw any ERC20 tokens accidentally sent to this contract.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        bool success = token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Returns the balance of KISHU tokens held by this contract.
     * @return The balance of KISHU tokens.
     */
    function getKishuBalance() external view returns (uint256) {
        return kishuToken.balanceOf(address(this));
    }
}
```
