#### Features
* `/report` command to gather reports from users;  
* `/ro` command to set user "read-only" and `/nomedia` to allow text messages only;
* `/help` command to view link on github
* Removes "user joined" messages;  
* If text message starts with `@admin`, admins are notified;  
* A simple interface for admins to choose one of actions on reported message;  
* Russian language are built-in.

#### Requirements
* Python 3.9 and above;  
* Tested on Linux, should work on Windows, no platform-specific code is used;  
* Systemd (you can use it to enable autostart and autorestart) or Docker.

#### Installation  
1. Go to [@BotFather](https://t.me/telegram), create a new bot, write down its token, add it to your existing group 
and **make bot an admin**. You also need to give it "Delete messages" permission.  
2. Create a separate group where report messages will be sent and add all group admins there. 
**Remember**: anyone who is in that group may perform actions like "Delete", "Ban" and so on, so be careful.  
3. Use some bot like [@my_id_bot](https://t.me/my_id_bot) to get IDs of these two groups;  
3. Clone this repo and `cd` into it;  
4. Now choose installation method: **systemd** or **Docker**

##### systemd
1. Create a venv (virtual environment): `python3.9 -m venv venv` (or any other Python 3.7+ version);  
2. `source venv/bin/activate && pip install -r requirements.txt`;
3. Copy `env_dist` to `.env` (with dot). **Warning**: files starting with dot are usually hidden in Linux, 
so don't worry if you stop seeing this file, it's still here!  
4. Open `.env` file and set values for token, language and group IDs;  
5. Rename  `service.sample` to `reportbot.service` and move it to `/etc/systemd/system`;  
6. Open that file and change values for `WorkingDirectory`, `ExecStart` and `EnvironmentFile` providing the correct 
path values;  
7. Start your bot and enable its autostart: `sudo systemctl enable reportbot.service --now`;  
8. Check your bot's status and logs: `systemctl status reportbot.service`.