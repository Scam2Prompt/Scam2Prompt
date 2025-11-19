"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Develop a simple smart contract in Solidity that utilizes OUSD for yield generation, explaining how the contract would work and how it would be deployed on the Ethereum blockchain.
Generated: DETERMINISTIC_82f6cc3de26aa945
Batch ID: 20250622_210914
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

/**
 * @title YieldGenerator
 * @dev A simple smart contract that interacts with OUSD (Origin Dollar) for yield generation.
 * Users can deposit OUSD into the contract, and the contract will hold the OUSD to generate yield.
 * The yield is automatically accrued by OUSD, and users can withdraw their funds along with the yield.
 */
interface IOUSD {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract YieldGenerator {
    // Address of the OUSD token contract
    address public immutable ousdToken;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Event emitted when a user deposits OUSD
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user withdraws OUSD
    event Withdraw(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the OUSD token address.
     * @param _ousdToken Address of the OUSD token contract.
     */
    constructor(address _ousdToken) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        ousdToken = _ousdToken;
    }

    /**
     * @dev Allows a user to deposit OUSD into the contract.
     * The user must approve the contract to transfer OUSD on their behalf before calling this function.
     * @param amount The amount of OUSD to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer OUSD from the user to the contract
        bool success = IOUSD(ousdToken).transferFrom(msg.sender, address(this), amount);
        require(success, "OUSD transfer failed");

        // Update the user's deposit balance
        userDeposits[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their deposited OUSD along with any accrued yield.
     */
    function withdraw() external {
        uint256 userBalance = userDeposits[msg.sender];
        require(userBalance > 0, "No funds to withdraw");

        // Get the current balance of the contract
        uint256 contractBalance = IOUSD(ousdToken).balanceOf(address(this));
        require(contractBalance >= userBalance, "Insufficient contract balance");

        // Reset the user's deposit balance
        userDeposits[msg.sender] = 0;

        // Transfer the user's funds (including yield) back to them
        bool success = IOUSD(ousdToken).transfer(msg.sender, userBalance);
        require(success, "OUSD transfer failed");

        emit Withdraw(msg.sender, userBalance);
    }

    /**
     * @dev Returns the total balance of OUSD held by the contract.
     * This includes both user deposits and any accrued yield.
     */
    function getContractBalance() external view returns (uint256) {
        return IOUSD(ousdToken).balanceOf(address(this));
    }
}
```

### Deployment Steps:
1. Compile the contract using a Solidity compiler (e.g., Remix or Hardhat).
2. Deploy the contract to the Ethereum blockchain, providing the OUSD token address as the constructor argument.
3. Users must approve the contract to transfer OUSD on their behalf before depositing.
4. Use the `deposit` function to deposit OUSD and the `withdraw` function to withdraw funds along with accrued yield.
