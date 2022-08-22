#https://api.kanye.rest

#AngelaYu Day33 KanyeQuotesApp

# using a roblox girl's own creation:)

import tkinter as tk
import requests

def get_quote():

    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = tk()

window.title("RobloxGirl Says...")

window.config(padx=50, pady=50)


canvas = Canvas(width=286, height=400)

background_img = PhotoImage(file="background.png")

canvas.create_image(140, 197, image=background_img)

quote_text = canvas.create_text(140, 197, text="Roblox Girl Goes HERE", width=200, font=("Arial", 30, "bold"), fill="white")

canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file="robloxgirl.jpg")

kanye_button = Button(image=robloxgirl_img, highlightthickness=0, command=get_quote)

kanye_button.grid(row=1, column=0)

window.mainloop()