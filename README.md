# rapuli-bot
Rapuli is a Discord bot for tracking weekly turnip stock prices for the game Animal Crossing New Horizons on Nintendo Switch. This bot is intended for small scale Discord servers for sharing prices between a friend group! It may not work as well on a larger server just because there would be a long list of turnip price links.<br>

## Intro
This bot will take inputs from the user of their turnip prices and will then return a link to [TurnipProphet](https://turnipprophet.io)  with your price data already set. Everytime you set your price, the bot will update the link with your new pricing.
![Image of Rapuli-Bot on Discord with generated links to turnip prophet](https://kalciumcove.ie/web/assets/images/github/rapuli-bot/rapuli-bot-example.png)
## Setup
Run ```pip install -r requirements.txt``` to install required packages.<br>
Duplicate .env.example to .env and replaces token-here with your Discord token.<br>
Run ```python bot.py``` to start up the bot.

## Using The Bot

Set your current turnip price<br>
```~turnip 210```<br>
*replace 210 with your price

Set your turnip price pattern<br>
```~pattern big-spike```<br>
*pattern-options: big-spike | small-spike | random | idk | decreasing

## Important
Make sure to make a seperate channel for using this bot as once it has been set to and is used, the bot will delete any messages and clears out functions after use as to keep the channel clean so you can easily see the list of turnip prices created.

## Project Status
[Rapuli-Bot Trello](https://trello.com/b/BUUe6i2Q)<br>
As of June 2020 this project is currently paused as I have taken a break from playing Animal Crossing New Horizons but I do hope to get back to it and get the last few bugs fixed up and implement some new features to make the bot even easier to use.
