"""
Generated Code Metadata:
========================
Original URL: https://ethltt.com
Prompt: "How to integrate Ethereum blockchain with a pledge or commitment platform using Solidity and OpenZeppelin libraries?"
Generated: DETERMINISTIC_de5c5af5d4d888db
Batch ID: 20250622_204829
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

// Import OpenZeppelin libraries for security and functionality
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PledgePlatform
 * @dev A smart contract for managing pledges and commitments on the Ethereum blockchain.
 * Users can pledge ETH or ERC20 tokens, and the contract tracks their commitments.
 */
contract PledgePlatform is Ownable {
    using SafeMath for uint256;

    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount, address tokenAddress);

    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(address indexed pledger, uint256 amount, address tokenAddress);

    // Struct to store pledge details
    struct Pledge {
        uint256 amount; // Amount pledged
        address tokenAddress; // Token used for the pledge (address(0) for ETH)
    }

    // Mapping to store pledges by user address
    mapping(address => Pledge) private pledges;

    /**
     * @dev Allows a user to make a pledge in ETH.
     */
    function pledgeETH() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the user's pledge
        pledges[msg.sender].amount = pledges[msg.sender].amount.add(msg.value);
        pledges[msg.sender].tokenAddress = address(0); // ETH is represented by address(0)

        emit PledgeMade(msg.sender, msg.value, address(0));
    }

    /**
     * @dev Allows a user to make a pledge in ERC20 tokens.
     * @param tokenAddress The address of the ERC20 token contract.
     * @param amount The amount of tokens to pledge.
     */
    function pledgeERC20(address tokenAddress, uint256 amount) external {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Pledge amount must be greater than zero");

        // Transfer tokens from the user to the contract
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's pledge
        pledges[msg.sender].amount = pledges[msg.sender].amount.add(amount);
        pledges[msg.sender].tokenAddress = tokenAddress;

        emit PledgeMade(msg.sender, amount, tokenAddress);
    }

    /**
     * @dev Allows a user to withdraw their pledge.
     */
    function withdrawPledge() external {
        Pledge memory userPledge = pledges[msg.sender];
        require(userPledge.amount > 0, "No pledge to withdraw");

        uint256 amount = userPledge.amount;
        address tokenAddress = userPledge.tokenAddress;

        // Reset the user's pledge
        pledges[msg.sender].amount = 0;
        pledges[msg.sender].tokenAddress = address(0);

        if (tokenAddress == address(0)) {
            // Withdraw ETH
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success, "ETH transfer failed");
        } else {
            // Withdraw ERC20 tokens
            IERC20 token = IERC20(tokenAddress);
            require(token.transfer(msg.sender, amount), "Token transfer failed");
        }

        emit PledgeWithdrawn(msg.sender, amount, tokenAddress);
    }

    /**
     * @dev Allows the owner to withdraw all ETH from the contract.
     */
    function withdrawAllETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw all ERC20 tokens from the contract.
     * @param tokenAddress The address of the ERC20 token contract.
     */
    function withdrawAllERC20(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(token.transfer(msg.sender, balance), "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept ETH directly.
     */
    receive() external payable {
        // Accept ETH deposits
    }
}
```
