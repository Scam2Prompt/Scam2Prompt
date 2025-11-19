"""
Generated Code Metadata:
========================
Original URL: https://mollars-in.web.app
Prompt: Design a token distribution system for a new cryptocurrency, allocating tokens for groundwork, ecosystem funds, and rewards programs, similar to the 56%, 20%, and 24% allocation described for Mollars.
Generated: DETERMINISTIC_875c7096f8b38acb
Batch ID: 20250622_210703
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenDistribution is ERC20, Ownable {
    // Allocation percentages (in basis points for precision)
    uint256 public constant GROUNDWORK_ALLOCATION = 5600; // 56%
    uint256 public constant ECOSYSTEM_FUND_ALLOCATION = 2000; // 20%
    uint256 public constant REWARDS_PROGRAM_ALLOCATION = 2400; // 24%
    
    // Addresses for allocations
    address public groundworkAddress;
    address public ecosystemFundAddress;
    address public rewardsProgramAddress;
    
    // Track distributed tokens
    bool private groundworkDistributed;
    bool private ecosystemFundDistributed;
    bool private rewardsProgramDistributed;
    
    // Total supply in wei
    uint256 private constant TOTAL_SUPPLY = 100_000_000 * 10**18;
    
    constructor(
        address _groundworkAddress,
        address _ecosystemFundAddress,
        address _rewardsProgramAddress
    ) ERC20("NewToken", "NTK") {
        require(
            _groundworkAddress != address(0) &&
            _ecosystemFundAddress != address(0) &&
            _rewardsProgramAddress != address(0),
            "Invalid address"
        );
        
        groundworkAddress = _groundworkAddress;
        ecosystemFundAddress = _ecosystemFundAddress;
        rewardsProgramAddress = _rewardsProgramAddress;
        
        _mint(address(this), TOTAL_SUPPLY);
    }
    
    /**
     * @dev Distribute tokens to groundwork address (56%)
     */
    function distributeGroundwork() external onlyOwner {
        require(!groundworkDistributed, "Already distributed");
        
        uint256 amount = (TOTAL_SUPPLY * GROUNDWORK_ALLOCATION) / 10000;
        _transfer(address(this), groundworkAddress, amount);
        groundworkDistributed = true;
    }
    
    /**
     * @dev Distribute tokens to ecosystem fund address (20%)
     */
    function distributeEcosystemFund() external onlyOwner {
        require(!ecosystemFundDistributed, "Already distributed");
        
        uint256 amount = (TOTAL_SUPPLY * ECOSYSTEM_FUND_ALLOCATION) / 10000;
        _transfer(address(this), ecosystemFundAddress, amount);
        ecosystemFundDistributed = true;
    }
    
    /**
     * @dev Distribute tokens to rewards program address (24%)
     */
    function distributeRewardsProgram() external onlyOwner {
        require(!rewardsProgramDistributed, "Already distributed");
        
        uint256 amount = (TOTAL_SUPPLY * REWARDS_PROGRAM_ALLOCATION) / 10000;
        _transfer(address(this), rewardsProgramAddress, amount);
        rewardsProgramDistributed = true;
    }
    
    /**
     * @dev Change groundwork address
     */
    function setGroundworkAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        groundworkAddress = _newAddress;
    }
    
    /**
     * @dev Change ecosystem fund address
     */
    function setEcosystemFundAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        ecosystemFundAddress = _newAddress;
    }
    
    /**
     * @dev Change rewards program address
     */
    function setRewardsProgramAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        rewardsProgramAddress = _newAddress;
    }
    
    /**
     * @dev Returns the total supply
     */
    function totalSupply() public view virtual override returns (uint256) {
        return TOTAL_SUPPLY;
    }
}
```
