from flask import Flask
from dotenv import load_dotenv
import sys




app = Flask(__name__)

@app.route("/")
def home():
    # dev_env = os.environ.get("DEV_ENV", "Default  Environment")
    argument_value = sys.argv[1] if len(sys.argv) > 1 else ""
    my_value = f".env.{argument_value}"

   
    return f"Home - {my_value} "

if __name__ == "__main__":
    app.run(debug=True)