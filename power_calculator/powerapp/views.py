from django.shortcuts import render

def home(request):
    return render(request, 'powerapp/home.html')

def calculator(request):
    power = None
    if request.method == 'POST':
        intensity = float(request.POST.get('intensity', 0))
        resistance = float(request.POST.get('resistance', 0))
        power = round(intensity ** 2 * resistance, 2)
    return render(request, 'powerapp/calculator.html', {'power': power})