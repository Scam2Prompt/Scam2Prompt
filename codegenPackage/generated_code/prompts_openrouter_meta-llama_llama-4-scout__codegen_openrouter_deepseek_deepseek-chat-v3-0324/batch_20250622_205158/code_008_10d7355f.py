"""
Generated Code Metadata:
========================
Original URL: https://d5crl8r4pqx.typeform.com
Prompt: "Create a Typeform NPS survey template for customer success teams, with analysis and reporting features."
Generated: DETERMINISTIC_10d7355f9e06f6a4
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Typeform NPS survey implementation with analysis and reporting features:

```typescript
// nps-survey.ts
import { createClient } from '@typeform/api-client';
import { calculateNPS, generateReport } from './nps-analyzer';

interface SurveyResponse {
  id: string;
  answers: {
    score: number;
    comment?: string;
  };
  metadata: {
    respondentId: string;
    date: string;
  };
}

interface NPSSurveyConfig {
  typeformApiKey: string;
  formId: string;
}

export class NPSSurvey {
  private typeformClient: ReturnType<typeof createClient>;
  private formId: string;

  constructor(config: NPSSurveyConfig) {
    if (!config.typeformApiKey || !config.formId) {
      throw new Error('Missing required configuration: typeformApiKey and formId');
    }

    this.typeformClient = createClient({ token: config.typeformApiKey });
    this.formId = config.formId;
  }

  /**
   * Fetch survey responses from Typeform
   */
  async getResponses(): Promise<SurveyResponse[]> {
    try {
      const responses = await this.typeformClient.responses.list({
        uid: this.formId,
        pageSize: 1000,
      });

      return responses.items.map((item: any) => ({
        id: item.response_id,
        answers: {
          score: parseInt(item.answers.find((a: any) => a.field.id === 'nps_score').number),
          comment: item.answers.find((a: any) => a.field.id === 'nps_comment')?.text,
        },
        metadata: {
          respondentId: item.hidden?.respondent_id || 'anonymous',
          date: item.submitted_at,
        },
      }));
    } catch (error) {
      console.error('Failed to fetch survey responses:', error);
      throw new Error('Failed to fetch survey responses');
    }
  }

  /**
   * Generate NPS analysis report
   */
  async generateAnalysisReport(): Promise<any> {
    const responses = await this.getResponses();
    if (responses.length === 0) {
      throw new Error('No responses found for analysis');
    }

    const scores = responses.map(r => r.answers.score);
    return generateReport(scores, responses);
  }
}
```

```typescript
// nps-analyzer.ts
interface NPSReport {
  nps: number;
  totalResponses: number;
  promoters: number;
  passives: number;
  detractors: number;
  promoterPercentage: number;
  detractorPercentage: number;
  comments: string[];
}

/**
 * Calculate Net Promoter Score from survey responses
 */
export function calculateNPS(scores: number[]): number {
  if (!scores || scores.length === 0) {
    throw new Error('No scores provided for NPS calculation');
  }

  const promoters = scores.filter(score => score >= 9).length;
  const detractors = scores.filter(score => score <= 6).length;
  const total = scores.length;

  return Math.round(((promoters - detractors) / total) * 100);
}

/**
 * Generate comprehensive NPS report
 */
export function generateReport(scores: number[], responses: SurveyResponse[]): NPSReport {
  const nps = calculateNPS(scores);
  const totalResponses = scores.length;
  const promoters = scores.filter(score => score >= 9).length;
  const passives = scores.filter(score => score > 6 && score < 9).length;
  const detractors = scores.filter(score => score <= 6).length;

  return {
    nps,
    totalResponses,
    promoters,
    passives,
    detractors,
    promoterPercentage: Math.round((promoters / totalResponses) * 100),
    detractorPercentage: Math.round((detractors / totalResponses) * 100),
    comments: responses
      .filter(r => r.answers.comment)
      .map(r => r.answers.comment) as string[],
  };
}
```

```typescript
// typeform-template.json
{
  "title": "Customer Success NPS Survey",
  "fields": [
    {
      "title": "How likely are you to recommend our product to a friend or colleague?",
      "type": "opinion_scale",
      "id": "nps_score",
      "properties": {
        "steps": 11,
        "start_at_one": true,
        "labels": {
          "left": "Not likely",
          "right": "Very likely"
        }
      },
      "validations": {
        "required": true
      }
    },
    {
      "title": "What's the main reason for your score?",
      "type": "long_text",
      "id": "nps_comment",
      "properties": {
        "description": "Optional feedback"
      }
    },
    {
      "type": "hidden",
      "id": "respondent_id",
      "ref": "hidden_respondent_id"
    }
  ],
  "logic": [],
  "thankyou_screens": [
    {
      "ref": "thankyou",
      "title": "Thank you for your feedback!",
      "properties": {
        "show_button": false,
        "share_icons": false
      }
    }
  ]
}
```

```typescript
// index.ts
import { NPSSurvey } from './nps-survey';

// Example usage
const survey = new NPSSurvey({
  typeformApiKey: 'your_typeform_api_key',
  formId: 'your_form_id'
});

async function runAnalysis() {
  try {
    const report = await survey.generateAnalysisReport();
    console.log('NPS Report:', report);
  } catch (error) {
    console.error('Error generating report:', error);
  }
}

runAnalysis();
```
