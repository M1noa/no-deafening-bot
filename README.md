# No Deafenening User Disconnect Bot
[![ViewCount](https://img.shields.io/endpoint?url=https://hits.dwyl.com/Minoa/FreshPC.json%3Fcolor%3Dblue&label=Views)](http://hits.dwyl.com/Minoa/FreshPC)
 [![GitHub forks](https://img.shields.io/github/forks/M1noa/FreshPC.svg)](https://github.com/M1noa/FreshPC/network)

## Introduction

The Deafened User Disconnect Bot is a Discord bot designed to monitor voice channels in a specific guild (server) and disconnect users who have deafened themselves. The bot aims to promote active communication within voice channels by removing users who are deafened and sending them a message.

## Features

- Automatic detection of deafened users in all voice channels.
- Disconnection of deafened users.
- Sending a direct message to disconnected users with a specified message.
- Customizable exclusion of specific users by their Discord user ID.

## Configuring
   - Replace `'BOT_TOKEN'` in the code with your Discord bot token.
   - Customize the `ID_OF_USER_TO_EXCLUDE` variable with the ID of any user you want to exclude from disconnection.
   - Change `GUILD_TO_RUN_IN` with the ID of the guild/server to run the discord bot in.

## Usage

The bot will automatically check for deafened users every second in all voice channels of the specified guild. If a deafened user is detected, they will be disconnected from the voice channel, and the bot will send them a direct message with the specified message.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!
