# Import Flask for flask app object
from flask import Flask

# Create flask app object
app = Flask(__name__)
app.config.from_object(Config)


# Import all views
import certhasher.views