"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockeptool.xyz
Prompt: Develop a smart contract that uses the Rocket Pool protocol to automate ETH staking and rETH distribution, ensuring compliance with the protocol's node commission rate.
Generated: DETERMINISTIC_cac90b7a30d488d7
Batch ID: 20250612_153925
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

// Import Rocket Pool's interface for staking
interface IRocketPoolDeposit {
    function deposit() external payable;
}

interface IRocketPoolToken {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract RocketPoolAutoStaker {
    // Rocket Pool deposit contract address
    address public constant rocketDepositAddress = 0x1234567890123456789012345678901234567890; // Replace with actual Rocket Pool deposit address
    IRocketPoolDeposit private rocketDeposit = IRocketPoolDeposit(rocketDepositAddress);

    // Rocket Pool rETH token contract address
    address public constant rETHAddress = 0x0987654321098765432109876543210987654321; // Replace with actual rETH token address
    IRocketPoolToken private rETH = IRocketPoolToken(rETHAddress);

    // Event emitted when ETH is staked
    event ETHStaked(address indexed staker, uint256 amount);

    // Event emitted when rETH is distributed
    event rETHDistributed(address indexed recipient, uint256 amount);

    // Fallback function to accept ETH deposits
    receive() external payable {
        stakeETH();
    }

    /**
     * @dev Allows a user to stake ETH into Rocket Pool and receive rETH.
     */
    function stakeETH() public payable {
        require(msg.value > 0, "Must send ETH to stake");

        // Deposit ETH into Rocket Pool
        rocketDeposit.deposit{value: msg.value}();

        emit ETHStaked(msg.sender, msg.value);
    }

    /**
     * @dev Distributes rETH tokens to a specified recipient.
     * @param recipient The recipient who will receive the rETH tokens.
     * @param amount The amount of rETH to transfer.
     */
    function distributeRETH(address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 rETHBalance = rETH.balanceOf(address(this));
        require(amount <= rETHBalance, "Insufficient rETH balance");

        // Transfer rETH to the recipient
        bool success = rETH.transfer(recipient, amount);
        require(success, "rETH transfer failed");

        emit rETHDistributed(recipient, amount);
    }

    /**
     * @dev Returns the current rETH balance held by the contract.
     */
    function getRETHBalance() public view returns (uint256) {
        return rETH.balanceOf(address(this));
    }

    /**
     * @dev Allows the owner to withdraw any accidentally sent ETH.
     * @param to The address to send the withdrawn ETH.
     */
    function withdrawETH(address to) external {
        require(to != address(0), "Invalid address");

        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = to.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }
}
```
