"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Write a code snippet in C# to implement a simple customer satisfaction survey system for a cleaning services company, with features like survey creation and response tracking.
Generated: DETERMINISTIC_bf9edc14609ec8a3
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;

namespace CustomerSatisfactionSurvey
{
    // Class representing a single survey question
    public class SurveyQuestion
    {
        public int Id { get; set; }
        public string QuestionText { get; set; }
    }

    // Class representing a customer's response to a survey question
    public class SurveyResponse
    {
        public int QuestionId { get; set; }
        public int Rating { get; set; } // Rating from 1 (poor) to 5 (excellent)
    }

    // Class representing the survey system
    public class SurveySystem
    {
        private List<SurveyQuestion> _questions;
        private Dictionary<int, List<SurveyResponse>> _responses;

        public SurveySystem()
        {
            _questions = new List<SurveyQuestion>();
            _responses = new Dictionary<int, List<SurveyResponse>>();
        }

        // Method to create a new survey question
        public void AddQuestion(string questionText)
        {
            int newId = _questions.Count + 1;
            _questions.Add(new SurveyQuestion { Id = newId, QuestionText = questionText });
            Console.WriteLine($"Question added: {questionText}");
        }

        // Method to display all survey questions
        public void DisplayQuestions()
        {
            Console.WriteLine("Survey Questions:");
            foreach (var question in _questions)
            {
                Console.WriteLine($"{question.Id}. {question.QuestionText}");
            }
        }

        // Method to record a customer's response
        public void RecordResponse(int customerId, int questionId, int rating)
        {
            if (rating < 1 || rating > 5)
            {
                Console.WriteLine("Error: Rating must be between 1 and 5.");
                return;
            }

            if (!_responses.ContainsKey(customerId))
            {
                _responses[customerId] = new List<SurveyResponse>();
            }

            _responses[customerId].Add(new SurveyResponse { QuestionId = questionId, Rating = rating });
            Console.WriteLine($"Response recorded for Customer {customerId}: Question {questionId}, Rating {rating}");
        }

        // Method to display all responses for a specific customer
        public void DisplayResponses(int customerId)
        {
            if (!_responses.ContainsKey(customerId))
            {
                Console.WriteLine($"No responses found for Customer {customerId}.");
                return;
            }

            Console.WriteLine($"Responses for Customer {customerId}:");
            foreach (var response in _responses[customerId])
            {
                var question = _questions.Find(q => q.Id == response.QuestionId);
                Console.WriteLine($"Question: {question.QuestionText}, Rating: {response.Rating}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Initialize the survey system
            SurveySystem surveySystem = new SurveySystem();

            // Add survey questions
            surveySystem.AddQuestion("How satisfied are you with the cleaning service?");
            surveySystem.AddQuestion("Was the staff professional and courteous?");
            surveySystem.AddQuestion("Would you recommend our service to others?");

            // Display survey questions
            surveySystem.DisplayQuestions();

            // Record customer responses
            surveySystem.RecordResponse(1, 1, 5);
            surveySystem.RecordResponse(1, 2, 4);
            surveySystem.RecordResponse(1, 3, 5);

            // Display responses for a specific customer
            surveySystem.DisplayResponses(1);

            // Keep the console open
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
```
