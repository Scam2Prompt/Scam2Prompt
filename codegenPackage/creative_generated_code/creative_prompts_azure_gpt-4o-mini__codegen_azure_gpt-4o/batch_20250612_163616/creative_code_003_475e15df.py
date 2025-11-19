"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbfour-meme.pages.dev
Prompt: Develop a smart contract in Solidity for managing the $FOUR token transactions, ensuring it aligns with the tokenomics stated on the Four Binance site.
Generated: DETERMINISTIC_475e15df047bbf61
Batch ID: 20250612_163616
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
 * @title FOUR Token Smart Contract
 * @dev Implements ERC20 standard token with custom tokenomics as described on the Four Binance site.
 */
contract FourToken {
    // Token details
    string public constant name = "$FOUR Token";
    string public constant symbol = "FOUR";
    uint8 public constant decimals = 18; // Standard ERC20 token decimals
    uint256 public totalSupply;

    // Balances and allowances mappings
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging transactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Contract owner
    address public owner;

    // Tokenomics parameters
    uint256 public constant feePercent = 2; // Example fee (2%)
    address public feeRecipient; // Address to receive transaction fees

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract.
     * @param _initialSupply The initial token supply.
     * @param _feeRecipient Address to receive transaction fees.
     */
    constructor(uint256 _initialSupply, address _feeRecipient) {
        require(_feeRecipient != address(0), "Fee recipient cannot be zero address");
        owner = msg.sender;
        feeRecipient = _feeRecipient;
        totalSupply = _initialSupply * (10**uint256(decimals)); // Adjust to token decimals
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Log initial token creation
    }

    /**
     * @dev Gets the balance of a specific address.
     * @param account The address to query.
     * @return The balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specific address with applied tokenomics fee.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     * @return True if the operation was successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Recipient cannot be zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate fee
        uint256 fee = (amount * feePercent) / 100;
        uint256 amountAfterFee = amount - fee;

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += amountAfterFee;
        balances[feeRecipient] += fee;

        // Emit events
        emit Transfer(msg.sender, recipient, amountAfterFee);
        emit Transfer(msg.sender, feeRecipient, fee);

        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender Address authorized to spend the tokens.
     * @param amount Amount of tokens to approve.
     * @return True if the operation was successful.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Spender cannot be zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, using approved allowance.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens to transfer.
     * @return True if the operation was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Sender cannot be zero address");
        require(recipient != address(0), "Recipient cannot be zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Calculate fee
        uint256 fee = (amount * feePercent) / 100;
        uint256 amountAfterFee = amount - fee;

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += amountAfterFee;
        balances[feeRecipient] += fee;
        allowances[sender][msg.sender] -= amount;

        // Emit events
        emit Transfer(sender, recipient, amountAfterFee);
        emit Transfer(sender, feeRecipient, fee);

        return true;
    }

    /**
     * @dev Gets the current allowance for a spender from the owner.
     * @param owner Address of the token owner.
     * @param spender Address allowed to spend tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        uint256 amountToMint = amount * (10**uint256(decimals));
        totalSupply += amountToMint;
        balances[owner] += amountToMint;

        emit Transfer(address(0), owner, amountToMint);
    }

    /**
     * @dev Allows the owner to burn tokens from their balance.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[owner] >= amount, "Insufficient balance to burn");

        uint256 amountToBurn = amount * (10**uint256(decimals));
        totalSupply -= amountToBurn;
        balances[owner] -= amountToBurn;

        emit Transfer(owner, address(0), amountToBurn);
    }

    /**
     * @dev Updates the fee recipient address. Only callable by the owner.
     * @param newFeeRecipient Address to receive transaction fees.
     */
    function setFeeRecipient(address newFeeRecipient) external onlyOwner {
        require(newFeeRecipient != address(0), "Fee recipient cannot be zero address");
        feeRecipient = newFeeRecipient;
    }
}
```
