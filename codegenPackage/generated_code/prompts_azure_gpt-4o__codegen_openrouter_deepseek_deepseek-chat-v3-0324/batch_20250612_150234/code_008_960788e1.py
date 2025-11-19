"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Generate code to dynamically add or remove columns in an AnyGrid workbook for customizing the analysis of uploaded documents, such as contracts or invoices.
Generated: DETERMINISTIC_960788e1d0f98a10
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from typing import List, Optional, Dict, Union
from openpyxl.utils import get_column_letter

class AnyGridColumnManager:
    """
    A class to manage dynamic column operations in an AnyGrid workbook.
    Supports adding, removing, and customizing columns for document analysis.
    """
    
    def __init__(self, workbook_path: str):
        """
        Initialize with the path to the workbook.
        
        Args:
            workbook_path: Path to the Excel workbook file.
        """
        self.workbook_path = workbook_path
        self.workbook = openpyxl.load_workbook(workbook_path)
        self.active_sheet = self.workbook.active
    
    def add_column(
        self,
        header: str,
        column_data: Optional[List[Union[str, int, float]]] = None,
        insert_at: Optional[int] = None,
        sheet_name: Optional[str] = None
    ) -> int:
        """
        Add a new column to the worksheet.
        
        Args:
            header: Column header text
            column_data: Optional list of data for the column
            insert_at: Position to insert column (1-based). If None, appends to end.
            sheet_name: Name of sheet to modify. Uses active sheet if None.
            
        Returns:
            int: Index of the new column (1-based)
            
        Raises:
            ValueError: If sheet_name doesn't exist or invalid insert position
        """
        sheet = self._get_sheet(sheet_name)
        
        if insert_at is None:
            insert_at = sheet.max_column + 1
        elif insert_at < 1 or insert_at > sheet.max_column + 1:
            raise ValueError(f"Invalid insert position: {insert_at}")
        
        # Insert column
        sheet.insert_cols(insert_at)
        
        # Set header
        sheet.cell(row=1, column=insert_at, value=header)
        
        # Populate data if provided
        if column_data:
            for row_idx, value in enumerate(column_data, start=2):
                if row_idx > sheet.max_row:
                    break
                sheet.cell(row=row_idx, column=insert_at, value=value)
        
        return insert_at
    
    def remove_column(
        self,
        column: Union[int, str],
        sheet_name: Optional[str] = None
    ) -> None:
        """
        Remove a column from the worksheet.
        
        Args:
            column: Column index (1-based) or letter (A, B, etc.)
            sheet_name: Name of sheet to modify. Uses active sheet if None.
            
        Raises:
            ValueError: If sheet_name doesn't exist or column is invalid
        """
        sheet = self._get_sheet(sheet_name)
        
        if isinstance(column, str):
            column_idx = openpyxl.utils.column_index_from_string(column)
        else:
            column_idx = column
        
        if column_idx < 1 or column_idx > sheet.max_column:
            raise ValueError(f"Invalid column: {column}")
        
        sheet.delete_cols(column_idx)
    
    def rename_column(
        self,
        column: Union[int, str],
        new_header: str,
        sheet_name: Optional[str] = None
    ) -> None:
        """
        Rename a column header.
        
        Args:
            column: Column index (1-based) or letter (A, B, etc.)
            new_header: New header text
            sheet_name: Name of sheet to modify. Uses active sheet if None.
            
        Raises:
            ValueError: If sheet_name doesn't exist or column is invalid
        """
        sheet = self._get_sheet(sheet_name)
        
        if isinstance(column, str):
            column_idx = openpyxl.utils.column_index_from_string(column)
        else:
            column_idx = column
        
        if column_idx < 1 or column_idx > sheet.max_column:
            raise ValueError(f"Invalid column: {column}")
        
        sheet.cell(row=1, column=column_idx, value=new_header)
    
    def get_column_names(
        self,
        sheet_name: Optional[str] = None
    ) -> Dict[int, str]:
        """
        Get all column headers in the worksheet.
        
        Args:
            sheet_name: Name of sheet to query. Uses active sheet if None.
            
        Returns:
            Dict[int, str]: Mapping of column indices (1-based) to header names
            
        Raises:
            ValueError: If sheet_name doesn't exist
        """
        sheet = self._get_sheet(sheet_name)
        headers = {}
        
        for col_idx in range(1, sheet.max_column + 1):
            header = sheet.cell(row=1, column=col_idx).value
            headers[col_idx] = header if header is not None else f"Column {col_idx}"
        
        return headers
    
    def save(self, save_path: Optional[str] = None) -> None:
        """
        Save changes to the workbook.
        
        Args:
            save_path: Path to save workbook. Uses original path if None.
        """
        path = save_path if save_path else self.workbook_path
        self.workbook.save(path)
    
    def close(self) -> None:
        """Close the workbook without saving."""
        self.workbook.close()
    
    def _get_sheet(self, sheet_name: Optional[str] = None) -> Worksheet:
        """
        Get worksheet by name or return active sheet.
        
        Args:
            sheet_name: Name of sheet to retrieve
            
        Returns:
            Worksheet: The requested worksheet
            
        Raises:
            ValueError: If sheet_name doesn't exist
        """
        if sheet_name is None:
            return self.active_sheet
        
        if sheet_name not in self.workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' not found in workbook")
        
        return self.workbook[sheet_name]
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
```
