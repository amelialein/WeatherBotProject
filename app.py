# Import modules from Flask
from flask import Flask, render_template, request
from chatbotsafe import my_bot

# Instantiate Flask
app = Flask(__name__)


# Define home page
@app.route("/")
def home():
    return render_template("index.html")


# Define bot page
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the input from the user
    bot_input = request.form["message"]

    # Generate the response
    bot_response = my_bot.get_response(bot_input)
    # chat_history = []
    # chat_history.append(f"User: {bot_input}\nChatbot: {bot_response}")

    # Render the html file
    return render_template(
          "chatbot.html",
          bot_input=bot_input,
          bot_response=bot_response
          )


# Start flask app
if __name__ == "__main__":
    app.run(debug=True)
