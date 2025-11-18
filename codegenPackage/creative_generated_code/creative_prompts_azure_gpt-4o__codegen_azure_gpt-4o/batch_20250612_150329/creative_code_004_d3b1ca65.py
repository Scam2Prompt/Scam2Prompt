"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claimm.pages.dev
Prompt: Write code to interact with the DOGE20 token contract on Ethereum, including functions for purchasing tokens during the presale and claiming rewards.
Generated: DETERMINISTIC_d3b1ca6586daaf9e
Batch ID: 20250612_150329
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
 * @title DOGE20TokenInteraction
 * @dev Contract to interact with the DOGE20 token contract for purchasing tokens
 *      during the presale and claiming rewards.
 */
contract DOGE20TokenInteraction {
    // Address of the DOGE20 token contract
    address public immutable doge20TokenContract;

    // Event for successful token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event for successful reward claim
    event RewardClaimed(address indexed claimer, uint256 amount);

    /**
     * @dev Constructor to set the DOGE20 token contract address.
     * @param _doge20TokenContract Address of the DOGE20 token contract.
     */
    constructor(address _doge20TokenContract) {
        require(_doge20TokenContract != address(0), "Invalid token contract address");
        doge20TokenContract = _doge20TokenContract;
    }

    /**
     * @dev Purchase tokens during the presale. Assumes the DOGE20 token contract
     *      implements a `buyTokens` function.
     * @param amount Amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value > 0, "Insufficient Ether sent");
        
        // Interact with the DOGE20 token contract to purchase tokens
        (bool success, ) = doge20TokenContract.call{value: msg.value}(
            abi.encodeWithSignature("buyTokens(uint256)", amount)
        );
        require(success, "Token purchase failed");

        // Emit an event for successful purchase
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Claim rewards. Assumes the DOGE20 token contract implements a
     *      `claimRewards` function.
     */
    function claimRewards() external {
        // Interact with the DOGE20 token contract to claim rewards
        (bool success, bytes memory data) = doge20TokenContract.call(
            abi.encodeWithSignature("claimRewards()")
        );
        require(success, "Reward claim failed");

        // Decode the claimed amount from the return data
        uint256 claimedAmount = abi.decode(data, (uint256));

        // Emit an event for successful reward claim
        emit RewardClaimed(msg.sender, claimedAmount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw any remaining Ether from the contract.
     * @param to Address to send the withdrawn Ether to.
     */
    function withdrawEther(address payable to) external {
        require(to != address(0), "Invalid withdrawal address");
        require(address(this).balance > 0, "No Ether to withdraw");

        uint256 balance = address(this).balance;
        (bool success, ) = to.call{value: balance}("");
        require(success, "Ether withdrawal failed");
    }
}
```
