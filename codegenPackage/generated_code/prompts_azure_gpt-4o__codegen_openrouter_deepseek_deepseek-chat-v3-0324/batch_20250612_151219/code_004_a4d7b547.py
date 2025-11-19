"""
Generated Code Metadata:
========================
Original URL: https://ackinacki-air.live
Prompt: Develop a decentralized application (dApp) on Acki Nacki that leverages its gas-free transaction feature and integrates tokenomics for $NACKL and $SHELL.
Generated: DETERMINISTIC_a4d7b547a69d3390
Batch ID: 20250612_151219
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

interface IAckiNacki {
    function isGasFreeTransaction(address sender) external view returns (bool);
}

contract NackiDApp is Ownable, ReentrancyGuard {
    IERC20 public nacklToken;
    IERC20 public shellToken;
    IAckiNacki public ackiNackiNetwork;

    uint256 public constant NACKL_REWARD_RATE = 10; // 10 NACKL per action
    uint256 public constant SHELL_BURN_RATE = 1; // 1 SHELL burned per action
    uint256 public constant ACTION_COOLDOWN = 1 days;

    mapping(address => uint256) public lastActionTimestamp;
    mapping(address => uint256) public userRewards;

    event ActionPerformed(address indexed user, uint256 nacklRewarded, uint256 shellBurned);
    event RewardsClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 nacklAmount, uint256 shellAmount);

    constructor(
        address _nacklTokenAddress,
        address _shellTokenAddress,
        address _ackiNackiNetworkAddress
    ) {
        nacklToken = IERC20(_nacklTokenAddress);
        shellToken = IERC20(_shellTokenAddress);
        ackiNackiNetwork = IAckiNacki(_ackiNackiNetworkAddress);
    }

    modifier onlyGasFree() {
        require(ackiNackiNetwork.isGasFreeTransaction(msg.sender), "NackiDApp: Only gas-free transactions allowed");
        _;
    }

    modifier cooldownCheck() {
        require(
            block.timestamp >= lastActionTimestamp[msg.sender] + ACTION_COOLDOWN,
            "NackiDApp: Action cooldown not passed"
        );
        _;
    }

    function performAction() external onlyGasFree cooldownCheck nonReentrant {
        require(
            shellToken.balanceOf(msg.sender) >= SHELL_BURN_RATE,
            "NackiDApp: Insufficient SHELL balance"
        );

        // Burn SHELL tokens
        shellToken.transferFrom(msg.sender, address(this), SHELL_BURN_RATE);
        
        // Reward NACKL tokens
        userRewards[msg.sender] += NACKL_REWARD_RATE;
        lastActionTimestamp[msg.sender] = block.timestamp;

        emit ActionPerformed(msg.sender, NACKL_REWARD_RATE, SHELL_BURN_RATE);
    }

    function claimRewards() external nonReentrant {
        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "NackiDApp: No rewards to claim");

        userRewards[msg.sender] = 0;
        require(
            nacklToken.transfer(msg.sender, rewards),
            "NackiDApp: Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    function withdrawTokens(uint256 nacklAmount, uint256 shellAmount) external onlyOwner {
        if (nacklAmount > 0) {
            require(
                nacklToken.transfer(owner(), nacklAmount),
                "NackiDApp: NACKL withdrawal failed"
            );
        }

        if (shellAmount > 0) {
            require(
                shellToken.transfer(owner(), shellAmount),
                "NackiDApp: SHELL withdrawal failed"
            );
        }

        emit TokensWithdrawn(owner(), nacklAmount, shellAmount);
    }

    function setTokenAddresses(address _nacklTokenAddress, address _shellTokenAddress) external onlyOwner {
        require(_nacklTokenAddress != address(0), "NackiDApp: Invalid NACKL address");
        require(_shellTokenAddress != address(0), "NackiDApp: Invalid SHELL address");
        
        nacklToken = IERC20(_nacklTokenAddress);
        shellToken = IERC20(_shellTokenAddress);
    }

    function setAckiNackiNetwork(address _ackiNackiNetworkAddress) external onlyOwner {
        require(_ackiNackiNetworkAddress != address(0), "NackiDApp: Invalid network address");
        ackiNackiNetwork = IAckiNacki(_ackiNackiNetworkAddress);
    }
}
```
