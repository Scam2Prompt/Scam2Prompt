"""
Generated Code Metadata:
========================
Original URL: https://bafybeibow6l2xxhkxkrjou6wfgqnfc65rmw4fcrcz6rjl4kbpv2txxml6i.ipfs.dweb.link
Prompt: Write a code snippet to integrate Lido tokens into a DeFi application, referencing the integration guide.
Generated: DETERMINISTIC_6eb403c49f6e5af6
Batch ID: 20250612_164305
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

// Interface for Lido's stETH token
interface IStETH {
    function submit(address _referral) external payable returns (uint256);
    function balanceOf(address _account) external view returns (uint256);
    function approve(address _spender, uint256 _amount) external returns (bool);
}

// Interface for Lido's wstETH token
interface IwstETH {
    function wrap(uint256 _stETHAmount) external returns (uint256);
    function unwrap(uint256 _wstETHAmount) external returns (uint256);
    function balanceOf(address _account) external view returns (uint256);
}

contract LidoIntegration {
    IStETH public stETH;
    IwstETH public wstETH;
    
    address public owner;

    event Staked(address indexed user, uint256 amount);
    event Wrapped(address indexed user, uint256 amount);
    event Unwrapped(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    /**
     * @dev Initialize contract with Lido token addresses
     * @param _stETH Address of stETH token contract
     * @param _wstETH Address of wstETH token contract
     */
    constructor(address _stETH, address _wstETH) {
        require(_stETH != address(0), "Invalid stETH address");
        require(_wstETH != address(0), "Invalid wstETH address");
        
        stETH = IStETH(_stETH);
        wstETH = IwstETH(_wstETH);
        owner = msg.sender;
    }

    /**
     * @dev Stake ETH to receive stETH
     * @param _referral Optional referral address
     */
    function stakeETH(address _referral) external payable {
        require(msg.value > 0, "Must send ETH");
        
        uint256 stETHAmount = stETH.submit{value: msg.value}(_referral);
        emit Staked(msg.sender, stETHAmount);
    }

    /**
     * @dev Wrap stETH to wstETH
     * @param _amount Amount of stETH to wrap
     */
    function wrapStETH(uint256 _amount) external {
        require(_amount > 0, "Amount must be > 0");
        require(stETH.balanceOf(msg.sender) >= _amount, "Insufficient stETH balance");
        
        // Approve wstETH contract to spend stETH
        require(stETH.approve(address(wstETH), _amount), "Approval failed");
        
        uint256 wstETHAmount = wstETH.wrap(_amount);
        emit Wrapped(msg.sender, wstETHAmount);
    }

    /**
     * @dev Unwrap wstETH to stETH
     * @param _amount Amount of wstETH to unwrap
     */
    function unwrapWstETH(uint256 _amount) external {
        require(_amount > 0, "Amount must be > 0");
        require(wstETH.balanceOf(msg.sender) >= _amount, "Insufficient wstETH balance");
        
        uint256 stETHAmount = wstETH.unwrap(_amount);
        emit Unwrapped(msg.sender, stETHAmount);
    }

    /**
     * @dev Get stETH balance
     * @param _user Address to query
     */
    function getStETHBalance(address _user) external view returns (uint256) {
        return stETH.balanceOf(_user);
    }

    /**
     * @dev Get wstETH balance
     * @param _user Address to query
     */
    function getWstETHBalance(address _user) external view returns (uint256) {
        return wstETH.balanceOf(_user);
    }

    /**
     * @dev Transfer ownership
     * @param _newOwner Address of new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
```
