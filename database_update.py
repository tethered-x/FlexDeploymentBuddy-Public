import sqlite3

connect = sqlite3.connect('vroom_crm.db')
cursor = connect.cursor()
try:
    cursor.execute("ALTER TABLE agencies ADD COLUMN gis_tech TEXT")
    print("GIS Tech Column Added Successfully")
except:
    print("GIS FAILED")

try:
    cursor.execute("ALTER TABLE agencies ADD COLUMN app_specialist TEXT")
    print("AS Column added successfully.")
except:
    print("AS Failed")

connect.commit()
connect.close()
