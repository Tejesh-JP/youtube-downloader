from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def down():
    quality = clicked.get()
    url = elink.get()
    try:
        yt = YouTube(url)
    except:
        messagebox.showinfo("Oops",f"Download failed due to: {e}")  
    video = yt.streams.filter(file_extension='mp4',resolution=f"{quality}")
    try:
        video.first().download()
        messagebox.showinfo("Success",f"Download complete for: {yt.title}")
    except Exception as e:
        messagebox.showinfo("Oops",f"Download failed due to: {e}")

window=Tk()
window.title('YouTube Downloader')
window.geometry("500x400")
window.iconbitmap(r"yticon.ico")
window.configure(background = "#B4161B")
lbl=Label(window, text="YouTube Downloader",anchor="center", fg='#CAD5E2',bg ="#B4161B", font=("Helvetica", 24))
lbl.pack(pady=20)
clicked = StringVar()
clicked.set("Set Quality")
elink = StringVar()
e1 = Entry(window , textvariable = elink ,width = 50 ,font = ('calibre',10,'normal'))
e1.pack(pady = 40)
drop = OptionMenu(window, clicked, "360p" ,"480p" , "720p" , "1080p")
drop.pack(pady = 20)
drop ["menu"] ["bg"] = "#19B5FE"
drop ["bg"] = "#19B5FE" 
drop ["activebackground"] = "#19B5FE"
b1 = Button(window , text = "Download Now" , bg = "#66AD47" , fg = "#F2F1EF", command = down )
b1.pack()
window.mainloop()
