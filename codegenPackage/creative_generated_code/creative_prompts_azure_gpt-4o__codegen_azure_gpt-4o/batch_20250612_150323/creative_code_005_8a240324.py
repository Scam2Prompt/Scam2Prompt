"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Provide an example of a Solidity contract for a prize wallet system, similar to the MotorBoat Prize Wallet described on the CryptoTitties webpage.
Generated: DETERMINISTIC_8a240324b21bd7a6
Batch ID: 20250612_150323
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
 * @title PrizeWallet
 * @dev A contract for a prize wallet system where users can deposit funds,
 *      an owner can distribute prizes, and the winner can withdraw their prize.
 */
contract PrizeWallet {
    // Address of the contract owner
    address public owner;

    // Mapping to track balances of each participant
    mapping(address => uint256) public balances;

    // Address of the winner
    address public winner;

    // Event for deposit logging
    event Deposit(address indexed participant, uint256 amount);

    // Event for prize distribution logging
    event PrizeDistributed(address indexed winner, uint256 prizeAmount);

    // Event for withdrawal logging
    event Withdrawal(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Function for participants to deposit funds into the prize wallet.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to set the winner and distribute the prize.
     * @param _winner Address of the winner.
     */
    function distributePrize(address _winner) external onlyOwner {
        require(_winner != address(0), "Winner address cannot be zero");
        require(address(this).balance > 0, "No funds available to distribute");

        winner = _winner;
        uint256 prizeAmount = address(this).balance;

        (bool success, ) = winner.call{value: prizeAmount}("");
        require(success, "Failed to transfer prize to the winner");

        emit PrizeDistributed(winner, prizeAmount);
    }

    /**
     * @dev Function for a user to withdraw their balance (if any).
     */
    function withdraw() external {
        uint256 userBalance = balances[msg.sender];
        require(userBalance > 0, "No funds available to withdraw");

        balances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: userBalance}("");
        require(success, "Failed to withdraw funds");

        emit Withdrawal(msg.sender, userBalance);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to get the contract's balance.
     * @return The total balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
