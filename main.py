from telethon import TelegramClient
import getpass
import time

print("*******************")
print("~ Loading APP ...")
print("! APP loaded.\n\n\n")

print("<----    ^_^ Welcome to Saeed's Telesend.    ---->")

api_id = input("[-- Please Enter Your api_id: ")
api_hash = input("[-- Please Enter Your api_hash: ")

phone_number = input("[-- Please Enter Your Phone number (including country code with +): ")
app_password = getpass.getpass("[-- Please Enter your password (* if no password):  ")


print("~ Loging in to your account ...")

# Create a new Telegram client session
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Log in to the Telegram API using your phone number and app password
    await client.start(phone_number, app_password)

    print("! Logged into your account.")

    print("~ Downloading your chats ...")
    # Get the list of personal chats
    dialogs = await client.get_dialogs()

    print("! All chats downloaded")

    msg = input("[-- Please enter your text:\n--> ")
    delay = int(input("[-- Please enter delay time (in seconds): "))

    print("\n\n~ SENDING MESSAGES ...")

    failed = 0
    sent = 0

    # Send 'hello' message to each personal chat
    for dialog in dialogs:
        if not dialog.is_group and not dialog.is_channel:
            try:
                await client.send_message(dialog.id, msg)
                sent += 1
                print(f"Sent: {sent},  Failed: {failed}", end="\r")
                # print(f'Sent "hello" to {dialog.name} ({dialog.id})')
                time.sleep(delay)
            except Exception as e:
                failed += 1
                print(f"Sent: {sent}, Failed: {failed}", end="\r")
                # print(f'Failed to send message to {dialog.name} ({dialog.id}): {e}')
    print(f"Sent: {sent}, Failed: {failed}")
    print("\n!Sent messages successfully")

    print("~ Logging out of your account ...")

    # Log out of the Telegram API
    await client.log_out()

    print("! Logged out. Good Luck.")

# Run the main function
with client:
    client.loop.run_until_complete(main())
