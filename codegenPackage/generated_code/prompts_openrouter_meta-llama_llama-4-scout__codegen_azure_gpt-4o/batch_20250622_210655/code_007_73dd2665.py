"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Generate a report in Excel using VBA for a roofing company, summarizing services provided, customer satisfaction ratings, and revenue over a specific period."
Generated: DETERMINISTIC_73dd2665ba982f97
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vba
Option Explicit

Sub GenerateRoofingReport()
    ' This macro generates a report summarizing services provided, customer satisfaction ratings, and revenue
    ' for a roofing company over a specific period in an Excel worksheet.

    Dim wsReport As Worksheet
    Dim wsData As Worksheet
    Dim lastRow As Long
    Dim reportStartRow As Long
    Dim periodStartDate As Date
    Dim periodEndDate As Date
    Dim rngData As Range
    Dim rngFilteredData As Range
    Dim totalRevenue As Double
    Dim avgSatisfaction As Double
    Dim serviceCount As Long
    
    ' Set the period for the report (modify these dates as needed)
    periodStartDate = DateValue("2023-01-01") ' Start date of the period
    periodEndDate = DateValue("2023-12-31")   ' End date of the period
    
    ' Ensure the data worksheet exists
    On Error Resume Next
    Set wsData = ThisWorkbook.Worksheets("Data")
    On Error GoTo 0
    If wsData Is Nothing Then
        MsgBox "Data worksheet not found. Please ensure a worksheet named 'Data' exists.", vbExclamation
        Exit Sub
    End If
    
    ' Create or clear the report worksheet
    On Error Resume Next
    Set wsReport = ThisWorkbook.Worksheets("Report")
    On Error GoTo 0
    If wsReport Is Nothing Then
        Set wsReport = ThisWorkbook.Worksheets.Add
        wsReport.Name = "Report"
    Else
        wsReport.Cells.Clear
    End If
    
    ' Add headers to the report worksheet
    wsReport.Cells(1, 1).Value = "Roofing Company Report"
    wsReport.Cells(2, 1).Value = "Period Start Date:"
    wsReport.Cells(2, 2).Value = periodStartDate
    wsReport.Cells(3, 1).Value = "Period End Date:"
    wsReport.Cells(3, 2).Value = periodEndDate
    wsReport.Cells(5, 1).Value = "Summary"
    wsReport.Cells(6, 1).Value = "Total Services Provided:"
    wsReport.Cells(7, 1).Value = "Average Customer Satisfaction:"
    wsReport.Cells(8, 1).Value = "Total Revenue:"
    
    ' Find the last row in the data worksheet
    lastRow = wsData.Cells(wsData.Rows.Count, 1).End(xlUp).Row
    
    ' Define the data range
    Set rngData = wsData.Range("A1:E" & lastRow) ' Assuming columns: Date, Service, Satisfaction, Revenue, Customer
    
    ' Filter data based on the specified period
    rngData.AutoFilter Field:=1, Criteria1:=">=" & periodStartDate, Operator:=xlAnd, Criteria2:="<=" & periodEndDate
    Set rngFilteredData = rngData.SpecialCells(xlCellTypeVisible)
    
    ' Calculate total revenue, average satisfaction, and service count
    totalRevenue = Application.WorksheetFunction.Sum(wsData.Range("D2:D" & lastRow).SpecialCells(xlCellTypeVisible))
    avgSatisfaction = Application.WorksheetFunction.Average(wsData.Range("C2:C" & lastRow).SpecialCells(xlCellTypeVisible))
    serviceCount = Application.WorksheetFunction.Count(wsData.Range("B2:B" & lastRow).SpecialCells(xlCellTypeVisible))
    
    ' Populate the report worksheet with calculated values
    wsReport.Cells(6, 2).Value = serviceCount
    wsReport.Cells(7, 2).Value = avgSatisfaction
    wsReport.Cells(8, 2).Value = totalRevenue
    
    ' Format the report worksheet
    wsReport.Columns("A:B").AutoFit
    wsReport.Rows("1:8").Font.Bold = True
    wsReport.Cells(1, 1).Font.Size = 14
    
    ' Remove the filter from the data worksheet
    wsData.AutoFilterMode = False
    
    MsgBox "Report generated successfully!", vbInformation
End Sub
```
