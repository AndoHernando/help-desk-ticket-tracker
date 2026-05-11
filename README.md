# Help Desk Ticket Tracker

A Python command-line application that simulates a real-world IT help desk ticketing system. Built to demonstrate practical software development skills including data persistence, modular design, and CLI-based user interaction.

---

## Features

- **Create tickets** — log new issues with a title, category, priority, and description
- **View tickets** — list all tickets or filter by status (Open, In Progress, Resolved)
- **Ticket detail** — view full information for any individual ticket
- **Update status** — move tickets through the support lifecycle
- **Add notes** — append timestamped notes to any ticket for documentation
- **Delete tickets** — remove resolved or duplicate entries
- **Dashboard summary** — get a live count of open, in-progress, resolved, and critical tickets
- **Persistent storage** — all ticket data is saved locally to a `tickets.json` file and reloaded on startup

---

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON (file-based persistence)
- **IDE:** VS Code
- **Version Control:** Git / GitHub

---

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Run the app

```bash
git clone https://github.com/AndoHernando/help-desk-ticket-tracker.git
cd help-desk-ticket-tracker
python ticket_tracker.py
```

No external libraries required — runs entirely on Python's standard library.

---

## Usage

On launch you'll see the main menu:

```
╔══════════════════════════════════════════╗
║      Help Desk Ticket Tracker v1.0       ║
║           Andy Hernandez, 2025           ║
╚══════════════════════════════════════════╝

── Menu ───────────────────────────────────
  1. Create new ticket
  2. View all tickets
  3. View open tickets
  4. View ticket detail
  5. Update ticket status
  6. Add note to ticket
  7. Delete ticket
  8. Summary / dashboard
  9. Exit
```

Select an option by entering its number. Tickets are automatically saved after every action.

---

## Project Structure

```
help-desk-ticket-tracker/
├── ticket_tracker.py   # Main application
├── tickets.json        # Auto-generated data file (created on first run)
└── README.md
```

---

## Background

This project was built to reinforce my understanding of IT support workflows — including ticket lifecycle management, issue categorization, and escalation procedures — while practicing core Python development skills. It complements hands-on IT simulation work I do using IT Specialist Simulator and my studies toward CompTIA A+.

---

## Author

**Andy Hernandez**  
Computer Information Systems, FGCU '24  
[LinkedIn](https://linkedin.com/in/andyhernandezceb) • [GitHub](https://github.com/AndoHernando)
