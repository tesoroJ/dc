import os
import pymysql.cursors
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    database='DC',
    user='root',
    password='qwerty',
)
cursor = conn.cursor()
sql1 = 'USE DC'
etn80 = '''select UPS_part.brand, UPS_part.model, UPS_part.power,  cap.oem_name, cap.dc_name, cap_dc.quantity from cap
inner join UPS_part on cap.id=UPS_part.DC_cap
inner join cap_dc on cap_dc.ups_id=UPS_part.id
where UPS_part.id=2

union

select UPS_part.brand, UPS_part.model, UPS_part.power,  cap.oem_name, cap.dc_name, cap_input.quantity from cap
inner join UPS_part on cap.id=UPS_part.input_cap
inner join cap_input on cap_input.ups_id=UPS_part.id
where UPS_part.id=2
union

select UPS_part.brand, UPS_part.model, UPS_part.power,  cap.oem_name, cap.dc_name, cap_output.quantity from cap
inner join UPS_part on cap.id=UPS_part.output_cap
inner join cap_output on cap_output.ups_id=UPS_part.id
where UPS_part.id=2;'''

sql3='select * from cap'

cursor.execute(sql1)
cursor.execute(etn80)

row = cursor.fetchall()
print(row)
print(cursor.execute(sql3))

name = input()
f = 'Hello {}'

print(f.format(name))