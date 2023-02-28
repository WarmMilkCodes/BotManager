import config
import subprocess
import tkinter as tk

class BotManager:
    def __init__(self, bot_id, script_path):
        self.bot_id = bot_id
        self.script_path = script_path
        self.is_running = False

        self.root = tk.Tk()
        self.root.geometry('370x200')
        self.root.title('Bot Manager')

        self.status_label = tk.Label(self.root, text='Bot Status: Stopped', fg="red")
        self.status_label.pack(pady=20)

        start_button = tk.Button(self.root, text='Start Bot', command=self.start_bot)
        start_button.pack(side=tk.LEFT, padx=10)

        stop_button = tk.Button(self.root, text='Stop Bot', command=self.stop_bot)
        stop_button.pack(side=tk.RIGHT, padx=10)

        edit_button = tk.Button(self.root, text="Edit Script", command=self.edit_script)
        edit_button.pack(side=tk.LEFT, padx=10)

        self.root.mainloop()

    def start_bot(self):
        if not self.is_running:
            subprocess.Popen(['/usr/bin/python3', self.script_path])
            self.is_running = True
            self.update_status_label()

    def stop_bot(self):
        if self.is_running:
            subprocess.Popen(['pkill', '-f', self.script_path])
            self.is_running = False
            self.update_status_label()

    def edit_script(self):
        subprocess.Popen(['code', self.script_path])

    def update_status_label(self):
        status_text = f'Bot Status: {"Running" if self.is_running else "Stopped"}'
        self.status_label.config(text=status_text)
        if self.is_running:
            self.status_label.config(fg="green")
        else:
            self.status_label.config(fg="red")

if __name__ == '__main__':
    bot_id = config.FL_BOT_ID
    script_path = '/home/dylan/FLBOT/main.py'

    bot_manager = BotManager(bot_id, script_path)
