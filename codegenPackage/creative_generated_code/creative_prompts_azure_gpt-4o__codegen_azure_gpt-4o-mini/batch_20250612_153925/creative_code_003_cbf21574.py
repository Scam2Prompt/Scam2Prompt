"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-fi.us
Prompt: Create a smart contract in Solidity that mirrors Ethena.fi’s approach to transparency and security in stablecoin transactions.
Generated: DETERMINISTIC_cbf2157492d8631c
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TransparentStableCoin
 * @dev A smart contract that implements a stablecoin with transparency and security in transactions.
 */
contract TransparentStableCoin is ERC20, Ownable {
    // Mapping to keep track of transaction approvals
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event for logging deposits
    event Deposit(address indexed user, uint256 amount);
    
    // Event for logging withdrawals
    event Withdrawal(address indexed user, uint256 amount);

    // Constructor that initializes the token with a name and symbol
    constructor() ERC20("Transparent Stable Coin", "TSC") {
        // Mint an initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens with decimals
    }

    /**
     * @dev Deposit function that allows users to deposit Ether and mint equivalent stablecoins.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Mint stablecoins equivalent to the value of Ether deposited (1:1 ratio)
        _mint(msg.sender, msg.value);

        // Emit deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw function that allows users to burn stablecoins and withdraw Ether.
     * @param amount The amount of stablecoins to burn for Ether.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the stablecoins from the user's balance
        _burn(msg.sender, amount);

        // Send Ether to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Override the allowance function to include proper error handling.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The amount of tokens allowed to be spent.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Allowance function to approve a spender to spend a specific amount of tokens.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Internal function to handle the approval logic.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Fallback function to accept incoming Ether deposits directly.
     */
    receive() external payable {
        deposit(); // Automatically deposit when Ether is sent
    }

    /**
     * @dev Function to withdraw any Ether accidentally sent to the contract by the owner.
     */
    function withdrawContractEther() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success, ) = msg.sender.call{value: contractBalance}("");
        require(success, "Transfer failed");
    }
}
```
