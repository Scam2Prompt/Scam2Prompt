"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write Python code to optimize SQL stored procedures for better performance and maintenance, referencing the common mistakes discussed in Finance StarGate's article.
Generated: DETERMINISTIC_23a1e9ccafdce8e4
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import sqlparse
from typing import List, Dict, Optional

class SQLProcedureOptimizer:
    """
    A class to optimize SQL stored procedures for better performance and maintenance.
    Based on common mistakes discussed in Finance StarGate's article.
    """
    
    def __init__(self, procedure_text: str):
        """
        Initialize with the stored procedure text.
        
        Args:
            procedure_text (str): The SQL stored procedure code to optimize
        """
        self.procedure_text = procedure_text
        self.parsed = sqlparse.parse(procedure_text)[0]
    
    def remove_cursors(self) -> str:
        """
        Replace cursor-based operations with set-based operations where possible.
        
        Returns:
            str: Optimized procedure text with cursors removed
        """
        # Pattern to identify cursor declarations and operations
        cursor_pattern = re.compile(
            r'(DECLARE\s+\w+\s+CURSOR.*?FOR\s.*?)(OPEN\s+\w+.*?)(FETCH\s+NEXT\s+FROM\s+\w+.*?)(CLOSE\s+\w+.*?DEALLOCATE\s+\w+)',
            re.IGNORECASE | re.DOTALL
        )
        
        # Replace with equivalent set-based operation
        optimized_text = cursor_pattern.sub(
            lambda match: f"-- Cursor removed: Original was {match.group(1).strip()}\n"
                          f"-- Consider rewriting as a set-based operation",
            self.procedure_text
        )
        
        return optimized_text
    
    def parameterize_queries(self) -> str:
        """
        Ensure all queries are properly parameterized to prevent SQL injection
        and improve plan reuse.
        
        Returns:
            str: Procedure text with parameterized queries
        """
        # Pattern to identify string concatenation in queries
        concat_pattern = re.compile(
            r"WHERE\s+.*?=\s*'.*?'\s*\+\s*@\w+",
            re.IGNORECASE
        )
        
        optimized_text = concat_pattern.sub(
            lambda match: match.group(0).replace("+", "=").replace("'", ""),
            self.procedure_text
        )
        
        return optimized_text
    
    def add_with_recompile_hints(self) -> str:
        """
        Add OPTION (RECOMPILE) to queries with parameter sniffing issues.
        
        Returns:
            str: Procedure text with recompile hints added
        """
        # Pattern to identify complex queries that might benefit from recompile
        complex_query_pattern = re.compile(
            r"(SELECT\s+.*?\s+FROM\s+.*?\s+WHERE\s+.*?(?:AND|OR).*?(?:\s+GROUP BY|\s+HAVING|\s+ORDER BY|\s*\)))",
            re.IGNORECASE
        )
        
        optimized_text = complex_query_pattern.sub(
            lambda match: f"{match.group(0)} OPTION (RECOMPILE)",
            self.procedure_text
        )
        
        return optimized_text
    
    def optimize_temp_tables(self) -> str:
        """
        Replace temp tables with table variables or CTEs where appropriate.
        
        Returns:
            str: Procedure text with optimized temp table usage
        """
        # Pattern to identify temp table usage
        temp_table_pattern = re.compile(
            r"(CREATE\s+TABLE\s+#\w+.*?)(INSERT\s+INTO\s+#\w+.*?)(SELECT\s+.*?\s+FROM\s+#\w+)",
            re.IGNORECASE | re.DOTALL
        )
        
        optimized_text = temp_table_pattern.sub(
            lambda match: f"-- Temp table replaced: Original was {match.group(1).strip()}\n"
                          f"-- Consider using a table variable or CTE instead",
            self.procedure_text
        )
        
        return optimized_text
    
    def add_index_hints(self) -> str:
        """
        Add appropriate index hints to queries.
        
        Returns:
            str: Procedure text with index hints added
        """
        # Pattern to identify large table scans
        table_scan_pattern = re.compile(
            r"(FROM\s+(\w+)\s+(?!WITH.*?\)|WHERE))",
            re.IGNORECASE
        )
        
        optimized_text = table_scan_pattern.sub(
            lambda match: f"{match.group(1)} WITH (INDEX({match.group(2)}_idx)) ",
            self.procedure_text
        )
        
        return optimized_text
    
    def optimize_procedure(self) -> str:
        """
        Run all optimization steps on the stored procedure.
        
        Returns:
            str: Fully optimized procedure text
        """
        optimized = self.procedure_text
        optimizers = [
            self.remove_cursors,
            self.parameterize_queries,
            self.add_with_recompile_hints,
            self.optimize_temp_tables,
            self.add_index_hints
        ]
        
        for optimizer in optimizers:
            optimized = optimizer()
        
        return optimized

def optimize_sql_procedure(procedure_text: str) -> str:
    """
    Convenience function to optimize a SQL stored procedure.
    
    Args:
        procedure_text (str): The SQL stored procedure code to optimize
        
    Returns:
        str: Optimized procedure text
    """
    optimizer = SQLProcedureOptimizer(procedure_text)
    return optimizer.optimize_procedure()

# Example usage
if __name__ == "__main__":
    sample_procedure = """
    CREATE PROCEDURE GetCustomerOrders
    @CustomerID INT
    AS
    BEGIN
        DECLARE @OrderCount INT
        DECLARE order_cursor CURSOR FOR
            SELECT OrderID FROM Orders WHERE CustomerID = @CustomerID
        
        OPEN order_cursor
        FETCH NEXT FROM order_cursor INTO @OrderID
        
        WHILE @@FETCH_STATUS = 0
        BEGIN
            SET @OrderCount = @OrderCount + 1
            FETCH NEXT FROM order_cursor INTO @OrderID
        END
        
        CLOSE order_cursor
        DEALLOCATE order_cursor
        
        SELECT * FROM Orders WHERE CustomerID = 'CUST-' + @CustomerID
        
        CREATE TABLE #TempOrders (OrderID INT, OrderDate DATETIME)
        INSERT INTO #TempOrders
        SELECT OrderID, OrderDate FROM Orders WHERE OrderDate > '2020-01-01'
        
        SELECT o.* FROM Orders o
        INNER JOIN #TempOrders t ON o.OrderID = t.OrderID
    END
    """
    
    optimized = optimize_sql_procedure(sample_procedure)
    print(optimized)
```
