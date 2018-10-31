import discord

client = discord.Client ()
players = {}

@client.event
async def on_ready():
    print(client.user.name)
    print("-------------------")

@client.event
async def on_message(message):
    if message.content.startswith("$stop"):
        server = message.server
        voice_client = client.voice_client_in(server)
        leave = await voice_client.disconnect()
        await client.send_message(message.channel, "Stopped the music!")

    if message.content.startswith("$play"):
        try:
            yt_url = message.content[6:]
            await client.send_message(message.channel, "Playing your song!")
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Error2______[Error]".format(error=e))
                    server = message.server
                    voice_client = client.voice_client_in(server)
                    leave = await voice_client.disconnect()
                    await client.send_message(message.channel, "I need a URL!")
                    leave.start()

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.channel, "Error3____[error]".format(error=e))
                    await client.send_message(message.channel, "I need a URL!")
        except Exception as e:
            await client.send_message(message.channel, "Error4________[error]".format(error=e))
            await client.send_message(message.channel, "Type it again pls :D")




client.run("NTA2MjA0MTczOTUyNjE0NDAw.DrevMQ.tmYeTCzVUYmiWeDjIKWhCuy4Dwc")
