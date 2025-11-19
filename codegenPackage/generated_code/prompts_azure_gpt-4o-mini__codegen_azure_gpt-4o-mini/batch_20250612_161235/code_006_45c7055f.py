"""
Generated Code Metadata:
========================
Original URL: https://monad.at
Prompt: Construct a simple example of a hackathon project that utilizes Monad's features, emphasizing the scalability and performance advantages for developers.
Generated: DETERMINISTIC_45c7055fa37e53f3
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```haskell
{-# LANGUAGE FlexibleContexts #-}

-- | A simple hackathon project demonstrating the use of Monads in Haskell.
-- This project simulates a basic task management system where tasks can be created,
-- executed, and logged. It emphasizes the scalability and performance advantages of using Monads.

module Main where

import Control.Monad (forM_)
import Control.Monad.State
import Control.Monad.Except

-- | Define a Task type that holds a description and a status.
data Task = Task
  { description :: String
  , completed   :: Bool
  } deriving (Show)

-- | Define a type for our application state, which includes a list of tasks.
type AppState = [Task]

-- | Define a custom error type for our application.
data AppError = TaskError String deriving (Show)

-- | Type alias for our application monad, which combines State and Except.
type App a = ExceptT AppError (State AppState) a

-- | Function to add a new task to the state.
addTask :: String -> App ()
addTask desc = do
    tasks <- get
    let newTask = Task desc False
    put (newTask : tasks)

-- | Function to complete a task by its description.
completeTask :: String -> App ()
completeTask desc = do
    tasks <- get
    let updatedTasks = map (\task -> if description task == desc then task { completed = True } else task) tasks
    put updatedTasks

-- | Function to list all tasks.
listTasks :: App [Task]
listTasks = get

-- | Function to run the application with initial state.
runApp :: App a -> AppState -> (Either AppError a, AppState)
runApp app initialState = runState (runExceptT app) initialState

-- | Main function to demonstrate the task management system.
main :: IO ()
main = do
    let initialState = []
    let (result, finalState) = runApp app initialState

    case result of
        Left err -> putStrLn $ "Error: " ++ show err
        Right _  -> do
            putStrLn "Final Task List:"
            forM_ finalState $ \task -> do
                putStrLn $ description task ++ " - " ++ (if completed task then "Completed" else "Pending")

-- | Application logic to demonstrate adding and completing tasks.
app :: App ()
app = do
    addTask "Write project proposal"
    addTask "Implement task management system"
    completeTask "Write project proposal"
    addTask "Prepare presentation"
```
