from tkinter import *

root = Tk()
root.title('Enigma-Secret Messenger')
root.iconbitmap('D:\Edrive files\Python Programming\Python_Projects\Project Enigma/Enigma_icon.ico')
enigma = PhotoImage(file = 'D:\Edrive files\Python Programming\Python_Projects\Project Enigma\Enigma_icon.png')
image_label = Label(root,image =enigma ,bd =0)
image_label.pack()

myLabel1 = Label(root, text = "Enigma",font=("Helvetica",25),fg = "#4B0082",bg="#B8A0F0")
myLabel1.pack(pady = 30)

root.geometry("500x700")
root.config(bg="#B8A0F0")#hex color code is used
#BDA6F1


e = Entry(root,width = 50,font=("Times",12),borderwidth = 2)
e.insert(0,"Enter your secret message here:- ")
e.pack(pady = 10)




keys = 'abcdefghijklmnopqrstuvwxyz0123456789 ,.!?:;ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#value = keys[::-1]#string reverse by slicing
value = keys[-1] + keys[0:-1]

encryptDict = dict(zip(keys,value))
decryptDict = dict(zip(value,keys))


myLabel2 = Label(root, text = "Choose the mode : Encode or Decode: ",font=("Helvetica",14),bg="#B8A0F0")
myLabel2.pack(pady = 10)


def Encode():
	new_msg = ''.join([encryptDict[letter] for letter in e.get()])
	myLabel3 = Label(root, text = "Cypher text: ",font=("Helvetica",14),bg="#B8A0F0")
	myLabel3.pack(pady = 10)
	my_entry = Entry(root,
			font=("Helvetica",14),
			bd =0,
			
			)
	my_entry.insert(0,new_msg)
	my_entry.config(state = "readonly")
	my_entry.pack(pady = 15)





encode_button = Button(root,text="Encode",fg = "red",command = Encode)
encode_button.pack(pady = 10)

def Decode():
	new_msg = ''.join([decryptDict[letter] for letter in e.get()])
	myLabel4 = Label(root, text = "Real message: ",font=("Helvetica",14),bg="#B8A0F0")
	myLabel4.pack(pady = 10)

	my_entry = Entry(root,
			font=("Helvetica",14),
			bd =0,
			
			)
	my_entry.insert(0,new_msg)
	my_entry.config(state = "readonly")
	my_entry.pack(pady = 15)





decode_button = Button(root,text="Decode",fg = "green",command = Decode)
decode_button.pack(pady=10)

'''my_entry = Entry(root,
			font=("Helvetica",20),
			bd =0,
			state = "readonly",
			textvariable = new_msg)'''





root.mainloop()
