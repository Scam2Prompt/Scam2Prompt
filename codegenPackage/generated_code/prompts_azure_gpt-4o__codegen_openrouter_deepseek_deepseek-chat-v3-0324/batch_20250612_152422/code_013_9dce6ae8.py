"""
Generated Code Metadata:
========================
Original URL: https://raca3-2.pages.dev
Prompt: Create a function to enable staking of $RACA tokens in a blockchain-based game to unlock special roles like "Inspector" or "Silencer."
Generated: DETERMINISTIC_9dce6ae8b779c6c4
Batch ID: 20250612_152422
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RACAStaking is Ownable, ReentrancyGuard {
    IERC20 public racaToken;
    
    struct Role {
        string name;
        uint256 requiredStake;
        bool exists;
    }
    
    struct Staker {
        uint256 amountStaked;
        uint256 stakingStartTime;
        string[] unlockedRoles;
    }
    
    mapping(string => Role) public roles;
    mapping(address => Staker) public stakers;
    
    event RoleAdded(string roleName, uint256 requiredStake);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RoleUnlocked(address indexed user, string roleName);
    
    constructor(address _racaTokenAddress) {
        require(_racaTokenAddress != address(0), "Invalid token address");
        racaToken = IERC20(_racaTokenAddress);
        
        // Initialize with default roles
        _addRole("Inspector", 10000 * 10**18); // 10,000 RACA
        _addRole("Silencer", 50000 * 10**18); // 50,000 RACA
    }
    
    function addRole(string memory _roleName, uint256 _requiredStake) external onlyOwner {
        _addRole(_roleName, _requiredStake);
    }
    
    function _addRole(string memory _roleName, uint256 _requiredStake) internal {
        require(!roles[_roleName].exists, "Role already exists");
        require(_requiredStake > 0, "Stake amount must be positive");
        
        roles[_roleName] = Role({
            name: _roleName,
            requiredStake: _requiredStake,
            exists: true
        });
        
        emit RoleAdded(_roleName, _requiredStake);
    }
    
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        // Transfer tokens from user to contract
        bool success = racaToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");
        
        staker.amountStaked += _amount;
        staker.stakingStartTime = block.timestamp;
        
        // Check and unlock roles
        _checkRoleUnlocks(msg.sender);
        
        emit Staked(msg.sender, _amount);
    }
    
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");
        
        // Transfer tokens back to user
        bool success = racaToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");
        
        staker.amountStaked -= _amount;
        
        // Re-check roles after unstaking
        _checkRoleUnlocks(msg.sender);
        
        emit Unstaked(msg.sender, _amount);
    }
    
    function _checkRoleUnlocks(address _user) internal {
        Staker storage staker = stakers[_user];
        
        // Clear existing unlocked roles
        delete staker.unlockedRoles;
        
        // Check all roles for eligibility
        string[] memory roleNames = getRoleNames();
        for (uint i = 0; i < roleNames.length; i++) {
            Role storage role = roles[roleNames[i]];
            if (staker.amountStaked >= role.requiredStake) {
                staker.unlockedRoles.push(role.name);
                emit RoleUnlocked(_user, role.name);
            }
        }
    }
    
    function getRoleNames() public view returns (string[] memory) {
        // This is a simplified implementation. In production, you might want to maintain 
        // a separate array of role names for better efficiency.
        string[] memory roleNames = new string[](2);
        roleNames[0] = "Inspector";
        roleNames[1] = "Silencer";
        return roleNames;
    }
    
    function getUnlockedRoles(address _user) public view returns (string[] memory) {
        return stakers[_user].unlockedRoles;
    }
    
    function hasRole(address _user, string memory _roleName) public view returns (bool) {
        Staker storage staker = stakers[_user];
        for (uint i = 0; i < staker.unlockedRoles.length; i++) {
            if (keccak256(bytes(staker.unlockedRoles[i])) == keccak256(bytes(_roleName))) {
                return true;
            }
        }
        return false;
    }
    
    // Emergency function to recover accidentally sent tokens
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
