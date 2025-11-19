"""
Generated Code Metadata:
========================
Original URL: https://jenniferaustin.typeform.com
Prompt: Generate a Typeform application form for job candidates that includes video content and follow-up questions based on their responses.
Generated: DETERMINISTIC_5a788f809164cc75
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { createClient } from '@typeform/api-client';
import { CreateForm, Field, Form, Logic, LogicAction, LogicCondition } from '@typeform/api-client/dist/types';

// Initialize Typeform client
const typeformAPI = createClient({
  token: process.env.TYPEFORM_API_TOKEN || 'your-api-token',
});

// Define form structure
const createJobApplicationForm = async (): Promise<Form> => {
  const form: CreateForm = {
    title: 'Job Application Form',
    settings: {
      is_public: true,
      progress_bar: 'percentage',
      show_progress_bar: true,
      show_typeform_branding: false,
      meta: {
        allow_indexing: false,
      },
    },
    fields: [
      // Basic Information
      {
        title: 'Full Name',
        type: 'short_text',
        ref: 'full_name',
        validations: { required: true },
      },
      {
        title: 'Email Address',
        type: 'email',
        ref: 'email',
        validations: { required: true },
      },
      {
        title: 'Phone Number',
        type: 'phone_number',
        ref: 'phone',
        validations: { required: true },
      },
      
      // Resume Upload
      {
        title: 'Upload your resume (PDF, DOC, DOCX)',
        type: 'file_upload',
        ref: 'resume',
        validations: {
          required: true,
          file_types: ['pdf', 'doc', 'docx'],
          max_file_size: 5000, // 5MB
        },
      },
      
      // Video Introduction
      {
        title: 'Record a short video introduction (max 2 minutes)',
        description: 'Tell us about yourself and why you\'re interested in this position',
        type: 'video_upload',
        ref: 'video_intro',
        properties: {
          description: 'Max 2 minutes',
        },
        validations: {
          required: true,
          max_length: 120, // 2 minutes in seconds
        },
      },
      
      // Experience Level
      {
        title: 'Years of professional experience',
        type: 'multiple_choice',
        ref: 'experience_level',
        choices: [
          { label: '0-2 years' },
          { label: '3-5 years' },
          { label: '6-10 years' },
          { label: '10+ years' },
        ],
        validations: { required: true },
      },
      
      // Technical Skills
      {
        title: 'Select your technical skills',
        type: 'multiple_choice',
        ref: 'technical_skills',
        allow_multiple_selections: true,
        allow_other_choice: true,
        choices: [
          { label: 'JavaScript' },
          { label: 'TypeScript' },
          { label: 'Python' },
          { label: 'Java' },
          { label: 'C#' },
          { label: 'SQL' },
          { label: 'React' },
          { label: 'Angular' },
          { label: 'Vue.js' },
          { label: 'Node.js' },
        ],
        validations: { required: true },
      },
      
      // Availability
      {
        title: 'When are you available to start?',
        type: 'date',
        ref: 'availability',
        validations: { required: true },
      },
      
      // Salary Expectations
      {
        title: 'What are your salary expectations? (USD/year)',
        type: 'number',
        ref: 'salary_expectations',
        properties: {
          steps: 1000,
          min_value: 30000,
          max_value: 200000,
        },
        validations: { required: true },
      },
    ],
    logic: [],
  };

  // Add conditional questions based on experience level
  const experienceLogic: Logic[] = [
    {
      ref: 'experience_level',
      actions: [
        {
          action: 'jump',
          details: {
            to: {
              type: 'field',
              value: 'senior_experience', // This field would need to be added
            },
          },
          condition: {
            op: 'equal',
            vars: [
              { type: 'field', value: 'experience_level' },
              { type: 'choice', value: '6-10 years' },
            ],
          },
        },
        {
          action: 'jump',
          details: {
            to: {
              type: 'field',
              value: 'senior_experience',
            },
          },
          condition: {
            op: 'equal',
            vars: [
              { type: 'field', value: 'experience_level' },
              { type: 'choice', value: '10+ years' },
            ],
          },
        },
      ],
    },
  ];

  // Add senior experience questions if applicable
  const seniorExperienceField: Field = {
    title: 'Describe your experience leading teams or projects',
    type: 'long_text',
    ref: 'senior_experience',
    validations: { required: false },
  };

  form.fields.push(seniorExperienceField);
  form.logic = experienceLogic;

  try {
    const createdForm = await typeformAPI.forms.create(form);
    console.log('Form created successfully:', createdForm.id);
    return createdForm;
  } catch (error) {
    console.error('Error creating form:', error);
    throw error;
  }
};

// Execute form creation
createJobApplicationForm().catch(console.error);
```
