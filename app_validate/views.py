from django.http import JsonResponse
from .email_validator import validar_email

# Create your views here.
def validate_email_view(request):
    email = request.GET.get('email')
    print(email)
    debug = request.GET.get('debug', 'false').lower() in ('true', '1', 't')
    resultado = validar_email(email, debug)
    if resultado:
        return JsonResponse({'message': 'La cuenta existe'})
    elif resultado is None:
        return JsonResponse({'message': 'No se puede determinar'})
    else:
        return JsonResponse({'message': 'La cuenta no existe'})