from memory import get_ticket, delete_ticket

async def handle_close(ctx):
    user_id = str(ctx.author.id)
    ticket_id = get_ticket(user_id)
    if not ticket_id:
        await ctx.send("❌ You don't have any open tickets to close.")
        return
    delete_ticket(user_id)
    await ctx.send(f"✅ Ticket #{ticket_id} has been closed and removed from your record.")
