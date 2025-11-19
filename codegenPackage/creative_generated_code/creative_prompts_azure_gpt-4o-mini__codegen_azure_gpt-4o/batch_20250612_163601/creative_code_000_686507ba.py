"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-hat.fund
Prompt: Generate a smart contract for the $MAGA token on the Ethereum network, incorporating features like 0% tax and community-driven governance.
Generated: DETERMINISTIC_686507ba249eb8cd
Batch ID: 20250612_163601
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
 * @title MAGA Token Smart Contract
 * @dev Implementation of a community-driven ERC20 token with 0% transaction tax.
 */
contract MAGAToken {
    // ERC20 Token Details
    string public constant name = "$MAGA Token";
    string public constant symbol = "MAGA";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping for tracking balances
    mapping(address => uint256) private balances;
    // Mapping for tracking allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Governance-related variables
    address public governance; // Address of the governance contract or account
    mapping(address => bool) public isAdmin; // Admins for community-driven governance

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event AdminAdded(address indexed account);
    event AdminRemoved(address indexed account);
    event GovernanceTransferred(address indexed previousGovernance, address indexed newGovernance);

    /**
     * @dev Modifier to restrict access to the governance address.
     */
    modifier onlyGovernance() {
        require(msg.sender == governance, "MAGA: caller is not governance");
        _;
    }

    /**
     * @dev Modifier to restrict access to admin accounts.
     */
    modifier onlyAdmin() {
        require(isAdmin[msg.sender], "MAGA: caller is not an admin");
        _;
    }

    /**
     * @dev Constructor to initialize the token.
     * @param _initialSupply The initial token supply.
     */
    constructor(uint256 _initialSupply) {
        governance = msg.sender; // Set the deployer as the initial governance
        isAdmin[msg.sender] = true; // Add the deployer as an initial admin
        mint(msg.sender, _initialSupply); // Mint initial supply
    }

    /**
     * @dev Transfer function for token holders.
     * @param recipient Address to receive the tokens.
     * @param amount Number of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "MAGA: transfer to zero address");
        require(balances[msg.sender] >= amount, "MAGA: insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param spender Address allowed to spend.
     * @param amount Number of tokens approved for spending.
     * @return Success status of the approval.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one account to another using allowance mechanism.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Number of tokens to transfer.
     * @return Success status of the transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "MAGA: transfer from zero address");
        require(recipient != address(0), "MAGA: transfer to zero address");
        require(balances[sender] >= amount, "MAGA: insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "MAGA: allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get balance of a specific account.
     * @param account Address of the account.
     * @return Token balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Mint new tokens.
     * @param account Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address account, uint256 amount) public onlyGovernance {
        require(account != address(0), "MAGA: mint to zero address");
        totalSupply += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Burn tokens from an account.
     * @param account Address of the account to burn tokens from.
     * @param amount Number of tokens to burn.
     */
    function burn(address account, uint256 amount) public onlyGovernance {
        require(account != address(0), "MAGA: burn from zero address");
        require(balances[account] >= amount, "MAGA: insufficient balance to burn");

        balances[account] -= amount;
        totalSupply -= amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @dev Add a new admin account for governance.
     * @param account Address of the new admin.
     */
    function addAdmin(address account) external onlyGovernance {
        require(!isAdmin[account], "MAGA: account is already an admin");
        isAdmin[account] = true;
        emit AdminAdded(account);
    }

    /**
     * @dev Remove an admin account.
     * @param account Address of the admin to remove.
     */
    function removeAdmin(address account) external onlyGovernance {
        require(isAdmin[account], "MAGA: account is not an admin");
        isAdmin[account] = false;
        emit AdminRemoved(account);
    }

    /**
     * @dev Transfer governance to a new address.
     * @param newGovernance Address of the new governance.
     */
    function transferGovernance(address newGovernance) external onlyGovernance {
        require(newGovernance != address(0), "MAGA: new governance is zero address");
        emit GovernanceTransferred(governance, newGovernance);
        governance = newGovernance;
    }
}
```
