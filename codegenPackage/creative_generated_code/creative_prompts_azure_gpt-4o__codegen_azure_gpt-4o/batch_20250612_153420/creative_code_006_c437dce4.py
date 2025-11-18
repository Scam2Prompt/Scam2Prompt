"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Develop a web application prototype for managing daily meme contests with prizes, as described in the "Rich Pepe" Frogmap Phase 2.
Generated: DETERMINISTIC_c437dce4f567af0e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based web application prototype using the Flask framework. It includes the basic functionality for managing daily meme contests with prizes.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.exceptions import HTTPException
from datetime import datetime
import os

# Create a Flask application instance
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Simple in-memory data storage for prototype
# Production apps should use a database
meme_contests = []  # List to store contests
submissions = {}    # Dictionary to store submissions (key: contest_id)
votes = {}          # Dictionary to store votes (key: contest_id)

# Error handling
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions gracefully."""
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).get_data()
    return response

# Route: Homepage - List all meme contests
@app.route('/')
def home():
    """Display all meme contests."""
    return render_template('home.html', contests=meme_contests)

# Route: Create a new meme contest
@app.route('/create', methods=['GET', 'POST'])
def create_contest():
    """Create a new daily meme contest."""
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        prize = request.form.get('prize')

        # Validation
        if not title or not prize or not description:
            flash('All fields are required!', 'danger')
            return redirect(url_for('create_contest'))

        contest = {
            'id': len(meme_contests) + 1,
            'title': title,
            'description': description,
            'prize': prize,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        meme_contests.append(contest)
        submissions[contest['id']] = []
        votes[contest['id']] = {}
        flash('Meme contest created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('create_contest.html')

# Route: View contest details and submissions
@app.route('/contest/<int:contest_id>')
def view_contest(contest_id):
    """View details of a specific contest and its submissions."""
    contest = next((c for c in meme_contests if c['id'] == contest_id), None)
    if not contest:
        flash('Contest not found!', 'danger')
        return redirect(url_for('home'))
    contest_submissions = submissions.get(contest_id, [])
    return render_template('view_contest.html', contest=contest, submissions=contest_submissions)

# Route: Submit a meme to a contest
@app.route('/contest/<int:contest_id>/submit', methods=['POST'])
def submit_meme(contest_id):
    """Submit a meme to a specific contest."""
    contest = next((c for c in meme_contests if c['id'] == contest_id), None)
    if not contest:
        flash('Contest not found!', 'danger')
        return redirect(url_for('home'))

    username = request.form.get('username')
    meme_url = request.form.get('meme_url')

    # Validation
    if not username or not meme_url:
        flash('All fields are required!', 'danger')
        return redirect(url_for('view_contest', contest_id=contest_id))

    # Add submission
    submission = {
        'id': len(submissions[contest_id]) + 1,
        'username': username,
        'meme_url': meme_url,
        'votes': 0,
        'submitted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    submissions[contest_id].append(submission)
    flash('Meme submitted successfully!', 'success')
    return redirect(url_for('view_contest', contest_id=contest_id))

# Route: Vote for a meme
@app.route('/contest/<int:contest_id>/vote/<int:submission_id>', methods=['POST'])
def vote_meme(contest_id, submission_id):
    """Vote for a meme submission."""
    contest = next((c for c in meme_contests if c['id'] == contest_id), None)
    if not contest:
        flash('Contest not found!', 'danger')
        return redirect(url_for('home'))

    contest_submissions = submissions.get(contest_id, [])
    submission = next((s for s in contest_submissions if s['id'] == submission_id), None)
    if not submission:
        flash('Meme submission not found!', 'danger')
        return redirect(url_for('view_contest', contest_id=contest_id))

    username = request.form.get('username')
    if not username:
        flash('Username is required to vote!', 'danger')
        return redirect(url_for('view_contest', contest_id=contest_id))

    # Prevent double voting
    if votes[contest_id].get(username) == submission_id:
        flash('You already voted for this meme!', 'danger')
        return redirect(url_for('view_contest', contest_id=contest_id))

    # Register the vote
    submission['votes'] += 1
    votes[contest_id][username] = submission_id
    flash('Vote registered successfully!', 'success')
    return redirect(url_for('view_contest', contest_id=contest_id))

# Main entry point
if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)
```

### Templates:
You will need corresponding HTML templates for this app (`home.html`, `create_contest.html`, `view_contest.html`). Here is a summary of their content:

1. **`home.html`**
   - Displays a list of meme contests with links to view them.
   - Includes a button to create a new contest.

2. **`create_contest.html`**
   - Contains a form to create a new meme contest.

3. **`view_contest.html`**
   - Displays contest details and meme submissions.
   - Includes forms to submit memes and vote.

Remember to populate the `templates/` directory with the appropriate HTML files and use CSS for styling.
