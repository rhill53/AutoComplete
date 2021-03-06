# Some code below from:
# http://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/

from tkinter import *
import re
import binTreeWordSearch as bin_tree

tree = bin_tree.Tree()


class AutocompleteEntry(Entry):

    def __init__(self, lista, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

        self.lb_up = False

    def changed(self, name, index, mode):

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.lb_up = True

                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END, w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)

    def comparison(self):
        tree.auto_suggestions(self.var.get())
        pattern = re.compile(self.var.get() + '.*') # This line is prefix only search
        # pattern = re.compile('.*' + self.var.get() + '.*') # This line instead is FUZZY SEARCH
        returns = [w for w in tree.word_list if re.match(pattern, w)]
        returns = list(dict.fromkeys(returns))
        return [r for r in returns[:10]]
    

if __name__ == '__main__':
    lista = []
    f = open("words.txt", "r")
    for line in f:
        lista.append(line)
    f.close()

    tree.form_tree(lista)

    root = Tk()
    root.geometry("100x185")

    entry = AutocompleteEntry(lista, root)
    entry.grid(row=0, column=0)

    root.mainloop()
