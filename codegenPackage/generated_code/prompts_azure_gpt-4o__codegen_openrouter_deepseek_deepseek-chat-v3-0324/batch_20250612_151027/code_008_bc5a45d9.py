"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Generate code for building a decentralized application (dApp) that uses Moxie Protocol to convert followers into paid fans with exclusive benefits.
Generated: DETERMINISTIC_bc5a45d94d9a4d24
Batch ID: 20250612_151027
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

interface IMoxieProtocol {
    function createSubscription(
        address subscriber,
        address creator,
        uint256 amount,
        uint256 frequency,
        uint256 duration
    ) external returns (uint256);
    
    function cancelSubscription(uint256 subscriptionId) external;
}

contract FanMembership is Ownable, ReentrancyGuard {
    IERC20 public paymentToken;
    IMoxieProtocol public moxieProtocol;
    
    struct MembershipTier {
        uint256 price;
        uint256 frequency; // in seconds
        uint256 duration; // in seconds
        string benefits;
    }
    
    struct Subscription {
        uint256 tierId;
        uint256 subscriptionId;
        uint256 startTime;
        bool active;
    }
    
    mapping(uint256 => MembershipTier) public tiers;
    mapping(address => Subscription) public userSubscriptions;
    mapping(address => bool) public creators;
    
    uint256 public nextTierId = 1;
    
    event TierCreated(uint256 tierId, uint256 price, string benefits);
    event Subscribed(address user, uint256 tierId, uint256 subscriptionId);
    event Unsubscribed(address user, uint256 subscriptionId);
    event CreatorAdded(address creator);
    event CreatorRemoved(address creator);
    
    constructor(address _paymentToken, address _moxieProtocol) {
        paymentToken = IERC20(_paymentToken);
        moxieProtocol = IMoxieProtocol(_moxieProtocol);
    }
    
    modifier onlyCreator() {
        require(creators[msg.sender], "Not an authorized creator");
        _;
    }
    
    function addCreator(address _creator) external onlyOwner {
        creators[_creator] = true;
        emit CreatorAdded(_creator);
    }
    
    function removeCreator(address _creator) external onlyOwner {
        creators[_creator] = false;
        emit CreatorRemoved(_creator);
    }
    
    function createTier(
        uint256 _price,
        uint256 _frequency,
        uint256 _duration,
        string memory _benefits
    ) external onlyCreator {
        require(_price > 0, "Price must be greater than 0");
        require(_frequency > 0, "Frequency must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        
        uint256 tierId = nextTierId++;
        tiers[tierId] = MembershipTier({
            price: _price,
            frequency: _frequency,
            duration: _duration,
            benefits: _benefits
        });
        
        emit TierCreated(tierId, _price, _benefits);
    }
    
    function subscribe(uint256 _tierId) external nonReentrant {
        require(tiers[_tierId].price > 0, "Invalid tier");
        require(userSubscriptions[msg.sender].active == false, "Already subscribed");
        
        MembershipTier memory tier = tiers[_tierId];
        
        require(
            paymentToken.allowance(msg.sender, address(this)) >= tier.price,
            "Insufficient allowance"
        );
        
        require(
            paymentToken.transferFrom(msg.sender, address(this), tier.price),
            "Payment failed"
        );
        
        uint256 subscriptionId = moxieProtocol.createSubscription(
            msg.sender,
            owner(),
            tier.price,
            tier.frequency,
            tier.duration
        );
        
        userSubscriptions[msg.sender] = Subscription({
            tierId: _tierId,
            subscriptionId: subscriptionId,
            startTime: block.timestamp,
            active: true
        });
        
        emit Subscribed(msg.sender, _tierId, subscriptionId);
    }
    
    function unsubscribe() external nonReentrant {
        Subscription storage sub = userSubscriptions[msg.sender];
        require(sub.active, "No active subscription");
        
        moxieProtocol.cancelSubscription(sub.subscriptionId);
        sub.active = false;
        
        emit Unsubscribed(msg.sender, sub.subscriptionId);
    }
    
    function getUserSubscription(address _user) external view returns (
        uint256 tierId,
        uint256 subscriptionId,
        uint256 startTime,
        bool active,
        string memory benefits
    ) {
        Subscription memory sub = userSubscriptions[_user];
        if (sub.active) {
            MembershipTier memory tier = tiers[sub.tierId];
            return (
                sub.tierId,
                sub.subscriptionId,
                sub.startTime,
                sub.active,
                tier.benefits
            );
        }
        return (0, 0, 0, false, "");
    }
    
    function withdrawFunds() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(paymentToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
