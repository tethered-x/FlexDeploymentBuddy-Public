import tkinter as tk
from tkinter import ttk # for combo box
import sqlite3
from tkcalendar import DateEntry
import datetime
import json
import re

settings_data = ""
with open("lib\\settings.json") as s:
    settings_data = json.load(s)
dex_folder_location = settings_data['Client']['DEX_FOLDER']
gui_theme = settings_data['Client']['THEME_CHOICE']
theme_data = settings_data['Client']['GUI_THEMES'][gui_theme]

gui_success = theme_data['success']
gui_error = theme_data['error'] 
gui_text = theme_data['text'] 
gui_labels = theme_data['labels'] 
gui_bg = theme_data['background'] 
gui_fields = theme_data['field_background'] 

today_date = datetime.date.today()

# Connect to a database file (or create it if it doesn't exist)
#connect = sqlite3.connect('vroom_crm.db')
connect = sqlite3.connect('lib\\dev_dbs.db')
cursor = connect.cursor()

### [TO-DO]: Add gis_tech and app_specialist columns
### Create table if it doesn't exist
# cursor.execute("CREATE TABLE IF NOT EXISTS agencies (code TEXT PRIMARY KEY, name TEXT, project_manager TEXT, go_live_date TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS agencies (code TEXT PRIMARY KEY, name TEXT, project_manager TEXT, go_live_date TEXT, gis_tech TEXT, app_specialist TEXT)")
#cursor.execute("CREATE TABLE IF NOT EXISTS agency_notes (agency_code TEXT PRIMARY KEY, notes TEXT)")
# code 
# name 
# project_manager 
# go_live_date 
# gis_tech
# app_specialist

root = tk.Tk()
#root.title("Go-Live Tracker ver. 1.1.1")
root.title("Deployment Buddy - Python Edition")
root.config(bg=gui_bg)

window_header = tk.Label(root, text="Agency Info", font=('Tahoma', 14), background=gui_bg, foreground=gui_labels)
window_header.grid(row=0,column=1,columnspan=2, pady=10)

# right side of window
top_5_header = tk.Label(root, text="Upcoming Go-Lives", font=('Tahoma', 14), background=gui_bg, foreground=gui_labels)
top_5_header.grid(row=0, column=4, columnspan=3, pady=10, sticky='n')

# background=gui_bg, foreground=gui_text
agency_code_lbl = tk.Label(root, text='Agency Code', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=1, column=1, pady=5, sticky="W")
agency_name_lbl = tk.Label(root, text='Agency Name', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=2, column=1, pady=5, sticky="W")
agency_pm_lbl = tk.Label(root, text='Project Manager', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=3, column=1, pady=5, sticky="W")
agency_golive_lbl = tk.Label(root, text='Go-Live Date', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=6, column=1, pady=5, sticky="W")

agency_code_value = tk.StringVar()
agency_name_value = tk.StringVar()
agency_pm_value = tk.StringVar()
agency_as_value = tk.StringVar()
agency_gis_value = tk.StringVar()
agency_golive_value = tk.StringVar()
agency_golive_tbd_toggle_value = tk.IntVar()

