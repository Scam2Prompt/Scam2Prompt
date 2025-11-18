"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Create a Windows desktop application in C# that integrates Ookla Speedtest functionality to test internet speed and store the results in a local database.
Generated: DETERMINISTIC_9b709eb256c7bc08
Batch ID: 20250612_150347
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.speedtest.net/apps/cli": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;
using System.Data.SQLite; // Install System.Data.SQLite using NuGet package manager

namespace SpeedTestApp
{
    public partial class MainForm : Form
    {
        private string dbFilePath = "SpeedTestResults.db";

        public MainForm()
        {
            InitializeComponent();
            InitializeDatabase();
        }

        private void InitializeComponent()
        {
            this.Text = "Internet Speed Test";
            this.Width = 400;
            this.Height = 300;

            Button btnRunSpeedTest = new Button
            {
                Text = "Run Speed Test",
                Location = new System.Drawing.Point(150, 50),
                Width = 100
            };
            btnRunSpeedTest.Click += BtnRunSpeedTest_Click;

            this.Controls.Add(btnRunSpeedTest);
        }

        private void BtnRunSpeedTest_Click(object sender, EventArgs e)
        {
            try
            {
                var result = RunSpeedTest();
                SaveResultsToDatabase(result);
                MessageBox.Show($"Download Speed: {result.DownloadSpeed} Mbps\nUpload Speed: {result.UploadSpeed} Mbps\nPing: {result.Ping} ms", "Speed Test Results");
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private SpeedTestResult RunSpeedTest()
        {
            // Require speedtest CLI (https://www.speedtest.net/apps/cli) installed and added to PATH
            Process process = new Process
            {
                StartInfo =
                {
                    FileName = "speedtest",
                    Arguments = "--format=json",
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };

            process.Start();
            string jsonOutput = process.StandardOutput.ReadToEnd();
            process.WaitForExit();

            if (process.ExitCode != 0)
            {
                throw new Exception("Speedtest failed to execute. Ensure Ookla Speedtest CLI is installed.");
            }

            // Parse JSON output (using System.Text.Json for simplicity)
            var result = System.Text.Json.JsonSerializer.Deserialize<SpeedTestResult>(jsonOutput);

            if (result == null)
            {
                throw new Exception("Failed to parse speedtest results.");
            }

            return result;
        }

        private void InitializeDatabase()
        {
            if (!File.Exists(dbFilePath))
            {
                SQLiteConnection.CreateFile(dbFilePath);
                using (var connection = new SQLiteConnection($"Data Source={dbFilePath};Version=3;"))
                {
                    connection.Open();
                    string createTableQuery = @"
                    CREATE TABLE SpeedTestResults (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        DownloadSpeed REAL,
                        UploadSpeed REAL,
                        Ping REAL,
                        TestDate TEXT
                    )";
                    using (var command = new SQLiteCommand(createTableQuery, connection))
                    {
                        command.ExecuteNonQuery();
                    }
                }
            }
        }

        private void SaveResultsToDatabase(SpeedTestResult result)
        {
            using (var connection = new SQLiteConnection($"Data Source={dbFilePath};Version=3;"))
            {
                connection.Open();
                string insertQuery = @"
                INSERT INTO SpeedTestResults (DownloadSpeed, UploadSpeed, Ping, TestDate)
                VALUES (@DownloadSpeed, @UploadSpeed, @Ping, @TestDate)";
                using (var command = new SQLiteCommand(insertQuery, connection))
                {
                    command.Parameters.AddWithValue("@DownloadSpeed", result.DownloadSpeed);
                    command.Parameters.AddWithValue("@UploadSpeed", result.UploadSpeed);
                    command.Parameters.AddWithValue("@Ping", result.Ping);
                    command.Parameters.AddWithValue("@TestDate", DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss"));
                    command.ExecuteNonQuery();
                }
            }
        }
    }

    public class SpeedTestResult
    {
        public double DownloadSpeed { get; set; } // Mbps
        public double UploadSpeed { get; set; }   // Mbps
        public double Ping { get; set; }         // ms
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
```
