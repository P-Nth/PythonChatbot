from Backend import app
from flask_cors import CORS

app = app.App()
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
