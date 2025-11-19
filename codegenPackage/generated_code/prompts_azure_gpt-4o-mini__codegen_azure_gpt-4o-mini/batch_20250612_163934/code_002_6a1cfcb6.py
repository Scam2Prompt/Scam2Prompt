"""
Generated Code Metadata:
========================
Original URL: https://dappdroppage.pages.dev
Prompt: Write a simple smart contract in Solidity that could be used for a dApp drop scenario, incorporating unique features that might have been discussed on a dApp drop page.
Generated: DETERMINISTIC_6a1cfcb6129a81d0
Batch ID: 20250612_163934
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DAppDrop
 * @dev A simple smart contract for managing a token drop scenario.
 * This contract allows the owner to distribute tokens to multiple addresses.
 */
contract DAppDrop is Ownable {
    using SafeMath for uint256;

    // The token being distributed
    IERC20 public token;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress The address of the ERC20 token to be distributed.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Distribute tokens to multiple addresses.
     * @param recipients An array of addresses to receive tokens.
     * @param amounts An array of amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            token.transfer(recipients[i], amounts[i]);
            emit TokensDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to this contract.
     * @param _tokenAddress The address of the ERC20 token to withdraw.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than zero");

        IERC20(_tokenAddress).transfer(owner(), _amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
