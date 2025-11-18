"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Create a smart contract in Solidity for a utility token like Lingo, ensuring it includes functionality for interacting with a Community DAO to select RWA investments.
Generated: DETERMINISTIC_29f0d314d29e4daa
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

/**
 * @title LingoToken
 * @dev ERC20-compliant utility token with integration to a Community DAO for Real-World Asset (RWA) investment selection.
 */
contract LingoToken {
    // Token details
    string public name = "LingoToken";
    string public symbol = "LINGO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // DAO contract address
    address public communityDAO;

    // Ownership control
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event DAOUpdated(address indexed oldDAO, address indexed newDAO);
    event InvestmentProposalSubmitted(address indexed proposer, string proposalDetails);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyDAO() {
        require(msg.sender == communityDAO, "Caller is not the DAO");
        _;
    }

    /**
     * @dev Constructor to set initial supply and owner.
     * @param initialSupply Initial token supply.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10**uint256(decimals));
        balances[msg.sender] = totalSupply;
        owner = msg.sender;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param to Recipient address.
     * @param value Amount to transfer.
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the caller.
     * @param spender Address authorized to spend.
     * @param value Amount authorized.
     */
    function approve(address spender, uint256 value) external returns (bool) {
        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another, utilizing allowances.
     * @param from Sender address.
     * @param to Recipient address.
     * @param value Amount to transfer.
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        allowances[from][msg.sender] -= value;
        balances[from] -= value;
        balances[to] += value;
        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @dev Retrieve the balance of a specific address.
     * @param account Address to query balance.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Retrieve the allowance of a spender for a given owner.
     * @param owner Token owner address.
     * @param spender Address authorized to spend.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Update the address of the Community DAO.
     * @param newDAO Address of the new DAO.
     */
    function setCommunityDAO(address newDAO) external onlyOwner {
        require(newDAO != address(0), "Invalid DAO address");
        address oldDAO = communityDAO;
        communityDAO = newDAO;
        emit DAOUpdated(oldDAO, newDAO);
    }

    /**
     * @dev Submit an investment proposal to the DAO.
     * @param proposalDetails Description or metadata of the investment proposal.
     */
    function submitInvestmentProposal(string calldata proposalDetails) external {
        require(bytes(proposalDetails).length > 0, "Proposal details cannot be empty");
        emit InvestmentProposalSubmitted(msg.sender, proposalDetails);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
