from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import EstacaoTrabalho, Impressoras, Telefones, User
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # login successful, redirect to homepage
            return redirect('/Start')
        else:
            # login failed, show error message
            return render(request, '127.4.4.1:800.html', {'error': 'Invalid username or password'})
    else:
        # render login form
        return render(request, 'Login.html')






    
@login_required
def Start(request):
    return render(request, 'Start.html')
    
    


def home(request):
    ativos = EstacaoTrabalho.objects.all()
    paginator = Paginator(ativos, 5) #mostra 5 objetos na página
    page = request.GET.get('page')
    ativos = paginator.get_page(page)
    return render(request, "GestaoEstacoes.html", {"ativos": ativos})

def registrarEstacao(request):
    nome = request.POST['txtNome']
    modelo = request.POST['txtmodelo']
    serial = request.POST['txtserial']
    setor = request.POST['txtsetor']
    
    estacao = EstacaoTrabalho.objects.create(nome=nome, modelo=modelo, serial=serial, setor=setor)
    return redirect('/Estacao')

def edicaoEstacao(request, identificador):
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    return render(request, "edicaoEstacao.html", {"estacao": estacao})
    

def editarEstacao(request, identificador):
    
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    
    estacao.nome = request.POST['txtNome']
    estacao.modelo = request.POST['txtmodelo']
    estacao.serial = request.POST['txtserial']
    estacao.setor = request.POST['txtsetor'] 
    estacao.save()
    return redirect('/Estacao')
    
        


def deletarEstacao(resquest, identificador):
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    estacao.delete()
    return redirect('/Estacao')



    #session class Impressora

def printer(request):
    printers = Impressoras.objects.all()
    return render(request, "GestaoImpressoras.html", {"ListarAtivos": printers})


def registrarImpressora(request):
    nome = request.POST['txtNome']
    modelo = request.POST['txtmodelo']
    cupsid = request.POST['txtcups']
    setor = request.POST['txtsetor']
    
    printers = Impressoras.objects.create(nome=nome, modelo=modelo, cupsid=cupsid, setor=setor)
    return redirect('/Impressoras')


def edicaoImpressora(request, ident):
    printers = Impressoras.objects.get(ident=ident)
    return render(request, "edicaoImpressora.html", {"printers": printers})
    

def editarImpressora(request, ident):
    
    printers = Impressoras.objects.get(ident=ident)
    
    printers.nome = request.POST['txtNome']
    printers.modelo = request.POST['txtmodelo']
    printers.cupsid = request.POST['txtcups']
    printers.setor = request.POST['txtsetor'] 
    printers.save()
    return redirect('/Impressoras')  


def deletarImpressora(resquest, ident):
    printers = Impressoras.objects.get(ident=ident)
    printers.delete()
    return redirect('/Impressoras')




   #session class Telefones

def telefones(request):
    tel = Telefones.objects.all()
    return render(request, "GestaoTelefones.html", {"ListarAtivos": tel})


def registrarTelefone(request):
    marca = request.POST['txtmarca']
    modelo = request.POST['txtmodelo']
    ramal = request.POST['txtramal']
    setor = request.POST['txtsetor']
    
    tel = Telefones.objects.create(marca=marca, modelo=modelo, ramal=ramal, setor=setor)
    return redirect('/Telefones')


def edicaoTelefone(request, identel):
    tel = Telefones.objects.get(identel=identel)
    return render(request, "edicaoTelefone.html", {"tel": tel})
    

def editarTelefone(request, identel):
    
    tel = Telefones.objects.get(identel=identel)
    
    tel.marca = request.POST['txtmarca']
    tel.modelo = request.POST['txtmodelo']
    tel.ramal = request.POST['txtramal']
    tel.setor = request.POST['txtsetor'] 
    tel.save()
    return redirect('/Telefones')  


def deletarTelefone(resquest, identel):
    tel = Telefones.objects.get(identel=identel)
    tel.delete()
    return redirect('/Telefones')
