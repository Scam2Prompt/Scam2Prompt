"""
Generated Code Metadata:
========================
Original URL: https://claim-0x0.web.app
Prompt: Generate a smart contract code snippet in Solidity that distributes 100% of the utility income generated from fees to 0x0 holders in ETH.
Generated: DETERMINISTIC_8d187f4bb16b86a1
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FeeDistributor is Ownable {
    using SafeMath for uint256;

    // Address of the token contract
    IERC20 public token;

    // Total ETH distributed to token holders
    uint256 public totalDistributed;

    // Mapping to track ETH claimed by each token holder
    mapping(address => uint256) public claimed;

    // Events
    event FeesDistributed(address indexed holder, uint256 amount);
    event FeesReceived(address indexed from, uint256 amount);

    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to receive ETH
    receive() external payable {
        emit FeesReceived(msg.sender, msg.value);
    }

    // Distribute fees to token holders
    function distributeFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to distribute");

        uint256 totalSupply = token.totalSupply();
        require(totalSupply > 0, "No token holders");

        uint256 amountPerToken = balance.mul(1e18).div(totalSupply);
        require(amountPerToken > 0, "Amount per token too small");

        // Distribute to 0x0 holders (burn address)
        address burnAddress = address(0);
        uint256 burnBalance = token.balanceOf(burnAddress);
        if (burnBalance > 0) {
            uint256 burnShare = amountPerToken.mul(burnBalance).div(1e18);
            if (burnShare > 0) {
                claimed[burnAddress] = claimed[burnAddress].add(burnShare);
                totalDistributed = totalDistributed.add(burnShare);
                payable(burnAddress).transfer(burnShare);
                emit FeesDistributed(burnAddress, burnShare);
            }
        }
    }

    // Withdraw any remaining ETH (safety measure)
    function withdrawRemaining() external onlyOwner {
        uint256 remaining = address(this).balance;
        payable(owner()).transfer(remaining);
    }
}
```
