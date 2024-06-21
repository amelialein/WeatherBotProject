from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from weather import weather_talk

my_bot = ChatBot(
name="WeatherBot",
 read_only=True,
 logic_adapters=["chatterbot.logic.MathematicalEvaluation",
 "chatterbot.logic.BestMatch"]
)

weather_talk2 = weather_talk[0]

weather_talk3 = weather_talk[1]

list_trainer = ListTrainer(my_bot)

for conv in weather_talk:
    for item in (conv):
        list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("Hi"))
print(my_bot.get_response("How are you?"))
print(my_bot.get_response("law of cosines"))
print(my_bot.get_response('What is the maximum temp in Cambridge today?'))

while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
