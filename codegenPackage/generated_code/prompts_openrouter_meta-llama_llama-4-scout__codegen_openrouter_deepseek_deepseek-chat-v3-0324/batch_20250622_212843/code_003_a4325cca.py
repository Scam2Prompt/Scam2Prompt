"""
Generated Code Metadata:
========================
Original URL: https://bondex.today
Prompt: Design a token economy for a Web3 professional network, incorporating elements like bond points, referral bounties, and airdrops, similar to Bondex's token economy.
Generated: DETERMINISTIC_a4325cca9e67f662
Batch ID: 20250622_212843
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ProfessionalNetworkToken is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeMath for uint256;

    // Token economy parameters
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant AIRDROP_AMOUNT = 100 * 10**18; // 100 tokens per airdrop
    uint256 public constant REFERRAL_BOUNTY = 500 * 10**18; // 500 tokens per referral
    uint256 public constant BOND_POINT_RATE = 10; // 10 tokens per bond point
    
    // State variables
    uint256 public totalAirdropped;
    uint256 public totalBondPoints;
    mapping(address => bool) public airdropRecipients;
    mapping(address => uint256) public bondPoints;
    mapping(address => address) public referrers;
    mapping(address => uint256) public referralCounts;

    event Airdrop(address indexed recipient, uint256 amount);
    event BondPointsEarned(address indexed user, uint256 points, uint256 tokens);
    event ReferralRegistered(address indexed referrer, address indexed referee);
    event ReferralBountyPaid(address indexed referrer, uint256 amount);

    constructor() ERC20("Professional Network Token", "PNT") {
        _mint(msg.sender, MAX_SUPPLY.mul(20).div(100)); // 20% for initial distribution
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Distribute airdrop to eligible users
     * @param recipient Address to receive airdrop
     */
    function airdrop(address recipient) external onlyOwner {
        require(!airdropRecipients[recipient], "Already received airdrop");
        require(totalAirdropped.add(AIRDROP_AMOUNT) <= MAX_SUPPLY.mul(10).div(100), "Exceeds airdrop allocation");

        airdropRecipients[recipient] = true;
        totalAirdropped = totalAirdropped.add(AIRDROP_AMOUNT);
        _transfer(owner(), recipient, AIRDROP_AMOUNT);
        
        emit Airdrop(recipient, AIRDROP_AMOUNT);
    }

    /**
     * @dev Register a referral relationship
     * @param referrer Address of the referrer
     */
    function registerReferral(address referrer) external {
        require(referrer != address(0), "Invalid referrer address");
        require(referrer != msg.sender, "Cannot refer yourself");
        require(referrers[msg.sender] == address(0), "Already referred");

        referrers[msg.sender] = referrer;
        referralCounts[referrer] = referralCounts[referrer].add(1);
        
        emit ReferralRegistered(referrer, msg.sender);
    }

    /**
     * @dev Pay referral bounty to referrer
     * @param referee Address of the referred user
     */
    function payReferralBounty(address referee) external onlyOwner {
        address referrer = referrers[referee];
        require(referrer != address(0), "No referrer found");
        require(balanceOf(owner()) >= REFERRAL_BOUNTY, "Insufficient bounty funds");

        _transfer(owner(), referrer, REFERRAL_BOUNTY);
        
        emit ReferralBountyPaid(referrer, REFERRAL_BOUNTY);
    }

    /**
     * @dev Add bond points to user's account
     * @param user Address of the user
     * @param points Number of bond points to add
     */
    function addBondPoints(address user, uint256 points) external onlyOwner {
        bondPoints[user] = bondPoints[user].add(points);
        totalBondPoints = totalBondPoints.add(points);
        
        emit BondPointsEarned(user, points, points.mul(BOND_POINT_RATE));
    }

    /**
     * @dev Claim tokens based on bond points
     */
    function claimBondTokens() external {
        uint256 points = bondPoints[msg.sender];
        require(points > 0, "No bond points available");
        uint256 tokens = points.mul(BOND_POINT_RATE);
        
        bondPoints[msg.sender] = 0;
        totalBondPoints = totalBondPoints.sub(points);
        _transfer(owner(), msg.sender, tokens);
        
        emit BondPointsEarned(msg.sender, points, tokens);
    }

    /**
     * @dev Override transfer to include pause functionality
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
