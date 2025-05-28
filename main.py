from tkinter import *
from data import result_string


def start_timer():
    text2.config(state=NORMAL)
    count_down(60)


def count_down(seconds):
    """Count down the timer and update the label."""
    minutes, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
    timer_text = f"{minutes}:{secs:02d}"  # Format the timer as MM:SS
    timer.config(text=timer_text)  # Update the timer label

    if seconds > 0:
        # Call count_down again after 1000ms (1 second)
        window.after(1000, count_down, seconds - 1)
    else:
        # Once the countdown finishes, you can trigger another event or display a message
        timer.config(text="Time's up!")
        action()


def action():
    reference_text = text.get("1.0", END).strip().lower()
    user_text = text2.get("1.0", END).strip().lower() # Get all text from line 1, character 0 to the end and strip whitespace

    reference_words = reference_text.split()
    user_words = user_text.split()

    matching_words = [word for word in user_words if word in reference_words]
    matching_count = len(matching_words)
    total_user_words = len(user_words)

    pop_up_window = Toplevel(window)
    pop_up_window.title("Result")
    pop_up_window.geometry("400x300")
    pop_up_window.config(padx=20, pady=20)

    print(type(user_text))

    Label(pop_up_window, text=f"Correctly typed words: {matching_count}/{total_user_words}", font=20).pack(pady=5)
    Label(pop_up_window, text=f"You can type {matching_count} words per minute!", font=20).pack(pady=5)
    Label(pop_up_window, text="You wrote:", font=20).pack(pady=5)
    Label(pop_up_window, text=user_text, wraplength=350, justify="left").pack(pady=10)


window = Tk()
window.title("Typing Speed Test")
window.minsize(width=480, height=450)
window.config(padx=40, pady=20)


text = Text(height=10, width=50, wrap="word")
text.insert(END, f"{result_string}")
text.grid(column=0, row=0, pady=20)

timer = Label(text="1:00", fg="red", font=("Arial", 36, "bold"))
timer.grid(column=0, row=2, pady=10)


text2 = Text(height=10, width=50, wrap="word", state=DISABLED)
text2.insert(END, "")
text2.focus()
text2.grid(column=0, row=1, pady=20)

label = Label(text="Click on the button to start the timer and type as many words as you can:", font=12)
label.grid(column=0, row=3, pady=20)

button = Button(text="Start", width=12, command=start_timer)
button.grid(column=0, row=4)

window.mainloop()


