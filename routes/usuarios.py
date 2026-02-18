from flask import Blueprint, render_template
from database.usuarios import USUARIOS 

usuarios_route = Blueprint('usuarios', __name__)


#rotas de usuarios
#usuarios/[GET] - listar usuarios
#usuarios/[POST] - inserir usuarios no BD
#usuarios/new[get] - rederizar o formulario para criar um novo usuarios
#usuarios/<id>[get] - obter dados dos usuarios
#usuarios/<id>/editar[GET] - editar usuarios
#usuarios/<id>/update[PUT] - atualizar dados do usuario
#usuarios/<id>/delete[DELETE] - deletar dados do usuarios

