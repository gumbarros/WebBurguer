from django.contrib import admin
from .models import BurguerUser, Franquia, Franqueada, Contrato, Produto, PedidoProduto, Pedido
# Register your models here.

admin.site.register(BurguerUser)
admin.site.register(Franquia)
admin.site.register(Franqueada)
admin.site.register(Contrato)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(PedidoProduto)