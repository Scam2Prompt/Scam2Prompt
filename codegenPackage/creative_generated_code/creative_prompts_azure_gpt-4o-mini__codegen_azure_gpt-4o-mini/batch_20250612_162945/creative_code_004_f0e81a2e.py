"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Write a Ruby on Rails controller action that handles the submission of MBA applications, validating the eligibility criteria as specified by the School of Management at Tribhuvan University.
Generated: DETERMINISTIC_f0e81a2e8ded0799
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
class MbaApplicationsController < ApplicationController
  # POST /mba_applications
  # Handles the submission of MBA applications.
  # Validates eligibility criteria specified by the School of Management at Tribhuvan University.
  def create
    @application = MbaApplication.new(application_params)

    # Validate eligibility criteria
    if eligible_for_application?(@application)
      if @application.save
        redirect_to @application, notice: 'Application submitted successfully.'
      else
        render :new, alert: 'There was an error submitting your application.'
      end
    else
      # Render the new application form with an error message
      flash.now[:alert] = 'You do not meet the eligibility criteria for this application.'
      render :new
    end
  end

  private

  # Strong parameters for application submission
  def application_params
    params.require(:mba_application).permit(:name, :email, :gpa, :work_experience_years)
  end

  # Check if the applicant meets the eligibility criteria
  def eligible_for_application?(application)
    # Example eligibility criteria:
    # 1. Minimum GPA of 3.0
    # 2. At least 2 years of work experience
    application.gpa >= 3.0 && application.work_experience_years >= 2
  end
end
```
