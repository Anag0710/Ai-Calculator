import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/Ai-Calculator/calc-be-main'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your app and create a WSGI application
from main import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
else:
    # For WSGI servers
    from uvicorn.middleware.wsgi import WSGIMiddleware
    application = WSGIMiddleware(app)
