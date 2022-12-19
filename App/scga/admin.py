from django.contrib import admin
from .models import EstacaoTrabalho, Impressoras, Telefones, User

# Register your models here.
admin.site.register(EstacaoTrabalho),
admin.site.register(Impressoras),
admin.site.register(Telefones),
admin.site.register(User)

