"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-pacmoonio.pages.dev
Prompt: Write a Solidity function to verify deposits to the $JENNER presale smart contract and calculate the corresponding JENNER token allocation based on the 0.1 ETH ~ 99,500 JENNER rate.
Generated: DETERMINISTIC_f2221065080e4d11
Batch ID: 20250612_151003
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

contract JennerPresale {
    // Token allocation rate: 0.1 ETH = 99,500 JENNER
    uint256 public constant TOKEN_RATE = 99500; // JENNER tokens per 0.1 ETH
    uint256 public constant ETH_RATE = 0.1 ether; // 0.1 ETH

    // Mapping to keep track of user deposits
    mapping(address => uint256) public userDeposits;

    // Mapping to track JENNER token allocation for each user
    mapping(address => uint256) public userTokenAllocation;

    // Event to log deposits and token allocation
    event DepositReceived(address indexed depositor, uint256 ethAmount, uint256 tokenAllocation);

    // Function to verify deposits and calculate token allocation
    function deposit() external payable {
        // Ensure the deposit amount is greater than zero
        require(msg.value > 0, "Deposit amount must be greater than zero.");

        // Calculate JENNER token allocation based on deposit
        uint256 jennerAllocation = (msg.value * TOKEN_RATE) / ETH_RATE;

        // Update user deposit and token allocation
        userDeposits[msg.sender] += msg.value;
        userTokenAllocation[msg.sender] += jennerAllocation;

        // Emit event for deposit
        emit DepositReceived(msg.sender, msg.value, jennerAllocation);
    }

    // Function to retrieve user's deposit and token allocation
    function getUserData(address user) external view returns (uint256 depositedEth, uint256 allocatedJenner) {
        return (userDeposits[user], userTokenAllocation[user]);
    }

    // Function for the owner to withdraw the contract's balance
    function withdrawFunds(address payable recipient) external {
        // Ensure only the contract owner can call this function
        require(msg.sender == owner, "Only the contract owner can withdraw funds.");

        // Transfer all ETH balance of the contract to the recipient
        recipient.transfer(address(this).balance);
    }

    // Fallback function to handle unexpected transactions
    fallback() external payable {
        // Revert if funds are sent without calling the deposit function
        revert("Direct transfers are not allowed. Use the deposit function.");
    }

    // Receive function, used for direct ETH transfers
    receive() external payable {
        revert("Direct transfers are not allowed. Use the deposit function.");
    }
}
```
