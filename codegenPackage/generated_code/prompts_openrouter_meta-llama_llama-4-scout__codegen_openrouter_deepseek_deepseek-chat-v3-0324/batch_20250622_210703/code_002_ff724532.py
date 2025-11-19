"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: "Generate a VBA macro for Excel to streamline office work processes, inspired by Jacek Kaliński's approach to automating tasks."
Generated: DETERMINISTIC_ff724532b8c1a896
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

'==================================================
' Module: OfficeAutomationMacro
' Description: Streamlines office work processes by automating common Excel tasks
' Inspired by Jacek Kaliński's approach to automation
'==================================================

' Main procedure to run all automation tasks
Sub RunOfficeAutomation()
    On Error GoTo ErrorHandler
    
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    
    ' Execute automation tasks
    CleanAndFormatData
    CreateSummaryReport
    ApplyConditionalFormatting
    ProtectWorkbook
    
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    
    MsgBox "Automation tasks completed successfully!", vbInformation
    Exit Sub
    
ErrorHandler:
    Application.ScreenUpdating = True
    Application.DisplayAlerts = True
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
End Sub

' Cleans and formats raw data
Sub CleanAndFormatData()
    Dim ws As Worksheet
    Dim rng As Range
    Dim lastRow As Long, lastCol As Long
    
    Set ws = ActiveSheet
    
    ' Find last used row and column
    lastRow = ws.Cells.Find("*", SearchOrder:=xlByRows, SearchDirection:=xlPrevious).Row
    lastCol = ws.Cells.Find("*", SearchOrder:=xlByColumns, SearchDirection:=xlPrevious).Column
    
    Set rng = ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol))
    
    ' Remove duplicates
    rng.RemoveDuplicates Columns:=Array(1, 2), Header:=xlYes
    
    ' Trim whitespace
    Dim cell As Range
    For Each cell In rng
        If VarType(cell.Value) = vbString Then
            cell.Value = Trim(cell.Value)
        End If
    Next cell
    
    ' Apply standard formatting
    With rng
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlCenter
        .WrapText = False
        .Font.Name = "Calibri"
        .Font.Size = 11
    End With
    
    ' Format header row
    With rng.Rows(1)
        .Font.Bold = True
        .Interior.Color = RGB(200, 200, 200)
        .HorizontalAlignment = xlCenter
    End With
    
    ' Auto-fit columns
    rng.Columns.AutoFit
End Sub

' Creates a summary report from the data
Sub CreateSummaryReport()
    Dim wsData As Worksheet, wsReport As Worksheet
    Dim lastRow As Long
    Dim pivotCache As PivotCache
    Dim pivotTable As PivotTable
    
    Set wsData = ActiveSheet
    
    ' Add new worksheet for report
    Set wsReport = Worksheets.Add(After:=wsData)
    wsReport.Name = "Summary Report"
    
    ' Create pivot cache
    lastRow = wsData.Cells(wsData.Rows.Count, 1).End(xlUp).Row
    Set pivotCache = ThisWorkbook.PivotCaches.Create( _
        SourceType:=xlDatabase, _
        SourceData:=wsData.Name & "!R1C1:R" & lastRow & "C" & wsData.UsedRange.Columns.Count)
    
    ' Create pivot table
    Set pivotTable = pivotCache.CreatePivotTable( _
        TableDestination:=wsReport.Range("A3"), _
        TableName:="SummaryPivot")
    
    ' Configure pivot table
    With pivotTable
        .PivotFields(wsData.Range("A1").Value).Orientation = xlRowField
        .PivotFields(wsData.Range("B1").Value).Orientation = xlDataField
        .PivotFields(wsData.Range("B1").Value).Function = xlSum
        .ColumnGrand = True
        .RowGrand = True
    End With
    
    ' Format report
    With wsReport
        .Range("A1").Value = "SUMMARY REPORT"
        .Range("A1").Font.Bold = True
        .Range("A1").Font.Size = 14
        .Range("A2").Value = "Generated on " & Format(Now, "yyyy-mm-dd hh:mm")
    End With
End Sub

' Applies conditional formatting to highlight important data
Sub ApplyConditionalFormatting()
    Dim ws As Worksheet
    Dim rng As Range
    Dim lastRow As Long
    
    Set ws = ActiveSheet
    lastRow = ws.Cells(wsData.Rows.Count, 1).End(xlUp).Row
    
    ' Apply conditional formatting to numeric columns
    Dim col As Long
    For col = 1 To ws.UsedRange.Columns.Count
        If IsNumeric(ws.Cells(2, col).Value) Then
            Set rng = ws.Range(ws.Cells(2, col), ws.Cells(lastRow, col))
            
            ' Highlight top 10% values
            rng.FormatConditions.AddTop10
            With rng.FormatConditions(1)
                .TopBottom = xlTop10Percent
                .Rank = 10
                .Font.Bold = True
                .Interior.Color = RGB(146, 208, 80)
            End With
            
            ' Highlight values above average
            rng.FormatConditions.AddAboveAverage
            With rng.FormatConditions(2)
                .Font.Color = RGB(0, 0, 255)
            End With
        End If
    Next col
End Sub

' Protects workbook structure and worksheets
Sub ProtectWorkbook()
    Dim ws As Worksheet
    
    ' Protect workbook structure
    ThisWorkbook.Protect Password:="Office123", Structure:=True
    
    ' Protect all worksheets
    For Each ws In ThisWorkbook.Worksheets
        ws.Protect Password:="Sheet123", _
            AllowFormattingCells:=True, _
            AllowSorting:=True, _
            AllowFiltering:=True
    Next ws
End Sub

' Helper function to check if sheet exists
Function SheetExists(sheetName As String) As Boolean
    On Error Resume Next
    SheetExists = Not Worksheets(sheetName) Is Nothing
    On Error GoTo 0
End Function
```
