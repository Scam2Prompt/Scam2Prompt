"""
Generated Code Metadata:
========================
Original URL: https://kineticairdrop.typeform.com
Prompt: Design a Typeform survey to gather employee satisfaction data, including questions and logic jumps.
Generated: DETERMINISTIC_a22ac124a122fdc8
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Typeform survey for employee satisfaction
const typeform = {
  title: "Employee Satisfaction Survey",
  welcome_screens: [
    {
      title: "Welcome to the Employee Satisfaction Survey",
      description: "Your feedback is important to us. This survey will take approximately 5 minutes to complete.",
      show_button: true,
      button_text: "Start Survey"
    }
  ],
  fields: [
    {
      title: "How long have you been with the company?",
      type: "dropdown",
      validations: { required: true },
      properties: {
        description: "Select your tenure",
        choices: [
          { label: "Less than 1 year", value: "0-1" },
          { label: "1-3 years", value: "1-3" },
          { label: "3-5 years", value: "3-5" },
          { label: "5+ years", value: "5+" }
        ]
      }
    },
    {
      title: "How satisfied are you with your current role?",
      type: "rating",
      validations: { required: true },
      properties: {
        description: "Rate from 1 (very dissatisfied) to 5 (very satisfied)",
        steps: 5,
        shape: "star"
      }
    },
    {
      title: "What do you enjoy most about working here?",
      type: "multiple_choice",
      validations: { required: false },
      properties: {
        description: "Select all that apply",
        choices: [
          { label: "Company culture", value: "culture" },
          { label: "Work-life balance", value: "balance" },
          { label: "Career growth opportunities", value: "growth" },
          { label: "Compensation and benefits", value: "compensation" },
          { label: "Team members", value: "team" },
          { label: "Other", value: "other" }
        ]
      }
    },
    {
      title: "Please specify 'Other'",
      type: "short_text",
      validations: { required: false },
      properties: { description: "If you selected 'Other', please specify" },
      logic: {
        jumps: [
          {
            conditions: [
              {
                field: "What do you enjoy most about working here?",
                operator: "contains",
                value: "other"
              }
            ],
            destination: {
              type: "field"
            }
          }
        ]
      }
    },
    {
      title: "How likely are you to recommend this company as a great place to work?",
      type: "opinion_scale",
      validations: { required: true },
      properties: {
        description: "Scale from 0 (not likely) to 10 (very likely)",
        steps: 11,
        start_at_one: false
      }
    },
    {
      title: "What could we improve to make your experience better?",
      type: "long_text",
      validations: { required: false },
      properties: { description: "Please share your suggestions" }
    },
    {
      title: "Would you like to schedule a follow-up conversation with HR?",
      type: "yes_no",
      validations: { required: true },
      properties: { description: "Select Yes if you'd like to discuss anything privately" }
    },
    {
      title: "Please provide your email for follow-up",
      type: "email",
      validations: { required: false },
      properties: { description: "Only required if you requested a follow-up" },
      logic: {
        jumps: [
          {
            conditions: [
              {
                field: "Would you like to schedule a follow-up conversation with HR?",
                operator: "equal",
                value: "yes"
              }
            ],
            destination: {
              type: "field"
            }
          }
        ]
      }
    }
  ],
  thankyou_screens: [
    {
      title: "Thank you for your feedback!",
      description: "Your responses will help us improve the employee experience.",
      show_button: false
    }
  ],
  settings: {
    language: "en",
    is_public: true,
    progress_bar: "percentage",
    show_progress_bar: true,
    show_typeform_branding: false,
    meta: {
      allow_indexing: false
    }
  }
};

// Export for use in Typeform API
module.exports = typeform;
```
