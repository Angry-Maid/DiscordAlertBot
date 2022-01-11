# Simple Helper Bot on Python
This bot was first created for one command that it contains - `alert`. It's use are generally for discord servers that are configured for schools, or something like remote learning. It's main purpose is only to keep record and track that students were alerted of upcoming lessons.
# Why there is need for `alert` when discord events exist
Because server for which it first was created is intended for preschoolers who are not technically apt with tasks like that, as well as their parents so not always they can see the alert for event on server. One more purpose for it is that there is no way as of writing this bot without some other bot help to reschedule the event right after it ends.
# Current existing functionality
Currently bot has small number of commands.(checklist are for completed implementations)
- [x] `debug`
- [x] `alert`
- [x] `generate_report`
## `debug` Command
`debug` purely exists to view how bot interprets given command as well as some additional diagnostic info that'll be recorded in database later down the line which will be used for command `generate_report`
## `alert` Command
Main command for which this bot was created, it used to send out DM message to anyone included in `role` which is passed as first argument of alert and text of message which will follow the `role` in command. It'll also include ability to send out a media file(picture).
## `generate_report` Command
Will be used to send out `csv` file to one who requested it. It's only limited to the people who has `role` with `Admininstator` permission.
# How to set up the bot?
This bot uses python 3.9-3.10 as well as couple of packages that need for it to work:
- `hikari`
- `pyyaml`
- `sqlalchemy`
```sh
$ git clone https://github.com/Angry-Maid/DiscordAlertBot.git
$ cd repo
$ python -mvenv venv
$ source venv\bin\activate
(venv) $ python -mpip install -r requirements.txt
```
Rename `config.yaml.example` to `config.yaml` and fill in needed values.
And bot are technically ready to work.
## To host bot
You can use `heroku` to host it because it doesn't require that much computational power and it'll be quick enough to respond if dyno will fall asleep. But requires PostgreSQL plugin.
To do that you'll just have to create `Procfile` in root directory of bot and set it contents to:
```
bot: python3 main.py
```
And create file `runtime.txt` and set it contents to:
```
python-3.9.5
```
And hook up heroku upstream to then push to it so heroku can start building application. It'll auto detect that you have `requirements.txt` and use it to install all packages.