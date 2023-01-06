import asyncio, time
from pyrogram import Client
from pyrogram.errors import FloodWait

app = Client("my_account")

async def main():
    try:
        async with app:
            for n in range(1, 99999):
                n = str(n)
                if len(n) == 1:
                    n = "0000" + n
                elif len(n) == 2:
                    n = "000" + n
                elif len(n) == 3:
                    n = "00" + n
                elif len(n) == 4:
                    n = "0" + n

                print(n)

                phoneNumber = f"99893{n}83"
                user = await app.add_contact(user_id=5251622961, first_name="Jasmina", phone_number=phoneNumber)

                if (int(n) % 30) == 0:
                    time.sleep(10)
    except FloodWait as e:
        await asyncio.sleep(e.value)

app.run(main())