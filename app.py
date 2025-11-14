# Step 1: Import the Flask library
from flask import Flask

# Step 2: Create a Flask "app" instance
# This 'app' is your entire web server.
app = Flask(__name__)

# Step 3: Define a "route"
# A route is a URL for your server.
# This '@' line tells Flask: "When someone visits the main URL ('/')..."
@app.route("/")
def home():
    # "...run this 'home' function and send back whatever it returns."
    return "Hello, World! My Flask server is running!"

# Step 4: Run the app
# This 'if' statement is standard Python. It means:
# "Only run the server if this script is executed directly."
if __name__ == "__main__":
    # This starts your server.
    # 'debug=True' is very helpful. It automatically restarts
    # your server every time you save the file, so you don't
    # have to stop and start it manually.
    app.run(debug=True)

