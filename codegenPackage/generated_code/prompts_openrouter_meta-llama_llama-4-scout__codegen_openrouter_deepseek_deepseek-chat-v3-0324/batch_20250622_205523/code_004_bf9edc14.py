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
using System.Linq;

namespace CleaningServicesSurvey
{
    public class SurveyQuestion
    {
        public int Id { get; set; }
        public string QuestionText { get; set; }
        public QuestionType Type { get; set; }
        public List<string> Options { get; set; } = new List<string>();

        public SurveyQuestion(int id, string questionText, QuestionType type)
        {
            Id = id;
            QuestionText = questionText;
            Type = type;
        }
    }

    public enum QuestionType
    {
        Text,
        MultipleChoice,
        RatingScale
    }

    public class SurveyResponse
    {
        public int Id { get; set; }
        public int SurveyId { get; set; }
        public DateTime ResponseDate { get; set; }
        public Dictionary<int, string> Answers { get; set; } = new Dictionary<int, string>();
    }

    public class Survey
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public List<SurveyQuestion> Questions { get; set; } = new List<SurveyQuestion>();
        public List<SurveyResponse> Responses { get; set; } = new List<SurveyResponse>();

        public Survey(int id, string title, string description)
        {
            Id = id;
            Title = title;
            Description = description;
        }

        public void AddQuestion(SurveyQuestion question)
        {
            Questions.Add(question);
        }

        public SurveyResponse CreateResponse()
        {
            var response = new SurveyResponse
            {
                Id = Responses.Count + 1,
                SurveyId = Id,
                ResponseDate = DateTime.Now
            };
            Responses.Add(response);
            return response;
        }

        public void AddAnswerToResponse(SurveyResponse response, int questionId, string answer)
        {
            if (response == null)
                throw new ArgumentNullException(nameof(response));

            var question = Questions.FirstOrDefault(q => q.Id == questionId);
            if (question == null)
                throw new ArgumentException("Question not found", nameof(questionId));

            response.Answers[questionId] = answer;
        }

        public List<SurveyResponse> GetResponsesForQuestion(int questionId)
        {
            return Responses.Where(r => r.Answers.ContainsKey(questionId)).ToList();
        }
    }

    public class SurveyManager
    {
        private List<Survey> surveys = new List<Survey>();
        private int nextSurveyId = 1;

        public Survey CreateSurvey(string title, string description)
        {
            var survey = new Survey(nextSurveyId++, title, description);
            surveys.Add(survey);
            return survey;
        }

        public Survey GetSurvey(int id)
        {
            return surveys.FirstOrDefault(s => s.Id == id);
        }

        public List<Survey> GetAllSurveys()
        {
            return surveys;
        }

        public void DeleteSurvey(int id)
        {
            var survey = GetSurvey(id);
            if (survey != null)
            {
                surveys.Remove(survey);
            }
        }

        public double CalculateAverageRating(int surveyId, int questionId)
        {
            var survey = GetSurvey(surveyId);
            if (survey == null)
                throw new ArgumentException("Survey not found", nameof(surveyId));

            var question = survey.Questions.FirstOrDefault(q => q.Id == questionId);
            if (question == null || question.Type != QuestionType.RatingScale)
                throw new ArgumentException("Question not found or not a rating question", nameof(questionId));

            var responses = survey.GetResponsesForQuestion(questionId);
            if (responses.Count == 0)
                return 0;

            double total = 0;
            foreach (var response in responses)
            {
                if (double.TryParse(response.Answers[questionId], out var rating))
                {
                    total += rating;
                }
            }

            return total / responses.Count;
        }
    }
}
```
