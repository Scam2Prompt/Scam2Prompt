"""
Generated Code Metadata:
========================
Original URL: https://airgiveaway.typeform.com
Prompt: Create a Typeform quiz template for lead generation, using AI analysis to provide personalized results.
Generated: DETERMINISTIC_3504bfc31ac3c80f
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Typeform Quiz Template for Lead Generation with AI Analysis

import { createClient } from '@typeform/api-client';
import { OpenAI } from 'openai';

// Initialize Typeform client
const typeformClient = createClient({
  token: process.env.TYPEFORM_API_KEY || '',
});

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY || '',
});

interface LeadData {
  name: string;
  email: string;
  company?: string;
  role?: string;
  responses: Record<string, any>;
}

interface PersonalizedResult {
  summary: string;
  recommendations: string[];
  nextSteps: string[];
}

// Create the lead generation form
async function createLeadGenerationForm() {
  try {
    const form = await typeformClient.forms.create({
      title: 'AI-Powered Business Assessment',
      settings: {
        is_public: true,
        language: 'en',
        progress_bar: 'proportion',
        show_progress_bar: true,
        show_typeform_branding: false,
      },
      fields: [
        {
          title: 'What is your name?',
          type: 'short_text',
          validations: { required: true },
        },
        {
          title: 'What is your email address?',
          type: 'email',
          validations: { required: true },
        },
        {
          title: 'What company do you work for?',
          type: 'short_text',
          validations: { required: false },
        },
        {
          title: 'What is your role?',
          type: 'short_text',
          validations: { required: false },
        },
        {
          title: 'What are your biggest business challenges?',
          type: 'long_text',
          validations: { required: true },
        },
        {
          title: 'What are your primary goals for the next quarter?',
          type: 'multiple_choice',
          properties: {
            choices: [
              { label: 'Increase revenue' },
              { label: 'Reduce costs' },
              { label: 'Improve customer satisfaction' },
              { label: 'Expand to new markets' },
              { label: 'Other' },
            ],
          },
          validations: { required: true },
        },
        {
          title: 'On a scale of 1-10, how would you rate your current solution?',
          type: 'number',
          validations: { required: true, min_value: 1, max_value: 10 },
        },
        {
          title: 'What is your budget for a solution?',
          type: 'dropdown',
          properties: {
            choices: [
              { label: 'Less than $10k' },
              { label: '$10k - $50k' },
              { label: '$50k - $100k' },
              { label: '$100k+' },
            ],
          },
          validations: { required: true },
        },
      ],
    });

    console.log('Form created successfully:', form.id);
    return form.id;
  } catch (error) {
    console.error('Error creating form:', error);
    throw error;
  }
}

// Process form responses and generate personalized results
async function processResponse(responseId: string): Promise<PersonalizedResult> {
  try {
    const response = await typeformClient.responses.get({
      uid: responseId,
    });

    const leadData: LeadData = {
      name: response.answers.find(a => a.field.ref === 'What is your name?')?.text || '',
      email: response.answers.find(a => a.field.ref === 'What is your email address?')?.text || '',
      company: response.answers.find(a => a.field.ref === 'What company do you work for?')?.text,
      role: response.answers.find(a => a.field.ref === 'What is your role?')?.text,
      responses: response.answers.reduce((acc, answer) => {
        acc[answer.field.ref] = answer[answer.type];
        return acc;
      }, {} as Record<string, any>),
    };

    // Generate AI-powered analysis
    const prompt = `Based on the following business assessment, provide a summary, recommendations, and next steps:
    
    Name: ${leadData.name}
    Company: ${leadData.company || 'Not provided'}
    Role: ${leadData.role || 'Not provided'}
    Challenges: ${leadData.responses['What are your biggest business challenges?']}
    Goals: ${leadData.responses['What are your primary goals for the next quarter?']}
    Current Solution Rating: ${leadData.responses['On a scale of 1-10, how would you rate your current solution?']}
    Budget: ${leadData.responses['What is your budget for a solution?']}

    Provide a concise summary of their situation, 3-5 specific recommendations, and 2-3 next steps they should consider.`;

    const aiResponse = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [
        {
          role: 'system',
          content: 'You are a business consultant analyzing assessment responses to provide personalized recommendations.',
        },
        { role: 'user', content: prompt },
      ],
      temperature: 0.7,
      max_tokens: 500,
    });

    const content = aiResponse.choices[0]?.message?.content || '';
    const [summary, recommendations, nextSteps] = content.split('\n\n');

    return {
      summary: summary.replace('Summary:', '').trim(),
      recommendations: recommendations
        .replace('Recommendations:', '')
        .trim()
        .split('\n')
        .map(r => r.replace(/^\d+\.\s*/, '').trim()),
      nextSteps: nextSteps
        .replace('Next Steps:', '')
        .trim()
        .split('\n')
        .map(s => s.replace(/^\d+\.\s*/, '').trim()),
    };
  } catch (error) {
    console.error('Error processing response:', error);
    throw error;
  }
}

// Main function to handle the lead generation workflow
async function handleLeadGeneration(responseId: string) {
  try {
    const results = await processResponse(responseId);
    
    // Here you would typically:
    // 1. Store the lead data in your CRM
    // 2. Send the personalized results to the lead
    // 3. Trigger any follow-up workflows
    
    return results;
  } catch (error) {
    console.error('Error in lead generation workflow:', error);
    throw error;
  }
}

// Example usage
// createLeadGenerationForm().then(formId => console.log('Form ID:', formId));
// handleLeadGeneration('response123').then(results => console.log(results));
```
