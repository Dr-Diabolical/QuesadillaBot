import discord as ds

# Create bot class
class MyBot(ds.Client):
    async def on_ready(self): # On ready, send start message
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message): # On message, display message in command line
        print('Message from {0.author}: {0.content}'.format(message))

# Obtain discord bot key
with open("key.txt", "r") as key_data:
    key = key_data.readline()

# Initialize and run bot
bot = MyBot()
bot.run(key)