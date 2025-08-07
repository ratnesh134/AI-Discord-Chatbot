from llm import ask_llm
from mantis import create_ticket
from memory import get_ticket, store_ticket

async def handle_ask(ctx, query, bot):
    user_id = str(ctx.author.id)
    existing_ticket = get_ticket(user_id)

    response = ask_llm(query)

    if existing_ticket:
        response += f"\n\n📌 You already have an open ticket: #{existing_ticket}"

    await ctx.send(f"🤖 {response}")

    if not existing_ticket and ("create a support ticket" in response.lower() or "shall I create" in response.lower()):
        await ctx.send("Do you want me to create a support ticket? Reply with `yes` to confirm.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            reply = await bot.wait_for('message', check=check, timeout=30.0)
            if reply.content.lower() == "yes":
                ticket_id = create_ticket(summary=query, description=query)
                if ticket_id:
                    store_ticket(user_id, ticket_id)
                    await ctx.send(f"✅ Ticket #{ticket_id} has been created and linked to your account.")
                else:
                    await ctx.send("⚠️ Failed to create ticket. Try again later.")
            else:
                await ctx.send("Okay, no ticket was created.")
        except:
            await ctx.send("⏳ Timed out. Please try again.")