agency_code_entry = tk.Entry(root, textvariable=agency_code_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
agency_code_entry.grid(row=1, column=2, pady=5)
agency_name_entry = tk.Entry(root, textvariable=agency_name_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
agency_name_entry.grid(row=2, column=2, pady=5)
agency_pm_entry = tk.Entry(root, textvariable=agency_pm_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
agency_pm_entry.grid(row=3, column=2, pady=5)

# agency AS
agency_as_lbl = tk.Label(root, text='App. Specialist', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=4, column=1, pady=5, sticky="W")
agency_as_entry = tk.Entry(root, textvariable=agency_as_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
agency_as_entry.grid(row=4, column=2, pady=5)
#agency GIS
agency_gis_lbl = tk.Label(root, text='GIS Tech', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=5, column=1, pady=5, sticky="W")
agency_gis_entry = tk.Entry(root, textvariable=agency_gis_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
agency_gis_entry.grid(row=5, column=2, pady=5)

agency_golive_tbd_toggle = tk.Checkbutton(root, text="TBD", font=('Tahoma', 10), variable=agency_golive_tbd_toggle_value, background=gui_bg, foreground=gui_labels)
agency_golive_tbd_toggle.grid(row=6, column=3)

agency_golive_calendar = DateEntry(root, font=('Tahoma', 10), width=18, background=gui_fields, selectbackground=gui_fields, foreground=gui_text, borderwidth=2, year=2025)
agency_golive_calendar.grid(row=6, column=2, pady=5)

## SETTINGS PAGE
def settings_page():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.config(background=gui_bg)
    # PADDING
    settings_header = tk.Label(settings_window, text="System Settings", font=('Tahoma', 14), background=gui_bg, foreground=gui_labels)
    settings_header.grid(row=0,column=1,columnspan=2, pady=10)
    settings_padL = tk.Label(settings_window, text="", background=gui_bg, foreground=gui_labels)
    settings_padL.grid(row=0,column=0, padx=20)
    settings_padR = tk.Label(settings_window, text="", background=gui_bg, foreground=gui_labels)
    settings_padR.grid(row=0,column=3, padx=20)
    settings_footer = tk.Label(settings_window, text="", background=gui_bg, foreground=gui_labels)
    settings_footer.grid(row=3,column=0, columnspan=4, pady=20)
    # THEME CHOOSER
    try:
        with open('lib\\settings.json', 'r') as settings_file:
            settings_data = json.load(settings_file)
            # dex_folder_location = settings_data['Client']['DEX_FOLDER']
            # gui_theme = settings_data['Client']['THEME_CHOICE']
            # theme_data = settings_data['Client']['GUI_THEMES'][gui_theme]
        theme_chooser_lbl = tk.Label(settings_window, text='Choose Theme:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
        theme_chooser_lbl.grid(row=1, column=1, pady=5, sticky="W")
        theme_list = []
        for theme in settings_data['Client']['GUI_THEMES']:
            #print(theme)
            theme_list.append(theme)
        theme_combo_box = ttk.Combobox(settings_window, values=theme_list, state='readonly', justify="right")
        theme_combo_box.grid(row=1, column=2, pady=5, padx=15)
        theme_combo_box.set(gui_theme)
        def save_settings():
            theme_choice = theme_combo_box.get()
            settings_data['Client']['THEME_CHOICE'] = theme_choice
            try:
                with open('lib\\settings.json', 'w') as settings_file:
                    json.dump(settings_data, settings_file, indent=4)
                print('Settings Successfully Updated')
                msg_footer = tk.Label(settings_window, text="Settings saved successfully. Please restart application.", background=gui_bg, foreground=gui_success)
                msg_footer.grid(row=3,column=1, columnspan=2)
            except:
                print("Failed to save settings.")
                msg_footer = tk.Label(settings_window, text="Failed to save settings.", background=gui_bg, foreground=gui_error)
                msg_footer.grid(row=3,column=1, columnspan=2)
            #print(theme_choice)
        save_settings_btn = tk.Button(settings_window, text='Save', width=15, command=save_settings, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
        save_settings_btn.grid(row=2,column=1, columnspan=2, pady=5)
    except:
        print("Settings page cannot be loaded.")
    # EXPORT DIRECTORY


## MENU BAR
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Settings', command=settings_page)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

def clear_entries():
    agency_code_entry.delete(0, tk.END)
    agency_name_entry.delete(0, tk.END)
    agency_pm_entry.delete(0, tk.END)
    agency_gis_entry.delete(0, tk.END)
    agency_as_entry.delete(0, tk.END)
    agency_golive_tbd_toggle_value.set(0)
    agency_golive_calendar.set_date(today_date)

def convert_string_to_date(date):
    date_string = date
    date_format = "%Y-%m-%d"
    datetime_object = datetime.datetime.strptime(date_string, date_format).date()
    delta = datetime_object - today_date
    days_difference = delta.days
    return days_difference

def modify_agency_record(code, name, pm, golive, appspec, gis):
    m_code = code
    m_name = name.get()
    m_pm = pm.get()
    m_golive = golive
    m_as = appspec.get()
    m_gis = gis.get()
    if m_golive == "2099-12-31":
        m_golive = "9999-12-31"
    # print(m_code, m_name, m_pm, m_golive)
    m_sql = f"UPDATE agencies SET name = '{m_name}', project_manager = '{m_pm}', go_live_date = '{m_golive}', app_specialist = '{m_as}', gis_tech = '{m_gis}' WHERE code = '{m_code}'"
    m_success_window = tk.Toplevel(root)
    m_success_window.config(background=gui_bg)
    m_success_window.title("Modify Record")
    m_msg = ""
    m_msg_color = ""
    try:
        cursor.execute(m_sql)
        m_msg = "Record Successfully Modified"
        m_msg_color = gui_success
        print_all_agencies(root, 5, 0)
        connect.commit()
    except:
        m_msg = "Modify Failed"
        m_msg_color = gui_error
        ### [TO-DO] implement some logging.
    m_success_label = tk.Label(m_success_window, text=m_msg, font=('Tahoma', 10), background=gui_bg, foreground=m_msg_color)
    m_success_label.pack(pady=50,padx=50)

def open_agency_info_window():
    agency_code = agency_code_value.get().upper()
    if agency_code != "":
        agency_window = tk.Toplevel(root)
        agency_window.title("Agency Info")
        agency_window.config(background=gui_bg)
        ### SELECT ALL CODES IN AGENCY AND CHECK IF THE CODE EXISTS
        check_sql = "SELECT code FROM agencies"
        code_list = []
        for code in cursor.execute(check_sql):
            code = code[0]
            code_list.append(code)
        if agency_code in code_list:
            agency_sql = f"SELECT * FROM agencies WHERE code = '{agency_code}'"
            for entry in cursor.execute(agency_sql):
                #print(entry)
                agncy_code = entry[0]
                agncy_name = entry[1]
                agncy_pm = entry[2]
                agncy_golive = entry[3]
                ### Convert these into strings just in case they are null
                agncy_gis = str(entry[4])
                agncy_as = str(entry[5])
                if agncy_golive == "9999-12-31":
                    agncy_golive = "TBD"
                # Agency Code label
                a_code_lbl = tk.Label(agency_window, text='Agency Code:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_code_lbl.grid(row=0, column=0, pady=5,  padx=10, sticky="W")
                # Agency Code Entry/Label for no edit
                a_code_e = tk.Label(agency_window, text=agncy_code, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_code_e.grid(row=0, column=1, pady=5,  padx=10, sticky="E")
                # Aegcny Name Label
                a_name_lbl = tk.Label(agency_window, text='Agency Name:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_name_lbl.grid(row=1, column=0, pady=5,  padx=10, sticky="W")
                # Agency Name Entry
                a_name_var = tk.StringVar()
                a_name_e = tk.Entry(agency_window, textvariable=a_name_var, width=30, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
                a_name_e.insert(0, agncy_name)
                a_name_e.grid(row=1, column=1, pady=5, padx=10, sticky="E")
                # Agency Project Manager Label
                a_pm_lbl = tk.Label(agency_window, text='Project Manager:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_pm_lbl.grid(row=2, column=0, pady=5,  padx=10, sticky="W")
                # Agency Project Manager Entry
                a_pm_var = tk.StringVar()
                a_pm_e = tk.Entry(agency_window, textvariable=a_pm_var, width=30, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
                a_pm_e.insert(0, agncy_pm)
                a_pm_e.grid(row=2, column=1, pady=5, padx=10, sticky="E")
                
                # AS
                #print("AS:", agncy_as)
                a_as_lbl = tk.Label(agency_window, text='App. Specialist:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_as_lbl.grid(row=3, column=0, pady=5,  padx=10, sticky="W")
                # Agency Project Manager Entry
                a_as_var = tk.StringVar()
                a_as_e = tk.Entry(agency_window, textvariable=a_as_var, width=30, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
                a_as_e.insert(0, agncy_as)
                a_as_e.grid(row=3, column=1, pady=5, padx=10, sticky="E")

                # GIS
                #print("GIS:", agncy_gis)
                a_gis_lbl = tk.Label(agency_window, text='GIS Tech:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_gis_lbl.grid(row=4, column=0, pady=5,  padx=10, sticky="W")
                # Agency Project Manager Entry
                a_gis_var = tk.StringVar()
                a_gis_e = tk.Entry(agency_window, textvariable=a_gis_var, width=30, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
                a_gis_e.insert(0, agncy_gis)
                a_gis_e.grid(row=4, column=1, pady=5, padx=10, sticky="E")

                # Agency Go-Live Label
                a_golive_lbl = tk.Label(agency_window, text='Go-Live Date:', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
                a_golive_lbl.grid(row=5, column=0, pady=5,  padx=10, sticky="W")
                # Agency Go-Live Entry
                a_golive_e = DateEntry(agency_window, font=('Tahoma', 10), background=gui_fields, selectbackground=gui_fields, foreground=gui_text, borderwidth=2, year=2025)
                a_golive_e.grid(row=5, column=1, padx=10, sticky="E")

                if agncy_golive == "TBD":
                    agncy_golive = "9999-12-31"
                a_golive_e.set_date(datetime.datetime.strptime(agncy_golive, "%Y-%m-%d").date())

                # MODIFY BUTTON
                a_mod_btn = tk.Button(agency_window, text='Modify', width=15, command=lambda: modify_agency_record(agncy_code, a_name_var, a_pm_var, str(a_golive_e.get_date()), a_as_var, a_gis_var), font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
                a_mod_btn.grid(row=6,column=0,columnspan=2, pady=10)
        else:
            agency_window_code = tk.Label(agency_window, text=f"Agency ({agency_code}) Not Found", font=('Tahoma', 10), background=gui_bg, foreground=gui_error)
            agency_window_code.pack(pady=50,padx=50)
    else:
        msg_label = tk.Label(root, text="Search by Agency Code", font=('Tahoma', 10), background=gui_fields, foreground=gui_error)
        msg_label.grid(row=8, column=1, columnspan=2)
        msg_label.after(3000, msg_label.destroy)
        # agency_window_code = tk.Label(agency_window, text="Search by Agency Code", font=('Tahoma', 10), background=gui_bg, foreground=gui_error)
        # agency_window_code.pack(pady=50,padx=50)
    clear_entries()

def print_all_agencies(screen, total, stop):
    index = 1
    agency_list = []
    day_color = ""
    for entry in cursor.execute("SELECT * FROM agencies"):
        agency_list.append(entry)
    agency_list.sort(key=lambda agency: agency[3])
    for item in agency_list:
        code_text = f"{item[0]}"
        date_text = f"{item[3]}"
        days_left = convert_string_to_date(date_text)
        if days_left >= stop:
            tk.Label(screen, text=code_text, font=('Tahoma', 10), background=gui_bg, foreground=gui_text).grid(row=index, column=4, padx=20)
            if date_text == "9999-12-31":
                date_text = "TBD"
            tk.Label(screen, text=date_text, font=('Tahoma', 10), background=gui_bg, foreground=gui_text).grid(row=index, column=5, padx=20)
            if days_left >= 20000:
                days_left = "TBD"
                day_color = gui_labels
            else:
                if days_left >= 30 or days_left == "TBD":
                    day_color = gui_success
                elif days_left < 0:
                    day_color = gui_labels
                else:
                    day_color = gui_error
            tk.Label(screen, text=days_left, font=('Tahoma', 10), background=gui_bg, foreground=day_color).grid(row=index, column=6, padx=10)
            index = index + 1
            if index >= (total + 1):
                break
        else:
            continue

def open_listall_window():
    listall_window = tk.Toplevel(root)
    listall_window.config(bg=gui_bg)
    listall_window.title("All Agencies")
    print_all_agencies(listall_window, 1000, -99999999)

def create_notes_page(agency_code):
    def_file = open("lib\\agency_note_template.txt")
    def_content = def_file.read()
    new_file_name = f"{agency_code}.txt"
    try:
        open(f"lib\\notes\\{new_file_name}", "x")
    except:
        pass
    with open(f"lib\\notes\\{new_file_name}", "w") as nf:
        nf.write(def_content)

# code 
# name 
# project_manager 
# go_live_date 
# gis_tech
# app_specialist
def add_agency():
    agency_code = agency_code_value.get().upper()
    agency_name = agency_name_value.get()
    agency_pm = agency_pm_value.get()
    agency_as = agency_as_value.get()
    agency_gis = agency_gis_value.get()
    agency_golive = str(agency_golive_calendar.get_date())
    agency_golive_tbd = agency_golive_tbd_toggle_value.get()
    add_msg = ""
    msg_color = ""
    try:
        if agency_code != "" and agency_name != "" and agency_pm != "":
            sql_insert = "INSERT OR IGNORE INTO agencies (code,name,project_manager,gis_tech,app_specialist,go_live_date) VALUES (?,?,?,?,?,?)"
            if agency_golive_tbd == 0:
                sql_values = (agency_code, agency_name, agency_pm, agency_gis, agency_as, agency_golive)
            else:
                sql_values = (agency_code, agency_name, agency_pm, agency_gis, agency_as, '9999-12-31')
            cursor.execute(sql_insert, sql_values)
            connect.commit()
            clear_entries()
            print_all_agencies(root, 5, 0)
            create_notes_page(agency_code)
            add_msg = "Add succeeded."
            msg_color = gui_success
        else:
            add_msg = "Add failed. One or more field is blank."
            msg_color = gui_error
    except:
        add_msg = "Add failed."
        msg_color = gui_error
    msg_label = tk.Label(root, text=add_msg, font=('Tahoma', 10), background=gui_fields, foreground=msg_color)
    msg_label.grid(row=8, column=1, columnspan=2)
    msg_label.after(3000, msg_label.destroy)

add_agency_btn = tk.Button(root, text='Add', width=15, command=add_agency, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
add_agency_btn.grid(row=7,column=1, pady=5)

search_agency_btn = tk.Button(root, text='Search', width=15, command=open_agency_info_window, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
search_agency_btn.grid(row=7,column=2)

# Initial List when opening app
print_all_agencies(root, 5, 0)

# LIST ALL BUTTON
listall_agencies_btn = tk.Button(root, text='List All', width=15, command=open_listall_window, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
listall_agencies_btn.grid(row=7,column=5, padx=10)

# LEFT PADDING
left_padding = tk.Label(root, text="", background=gui_bg)
left_padding.grid(row=0, column=0, padx=20)

# CENTER PADDING
center_padding = tk.Label(root, text="", background=gui_bg)
center_padding.grid(row=0, column=3, padx=20)

# FOOTER
footer = tk.Label(root, text="", background=gui_bg)
footer.grid(row=8, column=0, columnspan=8, pady=10)

# RIGHT PADDING
right_padding = tk.Label(root, text="", background=gui_bg)
right_padding.grid(row=0, column=7, padx=20)

#### AGENCY NOTES TABLE ####
# ROW 9 10
# COLUMNS 4 5 6
notes_header = tk.Label(root, text="Agency Notes", font=('Tahoma', 14), background=gui_bg, foreground=gui_labels)
notes_header.grid(row=9,column=4,columnspan=3, pady=10)

notes_agency_code_lbl = tk.Label(root, text='Agency Code', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=10, column=4, pady=5, sticky="W")

notes_agency_code_value = tk.StringVar()

notes_agency_code_entry = tk.Entry(root, textvariable=notes_agency_code_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
notes_agency_code_entry.grid(row=10, column=5, columnspan=2, pady=5)

def open_notes_page():
    an_agency_code = notes_agency_code_value.get().upper()
    an_agency_header_txt = f"Agency Notes"
    an_agency_name_long = ""
    if an_agency_code != "":
        #print(an_agency_code)
        code_search_sql = f"SELECT * FROM agencies WHERE code = '{an_agency_code}'"
        code_search_list = []
        for code in cursor.execute(code_search_sql):
            an_agency_name_long = code[1]
            code = code[0]
            code_search_list.append(code)
        if an_agency_code in code_search_list:
            agency_notes_window = tk.Toplevel(root)
            agency_notes_window.title(an_agency_header_txt + " - " + an_agency_code)
            agency_notes_window.config(background=gui_bg)

            ## Padding
            an_left_margin = tk.Label(agency_notes_window, text="", background=gui_bg)
            an_left_margin.grid(row=1, column=0, padx=10)
            an_right_margin = tk.Label(agency_notes_window, text="", background=gui_bg)
            an_right_margin.grid(row=1, column=4, padx=10)
            an_bottom_margin = tk.Label(agency_notes_window, text="", background=gui_bg)
            an_bottom_margin.grid(row=4, column=0, pady=5)

            an_agency_name_txt = f"Agency: {an_agency_name_long}"
            an_agency_name_lbl = tk.Label(agency_notes_window, text=an_agency_name_txt, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels)
            an_agency_name_lbl.grid(row=1, column=1, pady=5, sticky="W")

            agency_notes_file = open(f"lib\\notes\\{an_agency_code}.txt")
            textbox_value = agency_notes_file.read()
            agency_notes_textbox = tk.Text(agency_notes_window, height=30, width=120, background=gui_fields, foreground=gui_text)
            agency_notes_textbox.grid(row=2, column=1, columnspan=3)
            agency_notes_textbox.insert(tk.END, textbox_value)

            def save_new_text():
                new_text = agency_notes_textbox.get("1.0", tk.END)
                save_msg = ""
                msg_color = ""
                try:
                    with open(f"lib\\notes\\{an_agency_code}.txt", "w") as af:
                        af.write(new_text)
                        save_msg = "Notes Saved."
                        msg_color = gui_success
                except:
                    print("FAIL")
                    save_msg = "Save failed."
                    msg_color = gui_error
                save_msg_label = tk.Label(agency_notes_window, text=save_msg, font=('Tahoma', 10), background=gui_bg, foreground=msg_color)
                save_msg_label.grid(row=4, column=1, columnspan=3, pady=15)
                save_msg_label.after(3000, save_msg_label.destroy)


            an_save_btn = tk.Button(agency_notes_window, command=save_new_text, text='Save', width=15, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
            an_save_btn.grid(row=3,column=1, columnspan=3, pady=15)
            notes_agency_code_entry.delete(0, tk.END)
        else:
            an_error_msg = tk.Label(root, text="Agency not found.", font=('Tahoma', 10), background=gui_bg, foreground=gui_error)
            an_error_msg.grid(row=11, column=4, columnspan=3)
            an_error_msg.after(3000, an_error_msg.destroy)
    else:
        an_error_msg = tk.Label(root, text="Please enter agency code.", font=('Tahoma', 10), background=gui_bg, foreground=gui_error)
        #print("Code missing.")
        an_error_msg.grid(row=11, column=4, columnspan=3)
        an_error_msg.after(3000, an_error_msg.destroy)
        
notes_btn = tk.Button(root, text='Search', width=15, command=open_notes_page, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
notes_btn.grid(row=12,column=4, columnspan=3, pady=5)

#### DEX PRIVS BUILDER ####
# ROW 9 10 and 11
# COLUMNS 1 to 2
dex_priv_header = tk.Label(root, text="DEX Privs Builder", font=('Tahoma', 14), background=gui_bg, foreground=gui_labels)
dex_priv_header.grid(row=9,column=1,columnspan=2, pady=10)

def export_dex_privs_json():
    vendor = dex_vendor_combobox.get()
    flex_uid = dex_uid_value.get()
    syprivs = ""
    ### ADD THE LOGIC
    json_data = ""
    with open("lib\\DEX_privs.json") as j:
        json_data = json.load(j)
    vendor_data = json_data['VENDORS'][vendor]['SYPRIVS']
    for sypriv in vendor_data:
        new_line = re.sub("{flex_uid}", flex_uid, sypriv)
        if sypriv == vendor_data[-1]:
            syprivs += new_line
        else:
            syprivs += new_line + "\n"
    error_msg = ""
    msg_color = ""
    try:
        dex_settings_data = ""
        with open("lib\\settings.json") as d:
            dex_settings_data = json.load(d)
        dex_folder_location = dex_settings_data['Client']['DEX_FOLDER']
        file_name = f"{dex_folder_location}\\{vendor}.txt"
        with open(file_name, "w") as f:
            f.write(syprivs)
        error_msg = f"File {vendor}.txt successfully exported."
        msg_color = gui_text
    except Exception as e:
        error_msg = e
        msg_color = gui_error
    # RESET VALUES TO BLANK
    dex_vendor_combobox.set("")
    dex_uid_value.set("")
    msg_label = tk.Label(root, text=error_msg, font=('Tahoma', 10), background=gui_fields, foreground=msg_color)
    msg_label.grid(column=1, columnspan=3, row=13, pady=10)
    msg_label.after(3000, msg_label.destroy)


dex_vendor_lbl = tk.Label(root, text='Vendor', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=10, column=1, pady=5, sticky="W")
dex_uid_lbl = tk.Label(root, text='Flex UID', font=('Tahoma', 10), background=gui_bg, foreground=gui_labels).grid(row=11, column=1, pady=5, sticky="W")

def list_dex_vendors():
    vendor_list = []
    with open("lib\\DEX_privs.json") as j:
        json_data = json.load(j)
    dex_vendors = json_data['VENDORS']
    for vendor in dex_vendors:
        vendor_list.append(vendor)
    vendor_list.sort()
    return vendor_list

dex_vendor_value = list_dex_vendors()
dex_uid_value = tk.StringVar()

dex_vendor_combobox = ttk.Combobox(root, values=dex_vendor_value, state='readonly', font=('Tahoma', 10), width=18)
dex_vendor_combobox.grid(row=10, column=2, pady=5)

dex_uid_entry = tk.Entry(root, textvariable=dex_uid_value, font=('Tahoma', 10), background=gui_fields, foreground=gui_labels, justify="right")
dex_uid_entry.grid(row=11, column=2, pady=5)

dex_privs_btn = tk.Button(root, text='Export', width=15, command=export_dex_privs_json, font=('Tahoma', 10), background=gui_bg, foreground=gui_labels, activebackground=gui_fields, activeforeground=gui_labels)
dex_privs_btn.grid(row=12,column=1, columnspan=2, pady=5)

dex_footer= tk.Label(root, text="", background=gui_bg)
dex_footer.grid(row=13, column=0, columnspan=8, pady=10)

root.mainloop()

# [TODO] Create a way to delete an agency or notes record
### Delete record to table
# cursor.execute('''DELETE FROM agencies WHERE code = "NYVOLPD"''')

connect.close()