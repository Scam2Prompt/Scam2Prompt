"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Develop a code template for creating a customizable, gamified learning experience in Microsoft Office applications, such as Excel or Word, using Visual Basic for Applications (VBA)."
Generated: DETERMINISTIC_514557ae91606fe7
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

'=============================================
' Module: GamifiedLearningTemplate
' Description: Template for creating a gamified learning experience in Office applications
'=============================================

' Constants for game settings
Private Const MAX_LEVEL As Integer = 10
Private Const POINTS_PER_TASK As Integer = 100
Private Const BONUS_POINTS As Integer = 50

' User progress variables
Private Type UserProgress
    UserName As String
    CurrentLevel As Integer
    TotalPoints As Integer
    TasksCompleted As Integer
    Achievements As Collection
End Type

Private currentUser As UserProgress

'=============================================
' Initialize the gamified learning experience
'=============================================
Public Sub InitializeGame()
    On Error GoTo ErrorHandler
    
    ' Initialize user progress
    Set currentUser.Achievements = New Collection
    
    ' Load or create user profile
    If Not LoadUserProfile() Then
        CreateNewUserProfile
    End If
    
    ' Show welcome message
    ShowWelcomeMessage
    
    Exit Sub
ErrorHandler:
    MsgBox "Error initializing game: " & Err.Description, vbCritical, "Initialization Error"
End Sub

'=============================================
' Load user profile from document or storage
'=============================================
Private Function LoadUserProfile() As Boolean
    On Error GoTo ErrorHandler
    
    ' Check if user data exists in document variables
    If ThisDocument.Variables.Count > 0 Then
        currentUser.UserName = ThisDocument.Variables("UserName")
        currentUser.CurrentLevel = CInt(ThisDocument.Variables("CurrentLevel"))
        currentUser.TotalPoints = CInt(ThisDocument.Variables("TotalPoints"))
        currentUser.TasksCompleted = CInt(ThisDocument.Variables("TasksCompleted"))
        LoadUserProfile = True
    Else
        LoadUserProfile = False
    End If
    
    Exit Function
ErrorHandler:
    LoadUserProfile = False
End Function

'=============================================
' Create new user profile
'=============================================
Private Sub CreateNewUserProfile()
    On Error GoTo ErrorHandler
    
    currentUser.UserName = InputBox("Enter your name to begin your learning journey:", "New User")
    If currentUser.UserName = "" Then
        currentUser.UserName = "Anonymous"
    End If
    
    currentUser.CurrentLevel = 1
    currentUser.TotalPoints = 0
    currentUser.TasksCompleted = 0
    
    ' Store in document variables
    ThisDocument.Variables.Add "UserName", currentUser.UserName
    ThisDocument.Variables.Add "CurrentLevel", CStr(currentUser.CurrentLevel)
    ThisDocument.Variables.Add "TotalPoints", CStr(currentUser.TotalPoints)
    ThisDocument.Variables.Add "TasksCompleted", CStr(currentUser.TasksCompleted)
    
    Exit Sub
ErrorHandler:
    MsgBox "Error creating user profile: " & Err.Description, vbCritical, "Profile Creation Error"
End Sub

'=============================================
' Save user progress
'=============================================
Private Sub SaveUserProgress()
    On Error GoTo ErrorHandler
    
    ThisDocument.Variables("CurrentLevel") = CStr(currentUser.CurrentLevel)
    ThisDocument.Variables("TotalPoints") = CStr(currentUser.TotalPoints)
    ThisDocument.Variables("TasksCompleted") = CStr(currentUser.TasksCompleted)
    
    Exit Sub
ErrorHandler:
    MsgBox "Error saving progress: " & Err.Description, vbCritical, "Save Error"
End Sub

'=============================================
' Complete a task and update progress
'=============================================
Public Sub CompleteTask(taskName As String, Optional isBonus As Boolean = False)
    On Error GoTo ErrorHandler
    
    Dim pointsEarned As Integer
    
    ' Calculate points
    pointsEarned = POINTS_PER_TASK
    If isBonus Then pointsEarned = pointsEarned + BONUS_POINTS
    
    ' Update progress
    currentUser.TasksCompleted = currentUser.TasksCompleted + 1
    currentUser.TotalPoints = currentUser.TotalPoints + pointsEarned
    
    ' Check for level up
    If currentUser.TasksCompleted Mod 5 = 0 And currentUser.CurrentLevel < MAX_LEVEL Then
        currentUser.CurrentLevel = currentUser.CurrentLevel + 1
        ShowLevelUpMessage
    End If
    
    ' Save progress
    SaveUserProgress
    
    ' Show feedback
    ShowTaskCompleteMessage taskName, pointsEarned
    
    Exit Sub
