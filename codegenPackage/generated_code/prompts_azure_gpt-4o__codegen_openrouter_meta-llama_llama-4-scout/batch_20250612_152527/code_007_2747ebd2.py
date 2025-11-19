"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write code to integrate screenshots and photos into patent drawings using Microsoft Visio, based on the "Mastering Screenshot and Photo Integration in Patent Drawings" course.
Generated: DETERMINISTIC_2747ebd2fdf33fa8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for integrating screenshots and photos into patent drawings using Microsoft Visio. However, I need to clarify that I'll be providing a VBA (Visual Basic for Applications) script, as Microsoft Visio supports VBA for automation.

```vb
'*****************************************************************************************
'** Mastering Screenshot and Photo Integration in Patent Drawings                         **
'*****************************************************************************************

Option Explicit

' Required References:
' - Microsoft Visio 14.0 Object Library (or later)
' - Microsoft Office 14.0 Object Library (or later)

' Constants for image file formats
Const PNG_FORMAT As String = "PNG"
Const JPEG_FORMAT As String = "JPG"

' Function to add a screenshot to the active Visio page
Sub AddScreenshotToPage()
    On Error GoTo ErrHandler
    
    ' Declare variables
    Dim visApp As Visio.Application
    Dim visPage As Visio.Page
    Dim screenshotShape As Visio.Shape
    
    ' Initialize Visio application object
    Set visApp = Visio.Application
    Set visPage = visApp.ActivePage
    
    If visPage Is Nothing Then
        MsgBox "No active page in Visio.", vbExclamation
        Exit Sub
    End If
    
    ' Prompt user to select region for screenshot
    ' (For simplicity, this example assumes a fixed region)
    Dim screenshotWidth As Integer: screenshotWidth = 500
    Dim screenshotHeight As Integer: screenshotHeight = 300
    
    ' Capture the screenshot (this is a placeholder, implement actual screenshot logic here)
    Dim screenshotData As Variant
    ' screenshotData = CaptureScreenshot(screenshotWidth, screenshotHeight)
    
    ' Add the screenshot as a new shape on the page
    Set screenshotShape = visPage.Shapes.AddPicture( _
        "C:\Path\To\Placeholder\Screenshot.png", _
        visFalse, visTrue, 1, 1, screenshotWidth, screenshotHeight)
    
    ' Set shape properties
    screenshotShape.Text = "Screenshot"
    screenshotShape.Cells("PinX").FormulaU = "1"
    screenshotShape.Cells("PinY").FormulaU = "1"
    
    ' Clean up
    Set visPage = Nothing
    Set visApp = Nothing
    
    Exit Sub
    
ErrHandler:
    MsgBox "An error occurred: " & Err.Description, vbCritical
End Sub

' Function to add a photo to the active Visio page
Sub AddPhotoToPage()
    On Error GoTo ErrHandler
    
    ' Declare variables
    Dim visApp As Visio.Application
    Dim visPage As Visio.Page
    Dim photoShape As Visio.Shape
    
    ' Initialize Visio application object
    Set visApp = Visio.Application
    Set visPage = visApp.ActivePage
    
    If visPage Is Nothing Then
        MsgBox "No active page in Visio.", vbExclamation
        Exit Sub
    End If
    
    ' Prompt user to select a photo file
    Dim photoFilePath As String
    photoFilePath = GetFilePath("Select a photo", "Image Files (*.png;*.jpg)", PNG_FORMAT & ";JPEG_FORMAT)
    
    If Len(photoFilePath) = 0 Then
        MsgBox "No photo file selected.", vbExclamation
        Exit Sub
    End If
    
    ' Add the photo as a new shape on the page
    Set photoShape = visPage.Shapes.AddPicture( _
        photoFilePath, _
        visFalse, visTrue, 1, 1)
    
    ' Set shape properties
    photoShape.Text = "Photo"
    photoShape.Cells("PinX").FormulaU = "1"
    photoShape.Cells("PinY").FormulaU = "1"
    
    ' Clean up
    Set visPage = Nothing
    Set visApp = Nothing
    
    Exit Sub
    
ErrHandler:
    MsgBox "An error occurred: " & Err.Description, vbCritical
End Sub

' Helper function to prompt user for a file path
Function GetFilePath(prompt As String, filter As String, filterIndex As String) As String
    ' Declare variables
    Dim fileDialog As FileDialog
    
    ' Initialize file dialog object
    Set fileDialog = Application.FileDialog(msoFileDialogFilePicker)
    
    With fileDialog
        .AllowMultiSelect = False
        .Title = prompt
        .FileTypeDescription = filter
        .Filters.Clear
        .Filters.Add filter, filterIndex
        
        If .Show <> -1 Then
            GetFilePath = ""
        Else
            GetFilePath = .SelectedItems(1)
        End If
    End With
    
    ' Clean up
    Set fileDialog = Nothing
End Function
```
