import sqlite3
import argparse
from datetime import date
 
connection = sqlite3.connect("TicketList.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS TicketsInfo(
    ID_Number INTEGER PRIMARY KEY,
    Status TEXT,
    Date DATE,
    Description TEXT,
    Title TEXT,
    OS TEXT,
    Resolution TEXT
)""")
connection.commit()
 
 
def insert_ticket(status, ticket_date, description, title, os, resolution=None):
    if ticket_date is None:
        ticket_date = date.today().isoformat()
    cursor.execute(
        "INSERT INTO TicketsInfo (Status, Date, Description, Title, OS, Resolution) VALUES (?, ?, ?, ?, ?, ?)",
        (status, ticket_date, description, title, os, resolution),
    )
    connection.commit()
 
 
def retrieve_tickets(status_filter=None):
    if status_filter:
        cursor.execute("SELECT * FROM TicketsInfo WHERE Status = ?", (status_filter,))
    else:
        cursor.execute("SELECT * FROM TicketsInfo")
    return cursor.fetchall()
 
 
def update_ticket(ticket_id, new_status=None, resolution=None):
    if new_status is not None:
        cursor.execute("UPDATE TicketsInfo SET Status = ? WHERE ID_Number = ?", (new_status, ticket_id))
    if resolution is not None:
        cursor.execute("UPDATE TicketsInfo SET Resolution = ? WHERE ID_Number = ?", (resolution, ticket_id))
    connection.commit()
 
 
def delete_ticket(ticket_id):
    cursor.execute("DELETE FROM TicketsInfo WHERE ID_Number = ?", (ticket_id,))
    connection.commit()
 
 
parser = argparse.ArgumentParser(description="Ticket Tracker")
subparsers = parser.add_subparsers(dest="command")
 
list_parser = subparsers.add_parser("list", help="List all tickets")
list_parser.add_argument("--status", help="Only show tickets with this status (e.g. Open, Closed)")
 
add_parser = subparsers.add_parser("add", help="Add a new ticket")
add_parser.add_argument("--status", required=True)
add_parser.add_argument("--date", help="Defaults to today if not given")
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--title", required=True)
add_parser.add_argument("--os", required=True)
add_parser.add_argument("--resolution", help="How it was fixed, if already known")
 
update_parser = subparsers.add_parser("update", help="Update an existing ticket")
update_parser.add_argument("--id", type=int, required=True, help="ID of the ticket to update")
update_parser.add_argument("--status")
update_parser.add_argument("--resolution", help="How the ticket was resolved")
 
delete_parser = subparsers.add_parser("delete", help="Delete a ticket")
delete_parser.add_argument("--id", type=int, required=True, help="ID of the ticket to delete")
 
args = parser.parse_args()
 
if args.command == "add":
    insert_ticket(args.status, args.date, args.description, args.title, args.os, args.resolution)
    print(f"Ticket added: {args.title}")
elif args.command == "list":
    tickets = retrieve_tickets(args.status)
    if not tickets:
        print("No tickets found.")
    for ticket in tickets:
        print(ticket)
elif args.command == "update":
    update_ticket(args.id, args.status, args.resolution)
    print(f"Ticket with ID {args.id} updated.")
elif args.command == "delete":
    delete_ticket(args.id)
    print(f"Ticket with ID {args.id} deleted")
else:
    parser.print_help()
 
