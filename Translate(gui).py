import tkinter as tk
import textblob
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

def translate_it():
    translated_text.delete(1.0, tk.END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, tk.END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.insert(1.0, words)
    except Exception as e:
        messagebox.showerror("Translator", e)

root = tk.Tk()
root.geometry("1030x300")
root.title("Translator")
root.resizable(width=True, height=True) # should be resizeable +
root['bg'] = 'black'
translator = Translator()


languages = googletrans.LANGUAGES
language_list = list(languages.values())



label = tk.Label(root, fg='white', bg='black', font='Arial 15 bold', text='Enter the text you want to translate!') # user should be able to select language(you have to have the settings menu)
# according to python3the things mentioned above you have to move this code into a class
label.grid(row=0, column=0)
original_text = tk.Text(root, width=35, height=5, font='Arial 12 bold')
original_text.grid(padx=1, pady=0) #grid is better anyway(use grid)+

translate_button = tk.Button(root, width=45, text='Translate!', command=translate_it)
translate_button.grid(row=1, column=1)

label = tk.Label(root, fg='white', bg='black', font='Arial 15 bold', text='Your translation:')
label.grid(row=0, column=3)

translated_text = tk.Text(root, width=35, height=5, font='Arial 12 bold')
translated_text.grid(row=1, column=3, padx=15)

original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=2, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(21)
translated_combo.grid(row=2, column=3)


#I need not only one translation i need synonyms also
#Try to work with some api directly, not using the googletrans library
root.mainloop()