from django.shortcuts import render


# Create your views here.

def hello_alugar(request):
    lista = ['django', 'python', 'git', 'html',
     'banco de dados', 'linux', 'Nginx', 'Uwsgi','Sistmctl'
     ]
    data = {'name' : 'curso de django3', 'lista_tecnologias' : lista}
    return render(request,'index.html',data)