import requests
from termcolor import colored

def verificar_cabecalhos(url):
    response = requests.head(url)
    headers = response.headers

    cabecalhos = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Frame-Options',
        'X-Content-Type-Options',
        'Referrer-Policy',
        'Permissions-Policy',
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Origin',
        'X-XSS-Protection'
    ]

    for cabecalho in cabecalhos:
        if cabecalho in headers:
            print(f"{cabecalho}: {colored('OK', 'green')}")
        else:
            print(f"{cabecalho}: {colored('AUSENTE', 'red')}")


url = input("Digite a URL: ")


verificar_cabecalhos(url)
