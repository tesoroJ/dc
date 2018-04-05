from django.shortcuts import render
from .models import *
from django.db import connection

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

cursor = connection.cursor()


# Create your views here


def home(request):
    s = Note.objects.all()
    context = {
        'note': s
    }

    return render(request, 'jobs/templates/home.html', context)


def eaton_9315_100_160_caps(request):
    cursor.execute(etn80)
    d = cursor.fetchall()
    context = {
        'UPS': d[0][0],
        'model': d[0][1],
        'power': d[0][2],
        'OEM_DC': d[0][3],
        'DC_DC': d[0][4],
        'quantity': d[0][5],
        'OEM_In': d[1][3],
        'DC_IN': d[1][4],
        'In_q': d[1][5],
        'OEM_Out': d[2][3],
        'DC_Out': d[2][4],
        'Out_q': d[2][5],
    }
    return render(request, 'jobs/templates/Eaton_9315_100_160.html', context)


