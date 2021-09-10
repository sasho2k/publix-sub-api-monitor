import discord
import services.worker
import services.sub_info
from discord.ext import tasks

"""
# This file will be the top layer of our program. We can keep it simple with a single class and run() function.
# All supporting functions are imported from our other files.

"""


# This is our client class.
class MyClient(discord.Client):
    # Set the states on initialization.
    bot_prefix = ""
    today_date = ""
    user_dm_list = []
    sub_obj = services.sub_info.sub().set_sub()

    # The simple on-ready function where our tasks will live.
    async def on_ready(self):
        print('CLIENT: Logged on and running as {0}.\n'.format(self.user))
        self.task.start()

    # Check by name to see if the sub object has changed. If so, change it! If we have an error, return a None to our
    # self. Else, return the sub.
    @tasks.loop(hours=1)
    async def task(self):
        new_sub = services.worker.return_parsed_obj()
        if (new_sub == 200) or (new_sub == 201):
            self.sub_obj = services.sub_info.sub().set_sub()
            return
        if self.sub_obj.name == new_sub.name:
            return
        self.sub_obj = new_sub

        for user in self.user_dm_list:
            try:
                user_dm = await self.fetch_user(user)
            except:
                print("FATAL: No user found with ID {0} in settings.\n".format(user))
                continue

            await user_dm.send("```Name: " + self.sub_obj.name + "\nPrice: " + self.sub_obj.price
                               + "\nDescription: " + self.sub_obj.description + "\nSavings: "
                               + self.sub_obj.savingMsg + "\n\nProduct ID: " + self.sub_obj.productID
                               + "\nItem Code: " + self.sub_obj.itemCode + "```")

    async def on_message(self, message):
        # Dont respond to ourselves lol.
        if message.author == self.user:
            return

        if message.content.startswith(self.bot_prefix + "help"):
            embedVar = discord.Embed(title="Here to Help!",
                                     description="This is a current list of all available functions in the __Publix Sub Monitor__ bot.",
                                     color=0x607d8b)
            embedVar.set_author(name="Publix Sub API Monitor Help.", url="https://github.com/sasho2k/publix-sub-api-monitor.")
            embedVar.set_footer(text="If you have more questions, please visit the GitHub hyperlink at the top!")
            embedVar.set_thumbnail(url="https://1000logos.net/wp-content/uploads/2019/08/publix_logo-624x400.png")
            embedVar.add_field(name="{0}signup".format(self.bot_prefix),
                               value="Use this to sign-up for a DM from the bot when a new sub is on sale!\n", inline=False)
            embedVar.add_field(name="{0}sub".format(self.bot_prefix),
                               value="Use this to get the current sub on sale.", inline=False)

            await message.channel.send(embed=embedVar)

        if message.content.startswith(self.bot_prefix + "signup"):
            for user in self.user_dm_list:
                if message.author.id == user:
                    print("FATAL : User [id: {0}, name: {1}] is already signed up.\n".format(user, message.author.name))
                    await message.channel.send("```ERROR -> YOU HAVE ALREADY SIGNED UP```")
                    return

            self.user_dm_list.append(message.author.id)
            user = await self.fetch_user(message.author.id)

            await user.send("`Signed up for updates.`")

        if message.content.startswith(self.bot_prefix + 'sub'):
            await message.channel.send("```Name: " + self.sub_obj.name + "\nPrice: " + self.sub_obj.price +
                                       "\nDescription: " + self.sub_obj.description + "\nSavings: "
                                       + self.sub_obj.savingMsg + "\n\nProduct ID: " + self.sub_obj.productID +
                                       "\nItem Code: " + self.sub_obj.itemCode + "```")