ErrorHandler:
    MsgBox "Error completing task: " & Err.Description, vbCritical, "Task Error"
End Sub

'=============================================
' Display messages to user
'=============================================
Private Sub ShowWelcomeMessage()
    MsgBox "Welcome to Office Learning Adventure, " & currentUser.UserName & "!" & vbCrLf & _
           "You are starting at Level " & currentUser.CurrentLevel & ".", _
           vbInformation, "Welcome"
End Sub

Private Sub ShowTaskCompleteMessage(taskName As String, pointsEarned As Integer)
    MsgBox "Task Complete: " & taskName & vbCrLf & _
           "You earned " & pointsEarned & " points!" & vbCrLf & vbCrLf & _
           "Total Points: " & currentUser.TotalPoints & vbCrLf & _
           "Tasks Completed: " & currentUser.TasksCompleted, _
           vbInformation, "Task Complete"
End Sub

Private Sub ShowLevelUpMessage()
    MsgBox "Congratulations! You've reached Level " & currentUser.CurrentLevel & "!", _
           vbExclamation, "Level Up!"
End Sub

'=============================================
' Achievement system
'=============================================
Public Sub AwardAchievement(achievementName As String, achievementDesc As String)
    On Error GoTo ErrorHandler
    
    ' Check if achievement already exists
    Dim ach As Variant
    For Each ach In currentUser.Achievements
        If ach = achievementName Then Exit Sub
    Next ach
    
    ' Add new achievement
    currentUser.Achievements.Add achievementName
    
    ' Show notification
    MsgBox "Achievement Unlocked: " & achievementName & vbCrLf & _
           achievementDesc, vbInformation, "New Achievement"
    
    Exit Sub
ErrorHandler:
    MsgBox "Error awarding achievement: " & Err.Description, vbCritical, "Achievement Error"
End Sub

'=============================================
' Show user progress dashboard
'=============================================
Public Sub ShowProgressDashboard()
    On Error GoTo ErrorHandler
    
    Dim dashboard As String
    Dim ach As Variant
    Dim achList As String
    
    dashboard = "=== Learning Progress ===" & vbCrLf & vbCrLf & _
                "User: " & currentUser.UserName & vbCrLf & _
                "Level: " & currentUser.CurrentLevel & vbCrLf & _
                "Total Points: " & currentUser.TotalPoints & vbCrLf & _
                "Tasks Completed: " & currentUser.TasksCompleted & vbCrLf & vbCrLf & _
                "=== Achievements ===" & vbCrLf
    
    ' List achievements
    If currentUser.Achievements.Count > 0 Then
        For Each ach In currentUser.Achievements
            achList = achList & "• " & ach & vbCrLf
        Next ach
    Else
        achList = "No achievements yet. Keep learning!"
    End If
    
    MsgBox dashboard & achList, vbInformation, "Progress Dashboard"
    
    Exit Sub
ErrorHandler:
    MsgBox "Error displaying dashboard: " & Err.Description, vbCritical, "Dashboard Error"
End Sub

'=============================================
' Example task implementation for Word
'=============================================
Public Sub CompleteFormattingTask()
    On Error GoTo ErrorHandler
    
    ' Check if selection has formatting
    If Selection.Font.Bold Or Selection.Font.Italic Or Selection.Font.Underline <> wdUnderlineNone Then
        CompleteTask "Basic Formatting", True
        AwardAchievement "Format Master", "Applied bold, italic, or underline formatting"
    Else
        MsgBox "Please apply some formatting (bold, italic, or underline) to complete this task.", vbInformation, "Task Incomplete"
    End If
    
    Exit Sub
ErrorHandler:
    MsgBox "Error completing formatting task: " & Err.Description, vbCritical, "Task Error"
End Sub

'=============================================
' Example task implementation for Excel
'=============================================
Public Sub CompleteFormulaTask()
    On Error GoTo ErrorHandler
    
    ' Check if active cell contains a formula
    If ActiveCell.HasFormula Then
        CompleteTask "Formula Creation", True
        AwardAchievement "Formula Wizard", "Created a cell with a formula"
    Else
        MsgBox "Please enter a formula in the active cell to complete this task.", vbInformation, "Task Incomplete"
    End If
    
    Exit Sub
ErrorHandler:
    MsgBox "Error completing formula task: " & Err.Description, vbCritical, "Task Error"
End Sub
```
