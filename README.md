
## Discord Server Setupper by Asterdamous

This Python bot automatically sets up a fully structured Discord server for you with channels, roles, and categories—all based on your input. It's fast, clean, and exits automatically after setup!

### Features:

* Renames the server
* Deletes all existing channels
* Creates structured categories and channels:

  * **Main:** `announcement`, `rules`, `desk`
  * **World:** `chat`, `bot-cmds`, `socials`
  * **Memories:** `gallery`, `selfies`, `arts`
  * **Voice-Hangouts:** `VC 1`, `VC 2`, `VC 3`
  * (Optional) **Welcome:** `verify`
* Creates roles with specific colors:

  * Owner (Red)
  * Administrator (Blue)
  * Moderator (Green)
  * Top Hangouters (Violet)
  * Members (Sky Blue)
* Outputs a `result.txt` file with your setup details
* Leaves the server after setup
* Closes the terminal automatically after setup

---

## Tutorial: How to Use

1. **Run the script**
   Just launch the Python file like any script:
   `python server_setup.py`

2. **Answer the prompts in the terminal**
   You'll be asked:

   * What is the bot token?
   * What is the owner's ID?
   * What should be the new server name?
   * Do you want to create a Welcome category?

3. **Add the bot to your server**
   After running the script and entering the details, **invite the bot to your server** using the OAuth2 invite link from the [Discord Developer Portal](https://discord.com/developers/applications).

4. **Done!**
   The bot will:

   * Auto-run setup when it joins the server
   * Leave the server
   * Save everything in `result.txt`
   * Close the terminal automatically
