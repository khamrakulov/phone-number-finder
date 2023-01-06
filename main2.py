import asyncio, time
from pyrogram import Client

app = Client("my_account2")

async def main():
    async with app:
        for n in range(30000, 99999):
            phoneNumber = f"99893{n}83"
            user = await app.add_contact(user_id=5251622961, first_name="Jasmina", phone_number=phoneNumber)
            time.sleep(1.5)
            print(n)

            if (n % 40) == 0:
                time.sleep(20)



app.run(main())