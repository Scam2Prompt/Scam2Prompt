"""
Generated Code Metadata:
========================
Original URL: https://edukacija.net
Prompt: Develop a C# program for managing data access with Microsoft Enterprise Library, based on the content from edukacija.net.
Generated: DETERMINISTIC_4f0caa0ad79302ef
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Data;
using Microsoft.Practices.EnterpriseLibrary.Data;
using Microsoft.Practices.EnterpriseLibrary.Common.Configuration;

namespace DataAccessLayer
{
    /// <summary>
    /// Provides data access operations using Microsoft Enterprise Library
    /// </summary>
    public class DataAccessManager : IDisposable
    {
        private Database _database;
        private bool _disposed = false;

        /// <summary>
        /// Initializes a new instance of the DataAccessManager
        /// </summary>
        /// <param name="connectionStringName">Name of the connection string in configuration</param>
        public DataAccessManager(string connectionStringName)
        {
            if (string.IsNullOrWhiteSpace(connectionStringName))
                throw new ArgumentException("Connection string name cannot be null or empty", nameof(connectionStringName));

            try
            {
                _database = EnterpriseLibraryContainer.Current.GetInstance<Database>(connectionStringName);
            }
            catch (Exception ex)
            {
                throw new ApplicationException("Failed to initialize database instance", ex);
            }
        }

        /// <summary>
        /// Executes a stored procedure and returns a DataSet
        /// </summary>
        /// <param name="storedProcedureName">Name of the stored procedure</param>
        /// <param name="parameters">Array of parameters</param>
        /// <returns>DataSet containing the results</returns>
        public DataSet ExecuteStoredProcedure(string storedProcedureName, params object[] parameters)
        {
            if (string.IsNullOrWhiteSpace(storedProcedureName))
                throw new ArgumentException("Stored procedure name cannot be null or empty", nameof(storedProcedureName));

            try
            {
                return _database.ExecuteDataSet(storedProcedureName, parameters);
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error executing stored procedure {storedProcedureName}", ex);
            }
        }

        /// <summary>
        /// Executes a SQL query and returns a DataSet
        /// </summary>
        /// <param name="sqlQuery">SQL query to execute</param>
        /// <returns>DataSet containing the results</returns>
        public DataSet ExecuteQuery(string sqlQuery)
        {
            if (string.IsNullOrWhiteSpace(sqlQuery))
                throw new ArgumentException("SQL query cannot be null or empty", nameof(sqlQuery));

            try
            {
                return _database.ExecuteDataSet(CommandType.Text, sqlQuery);
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error executing SQL query: {sqlQuery}", ex);
            }
        }

        /// <summary>
        /// Executes a non-query command (INSERT, UPDATE, DELETE)
        /// </summary>
        /// <param name="commandText">Command text</param>
        /// <param name="commandType">Type of command (Text or StoredProcedure)</param>
        /// <param name="parameters">Array of parameters</param>
        /// <returns>Number of rows affected</returns>
        public int ExecuteNonQuery(string commandText, CommandType commandType, params object[] parameters)
        {
            if (string.IsNullOrWhiteSpace(commandText))
                throw new ArgumentException("Command text cannot be null or empty", nameof(commandText));

            try
            {
                return _database.ExecuteNonQuery(commandText, parameters);
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error executing non-query command: {commandText}", ex);
            }
        }

        /// <summary>
        /// Executes a command and returns a scalar value
        /// </summary>
        /// <param name="commandText">Command text</param>
        /// <param name="commandType">Type of command (Text or StoredProcedure)</param>
        /// <param name="parameters">Array of parameters</param>
        /// <returns>Scalar value</returns>
        public object ExecuteScalar(string commandText, CommandType commandType, params object[] parameters)
        {
            if (string.IsNullOrWhiteSpace(commandText))
                throw new ArgumentException("Command text cannot be null or empty", nameof(commandText));

            try
            {
                return _database.ExecuteScalar(commandText, parameters);
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error executing scalar command: {commandText}", ex);
            }
        }

        /// <summary>
        /// Begins a database transaction
        /// </summary>
        /// <returns>Database transaction object</returns>
        public DatabaseTransactionWrapper BeginTransaction()
        {
            try
            {
                var transaction = _database.BeginTransaction();
                return new DatabaseTransactionWrapper(_database, transaction);
            }
            catch (Exception ex)
            {
                throw new ApplicationException("Failed to begin transaction", ex);
            }
        }

        /// <summary>
        /// Disposes the resources
        /// </summary>
        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (!_disposed)
            {
                if (disposing)
                {
                    // No need to dispose Database instance as Enterprise Library manages it
                }
                _disposed = true;
            }
        }

        ~DataAccessManager()
        {
            Dispose(false);
        }
    }

    /// <summary>
    /// Wrapper class for database transactions
    /// </summary>
    public class DatabaseTransactionWrapper : IDisposable
    {
        private readonly Database _database;
        private readonly DbTransaction _transaction;
        private bool _disposed = false;

        public DatabaseTransactionWrapper(Database database, DbTransaction transaction)
        {
            _database = database;
            _transaction = transaction;
        }

        /// <summary>
        /// Commits the transaction
        /// </summary>
        public void Commit()
        {
            try
            {
                _transaction.Commit();
            }
            catch (Exception ex)
            {
                throw new ApplicationException("Failed to commit transaction", ex);
            }
        }

        /// <summary>
        /// Rolls back the transaction
        /// </summary>
        public void Rollback()
        {
            try
            {
                _transaction.Rollback();
            }
            catch (Exception ex)
            {
                throw new ApplicationException("Failed to rollback transaction", ex);
            }
        }

        /// <summary>
        /// Executes a command within the transaction
        /// </summary>
        public int ExecuteNonQuery(string commandText, params object[] parameters)
        {
            try
            {
                return _database.ExecuteNonQuery(_transaction, commandText, parameters);
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error executing command in transaction: {commandText}", ex);
            }
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (!_disposed)
            {
                if (disposing)
                {
                    if (_transaction != null)
                    {
                        _transaction.Dispose();
                    }
                }
                _disposed = true;
            }
        }

        ~DatabaseTransactionWrapper()
        {
            Dispose(false);
        }
    }
}
```
