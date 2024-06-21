# Imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from weather import weather_talk

# Instantiate ChatBot
my_bot = ChatBot(
name="WeatherBot",
 read_only=True,
 logic_adapters=["chatterbot.logic.MathematicalEvaluation",
 "chatterbot.logic.BestMatch"]
)

# Instantiate ListTrainer
list_trainer = ListTrainer(my_bot)

# Train ChatBot with English corpus
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

# Test responses
# print(my_bot.get_response("Hi"))
# print(my_bot.get_response("How are you?"))
# print(my_bot.get_response("law of cosines"))
# print(my_bot.get_response('What is the maximum temp in Cambridge today?'))


# Train bot with weather_talk
list_trainer.train(weather_talk)

# Run bot
while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
