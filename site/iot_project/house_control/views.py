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
            ledId = request.POST.get('ledId')
            arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            if ledId == '1':
                print(ledId)
                arduino.write(b'H')

            resposta = 'Led Aceso!'
        except Exception as e:
            resposta = f'Ocorreu o erro, {e}'
    
    return JsonResponse({'resposta':resposta})