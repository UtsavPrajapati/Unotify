from Windows import *


class SwitchWindow:
    def __init__(self):
        self.address = read_from_database()[0]
        self.tk = tk
        self.stat = True
        window = tk.Tk()
        window.protocol("WM_DELETE_WINDOW", self.do_nothing)
        self.window = window
        window.title("Unotify")
        tk.Label(window, text="      The app is currently:     ").pack()
        self.text = tk.Label(window, text="ON", fg="green")
        self.text.pack()
        tk.Button(window, text="SWITCH", command=self.switch).pack()
        tk.Label(window, text="Logged as " + self.address).pack()
        tk.Label(window, text=self.address, fg="green").pack()
        tk.Button(window, text="Change account").pack()
        tk.mainloop()

    def switch(self):
        if self.stat:
            self.stat = False
            self.text["text"] = "OFF"
            self.text["fg"] = "red"
        else:
            self.stat = True
            self.text["text"] = "ON"
            self.text["fg"] = "green"
        self.write_to_file(str(self.stat))

    def change_account(self):
        if "INFO.db" in os.listdir(os.getcwd()):
            os.unlink("INFO.db")
        a = SetAccount()

    def do_nothing(self):
        pass

    def write_to_file(self, text):
        f = open("switch", "w")
        f.write(text)
        f.close()

if "downloads" in os.listdir(os.getcwd()):
    SwitchWindow()
