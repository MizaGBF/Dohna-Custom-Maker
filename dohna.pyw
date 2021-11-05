import time
import tkinter as Tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import pathlib

class Dohna(Tk.Tk):
    def __init__(self, ver):
        Tk.Tk.__init__(self,None)
        self.ranks = ["S+", "S", "A+", "A", "B+", "B", "C", "D+", "D"]
        self.stats = ["LKS", "TEC", "MEN"]
        self.traits = ["Boobs", "Flat", "Hips", "Legs", "Glowing", "Muscly", "Plump", "Good V", "Tomgirl", "Futa", "Crutches", "Handicap", "Anemic", "Sickly", "Blind", "Tattoo", "Piercings", "Sensitive", "Smelly", "Rich", "Celeb", "Strict", "Clever", "Sporty", "Truant", "Poor", "Has BF", "Has GF", "Married", "Has Kids", "Princely", "Quirky", "Cool", "Quiet", "Stubborn", "Chipper", "Devoted", "Shy", "Fearful", "Obedient", "Serious", "Impish", "Haughty", "Tidy", "Pure", "Sexy", "Pervy", "Healing", "Casual", "Mystic", "Self-Hate", "Psycho", "Elegant", "Domestic", "Devious", "Wounded", "Popular", "Just", "Emo"]
        self.voices = ["Random", "4/Serious", "4/Bright", "4/Strong", "3/Serious", "3/Lively", "3/Bright", "3/Quiet", "3/Innocent", "2/Serious", "2/Lively", "2/Quiet", "1/Innocent", "1/Brash", "1/Quiet"]
        self.presents = self.traits.copy()
        for i in range(0, 3):
            for t in self.stats:
                self.presents.append(t +"+" + str(i+1))
                self.presents.append(t + "-" + str(i+1))
        self.traits = ["Random"] + sorted(self.traits)
        self.presents = ["Random"] + sorted(self.presents)
        self.parent = None
        self.apprunning = True
        self.title("Dohna Custom Girl v{}".format(ver))
        self.resizable(width=False, height=False) # not resizable
        self.protocol("WM_DELETE_WINDOW", self.close) # call close() if we close the window
        
        Tk.Button(self, text="New", command=self.new).grid(row=0, column=0, sticky="we")
        Tk.Button(self, text="Open", command=self.open).grid(row=0, column=1, sticky="we")
        Tk.Button(self, text="Save", command=self.save).grid(row=0, column=2, sticky="we")
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0, columnspan=4, sticky="we")
        
        # talent
        self.talentframe = ttk.Frame(self)
        self.notebook.add(self.talentframe, text="Talent")
        Tk.Label(self.talentframe, text="Image").grid(row=0, column=0)
        self.t_image = Tk.Text(self.talentframe, height = 1, width = 20)
        self.t_image.grid(row=0, column=1, columnspan=2, sticky="we")
        Tk.Button(self.talentframe, text="Select", command=self.i_open).grid(row=0, column=3, sticky="we")
        Tk.Label(self.talentframe, text="First Name").grid(row=1, column=0)
        self.t_fn = Tk.Text(self.talentframe, height = 1, width = 11)
        self.t_fn.grid(row=1, column=1, sticky="we")
        Tk.Label(self.talentframe, text="Last Name").grid(row=1, column=2)
        self.t_ln = Tk.Text(self.talentframe, height = 1, width = 11)
        self.t_ln.grid(row=1, column=3, sticky="we")
        Tk.Label(self.talentframe, text="Last Name").grid(row=1, column=2)
        Tk.Label(self.talentframe, text="Stats").grid(row=2, column=0)
        self.tv_s = []
        self.t_s = []
        for s in self.stats:
            self.tv_s.append(Tk.StringVar(value=s))
            self.t_s.append(Tk.OptionMenu(self.talentframe, self.tv_s[-1], *([s]+self.ranks)))
            self.t_s[-1].grid(row=2, column=len(self.t_s))
        Tk.Label(self.talentframe, text="Traits").grid(row=3, column=0)
        self.tv_t = []
        self.t_t = []
        for i in range(3):
            self.tv_t.append(Tk.StringVar(value=self.traits[0]))
            self.t_t.append(Tk.OptionMenu(self.talentframe, self.tv_t[-1], *self.traits))
            self.t_t[-1].grid(row=3, column=i+1)
        Tk.Label(self.talentframe, text="Virgin").grid(row=4, column=0)
        self.tv_virgin = Tk.StringVar(value="Random")
        self.t_virgin = Tk.OptionMenu(self.talentframe, self.tv_virgin, *["Random", "Yes", "No"])
        self.t_virgin.grid(row=4, column=1)
        Tk.Label(self.talentframe, text="Voice").grid(row=4, column=2)
        self.tv_v = Tk.StringVar(value=self.voices[0])
        self.t_v = Tk.OptionMenu(self.talentframe, self.tv_v, *self.voices)
        self.t_v.grid(row=4, column=3)
        Tk.Label(self.talentframe, text="Bio").grid(row=5, column=0)
        self.t_bio = []
        for i in range(3):
            self.t_bio.append(Tk.Text(self.talentframe, height = 1, width = 40))
            self.t_bio[-1].grid(row=5+i, column=1, columnspan=3)
        
        # client
        self.clientframe = ttk.Frame(self)
        self.notebook.add(self.clientframe, text="Client")
        Tk.Label(self.clientframe, text="Image").grid(row=0, column=0)
        self.c_image = Tk.Text(self.clientframe, height = 1, width = 20)
        self.c_image.grid(row=0, column=1, columnspan=2, sticky="we")
        Tk.Button(self.clientframe, text="Select", command=self.i_open).grid(row=0, column=3, sticky="we")
        Tk.Label(self.clientframe, text="First Name").grid(row=1, column=0)
        self.c_fn = Tk.Text(self.clientframe, height = 1, width = 11)
        self.c_fn.grid(row=1, column=1, sticky="we")
        Tk.Label(self.clientframe, text="Last Name").grid(row=1, column=2)
        self.c_ln = Tk.Text(self.clientframe, height = 1, width = 11)
        self.c_ln.grid(row=1, column=3, sticky="we")
        Tk.Label(self.clientframe, text="Last Name").grid(row=1, column=2)
        Tk.Label(self.clientframe, text="Income").grid(row=2, column=0)
        self.cv_i = Tk.StringVar(value="Random")
        self.c_i = Tk.OptionMenu(self.clientframe, self.cv_i, *(["Random"]+self.ranks))
        self.c_i.grid(row=2, column=1)
        Tk.Label(self.clientframe, text="Presents").grid(row=3, column=0)
        self.cv_p = []
        self.c_p = []
        for i in range(3):
            self.cv_p.append(Tk.StringVar(value=self.presents[0]))
            self.c_p.append(Tk.OptionMenu(self.clientframe, self.cv_p[-1], *self.presents))
            self.c_p[-1].grid(row=3, column=i+1)
        Tk.Label(self.clientframe, text="Targets").grid(row=4, column=0)
        self.cv_t = []
        self.c_t = []
        for i in range(3):
            self.cv_t.append(Tk.StringVar(value=self.traits[0]))
            self.c_t.append(Tk.OptionMenu(self.clientframe, self.cv_t[-1], *self.traits))
            self.c_t[-1].grid(row=4, column=i+1)
        Tk.Label(self.clientframe, text="Bio").grid(row=5, column=0)
        self.c_bio = []
        for i in range(2):
            self.c_bio.append(Tk.Text(self.clientframe, height = 1, width = 24))
            self.c_bio[-1].grid(row=5+i, column=1, columnspan=3, sticky="w")

        self.setChildrenState(self.talentframe.winfo_children(), "disabled")
        self.setChildrenState(self.clientframe.winfo_children(), "disabled")
        self.dtype = None

    def run(self):
        # main loop
        while self.apprunning:
            self.update()
            time.sleep(0.02)

    def close(self): # called by the app when closed
        self.apprunning = False
        self.destroy() # destroy the window

    def new(self):
        if not messagebox.askokcancel(title="Warning", message="Unsaved changes will be lost, continue?" ):
            return
        v = messagebox.askyesnocancel(title="Selection", message="Do you want to make a Talent?")
        if v is None: return
        self.reset()
        if v:
            self.dtype = 'TALENT'
            self.selectTab(0)
        else:
            self.dtype = 'CLIENT'
            self.selectTab(1)

    def setChildrenState(self, children, state):
        for child in children:
            child.configure(state=state)

    def selectTab(self, n):
        if n == 0:
            self.setChildrenState(self.talentframe.winfo_children(), "normal")
            self.setChildrenState(self.clientframe.winfo_children(), "disabled")
            self.notebook.select(0)
        elif n == 1:
            self.setChildrenState(self.talentframe.winfo_children(), "disabled")
            self.setChildrenState(self.clientframe.winfo_children(), "normal")
            self.notebook.select(1)
        elif n == -1:
            self.setChildrenState(self.talentframe.winfo_children(), "disabled")
            self.setChildrenState(self.clientframe.winfo_children(), "disabled")

    def reset(self):
        # enable to delete
        self.setChildrenState(self.talentframe.winfo_children(), "normal")
        self.setChildrenState(self.clientframe.winfo_children(), "normal")
        # talent
        self.t_image.delete(1.0, Tk.END)
        self.t_fn.delete(1.0, Tk.END)
        self.t_ln.delete(1.0, Tk.END)
        for i in range(0, 3):
            self.tv_s[i].set(self.stats[i])
        Tk.Label(self.talentframe, text="Traits").grid(row=3, column=0)
        for v in self.tv_t:
            v.set(self.traits[0])
        self.tv_virgin.set("Random")
        self.tv_v.set(self.voices[0])
        self.t_v.grid(row=4, column=3)
        Tk.Label(self.talentframe, text="Bio").grid(row=5, column=0)
        for v in self.t_bio:
            v.delete(1.0, Tk.END)
        # client
        self.c_image.delete(1.0, Tk.END)
        self.c_fn.delete(1.0, Tk.END)
        self.c_ln.delete(1.0, Tk.END)
        self.cv_i.set("Random")
        for v in self.cv_p:
            v.set(self.presents[0])
        for v in self.cv_t:
            v.set(self.traits[0])
        Tk.Label(self.clientframe, text="Bio").grid(row=5, column=0)
        for v in self.c_bio:
            v.delete(1.0, Tk.END)

    def open(self):
        filename = fd.askopenfilename(title='Open a file', initialdir=pathlib.Path().resolve(), filetypes=(('text files', '*.txt'),('text files', '*.txt')))
        if len(filename) == 0: return
        try:
            chara = {}
            with open(filename, "rb") as f:
                while True:
                    line = f.readline().decode("ascii")
                    if not line: break
                    line = line.replace('\r', '').replace('\n', '')
                    if line != '':
                        elements = line.split('=')
                        if len(elements) < 2:
                            messagebox.showerror(title="Error loading file", message='Line "{}" isn\'t valid'.format(line))
                            return
                        elif len(elements) > 2:
                            elements[1] = '='.join(elements[1:])
                        if elements[0] in chara:
                            if not isinstance(chara[elements[0]], list):
                                chara[elements[0]] = [chara[elements[0]]]
                            chara[elements[0]].append(elements[1])
                        else:
                            chara[elements[0]] = elements[1]
            if 'TYPE' not in chara:
                messagebox.showerror(title="Error reading file", message="Can't find data TYPE")
                return
            if not self.set('\\'.join(filename.replace('/', '\\').split('\\')[:-1]) + '\\', chara):
                self.reset()
                self.selectTab(-1)
        except Exception as e:
            messagebox.showerror(title="Error opening/parsing file", message=str(e))
            self.reset()
            self.selectTab(-1)

    def set(self, path, chara):
        t = chara.get('TYPE', '')
        if t == 'TALENT':
            self.reset()
            if 'IMAGE' in chara: self.t_image.insert(Tk.END, path + chara['IMAGE'])
            if 'NAME' in chara:
                n = chara['NAME'].split('\\n')
                if len(n) != 2:
                    messagebox.showerror(title="Error parsing file", message='Invalid NAME "{}"'.format(chara['NAME']))
                    return False
                self.t_fn.insert(Tk.END, n[0])
                self.t_ln.insert(Tk.END, n[1])
            for s in self.stats:
                if s in chara:
                    if chara[s] not in self.ranks:
                        messagebox.showerror(title="Error parsing file", message='Invalid {} "{}"'.format(s, chara[s]))
                        return False
                    self.tv_s[self.stats.index(s)].set(chara[s])
            if 'TRAIT' in chara:
                if isinstance(chara['TRAIT'], list): v = chara['TRAIT']
                else: v = [chara['TRAIT']]
                for i in range(len(v)):
                    if v[i] not in self.traits:
                        messagebox.showerror(title="Error parsing file", message='Invalid TRAIT "{}"'.format(v[i]))
                        return False
                    self.tv_t[i].set(v[i])
            if 'VIRGIN' in chara:
                self.tv_virgin.set("YES" if chara['VIRGIN'] == '1' else "NO")
            if 'VOICES' in chara:
                if chara['VOICES'] not in self.voices:
                    messagebox.showerror(title="Error parsing file", message='Invalid VOICE "{}"'.format(chara['VOICE']))
                    return False
                self.tv_v.set(chara['VOICE'])
            if 'BIO' in chara:
                if isinstance(chara['BIO'], list): v = chara['BIO']
                else: v = [chara['BIO']]
                for i in range(min(len(v), 3)):
                    self.t_bio[i].insert(Tk.END, v[i])
            self.dtype = t
            self.selectTab(0)
            return True
        elif t == 'CLIENT':
            self.reset()
            if 'IMAGE' in chara: self.c_image.insert(Tk.END, path + chara['IMAGE'])
            if 'NAME' in chara:
                n = chara['NAME'].split('\\n')
                if len(n) != 2:
                    messagebox.showerror(title="Error parsing file", message='Invalid NAME "{}"'.format(chara['NAME']))
                    return False
                self.c_fn.insert(Tk.END, n[0])
                self.c_ln.insert(Tk.END, n[1])
            if 'INCOME' in chara:
                if chara['INCOME'] not in self.ranks:
                    messagebox.showerror(title="Error parsing file", message='Invalid {} "{}"'.format(s, chara[s]))
                    return False
                self.cv_i.set(chara['INCOME'])
            if 'PRESENT' in chara:
                if isinstance(chara['PRESENT'], list): v = chara['PRESENT']
                else: v = [chara['PRESENT']]
                for i in range(len(v)):
                    if v[i] not in self.presents:
                        messagebox.showerror(title="Error parsing file", message='Invalid PRESENT "{}"'.format(v[i]))
                        return False
                    self.cv_p[i].set(v[i])
            if 'TARGET' in chara:
                if isinstance(chara['TARGET'], list): v = chara['TARGET']
                else: v = [chara['TARGET']]
                for i in range(len(v)):
                    if v[i] not in self.traits:
                        messagebox.showerror(title="Error parsing file", message='Invalid TARGET "{}"'.format(v[i]))
                        return False
                    self.cv_t[i].set(v[i])
            if 'BIO' in chara:
                if isinstance(chara['BIO'], list): v = chara['BIO']
                else: v = [chara['BIO']]
                for i in range(min(len(v), 2)):
                    self.c_bio[i].insert(Tk.END, v[i])
            self.dtype = t
            self.selectTab(1)
            return True
        else:
            messagebox.showerror(title="Error parsing file", message='Invalid TYPE "{}"'.format(t))
            return False

    def save(self):
        buffer = "TYPE=" + self.dtype + "\r\n"
        tmp = None
        if self.dtype == 'TALENT':
            filename = self.t_image.get(1.0, Tk.END).replace('\n', '')
            if filename == "" or not filename.endswith('.png'):
                messagebox.showerror(title="Error saving file", message='Invalid IMAGE path "{}"'.format(filename))
                return False
            tmp = filename.replace('/', '\\').split('\\')[-1]
            if tmp == "":
                messagebox.showerror(title="Error saving file", message='Invalid IMAGE name "{}"'.format(tmp))
                return False
            buffer += "IMAGE=" + tmp + "\r\n"
            fn = self.t_fn.get(1.0, Tk.END).replace('\n', '')
            ln = self.t_ln.get(1.0, Tk.END).replace('\n', '')
            if fn != '' or ln != '':
                if len(fn) > 10:
                    messagebox.showwarning(title="Warning", message='First name is over 10 characters, it might cause issues')
                if len(ln) > 10:
                    messagebox.showwarning(title="Warning", message='last name is over 10 characters, it might cause issues')
                buffer += "NAME={}\\n{}\r\n".format(fn, ln)
            for i in range(3):
                tmp = self.tv_s[i].get()
                if tmp not in self.stats:
                    buffer += "{}={}\r\n".format(self.stats[i], tmp)
            for t in self.tv_t:
                tmp = t.get()
                if tmp != 'Random':
                    buffer += "TRAIT={}\r\n".format(tmp)
            tmp = self.tv_virgin.get()
            if tmp == 'Yes': buffer += "VIRGIN=1\r\n"
            elif tmp == 'No': buffer += "VIRGIN=0\r\n"
            tmp = self.tv_v.get()
            if tmp != 'Random': buffer += "VOICE={}\r\n".format(tmp)
            for i in range(3):
                tmp = self.t_bio[i].get(1.0, Tk.END).replace('\n', '')
                if tmp != '': buffer += "BIO={}\r\n".format(tmp)
            try:
                with open(filename.replace('.png', '.txt'), 'wb') as f:
                    f.write(buffer.encode("ascii"))
                messagebox.showinfo(title="File saved", message='File saved with success to "{}"'.format(filename.replace('.png', '.txt')))
            except Exception as e:
                messagebox.showerror(title="Error writing file", message='Can\'t save file "{}"\nException: {}'.format(filename.replace('.png', '.txt'), e))
        elif self.dtype == 'CLIENT':
            filename = self.c_image.get(1.0, Tk.END).replace('\n', '')
            if filename == "" or not filename.endswith('.png'):
                messagebox.showerror(title="Error saving file", message='Invalid IMAGE path "{}"'.format(filename))
                return False
            tmp = filename.replace('/', '\\').split('\\')[-1]
            if tmp == "":
                messagebox.showerror(title="Error saving file", message='Invalid IMAGE name "{}"'.format(tmp))
                return False
            buffer += "IMAGE=" + tmp + "\r\n"
            fn = self.c_fn.get(1.0, Tk.END).replace('\n', '')
            ln = self.c_ln.get(1.0, Tk.END).replace('\n', '')
            if fn != '' or ln != '':
                if len(fn) > 10:
                    messagebox.showwarning(title="Warning", message='First name is over 10 characters, it might cause issues')
                if len(ln) > 10:
                    messagebox.showwarning(title="Warning", message='last name is over 10 characters, it might cause issues')
                buffer += "NAME={}\\n{}\r\n".format(fn, ln)
            tmp = self.cv_i.get()
            if tmp != 'Random':
                buffer += "INCOME={}\r\n".format(tmp)
            for t in self.cv_p:
                tmp = t.get()
                if tmp != 'Random':
                    buffer += "PRESENT={}\r\n".format(tmp)
            for t in self.cv_t:
                tmp = t.get()
                if tmp != 'Random':
                    buffer += "TARGET={}\r\n".format(tmp)
            for i in range(2):
                tmp = self.c_bio[i].get(1.0, Tk.END).replace('\n', '')
                if len(tmp) > 11:
                    messagebox.showwarning(title="Warning", message='This BIO lin is over 11 characters, it might not display properly\n"{}"'.format(tmp))
                if tmp != '': buffer += "BIO={}\r\n".format(tmp)
            try:
                with open(filename.replace('.png', '.txt'), 'wb') as f:
                    f.write(buffer.encode("ascii"))
                messagebox.showinfo(title="File saved", message='File saved with success to "{}"'.format(filename.replace('.png', '.txt')))
            except Exception as e:
                messagebox.showerror(title="Error writing file", message='Can\'t save file "{}"\nException: {}'.format(filename.replace('.png', '.txt'), e))

    def i_open(self):
        filename = fd.askopenfilename(title='Open an Image', initialdir=pathlib.Path().resolve(), filetypes=(('image files', '*.png'),('image files', '*.png')))
        if self.dtype == 'TALENT':
            self.t_image.delete(1.0, Tk.END)
            self.t_image.insert(Tk.END, filename)
        elif self.dtype == 'CLIENT':
            self.c_image.delete(1.0, Tk.END)
            self.c_image.insert(Tk.END, filename)

if __name__ == "__main__":
    Dohna("1.0").run()