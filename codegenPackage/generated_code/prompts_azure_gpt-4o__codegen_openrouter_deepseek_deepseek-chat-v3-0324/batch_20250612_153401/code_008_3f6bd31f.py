"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a test suite in Solidity to verify that the "$JESSE" presale smart contract enforces the presale cap of 1000 BASE and correctly calculates token distribution based on tiered pricing.
Generated: DETERMINISTIC_3f6bd31fde99dc36
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "forge-std/Test.sol";

contract JessePresaleTest is Test {
    using SafeMath for uint256;

    // Mock contract interfaces
    IERC20 public baseToken;
    IERC20 public jesseToken;

    // Presale contract to test
    address public presaleContract;

    // Test constants
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 BASE
    uint256 public constant TIER1_PRICE = 0.001 ether; // 0.001 BASE per token
    uint256 public constant TIER2_PRICE = 0.002 ether; // 0.002 BASE per token
    uint256 public constant TIER3_PRICE = 0.003 ether; // 0.003 BASE per token

    // Tier thresholds
    uint256 public constant TIER1_MAX = 500 ether;
    uint256 public constant TIER2_MAX = 800 ether;
    
    // Events from presale contract (if any)
    event TokensPurchased(address indexed buyer, uint256 baseAmount, uint256 tokenAmount);

    function setUp() public {
        // Deploy mock tokens
        baseToken = IERC20(address(new MockERC20("BASE", "BASE", 18)));
        jesseToken = IERC20(address(new MockERC20("JESSE", "JESSE", 18)));

        // Deploy presale contract (replace with actual constructor params)
        presaleContract = address(new JessePresale(
            address(baseToken),
            address(jesseToken),
            PRESALE_CAP,
            TIER1_PRICE,
            TIER2_PRICE,
            TIER3_PRICE,
            TIER1_MAX,
            TIER2_MAX
        ));

        // Fund presale contract with JESSE tokens
        uint256 initialSupply = 10_000_000 ether;
        MockERC20(address(jesseToken)).mint(presaleContract, initialSupply);
    }

    function testPresaleCapEnforcement() public {
        // Attempt to contribute more than the presale cap
        uint256 overCapAmount = PRESALE_CAP + 1 ether;
        baseToken.approve(presaleContract, overCapAmount);

        vm.expectRevert("Presale cap reached");
        JessePresale(presaleContract).buyTokens(overCapAmount);
    }

    function testTier1Pricing() public {
        uint256 contribution = 100 ether; // Within Tier 1
        uint256 expectedTokens = contribution.div(TIER1_PRICE);

        baseToken.approve(presaleContract, contribution);
        
        vm.expectEmit(true, true, true, true);
        emit TokensPurchased(address(this), contribution, expectedTokens);
        
        JessePresale(presaleContract).buyTokens(contribution);
        
        uint256 balance = jesseToken.balanceOf(address(this));
        assertEq(balance, expectedTokens, "Incorrect Tier 1 token amount");
    }

    function testTier2Pricing() public {
        // First fill Tier 1
        uint256 tier1Contribution = TIER1_MAX;
        baseToken.approve(presaleContract, tier1Contribution);
        JessePresale(presaleContract).buyTokens(tier1Contribution);

        // Test Tier 2 pricing
        uint256 tier2Contribution = 100 ether; // 100 BASE in Tier 2
        uint256 expectedTokens = tier2Contribution.div(TIER2_PRICE);

        baseToken.approve(presaleContract, tier2Contribution);
        JessePresale(presaleContract).buyTokens(tier2Contribution);
        
        uint256 balance = jesseToken.balanceOf(address(this));
        assertEq(balance, tier1Contribution.div(TIER1_PRICE) + expectedTokens, "Incorrect Tier 2 token amount");
    }

    function testTier3Pricing() public {
        // First fill Tier 1 and Tier 2
        uint256 tier1Contribution = TIER1_MAX;
        uint256 tier2Contribution = TIER2_MAX.sub(TIER1_MAX);
        
        baseToken.approve(presaleContract, tier1Contribution.add(tier2Contribution));
        JessePresale(presaleContract).buyTokens(tier1Contribution.add(tier2Contribution));

        // Test Tier 3 pricing
        uint256 tier3Contribution = 100 ether; // 100 BASE in Tier 3
        uint256 expectedTokens = tier3Contribution.div(TIER3_PRICE);

        baseToken.approve(presaleContract, tier3Contribution);
        JessePresale(presaleContract).buyTokens(tier3Contribution);
        
        uint256 balance = jesseToken.balanceOf(address(this));
        uint256 totalExpected = tier1Contribution.div(TIER1_PRICE)
                              .add(tier2Contribution.div(TIER2_PRICE))
                              .add(expectedTokens);
        assertEq(balance, totalExpected, "Incorrect Tier 3 token amount");
    }

    function testMultipleContributionsAcrossTiers() public {
        // Contribution 1: Tier 1
        uint256 contribution1 = 300 ether;
        uint256 expected1 = contribution1.div(TIER1_PRICE);
        baseToken.approve(presaleContract, contribution1);
        JessePresale(presaleContract).buyTokens(contribution1);

        // Contribution 2: Pushes into Tier 2
        uint256 contribution2 = 250 ether; // 300 + 250 = 550 (50 in Tier 2)
        uint256 expected2 = 200 ether.div(TIER1_PRICE) // Remaining Tier 1
                            .add(50 ether.div(TIER2_PRICE)); // Tier 2 part
        baseToken.approve(presaleContract, contribution2);
        JessePresale(presaleContract).buyTokens(contribution2);

        // Contribution 3: Pure Tier 3
        uint256 contribution3 = 200 ether;
        uint256 expected3 = contribution3.div(TIER3_PRICE);
        baseToken.approve(presaleContract, contribution3);
        JessePresale(presaleContract).buyTokens(contribution3);

        uint256 balance = jesseToken.balanceOf(address(this));
        uint256 totalExpected = expected1.add(expected2).add(expected3);
        assertEq(balance, totalExpected, "Incorrect total tokens across tiers");
    }

    function testPresaleCapReached() public {
        // Fill the entire presale cap
        baseToken.approve(presaleContract, PRESALE_CAP);
        JessePresale(presaleContract).buyTokens(PRESALE_CAP);

        // Attempt to contribute after cap is reached
        uint256 smallContribution = 1 ether;
        baseToken.approve(presaleContract, smallContribution);

        vm.expectRevert("Presale cap reached");
        JessePresale(presaleContract).buyTokens(smallContribution);
    }
}

// Mock ERC20 for testing
contract MockERC20 is IERC20 {
    using SafeMath for uint256;

    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    constructor(string memory _name, string memory _symbol, uint8 _decimals) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
    }

    function mint(address to, uint256 amount) public {
        balanceOf[to] = balanceOf[to].add(amount);
        totalSupply = totalSupply.add(amount);
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        allowance[msg.sender][spender] = amount;
        return true;
    }

    function transfer(address to, uint256 amount) public override returns (bool) {
        balanceOf[msg.sender] = balanceOf[msg.sender].sub(amount);
        balanceOf[to] = balanceOf[to].add(amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        allowance[from][msg.sender] = allowance[from][msg.sender].sub(amount);
        balanceOf[from] = balanceOf[from].sub(amount);
        balanceOf[to] = balanceOf[to].add(amount);
        return true;
    }
}

// Minimal interface of the actual presale contract for testing
abstract contract JessePresale {
    function buyTokens(uint256 baseAmount) public virtual;
}
```
