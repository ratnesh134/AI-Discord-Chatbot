from memory import get_ticket

async def handle_status(ctx):
    user_id = str(ctx.author.id)
    ticket_id = get_ticket(user_id)
    if ticket_id:
        await ctx.send(f"📩 Your open ticket is: #{ticket_id}")
    else:
        await ctx.send("📭 You don't have any open tickets.")
