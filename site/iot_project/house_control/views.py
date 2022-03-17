from django.shortcuts import render
from django.http import JsonResponse
import serial

# Create your views here.
def index(request):
    #Essa funçao juntará as informaçoes iniciais e renderizará de acordo com o que for passado
    titulo = "Bem vindo ao sistema de controle inteligente GABIN"
    return render(request, 'html/index.html', context={
        'titulo':titulo,
    })


def acende_led(request):
    if request.method == 'POST':
        try:
            ledCommand = request.POST.get('ledCommand')
            arduino = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
            command = '{}'.format(ledCommand).encode()
            arduino.write(command)
            
            resposta = 'Led Aceso!'
        except Exception as e:
            resposta = f'Ocorreu o erro, {e}'
    
    return JsonResponse({'resposta':resposta})


# def acende_led(request):
#     global init
#     if request.method == 'POST':
#         try:
#             ledCommand = request.POST.get('ledCommand')
#             if ledCommand != 'H' or 'l':
#                 if not init:
#                     ledCommand = ledCommand.upper()
#                     init = True
#                     print(ledCommand)
#                 else:
#                     ledCommand = ledCommand.lower()
#                     init = False

#             arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#             command = '{}'.format(ledCommand).encode()
#             arduino.write(command)
            
#             resposta = 'Led Aceso!'
#         except Exception as e:
#             resposta = f'Ocorreu o erro, {e}'
    
#     return JsonResponse({'resposta':resposta})