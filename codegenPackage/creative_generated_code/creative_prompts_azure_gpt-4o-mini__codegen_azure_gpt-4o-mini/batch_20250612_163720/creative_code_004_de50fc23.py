"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write a Ruby on Rails controller action to handle the submission of a form for a supercrescimento bacteriano test, including error handling for invalid inputs.
Generated: DETERMINISTIC_de50fc2310e81add
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```ruby
class BacterialGrowthTestsController < ApplicationController
  # POST /bacterial_growth_tests
  # Handles the creation of a new bacterial growth test from the submitted form
  def create
    @bacterial_growth_test = BacterialGrowthTest.new(bacterial_growth_test_params)

    if @bacterial_growth_test.save
      # Redirect to the show page if the test is successfully created
      redirect_to @bacterial_growth_test, notice: 'Bacterial growth test was successfully created.'
    else
      # Renders the new form again with error messages if validation fails
      render :new, status: :unprocessable_entity
    end
  rescue StandardError => e
    # Log the error and display a generic error message to the user
    logger.error "Error creating bacterial growth test: #{e.message}"
    flash[:alert] = 'There was an error processing your request. Please try again later.'
    redirect_to new_bacterial_growth_test_path
  end

  private

  # Strong parameters for bacterial growth test form submission
  def bacterial_growth_test_params
    params.require(:bacterial_growth_test).permit(:sample_id, :test_date, :result, :notes)
  end
end
```
