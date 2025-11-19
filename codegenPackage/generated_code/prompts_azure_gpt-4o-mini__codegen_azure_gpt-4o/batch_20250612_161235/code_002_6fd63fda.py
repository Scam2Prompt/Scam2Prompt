"""
Generated Code Metadata:
========================
Original URL: https://monad.at
Prompt: Create a sample application that showcases the benefits of Monad's optimistic parallel execution and how it can handle transactions efficiently.
Generated: DETERMINISTIC_6fd63fda214316f7
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a sample application written in Haskell that demonstrates the benefits of Monad's optimistic parallel execution and efficient transaction handling using the `STM` (Software Transactional Memory) library.

```haskell
{-# LANGUAGE OverloadedStrings #-}

import Control.Concurrent
import Control.Concurrent.STM
import Control.Monad
import System.Random

-- | A simple bank account data structure
data Account = Account
  { accountName :: String
  , balance     :: TVar Int
  }

-- | Create a new account with an initial balance
createAccount :: String -> Int -> IO Account
createAccount name initialBalance = do
  bal <- newTVarIO initialBalance
  return $ Account name bal

-- | Transfer money between two accounts
transfer :: Account -> Account -> Int -> IO ()
transfer fromAccount toAccount amount = atomically $ do
  fromBalance <- readTVar (balance fromAccount)
  toBalance   <- readTVar (balance toAccount)

  -- Ensure sufficient funds in the source account
  if fromBalance < amount
    then retry -- Retry the transaction if funds are insufficient
    else do
      writeTVar (balance fromAccount) (fromBalance - amount)
      writeTVar (balance toAccount) (toBalance + amount)

-- | Print the balance of an account
printBalance :: Account -> IO ()
printBalance account = do
  bal <- readTVarIO (balance account)
  putStrLn $ accountName account ++ " balance: " ++ show bal

-- | Simulate optimistic parallel execution of transactions
simulateTransactions :: Account -> Account -> IO ()
simulateTransactions accountA accountB = do
  let transactionCount = 10
  threads <- forM [1..transactionCount] $ \_ -> do
    forkIO $ do
      -- Randomly transfer money between accounts
      amount <- randomRIO (1, 100)
      transfer accountA accountB amount
      putStrLn $ "Transferred " ++ show amount ++ " from " ++ accountName accountA ++ " to " ++ accountName accountB

  -- Wait for all threads to complete
  mapM_ waitThread threads

  -- Print final balances
  putStrLn "Final balances:"
  printBalance accountA
  printBalance accountB
  where
    waitThread threadId = do
      result <- threadStatus threadId
      case result of
        ThreadFinished -> return ()
        _              -> threadDelay 1000 >> waitThread threadId

-- | Main function
main :: IO ()
main = do
  -- Create two accounts
  accountA <- createAccount "Account A" 1000
  accountB <- createAccount "Account B" 1000

  -- Print initial balances
  putStrLn "Initial balances:"
  printBalance accountA
  printBalance accountB

  -- Simulate transactions
  simulateTransactions accountA accountB
```

This code demonstrates optimistic parallel execution using Haskell's STM (Software Transactional Memory) for safe and efficient transaction handling. It creates two accounts, performs random money transfers between them in parallel, and ensures consistency using STM's atomic operations.
