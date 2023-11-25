import discord
import asyncio

intents = discord.Intents.default()
intents.voice_states = True

client = discord.Client(intents=intents)
guild_id = GUILD_TO_RUN_IN
excluded_user_id = ID_OF_USER_TO_EXCLUDE

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Start checking for deafened users every second
    await check_deafened_users()

async def check_deafened_users():
    guild = client.get_guild(guild_id)
    while True:
        for channel in guild.voice_channels:
            for member in channel.members:
                if member.id == excluded_user_id:
                    continue  # Skip the excluded user

                if member.voice.self_deaf:
                    # Disconnect the member
                    await member.edit(voice_channel=None)

                    # Send a DM to the member
                    await member.send("What's the point of being in a voice call if you're deafened..")
                    await member.send("If your one of thoose pepole that just sits in a call deafend doing nothing, you deaserve the punishment of death........")
                    await member.send("I mean, imagine joining a party and then putting on noise-canceling headphones; it's like you're physically there, but not really. It kind of defeats the purpose of the whole thing, right?")
                    await member.send("It's as if you're at a comedy show with earmuffs on. You might catch a few visual cues, but the laughter is lost in translation!")
                    await member.send("I'm not saying it's a crime or anything, but it's a bit perplexing, you know? Like having a TV show on mute you're missing out on the good stuff!")
                    await member.send("**Anyways heres a cool website!**||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _https://minoa.cat")
                    print(f"{member.display_name} has an extra chromosome.. Removed from {channel.name}")

        # Log that the bot checked the voice channels
        print("Femboys r epic!")

        # Wait for a second before checking again
        await asyncio.sleep(0.5)

client.run('BOT_TOKEN')
