"""
Generated Code Metadata:
========================
Original URL: https://pineappledex.org
Prompt: Generate a code example that demonstrates how to handle human verification in a web application, inspired by the methods used on PineappleDex.
Generated: DETERMINISTIC_32d8dab5dc7967e8
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template, session
import random
import string
import time
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # In production, use a proper secret key

# Configuration
VERIFICATION_TIMEOUT = 300  # 5 minutes in seconds
MAX_ATTEMPTS = 3
VERIFICATION_COOLDOWN = 60  # 1 minute in seconds after max attempts

def generate_verification_token(length=32):
    """Generate a random verification token."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_verification_question():
    """Generate a simple math question for verification."""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is {a} {operator} {b}?"
    
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    else:
        answer = a * b
    
    return question, str(answer)

def requires_verification(f):
    """Decorator to check if user needs verification."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('verified', False):
            return f(*args, **kwargs)
        
        if session.get('verification_attempts', 0) >= MAX_ATTEMPTS:
            if 'last_attempt_time' in session:
                if time.time() - session['last_attempt_time'] < VERIFICATION_COOLDOWN:
                    return jsonify({
                        'error': 'Too many attempts. Please try again later.',
                        'cooldown': VERIFICATION_COOLDOWN - int(time.time() - session['last_attempt_time'])
                    }), 429
                else:
                    session['verification_attempts'] = 0
        
        if 'verification_token' not in session:
            session['verification_token'] = generate_verification_token()
            session['verification_question'], session['verification_answer'] = generate_verification_question()
            session['verification_start_time'] = time.time()
        
        return jsonify({
            'verification_required': True,
            'question': session['verification_question'],
            'token': session['verification_token']
        }), 403
    return decorated_function

@app.route('/verify', methods=['POST'])
def verify():
    """Handle verification submission."""
    data = request.get_json()
    
    if not data or 'answer' not in data or 'token' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    
    if 'verification_token' not in session or 'verification_answer' not in session:
        return jsonify({'error': 'Session expired. Please refresh.'}), 400
    
    if data['token'] != session['verification_token']:
        return jsonify({'error': 'Invalid token'}), 400
    
    if time.time() - session.get('verification_start_time', 0) > VERIFICATION_TIMEOUT:
        return jsonify({'error': 'Verification timeout. Please try again.'}), 400
    
    if data['answer'].strip() == session['verification_answer']:
        session['verified'] = True
        session.pop('verification_token', None)
        session.pop('verification_question', None)
        session.pop('verification_answer', None)
        session.pop('verification_start_time', None)
        session.pop('verification_attempts', None)
        session.pop('last_attempt_time', None)
        return jsonify({'success': True})
    else:
        session['verification_attempts'] = session.get('verification_attempts', 0) + 1
        session['last_attempt_time'] = time.time()
        
        if session['verification_attempts'] >= MAX_ATTEMPTS:
            return jsonify({
                'error': 'Too many attempts. Please try again later.',
                'cooldown': VERIFICATION_COOLDOWN
            }), 429
        
        return jsonify({'error': 'Incorrect answer. Please try again.'}), 400

@app.route('/protected', methods=['GET'])
@requires_verification
def protected_route():
    """Example protected route that requires verification."""
    return jsonify({'message': 'You have access to this protected resource!'})

@app.route('/')
def index():
    """Home page with verification form."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Human Verification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .verification-form {
            display: none;
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .error {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <h1>Welcome to our website</h1>
    <div id="content">
        <p>This is a protected resource. Please complete human verification to continue.</p>
        <button id="request-access">Request Access</button>
    </div>

    <div id="verification-form" class="verification-form">
        <h2>Human Verification</h2>
        <p id="verification-question"></p>
        <input type="text" id="verification-answer" placeholder="Your answer">
        <input type="hidden" id="verification-token">
        <button id="submit-verification">Submit</button>
        <p id="verification-message"></p>
    </div>

    <div id="protected-content" style="display: none;">
        <h2>Protected Content</h2>
        <p id="protected-message"></p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const requestBtn = document.getElementById('request-access');
            const verificationForm = document.getElementById('verification-form');
            const verificationQuestion = document.getElementById('verification-question');
            const verificationAnswer = document.getElementById('verification-answer');
            const verificationToken = document.getElementById('verification-token');
            const submitBtn = document.getElementById('submit-verification');
            const verificationMessage = document.getElementById('verification-message');
            const protectedContent = document.getElementById('protected-content');
            const protectedMessage = document.getElementById('protected-message');
            const content = document.getElementById('content');

            requestBtn.addEventListener('click', function() {
                fetch('/protected')
                    .then(response => {
                        if (response.status === 403) {
                            return response.json();
                        }
                        throw new Error('Unexpected response');
                    })
                    .then(data => {
                        if (data.verification_required) {
                            verificationQuestion.textContent = data.question;
                            verificationToken.value = data.token;
                            verificationForm.style.display = 'block';
                            content.style.display = 'none';
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            });

            submitBtn.addEventListener('click', function() {
                const answer = verificationAnswer.value.trim();
                const token = verificationToken.value;

                if (!answer) {
                    verificationMessage.textContent = 'Please enter an answer';
                    verificationMessage.className = 'error';
                    return;
                }

                fetch('/verify', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        answer: answer,
                        token: token
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        verificationMessage.textContent = 'Verification successful!';
                        verificationMessage.className = 'success';
                        setTimeout(() => {
                            verificationForm.style.display = 'none';
                            protectedContent.style.display = 'block';
                            protectedMessage.textContent = 'You have successfully verified and can now access protected content.';
                        }, 1000);
                    } else if (data.error) {
                        verificationMessage.textContent = data.error;
                        verificationMessage.className = 'error';
                        if (data.cooldown) {
                            let seconds = data.cooldown;
                            const timer = setInterval(() => {
                                seconds--;
                                verificationMessage.textContent = `Too many attempts. Please try again in ${seconds} seconds.`;
                                if (seconds <= 0) {
                                    clearInterval(timer);
                                    verificationMessage.textContent = 'You may now try again.';
                                }
                            }, 1000);
                        }
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    verificationMessage.textContent = 'An error occurred. Please try again.';
                    verificationMessage.className = 'error';
                });
            });
        });
