"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: Suggest a method to implement a notification system for students using Araform's online platform to alert them about new course offerings.
Generated: DETERMINISTIC_adb959ed5d890ec6
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Notification System for Students using Terraform**
=====================================================

### Prerequisites

* Terraform 1.2+
* AWS SNS and Lambda services

### notification_system.tf
```terraform
# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

# Create an SNS topic for notifications
resource "aws_sns_topic" "course_notifications" {
  name = "course-notifications"
}

# Create an IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec" {
  name        = "lambda-exec"
  description = "Execution role for Lambda function"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Effect = "Allow"
        Sid      = ""
      }
    ]
  })
}

# Create an IAM policy for Lambda execution
resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda-policy"
  description = "Policy for Lambda execution"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Resource = "arn:aws:logs:*:*:*"
        Effect    = "Allow"
      },
      {
        Action = "sns:Publish"
        Resource = aws_sns_topic.course_notifications.arn
        Effect    = "Allow"
      }
    ]
  })
}

# Attach the IAM policy to the Lambda execution role
resource "aws_iam_role_policy_attachment" "lambda_attach" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

# Create a Lambda function for sending notifications
resource "aws_lambda_function" "send_notification" {
  filename      = "lambda_function_payload.zip"
  function_name = "send-notification"
  handler       = "index.handler"
  runtime       = "nodejs14.x"
  role          = aws_iam_role.lambda_exec.arn
}

# Create a Lambda event source mapping for SNS
resource "aws_lambda_subscription_filter" "course_notifications_filter" {
  name           = "course-notifications-filter"
  filter_name    = "course-notifications-filter"
  filter_pattern = "{\"source\": [\"course-offerings\"]}"
  depends_on     = [aws_lambda_function.send_notification]
}

resource "aws_sns_topic_subscription" "lambda_subscription" {
  topic_arn = aws_sns_topic.course_notifications.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_function.send_notification.arn
}
```

### lambda_function/index.js
```javascript
// Import required modules
const AWS = require('aws-sdk');
const sns = new AWS.SNS({ region: 'us-west-2' });
const ses = new AWS.SES({ region: 'us-west-2' });

// Define the handler function for Lambda
exports.handler = async (event) => {
  try {
    // Extract the course offering details from the event
    const courseOffering = JSON.parse(event.Records[0].Sns.Message);

    // Define the email message
    const emailMessage = {
      Source: 'your-verified-ses-email@example.com',
      Destination: {
        ToAddresses: courseOffering.studentEmails,
        CcAddresses: [],
        BccAddresses: []
      },
      Message: {
        Body: {
          Text: {
            Data: `New course offering: ${courseOffering.courseName} - ${courseOffering.courseDescription}`
          }
        },
        Subject: {
          Data: `New Course Offering: ${courseOffering.courseName}`
        }
      }
    };

    // Send the email using SES
    const data = await ses.sendEmail(emailMessage).promise();
    console.log(data);

    // Return a success response
    return {
      statusCode: 200,
      body: JSON.stringify('Email sent successfully!')
    };
  } catch (err) {
    console.error(err);
    return {
      statusCode: 500,
      body: JSON.stringify('Error sending email')
    };
  }
};
```

### main.tf (Example usage)
```terraform
# Create a new course offering
resource "aws_sns_topic" "course_offerings" {
  name = "course-offerings"
}

# Publish a new course offering to the SNS topic
resource "null_resource" "publish_course_offering" {
  provisioner "local-exec" {
    command = "aws sns publish --topic-arn ${aws_sns_topic.course_offerings.arn} --message '{\"courseName\":\"Math 101\",\"courseDescription\":\"Introduction to mathematics\",\"studentEmails\":[\"student1@example.com\",\"student2@example.com\"]}'"
  }
}
```
### variables.tf
```terraform
variable "aws_region" {
  type        = string
  default     = "us-west-2"
  description = "AWS region"
}

variable "course_offerings_topic_arn" {
  type        = string
  default     = aws_sns_topic.course_offerings.arn
  description = "Course offerings SNS topic ARN"
}
```
