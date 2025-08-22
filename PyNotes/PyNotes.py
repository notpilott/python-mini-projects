import os
import time

# Folder to store notes: Downloads
NOTES_DIR = os.path.join(os.path.expanduser("~"), "Downloads")


def note_editor():
    """Simple note editor where you can type text until :save or :quit."""
    note_content = []
    print("Loading PyNotes...")
    time.sleep(3)
    print("\nWelcome to PyNotes! Type your text below.")
    print("Commands: :save to save, :quit to exit without saving.\n")
    while True:
        line = input()  # no prompt for clean note-taking feel

        if line.startswith(":"):  # handle commands
            if line == ":quit":
                print("Exiting without saving...")
                return None
            elif line == ":save":
                return note_content
            else:
                print(f"Unknown command: {line}")
        else:
            note_content.append(line)


def save_note(content):
    """Save the collected note content to a text file."""
    filename = input("Enter a filename for your PyNote: ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    filepath = os.path.join(NOTES_DIR, filename)

    with open(filepath, "w") as f:
        f.write("\n".join(content))

    print(f"Note saved as {filepath}\n")


def view_notes():
    """List existing notes in Downloads and optionally display one."""
    notes = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    if not notes:
        print("No notes found in Downloads.")
        return

    print("\nExisting notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")

    choice = input(
        "\nEnter the number of a note to view (or press Enter to go back): "
    ).strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(notes):
            with open(os.path.join(NOTES_DIR, notes[idx]), "r") as f:
                print("\n" + f.read())
        else:
            print("Invalid selection.")
    else:
        print("Returning to menu.")


def main():
    while True:
        print("\n--- PyNotes by pilott  ---")
        print("1. New PyNote")
        print("2. View notes")
        print("3. Quit")

        choice = input("Choose an option >> ").strip()

        if choice == "1":
            content = note_editor()
            if content:
                save_note(content)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
