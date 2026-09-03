# Help Desk Ticket Tracker

A command-line ticket tracking tool built in Python, using SQLite for storage.

## Why I built this

I wanted a real, working coding project for my resume and portfolio as I work toward an entry-level IT Help Desk / Desktop Support role. Rather than relying on AI-generated code, I built this from scratch to understand exactly how a basic ticketing system works under the hood — the same kind of ticket lifecycle (create, update, resolve, close) that a real help desk runs on every day.

## Features

- **Add** a new ticket with a status, title, description, operating system, and optional resolution notes
- **List** all tickets, or filter to just one status (e.g. only "Open" tickets)
- **Update** an existing ticket's status and/or add resolution notes once it's been fixed
- **Delete** a ticket
- Dates default to today automatically if not specified

## How to use it

```bash
# Add a ticket
python tracker.py add --status Open --title "Printer not printing" --description "User reports printer offline" --os "Windows 11"

# List all tickets
python tracker.py list

# List only open tickets
python tracker.py list --status Open

# Update a ticket's status and log how it was resolved
python tracker.py update --id 1 --status Closed --resolution "Reinstalled printer driver"

# Delete a ticket
python tracker.py delete --id 1
```

## Built with

- Python 3
- SQLite3 (built into Python's standard library)
- argparse (built into Python's standard library)

## What I learned

Building this taught me how ticket data actually gets stored and queried (SQL basics — `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`), how to protect against SQL injection using parameterized queries, and how to build a real command-line interface with subcommands using `argparse`.
