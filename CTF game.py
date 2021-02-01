import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="green")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)


#black border right side
frame = tk.Frame(root, bg="black")
frame.place(relx=.97, rely=0, relwidth=0.05, relheight=1)

#black border left side
frame = tk.Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=0.03, relheight=1)

#black border top
frame = tk.Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=1, relheight=.03)

#black border bottom
frame = tk.Frame(root, bg="black")
frame.place(relx=0, rely=.97, relwidth=1, relheight=.95)

#border of green frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.1, anchor="n")

#The upper white frame
upper_frame = tk.Frame(root, bg="gray")
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.6, anchor="n")

#CTF Challenge Words
title_label = tk.Label(frame, text="CTF Challenge", fg="black", font=70)
title_label.place(relx=0.5, rely=0, relwidth=0.3, relheight=0.08, anchor="n")

#Question 1 words
label = tk.Label(frame, text="Question 1:", fg="black", font=40)
label.place(relx=0.07, rely=0.05, relwidth=0.19, relheight=0.1, anchor="n")

#Question 1s words
question1_label = tk.Label(frame, text="Gur nafjre vf Jrfg!", fg="black", font=40)
question1_label.place(relx=0.23, rely=0.05, relwidth=0.19, relheight=0.1, anchor="n")

answer1_label = tk.Label(frame, text="Answer 1:North\nAnswer 2:East\nAnswer 3:South\nAnswer 4:West\nType 5 for a Hint", fg="black", font=40)
answer1_label.place(relx=0.15, rely=0.12, relwidth=0.3, relheight=0.24, anchor="n")

answer2_label = tk.Label(frame, text="Question 2: JGH    YUJ    LOQ    JGH    VBQ    HJY    UHN    DFW", fg="black", font=20)
answer2_label.place(relx=0.4, rely=0.35, relwidth=0.8, relheight=0.07, anchor="n")

answer3_label = tk.Label(frame, text="JKI      YUJ       LOQ           VBQ       VGY", fg="black", font=20)
answer3_label.place(relx=0.15, rely=0.4, relwidth=0.6, relheight=0.07)

answer4_label = tk.Label(frame, text="UHN      UIHG      HJY           DFW       QGY", fg="black", font=20)
answer4_label.place(relx=0.15, rely=0.45, relwidth=0.6, relheight=0.07)

answer5_label = tk.Label(frame, text="JGH      AHS       GNU           CVU         WEA", fg="black", font=20)
answer5_label.place(relx=0.15, rely=0.5, relwidth=0.6, relheight=0.07)

answer6_label = tk.Label(frame, text="Then       Code       Is             MD5           Hash", fg="black", font=20)
answer6_label.place(relx=0.15, rely=0.58, relwidth=0.6, relheight=0.07)

answer7_label = tk.Label(frame, text="Of         Stuff      Hash        Banana        Cat", fg="black", font=20)
answer7_label.place(relx=0.15, rely=0.63, relwidth=0.6, relheight=0.07)

answer8_label = tk.Label(frame, text="The        Salad      MD2           Cheese        That\n", fg="black", font=20)
answer8_label.place(relx=0.15, rely=0.69, relwidth=0.6, relheight=0.07)

answer8_label = tk.Label(frame, text="Answer 1:1d3a6c06452f2debbd0314058c4e08a3\nAnswer 2:72b302bf297a228a75730123efef7c41\nAnswer 3:f1fbbfb6277cbf01e27d61238a72491a\nAnswer 4:5fb9bfd60fd9d0c4b6d15d0de139d7f2\nType 5 for a Hint", fg="black", font=20)
answer8_label.place(relx=0.02, rely=0.75, relwidth=0.7, relheight=0.2)

lower_frame = tk.Frame(root, bg="black")
lower_frame.place(relx=0.79, rely=0.75, relwidth=0.18, relheight=0.1, anchor="n")

second_lower_frame = tk.Frame(root, bg="black")
second_lower_frame.place(relx=0.41, rely=0.75, relwidth=0.58, relheight=0.1, anchor="n")

entry = tk.Entry(second_lower_frame, font=40)
entry.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.62, anchor="n")

def Question3():
	print("You Win!")
	return;

#Challenge 2
def Question2(answer2):
    if answer2 == "1":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 2:")
        return;
        Question2()
    if answer2 == "2":
        print ("Correct!")
        Question3()
        return;
    if answer2 == "3":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 2:")
        return;
        Question2()
    if answer2 == "4":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 2:")
        return;
        Question2()
    if answer2 == "5":
        print ("Hint: Maybe The answer lies in the order?")
        print ("Question 2:")
        return;
        Question2()
    else:
        print ("I did not understand that command.\nPlease try again\nQuestion 2:")
        return;
        Question2()

def entry1():
	entry2 = tk.Entry(second_lower_frame, font=40)
	entry2.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.62, anchor="n")
	button1 = tk.Button(lower_frame, text="Answer", bg="gray", command=lambda: Question2(entry2.get()))
	button1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.89)

#Answers to question 1
def Question1(answer1=entry):
    if answer1 == "1":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 1:")
        return;
        Question1()
    if answer1 == "2":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 1:")
        return;
        Question1()
    if answer1 == "3":
        print ("Incorrect!")
        print ("Try Again!")
        print ("Question 1:")
        return;
        Question1()
    if answer1 == "4":
        print ("correct!")
        print ("Next Question")
        print ("Question 2:")
        entry1()
        return;
    if answer1 == "5":
        print ("Hint: Better get the answer before it becomes ROTten3!\nQuestion 1:")
        return;
        Question1()
    else:
        print ("I did not understand that command.\nPlease try again\nQuestion 1:")
        return;
        Question1()

#Button
button = tk.Button(lower_frame, text="Answer", bg="gray", command=lambda: Question1(entry.get()))
button.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.89)

root.mainloop()