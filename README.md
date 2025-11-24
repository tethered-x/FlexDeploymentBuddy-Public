# Flex Deployment Buddy - Python Edition
Released 11/24/25

Made by Matt Vroom

NOTE: It is important that the DeploymentBuddy folder is granted the ability to read/add/modify files.

This is the main UI. It's broken down into 4 sections. 
1. Agency Info (for adding and searching for agencies)
2. Upcoming Go-Lives (includes the go-live date and how many days until then)
3. DEX Privs Builder (Exports .txt files that can be loaded into FLEX DB)
4. Agency Notes (A modifiable .txt file that can be saved within the app)
<img width="633" height="565" alt="Screenshot 2025-11-24 083331" src="https://github.com/user-attachments/assets/275d9750-aa5d-404e-bb67-c99f2aee8341" />

ADDING AN AGENCY:
Under the "Agency Info" section -
- Add an agency code (Required)
- Add an agency name (Required)
- Add the project manager name (Required)
- Add the app. specialist (if known) or you can put TBA/TBD in that field
- Add the GIS tech (if known) or you can put TBA/TBD in that field
<img width="382" height="291" alt="Screenshot 2025-11-24 083412" src="https://github.com/user-attachments/assets/898b2c2b-90a9-49d9-aa70-1d937bc8b401" />

You can choose the go-live date from the calendar drop down, or check on the "TBD" checkbox if it isn't known yet.
<img width="400" height="228" alt="Screenshot 2025-11-24 083439" src="https://github.com/user-attachments/assets/0a7f7081-0192-4aee-8585-1bdc2b491feb" />

NOTE: If you check TBD, the go-live date and days until go-live will show up as TBD in the "Upcoming Go-Lives" section, and 12-31-2099 in the database.

<img width="270" height="68" alt="Screenshot 2025-11-24 083453" src="https://github.com/user-attachments/assets/3d7cec08-979e-4ddb-a7a3-692b756db786" />

SEARCHING/MODIFYING AN AGENCY:
Under the "Agency Info" section -
- In the "Agency Code" field put your agency code.
- Then hit "Search"
  
<img width="366" height="301" alt="Screenshot 2025-11-24 083537" src="https://github.com/user-attachments/assets/bf6c7896-fed5-49f7-91b9-42fefee95566" />

If the agency is found you will get a new window that pops up.

<img width="366" height="275" alt="Screenshot 2025-11-24 083557" src="https://github.com/user-attachments/assets/0f314f5b-70ee-4af6-9b15-666fc8a3951c" />

From here you can make changes and hit "Modify" when you want to apply those changes. You'll see a success message pop-up once the record is saved.

<img width="277" height="164" alt="Screenshot 2025-11-24 083616" src="https://github.com/user-attachments/assets/cf8e4088-26f7-4daf-910d-049bf4d6eaee" />

UPCOMING GO-LIVES:
This section shows you the top 5 upcoming go-lives. Agencies are sorted by nearest to farthest away.
The list is broken up in three sections:
1. Agency Code
2. Go-Live Date
3. Days Until Go-Live

<img width="336" height="290" alt="Screenshot 2025-11-24 083512" src="https://github.com/user-attachments/assets/1895368e-b7ef-4d96-b0d9-2b456f8306f9" />

If you hit the "List All" button, it will show you a complete list of all the agencies that you have added and their corresponding go-live dates.

<img width="275" height="253" alt="Screenshot 2025-11-24 083524" src="https://github.com/user-attachments/assets/54fea51b-6960-4eb4-aed8-4bca8eae3f67" />

ADDING AGENCY NOTES:
When you add an agency, a .txt file is also created at the same time. These files are saved in the ..\DeploymentBuddy\lib\notes directory.

1. In the "Agency Code" field place the agency code for the agency that you want to make notes on.
2. If successful, a new window will open. But if the agency code is wrong or doesn't belong to an added agency then you'll get this error:

<img width="311" height="173" alt="Screenshot 2025-11-24 083650" src="https://github.com/user-attachments/assets/272970cc-f648-434e-88a3-6a0cfcef3109" />

With the new window open. You can make changes. The intial file creation copies from the agency_note_template.txt file located in ..\DeploymentBuddy\lib.
If you want to make changes to your template, then modify the agency_note_template.txt file.

<img width="1022" height="648" alt="Screenshot 2025-11-24 083700" src="https://github.com/user-attachments/assets/dab3bd5b-d343-45cc-bb52-5767067e92e7" />

Hit the "Save" button to apply your changes. 

<img width="200" height="129" alt="Screenshot 2025-11-24 083707" src="https://github.com/user-attachments/assets/a4322a81-df3a-4569-89a9-69c2ae22daf4" />

DATA EXCHANGE SYPRIV BUILDER:
You have the option to create a dbloadable .txt file from a collection of syprivs hosted in the DEX_privs.json file found in ..\DeploymentBuddy\lib.
There is a list of 33 DEX vendors available as of this writing.

<img width="305" height="252" alt="Screenshot 2025-11-24 083731" src="https://github.com/user-attachments/assets/da77f7da-ff18-4072-b937-607782199610" />

You need to create an XMLuser account for your vendor on the FLEX system prior to using this tool. You'll need the UID from SYUSRADM.

1. Choose the vendor that you need the syprivs for.
2. Put the UID from SYUSRADM in the Flex UID field.
3. Hit the "Export" button
You should a success message if the export worked.

<img width="355" height="201" alt="Screenshot 2025-11-24 083753" src="https://github.com/user-attachments/assets/d61dc0c1-008b-4aea-9e0d-ce6bbe719faa" />

The export .txt file will be saved to ..\DeploymentBuddy\DEX_Privs

<img width="754" height="369" alt="Screenshot 2025-11-24 083801" src="https://github.com/user-attachments/assets/4db7fe63-27ba-4d53-ad34-d855fac28f6e" />

CHANGING THEME COLORS:
The themes are located in the settings.json file in ..\DeploymentBuddy\lib
Feel free to create your own themes. Just follow the layout that the other themes use.

"COBALT": {
                "success": "#c2e37b",
                "error": "#de4a14",
                "text": "#ffffff",
                "labels": "#a8afb5",
                "background": "#142838",
                "field_background": "#0c547a"
            }

To set a new theme:
1. On the main window, click on "File" then "Settings"

<img width="149" height="128" alt="Screenshot 2025-11-24 083829" src="https://github.com/user-attachments/assets/56d7888e-41bb-43cc-a3c9-5ec96aaea524" />

2. Choose the theme you want from the drop down

<img width="364" height="215" alt="Screenshot 2025-11-24 083846" src="https://github.com/user-attachments/assets/3378eadd-7f23-4bcf-86d8-a7b3812d1025" />

3. Then hit save. You will be prompted to restart the application.

<img width="383" height="216" alt="Screenshot 2025-11-24 083856" src="https://github.com/user-attachments/assets/3c9573cf-525e-4998-85ee-33691ee3e646" />

You will see the new theme once you open the program back up.

<img width="682" height="562" alt="Screenshot 2025-11-24 083907" src="https://github.com/user-attachments/assets/362bd556-c4bd-4160-8ddb-c9b3d2b1c0bd" />





