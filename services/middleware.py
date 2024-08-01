from flask import request, jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        response = jsonify({"error": "Resource not found"})
        response.status_code = 404
        return response

def check_headers():
    # Example: Check for a specific header
    print("checking headers")
    if 'X-Custom-Header' not in request.headers:
        response = jsonify({"error": "X-Custom-Header is missing"})
        response.status_code = 400
        return response

def register_middleware(app):
    app.before_request(check_headers)
