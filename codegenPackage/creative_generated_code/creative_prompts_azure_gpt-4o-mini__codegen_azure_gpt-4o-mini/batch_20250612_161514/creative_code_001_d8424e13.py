"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.firebaseapp.com
Prompt: Write a code snippet for integrating the USUAL protocol's governance features into a DeFi application, focusing on the Long-Term Value Token.
Generated: DETERMINISTIC_d8424e13313ab406
Batch ID: 20250612_161514
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

// Import necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the USUAL protocol governance
interface IUsualGovernance {
    function propose(string memory proposal) external;
    function vote(uint proposalId, bool support) external;
    function execute(uint proposalId) external;
}

// Long-Term Value Token contract
contract LongTermValueToken is IERC20, Ownable {
    string public constant name = "LongTermValueToken";
    string public constant symbol = "LTVT";
    uint8 public constant decimals = 18;
    uint256 private _totalSupply;

    // Mapping of balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Governance contract instance
    IUsualGovernance public governance;

    // Events
    event GovernanceChanged(address indexed newGovernance);

    // Constructor to set initial supply and governance contract
    constructor(uint256 initialSupply, address governanceAddress) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply;
        governance = IUsualGovernance(governanceAddress);
    }

    // Function to change governance contract
    function changeGovernance(address newGovernance) external onlyOwner {
        require(newGovernance != address(0), "New governance address cannot be zero");
        governance = IUsualGovernance(newGovernance);
        emit GovernanceChanged(newGovernance);
    }

    // ERC20 implementation functions
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Governance features
    function proposeGovernanceChange(string memory proposal) external onlyOwner {
        governance.propose(proposal);
    }

    function voteOnProposal(uint proposalId, bool support) external {
        governance.vote(proposalId, support);
    }

    function executeProposal(uint proposalId) external onlyOwner {
        governance.execute(proposalId);
    }
}
```
