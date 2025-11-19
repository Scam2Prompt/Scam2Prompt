"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Illustrate how to implement a digital patient file system in C# that customizes patient records as described in the Luxteb software features.
Generated: DETERMINISTIC_c661eefbe13d8c92
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;

// Namespace for the digital patient file system
namespace DigitalPatientFileSystem
{
    // Enum to represent the patient's gender
    public enum Gender
    {
        Male,
        Female,
        Other
    }

    // Class representing a patient record
    public class PatientRecord
    {
        public int PatientId { get; private set; }
        public string Name { get; set; }
        public DateTime DateOfBirth { get; set; }
        public Gender Gender { get; set; }
        public List<string> MedicalHistory { get; private set; }

        // Constructor to initialize a patient record
        public PatientRecord(int patientId, string name, DateTime dateOfBirth, Gender gender)
        {
            PatientId = patientId;
            Name = name;
            DateOfBirth = dateOfBirth;
            Gender = gender;
            MedicalHistory = new List<string>();
        }

        // Method to add a medical history entry
        public void AddMedicalHistory(string entry)
        {
            if (string.IsNullOrWhiteSpace(entry))
            {
                throw new ArgumentException("Medical history entry cannot be empty.", nameof(entry));
            }

            MedicalHistory.Add(entry);
        }

        // Method to display patient details
        public void DisplayPatientDetails()
        {
            Console.WriteLine($"Patient ID: {PatientId}");
            Console.WriteLine($"Name: {Name}");
            Console.WriteLine($"Date of Birth: {DateOfBirth.ToShortDateString()}");
            Console.WriteLine($"Gender: {Gender}");
            Console.WriteLine("Medical History:");
            foreach (var history in MedicalHistory)
            {
                Console.WriteLine($" - {history}");
            }
        }
    }

    // Class to manage patient records
    public class PatientRecordManager
    {
        private readonly Dictionary<int, PatientRecord> _patientRecords;
        private int _nextPatientId;

        // Constructor to initialize the patient record manager
        public PatientRecordManager()
        {
            _patientRecords = new Dictionary<int, PatientRecord>();
            _nextPatientId = 1; // Starting Patient ID from 1
        }

        // Method to add a new patient record
        public PatientRecord AddPatient(string name, DateTime dateOfBirth, Gender gender)
        {
            var patientRecord = new PatientRecord(_nextPatientId++, name, dateOfBirth, gender);
            _patientRecords[patientRecord.PatientId] = patientRecord;
            return patientRecord;
        }

        // Method to retrieve a patient record by ID
        public PatientRecord GetPatientById(int patientId)
        {
            if (_patientRecords.TryGetValue(patientId, out var patientRecord))
            {
                return patientRecord;
            }
            else
            {
                throw new KeyNotFoundException($"No patient found with ID: {patientId}");
            }
        }

        // Method to display all patient records
        public void DisplayAllPatients()
        {
            foreach (var record in _patientRecords.Values)
            {
                record.DisplayPatientDetails();
                Console.WriteLine();
            }
        }
    }

    // Main class for application entry point
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                var patientManager = new PatientRecordManager();

                // Add patients
                var patient1 = patientManager.AddPatient("John Doe", new DateTime(1990, 5, 1), Gender.Male);
                patient1.AddMedicalHistory("Hypertension");

                var patient2 = patientManager.AddPatient("Jane Smith", new DateTime(1985, 8, 12), Gender.Female);
                patient2.AddMedicalHistory("Diabetes");

                // Display all patients
                patientManager.DisplayAllPatients();

                // Retrieve a specific patient record
                var retrievedPatient = patientManager.GetPatientById(1);
                retrievedPatient.DisplayPatientDetails();
            }
            catch (Exception ex)
            {
                // Error handling: Log the exception message
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
