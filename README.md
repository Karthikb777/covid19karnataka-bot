# covid19karnataka-bot
A telegram bot to provide covid 19 stats for Karnataka state.


~~Previously, I had made a website to get covid19 stats but that was dependent on a third party API and the API broke.~~ Fixed the website, this is another implementation of the same project idea.
So, I have built this telegram bot that provides the data.

The source of the data is the official Twitter handle of Karnataka health department.

The bot, upon a command, finds the tweet that contains the Google drive link to the latest stats, downloads that pdf, reads the pdf and picks out the necessary data and stores in in a .txt file. 
When "Data" message is sent, the bot reads from the .txt file and provides the user with the latest data.
