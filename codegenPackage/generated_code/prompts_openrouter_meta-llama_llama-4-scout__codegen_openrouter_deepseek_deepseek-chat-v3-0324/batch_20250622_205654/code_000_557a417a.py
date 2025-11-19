"""
Generated Code Metadata:
========================
Original URL: https://rsusi-aqaaa-aaaag-abhda-cai.ic0.app
Prompt: "Generate a smart contract for a decentralized finance (DeFi) application similar to ChapSwap Finance on the Internet Computer blockchain."
Generated: DETERMINISTIC_557a417a6aa93992
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```motoko
import Array "mo:base/Array";
import Buffer "mo:base/Buffer";
import HashMap "mo:base/HashMap";
import Iter "mo:base/Iter";
import Principal "mo:base/Principal";
import Result "mo:base/Result";
import Time "mo:base/Time";
import TrieMap "mo:base/TrieMap";

actor class ChapSwap() = this {
    // Token type representing fungible tokens
    public type Token = Principal;

    // User account type
    public type Account = {
        owner : Principal;
        tokens : HashMap.HashMap<Token, Nat>;
    };

    // Liquidity pool type
    public type Pool = {
        tokenA : Token;
        tokenB : Token;
        reserveA : Nat;
        reserveB : Nat;
        totalSupply : Nat;
    };

    // Swap event type
    public type SwapEvent = {
        caller : Principal;
        tokenIn : Token;
        tokenOut : Token;
        amountIn : Nat;
        amountOut : Nat;
        timestamp : Int;
    };

    // Error types
    public type Error = {
        #Unauthorized;
        #InsufficientBalance;
        #InsufficientLiquidity;
        #PoolExists;
        #PoolNotFound;
        #InvalidTokenPair;
        #TransferFailed;
    };

    // State variables
    private var accounts = TrieMap.TrieMap<Principal, Account>(Principal.equal, Principal.hash);
    private var pools = TrieMap.TrieMap<(Token, Token), Pool>(func (a, b) = a == b, func (a, b) = Principal.hash(a.0) + Principal.hash(a.1));
    private var swapEvents = Buffer.Buffer<SwapEvent>(0);

    // Initialize the contract with the creator as first account
    public shared(msg) func initialize() : async Result.Result<(), Error> {
        if (accounts.get(msg.caller) != null) {
            return #err(#Unauthorized);
        };

        let newAccount : Account = {
            owner = msg.caller;
            tokens = HashMap.HashMap<Token, Nat>(1, Principal.equal, Principal.hash);
        };

        accounts.put(msg.caller, newAccount);
        #ok(());
    };

    // Deposit tokens into user's account
    public shared(msg) func deposit(token : Token, amount : Nat) : async Result.Result<(), Error> {
        let account = switch (accounts.get(msg.caller)) {
            case null { return #err(#Unauthorized); };
            case (?acc) { acc };
        };

        let currentBalance = account.tokens.get(token);
        let newBalance = switch (currentBalance) {
            case null { amount };
            case (?bal) { bal + amount };
        };

        account.tokens.put(token, newBalance);
        #ok(());
    };

    // Withdraw tokens from user's account
    public shared(msg) func withdraw(token : Token, amount : Nat) : async Result.Result<(), Error> {
        let account = switch (accounts.get(msg.caller)) {
            case null { return #err(#Unauthorized); };
            case (?acc) { acc };
        };

        let currentBalance = switch (account.tokens.get(token)) {
            case null { return #err(#InsufficientBalance); };
            case (?bal) { bal };
        };

        if (currentBalance < amount) {
            return #err(#InsufficientBalance);
        };

        account.tokens.put(token, currentBalance - amount);
        #ok(());
    };

    // Create a new liquidity pool
    public shared(msg) func createPool(tokenA : Token, tokenB : Token) : async Result.Result<(), Error> {
        if (tokenA == tokenB) {
            return #err(#InvalidTokenPair);
        };

        let poolKey = if (Principal.less(tokenA, tokenB)) { (tokenA, tokenB) } else { (tokenB, tokenA) };

        if (pools.get(poolKey) != null) {
            return #err(#PoolExists);
        };

        let newPool : Pool = {
            tokenA = poolKey.0;
            tokenB = poolKey.1;
            reserveA = 0;
            reserveB = 0;
            totalSupply = 0;
        };

        pools.put(poolKey, newPool);
        #ok(());
    };

    // Add liquidity to a pool
    public shared(msg) func addLiquidity(
        tokenA : Token,
        tokenB : Token,
        amountADesired : Nat,
        amountBDesired : Nat
    ) : async Result.Result<(), Error> {
        let poolKey = if (Principal.less(tokenA, tokenB)) { (tokenA, tokenB) } else { (tokenB, tokenA) };

        let pool = switch (pools.get(poolKey)) {
            case null { return #err(#PoolNotFound); };
            case (?p) { p };
        };

        let account = switch (accounts.get(msg.caller)) {
            case null { return #err(#Unauthorized); };
            case (?acc) { acc };
        };

        let balanceA = switch (account.tokens.get(tokenA)) {
            case null { return #err(#InsufficientBalance); };
            case (?bal) { bal };
        };

        let balanceB = switch (account.tokens.get(tokenB)) {
            case null { return #err(#InsufficientBalance); };
            case (?bal) { bal };
        };

        if (balanceA < amountADesired or balanceB < amountBDesired) {
            return #err(#InsufficientBalance);
        };

        // Calculate liquidity amount
        let liquidity : Nat = if (pool.totalSupply == 0) {
            Nat.sqrt(amountADesired * amountBDesired);
        } else {
            Nat.min(
                (amountADesired * pool.totalSupply) / pool.reserveA,
                (amountBDesired * pool.totalSupply) / pool.reserveB
            );
        };

        if (liquidity == 0) {
            return #err(#InsufficientLiquidity);
        };

        // Update balances
        account.tokens.put(tokenA, balanceA - amountADesired);
        account.tokens.put(tokenB, balanceB - amountBDesired);

        // Update pool reserves
        let updatedPool : Pool = {
            tokenA = pool.tokenA;
            tokenB = pool.tokenB;
            reserveA = pool.reserveA + amountADesired;
            reserveB = pool.reserveB + amountBDesired;
            totalSupply = pool.totalSupply + liquidity;
        };

        pools.put(poolKey, updatedPool);
        #ok(());
    };

    // Remove liquidity from a pool
    public shared(msg) func removeLiquidity(
        tokenA : Token,
        tokenB : Token,
        liquidity : Nat
    ) : async Result.Result<(), Error> {
        let poolKey = if (Principal.less(tokenA, tokenB)) { (tokenA, tokenB) } else { (tokenB, tokenA) };

        let pool = switch (pools.get(poolKey)) {
            case null { return #err(#PoolNotFound); };
            case (?p) { p };
        };

        if (pool.totalSupply < liquidity) {
            return #err(#InsufficientLiquidity);
        };

        let account = switch (accounts.get(msg.caller)) {
            case null { return #err(#Unauthorized); };
            case (?acc) { acc };
        };

        // Calculate token amounts to return
        let amountA = (liquidity * pool.reserveA) / pool.totalSupply;
        let amountB = (liquidity * pool.reserveB) / pool.totalSupply;

        // Update balances
        let balanceA = switch (account.tokens.get(tokenA)) {
            case null { 0 };
            case (?bal) { bal };
        };

        let balanceB = switch (account.tokens.get(tokenB)) {
            case null { 0 };
            case (?bal) { bal };
        };

        account.tokens.put(tokenA, balanceA + amountA);
        account.tokens.put(tokenB, balanceB + amountB);

        // Update pool reserves
        let updatedPool : Pool = {
            tokenA = pool.tokenA;
            tokenB = pool.tokenB;
            reserveA = pool.reserveA - amountA;
            reserveB = pool.reserveB - amountB;
            totalSupply = pool.totalSupply - liquidity;
        };

        pools.put(poolKey, updatedPool);
        #ok(());
    };

    // Swap tokens
    public shared(msg) func swap(
        tokenIn : Token,
        tokenOut : Token,
        amountIn : Nat
    ) : async Result.Result<Nat, Error> {
        let poolKey = if (Principal.less(tokenIn, tokenOut)) { (tokenIn, tokenOut) } else { (tokenOut, tokenIn) };

        let pool = switch (pools.get(poolKey)) {
            case null { return #err(#PoolNotFound); };
            case (?p) { p };
        };

        let account = switch (accounts.get(msg.caller)) {
            case null { return #err(#Unauthorized); };
            case (?acc) { acc };
        };

        let balanceIn = switch
