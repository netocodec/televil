 ![Televil Logo](logo.png "Televil")

**Televil** is an automated script that allows you to spam messages into telegram bots.
**Disclaimer**: Do not use this for evil intentions! Use it with caution!

## Features

- [x] Uses TOR relays to do the requests
- [x] Detects and updates the waiting time to do more requests
- [x] Message can be customizable
- [ ] Can't continue when the user of the bot blocks you!


## Usage

`main.py [-h] -id ID -token TOKEN [-message MESSAGE] [-file-message FILE_MESSAGE] [-wait WAIT] [-follow-no-error-time]`

## Options

| Parameter | Description |
| --------- | ----------- |
| -h, --help | Show this help message and exit |
| -id ID | ID of the bot (e.g.: 6907124010) REQUIRED |
| -token TOKEN | Token of the bot (e.g.: 48302563512:itjhueorpdEv9j31jy1I5BdScXaWpQhjg) REQUIRED |
| -message MESSAGE, -m MESSAGE | Message text to send! |
| -file-message FILE_MESSAGE | Reads the message on a file and sets as a text to send! |
| -wait WAIT, -w WAIT | Time to wait for the next message (In seconds) |
| -follow-no-error-time | This flag is to disable the following error that Telegram App returns when there are too many requests ocurred it returns how many seconds the application should wait to resume the work again! |


