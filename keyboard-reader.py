import tkinter as tk
from pynput import keyboard

# Define maximum length for displayed text
MAX_LENGTH = 30

# Create the main window
root = tk.Tk()
root.title("Keyboard Monitor")
root.geometry("500x150")
root.config(bg="black")

# Create a label to display the text
key_label = tk.Label(root, text="", font=("Helvetica", 32))
key_label.pack(expand=True)
key_label.config(bg="black", fg="red")

# Variable to hold the current word being typed
current_word = []

# Function to update the label when a key is pressed
def on_press(key):
    global current_word

    try:
        if hasattr(key, 'char') and key.char:  # Check if the key has a printable character
            current_word.append(key.char)
        else:
            # Handle non-character keys like function keys, arrows, etc.
            if key == keyboard.Key.space:
                current_word.append(' ')
            elif key == keyboard.Key.enter:
                current_word.append('[Enter]')
            elif key == keyboard.Key.backspace:
                if current_word:
                    current_word.pop()
            elif key == keyboard.Key.shift:
                current_word.append('[Shift]')
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                current_word.append('[Ctrl]')
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                current_word.append('[Alt]')
            elif key == keyboard.Key.cmd_l or key == keyboard.Key.cmd_r:
                current_word.append('[Cmd]')
            elif key == keyboard.Key.f9:
                current_word.clear()
            elif key == keyboard.Key.tab:
                current_word.append('[Tab]')
            elif key == keyboard.Key.esc:
                current_word.append('[Esc]')
            elif key == keyboard.Key.caps_lock:
                current_word.append('[CapsLock]')
    except AttributeError:
        pass

    # Truncate text if it exceeds the maximum length
    text = ''.join(current_word)
    if len(text) > MAX_LENGTH:
        text = text[-MAX_LENGTH:]  # Keep only the last MAX_LENGTH characters

    # Update the label with the current word
    key_label.config(text=text)

# Start listening for key events
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Start the Tkinter event loop
root.mainloop()
