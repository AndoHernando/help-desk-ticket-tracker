"""
Help Desk Ticket Tracker
Author: Andy Hernandez
Description: A CLI application to log, categorize, track, and resolve
             IT support tickets with persistent JSON storage.
"""

import json
import os
from datetime import datetime

TICKETS_FILE = "tickets.json"

# ── Data Layer ─────────────────────────────────────────────────────────────────

def load_tickets():
    """Load tickets from JSON file, return empty list if file doesn't exist."""
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tickets(tickets):
    """Persist tickets list to JSON file."""
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=2)

def get_next_id(tickets):
    """Generate the next ticket ID."""
    if not tickets:
        return 1
    return max(t["id"] for t in tickets) + 1

# ── Core Functions ─────────────────────────────────────────────────────────────

def create_ticket(tickets):
    print("\n── New Ticket ─────────────────────────────")
    title       = input("Issue title       : ").strip()
    category    = choose_option("Category", ["Hardware", "Software", "Network", "Account", "Other"])
    priority    = choose_option("Priority", ["Low", "Medium", "High", "Critical"])
    description = input("Description       : ").strip()

    ticket = {
        "id":          get_next_id(tickets),
        "title":       title,
        "category":    category,
        "priority":    priority,
        "description": description,
        "status":      "Open",
        "created_at":  datetime.now().strftime("%Y-%m-%d %H:%M"),
        "resolved_at": None,
        "notes":       []
    }
    tickets.append(ticket)
    save_tickets(tickets)
    print(f"\n✔ Ticket #{ticket['id']} created successfully.")

def view_tickets(tickets, filter_status=None):
    filtered = [t for t in tickets if filter_status is None or t["status"] == filter_status]
    if not filtered:
        print("\n  No tickets found.")
        return
    print(f"\n{'ID':<5} {'Priority':<10} {'Status':<12} {'Category':<12} {'Title'}")
    print("─" * 65)
    for t in filtered:
        print(f"#{t['id']:<4} {t['priority']:<10} {t['status']:<12} {t['category']:<12} {t['title']}")

def view_ticket_detail(tickets):
    ticket_id = get_ticket_id_input("View ticket #: ")
    ticket = find_ticket(tickets, ticket_id)
    if not ticket:
        return
    print(f"""
── Ticket #{ticket['id']} Detail ──────────────────────────────
  Title       : {ticket['title']}
  Category    : {ticket['category']}
  Priority    : {ticket['priority']}
  Status      : {ticket['status']}
  Created     : {ticket['created_at']}
  Resolved    : {ticket['resolved_at'] or 'N/A'}
  Description : {ticket['description']}
  Notes       : {chr(10) + '             : '.join(ticket['notes']) if ticket['notes'] else 'None'}
""")

def update_ticket_status(tickets):
    ticket_id = get_ticket_id_input("Update ticket #: ")
    ticket = find_ticket(tickets, ticket_id)
    if not ticket:
        return
    new_status = choose_option("New status", ["Open", "In Progress", "Resolved", "Closed"])
    ticket["status"] = new_status
    if new_status in ("Resolved", "Closed"):
        ticket["resolved_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_tickets(tickets)
    print(f"✔ Ticket #{ticket_id} status updated to '{new_status}'.")

def add_note(tickets):
    ticket_id = get_ticket_id_input("Add note to ticket #: ")
    ticket = find_ticket(tickets, ticket_id)
    if not ticket:
        return
    note = input("Note: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    ticket["notes"].append(f"[{timestamp}] {note}")
    save_tickets(tickets)
    print("✔ Note added.")

def delete_ticket(tickets):
    ticket_id = get_ticket_id_input("Delete ticket #: ")
    ticket = find_ticket(tickets, ticket_id)
    if not ticket:
        return
    confirm = input(f"Are you sure you want to delete Ticket #{ticket_id}? (yes/no): ").strip().lower()
    if confirm == "yes":
        tickets.remove(ticket)
        save_tickets(tickets)
        print(f"✔ Ticket #{ticket_id} deleted.")
    else:
        print("Cancelled.")

def show_summary(tickets):
    total    = len(tickets)
    open_t   = sum(1 for t in tickets if t["status"] == "Open")
    in_prog  = sum(1 for t in tickets if t["status"] == "In Progress")
    resolved = sum(1 for t in tickets if t["status"] in ("Resolved", "Closed"))
    critical = sum(1 for t in tickets if t["priority"] == "Critical" and t["status"] == "Open")
    print(f"""
── Ticket Summary ─────────────────────────────
  Total Tickets   : {total}
  Open            : {open_t}
  In Progress     : {in_prog}
  Resolved/Closed : {resolved}
  ⚠  Critical Open : {critical}
""")

# ── Helpers ────────────────────────────────────────────────────────────────────

def choose_option(label, options):
    print(f"\n  {label}:")
    for i, opt in enumerate(options, 1):
        print(f"    {i}. {opt}")
    while True:
        choice = input(f"  Select (1-{len(options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("  Invalid choice, try again.")

def get_ticket_id_input(prompt):
    raw = input(prompt).strip()
    if raw.isdigit():
        return int(raw)
    print("  Invalid ID.")
    return None

def find_ticket(tickets, ticket_id):
    if ticket_id is None:
        return None
    match = next((t for t in tickets if t["id"] == ticket_id), None)
    if not match:
        print(f"  Ticket #{ticket_id} not found.")
    return match

# ── Main Menu ──────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════╗")
    print("║      Help Desk Ticket Tracker v1.0       ║")
    print("║           Andy Hernandez, 2025           ║")
    print("╚══════════════════════════════════════════╝")

    tickets = load_tickets()

    menu = {
        "1": ("Create new ticket",        lambda: create_ticket(tickets)),
        "2": ("View all tickets",          lambda: view_tickets(tickets)),
        "3": ("View open tickets",         lambda: view_tickets(tickets, "Open")),
        "4": ("View ticket detail",        lambda: view_ticket_detail(tickets)),
        "5": ("Update ticket status",      lambda: update_ticket_status(tickets)),
        "6": ("Add note to ticket",        lambda: add_note(tickets)),
        "7": ("Delete ticket",             lambda: delete_ticket(tickets)),
        "8": ("Summary / dashboard",       lambda: show_summary(tickets)),
        "9": ("Exit",                      None),
    }

    while True:
        print("\n── Menu ───────────────────────────────────")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\nSelect an option: ").strip()

        if choice == "9":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  Invalid option, try again.")

if __name__ == "__main__":
    main()
