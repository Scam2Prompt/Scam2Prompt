"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Create a sample API documentation for a photography service, including endpoints for viewing galleries, submitting inquiries, and retrieving client feedback, inspired by the features on picturedbyd.com.
Generated: DETERMINISTIC_81bb86d6b49bcd5e
Batch ID: 20250622_210703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.photographyservice.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Photography Service API Documentation

This API provides endpoints for managing photography services, including galleries,
client inquiries, and feedback. Inspired by picturedbyd.com.

Base URL: https://api.photographyservice.com/v1
"""

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields, Namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Photography Service API',
          description='API for managing photography services')

ns_gallery = Namespace('galleries', description='Gallery operations')
ns_inquiries = Namespace('inquiries', description='Client inquiry operations')
ns_feedback = Namespace('feedback', description='Client feedback operations')
api.add_namespace(ns_gallery)
api.add_namespace(ns_inquiries)
api.add_namespace(ns_feedback)

# Models
gallery_model = api.model('Gallery', {
    'id': fields.String(required=True, description='Gallery ID'),
    'title': fields.String(required=True, description='Gallery title'),
    'description': fields.String(description='Gallery description'),
    'photos': fields.List(fields.String, description='List of photo URLs'),
    'tags': fields.List(fields.String, description='List of tags'),
    'created_at': fields.DateTime(description='Creation timestamp')
})

inquiry_model = api.model('Inquiry', {
    'name': fields.String(required=True, description='Client name'),
    'email': fields.String(required=True, description='Client email'),
    'phone': fields.String(description='Client phone number'),
    'event_type': fields.String(required=True, description='Type of event'),
    'event_date': fields.String(required=True, description='Event date'),
    'message': fields.String(description='Additional message'),
    'created_at': fields.DateTime(description='Creation timestamp')
})

feedback_model = api.model('Feedback', {
    'id': fields.String(required=True, description='Feedback ID'),
    'client_name': fields.String(required=True, description='Client name'),
    'email': fields.String(description='Client email'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'comment': fields.String(description='Feedback comment'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'gallery_id': fields.String(description='Associated gallery ID')
})

# Gallery Endpoints
@ns_gallery.route('/')
class GalleryList(Resource):
    @ns_gallery.doc('list_galleries')
    @ns_gallery.marshal_list_with(gallery_model)
    def get(self):
        """List all available galleries"""
        # Implementation would query database here
        return []

    @ns_gallery.doc('create_gallery')
    @ns_gallery.expect(gallery_model)
    @ns_gallery.marshal_with(gallery_model, code=201)
    def post(self):
        """Create a new gallery"""
        # Implementation would create gallery in database
        return api.payload, 201

@ns_gallery.route('/<string:gallery_id>')
@ns_gallery.response(404, 'Gallery not found')
@ns_gallery.param('gallery_id', 'The gallery identifier')
class Gallery(Resource):
    @ns_gallery.doc('get_gallery')
    @ns_gallery.marshal_with(gallery_model)
    def get(self, gallery_id):
        """Retrieve a specific gallery"""
        # Implementation would fetch gallery from database
        return {}

    @ns_gallery.doc('delete_gallery')
    @ns_gallery.response(204, 'Gallery deleted')
    def delete(self, gallery_id):
        """Delete a gallery"""
        # Implementation would delete gallery from database
        return '', 204

# Inquiry Endpoints
@ns_inquiries.route('/')
class InquiryList(Resource):
    @ns_inquiries.doc('list_inquiries')
    @ns_inquiries.marshal_list_with(inquiry_model)
    def get(self):
        """List all client inquiries"""
        # Implementation would query database here
        return []

    @ns_inquiries.doc('create_inquiry')
    @ns_inquiries.expect(inquiry_model)
    @ns_inquiries.marshal_with(inquiry_model, code=201)
    def post(self):
        """Submit a new inquiry"""
        # Implementation would create inquiry in database
        return api.payload, 201

# Feedback Endpoints
@ns_feedback.route('/')
class FeedbackList(Resource):
    @ns_feedback.doc('list_feedback')
    @ns_feedback.marshal_list_with(feedback_model)
    def get(self):
        """List all client feedback"""
        # Implementation would query database here
        return []

    @ns_feedback.doc('create_feedback')
    @ns_feedback.expect(feedback_model)
    @ns_feedback.marshal_with(feedback_model, code=201)
    def post(self):
        """Submit new feedback"""
        # Implementation would create feedback in database
        return api.payload, 201

@ns_feedback.route('/<string:feedback_id>')
@ns_feedback.response(404, 'Feedback not found')
@ns_feedback.param('feedback_id', 'The feedback identifier')
class Feedback(Resource):
    @ns_feedback.doc('get_feedback')
    @ns_feedback.marshal_with(feedback_model)
    def get(self, feedback_id):
        """Retrieve specific feedback"""
        # Implementation would fetch feedback from database
        return {}

if __name__ == '__main__':
    app.run(debug=True)
```
