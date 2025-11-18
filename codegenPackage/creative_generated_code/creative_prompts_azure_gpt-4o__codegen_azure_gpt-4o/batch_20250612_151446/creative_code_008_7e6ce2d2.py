"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Suggest a library for creating localized Persian-language forms for vocational school administrators, such as leave request forms or student registration forms.
Generated: DETERMINISTIC_7e6ce2d29280def6
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly. Below is an example Python code using the Flask framework for creating a localized form for Persian-language vocational school administrators. This example leverages `WTForms` for form handling and includes error handling for form submission. The text localization assumes Persian translations are provided.

```python
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['BABEL_DEFAULT_LOCALE'] = 'fa'  # Set to Persian language
babel = Babel(app)

# Custom form class using Flask-WTF
class LeaveRequestForm(FlaskForm):
    full_name = StringField(_l('نام کامل'), validators=[
        DataRequired(message=_l('این قسمت الزامی است')),
        Length(max=50, message=_l('نام کامل نمی‌تواند بیش از 50 کاراکتر باشد'))
    ])
    leave_reason = SelectField(_l('دلیل مرخصی'), choices=[
        ('personal', _l('شخصی')),
        ('medical', _l('پزشکی')),
        ('other', _l('سایر'))
    ], validators=[DataRequired(message=_l('لطفاً یک دلیل انتخاب کنید'))])
    submit = SubmitField(_l('ارسال'))

@app.route('/leave_request', methods=['GET', 'POST'])
def leave_request():
    form = LeaveRequestForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Handle form submission logic here (e.g., save data to a database)
            flash(_l('فرم با موفقیت ارسال شد'), 'success')
        else:
            # Show validation errors
            flash(_l('لطفاً خطاهای فرم را بررسی کنید'), 'danger')
    return render_template('leave_request_form.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Template file (`leave_request_form.html`)**
```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>فرم درخواست مرخصی</title>
</head>
<body>
    <h1>فرم درخواست مرخصی</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        <div>
            <label for="full_name">{{ form.full_name.label }}</label>
            {{ form.full_name(class="form-control") }}
            {% for error in form.full_name.errors %}
                <span style="color:red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            <label for="leave_reason">{{ form.leave_reason.label }}</label>
            {{ form.leave_reason(class="form-control") }}
            {% for error in form.leave_reason.errors %}
                <span style="color:red;">{{ error }}</span>
            {% endfor %}
        </div>
        <div>
            {{ form.submit(class="btn btn-primary") }}
        </div>
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li style="color: {{ 'green' if category == 'success' else 'red' }};">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

### Requirements:
1. Install Python dependencies:
    ```bash
    pip install flask flask-wtf flask-babel
    ```
2. Ensure that your application is deployed with proper internationalization configurations for Persian translations.
