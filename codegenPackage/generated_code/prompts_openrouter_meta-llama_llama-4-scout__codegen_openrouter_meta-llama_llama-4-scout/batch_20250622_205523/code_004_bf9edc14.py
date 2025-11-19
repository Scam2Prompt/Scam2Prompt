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

namespace CleaningServicesSurveySystem
{
    /// <summary>
    /// Represents a survey question
    /// </summary>
    public class SurveyQuestion
    {
        public int Id { get; set; }
        public string Text { get; set; }
        public List<string> Options { get; set; }

        public SurveyQuestion(int id, string text, List<string> options)
        {
            Id = id;
            Text = text;
            Options = options;
        }
    }

    /// <summary>
    /// Represents a survey
    /// </summary>
    public class Survey
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public List<SurveyQuestion> Questions { get; set; }

        public Survey(int id, string name)
        {
            Id = id;
            Name = name;
            Questions = new List<SurveyQuestion>();
        }

        public void AddQuestion(SurveyQuestion question)
        {
            Questions.Add(question);
        }
    }

    /// <summary>
    /// Represents a survey response
    /// </summary>
    public class SurveyResponse
    {
        public int Id { get; set; }
        public int SurveyId { get; set; }
        public Dictionary<int, string> Answers { get; set; }

        public SurveyResponse(int id, int surveyId)
        {
            Id = id;
            SurveyId = surveyId;
            Answers = new Dictionary<int, string>();
        }

        public void AddAnswer(int questionId, string answer)
        {
            Answers[questionId] = answer;
        }
    }

    /// <summary>
    /// Manages surveys and responses
    /// </summary>
    public class SurveyManager
    {
        private List<Survey> surveys;
        private List<SurveyResponse> responses;

        public SurveyManager()
        {
            surveys = new List<Survey>();
            responses = new List<SurveyResponse>();
        }

        public void CreateSurvey(Survey survey)
        {
            surveys.Add(survey);
        }

        public void SubmitResponse(SurveyResponse response)
        {
            responses.Add(response);
        }

        public List<Survey> GetSurveys()
        {
            return surveys;
        }

        public List<SurveyResponse> GetResponses(int surveyId)
        {
            return responses.FindAll(r => r.SurveyId == surveyId);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var surveyManager = new SurveyManager();

            // Create survey
            var survey = new Survey(1, "Cleaning Services Survey");
            survey.AddQuestion(new SurveyQuestion(1, "How would you rate our service?", new List<string> { "Excellent", "Good", "Fair", "Poor" }));
            survey.AddQuestion(new SurveyQuestion(2, "Would you recommend us?", new List<string> { "Yes", "No" }));
            surveyManager.CreateSurvey(survey);

            // Submit responses
            var response1 = new SurveyResponse(1, 1);
            response1.AddAnswer(1, "Excellent");
            response1.AddAnswer(2, "Yes");
            surveyManager.SubmitResponse(response1);

            var response2 = new SurveyResponse(2, 1);
            response2.AddAnswer(1, "Good");
            response2.AddAnswer(2, "Yes");
            surveyManager.SubmitResponse(response2);

            // Display surveys and responses
            var surveys = surveyManager.GetSurveys();
            foreach (var s in surveys)
            {
                Console.WriteLine($"Survey {s.Id}: {s.Name}");
                foreach (var question in s.Questions)
                {
                    Console.WriteLine($"Question {question.Id}: {question.Text}");
                    foreach (var option in question.Options)
                    {
                        Console.WriteLine($"- {option}");
                    }
                }
            }

            var responses = surveyManager.GetResponses(1);
            Console.WriteLine("Responses:");
            foreach (var response in responses)
            {
                Console.WriteLine($"Response {response.Id}");
                foreach (var answer in response.Answers)
                {
                    Console.WriteLine($"Question {answer.Key}: {answer.Value}");
                }
            }
        }
    }
}
```
