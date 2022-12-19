from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login, name='login'),
    
    path('Start/', views.Start),  # Rotas homepage e estações de trabalho
    path('Estacao/',views.home),
    path('registrarEstacao/', views.registrarEstacao),
    path('Estacao/edicaoEstacao/<identificador>', views.edicaoEstacao),
    path('editarEstacao/<int:identificador>', views.editarEstacao),
    path('Estacao/deletarEstacao/<identificador>', views.deletarEstacao),

    path('Impressoras/', views.printer),   # Rotas impressoras
    path('resgistrarImpressora/', views.registrarImpressora),
    path('Impressoras/edicaoImpressora/<ident>', views.edicaoImpressora),
    path('editarImpressora/<int:ident>', views.editarImpressora),
    path('Impressoras/deletarImpressora/<ident>', views.deletarImpressora),

    path('Telefones/', views.telefones),   # Rotas Telefones
    path('resgistrarTelefone/', views.registrarTelefone),
    path('Telefones/edicaoTelefone/<identel>', views.edicaoTelefone),
    path('editarTelefone/<int:identel>', views.editarTelefone),
    path('Telefones/deletarTelefone/<identel>', views.deletarTelefone),

    
    
]