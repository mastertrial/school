student_intro = []
inited = False
with open('infomation.txt', "r", encoding="UTF8") as info:
    for i in str(info.readlines()).split("\\n"):
        student_intro.append(i[4:].split("|"))

student_intro = student_intro[1:]
print(student_intro)

for i in range(len(student_intro) - 1):
    if len(student_intro[i]) != 6:
        if i != 0:
            print(f'Number {i} have some problem')

import dearpygui.dearpygui as dpg
import clipboard

stduent = 0
batch = 0
def print_now() : print(student_intro[stduent][batch])
def do_next():
    global batch, stduent
    if batch == 5:
        batch = 0
        stduent += 1
        clipboard.copy(student_intro[stduent][batch])
        print_now()
    else:
        batch += 1
        clipboard.copy(student_intro[stduent][batch])
        print_now()


        
    # try:
    #     global batch, stduent
    #     if batch == 6:
    #         clipboard.copy(student_intro[stduent][batch])
    #         print(f"{stduent+1} is end")
    #         batch = 0
    #         stduent += 1
    #         return
    #     print(student_intro[stduent][batch])
    #     clipboard.copy(student_intro[stduent][batch])
    #     batch += 1
    # except IndexError:
    #     batch = 0
    #     stduent += 1
    #     clipboard.copy(student_intro[stduent][batch])
    #     print(student_intro[stduent][batch])

dpg.create_context()
dpg.create_viewport(width=500, height=500)
dpg.setup_dearpygui()

with dpg.window(label="Window", width=500, height=500):
    dpg.add_button(label="Save", callback=do_next)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

