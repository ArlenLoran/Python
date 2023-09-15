import time

from flet import *
import requests
import json

cor_botoes = "#F5A71E"

def trocar_cor():
    cor_botoes="#F58501"


#dados={'usuario': 'arlen', 'senha': '123123', 'email': 'arlen.loran@gmail.com'}


#post
#dados={'usuario': 'alon', 'senha': '123123', 'email': 'projetosdhldev@gmail.com'}
#requisicao = requests.post(f'{link}/Cadastro/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

#edit
#dados={'usuario': 'oiiisaidsaidiasidiasidiasi'}
#requisicao = requests.patch(f'{link_banco}/Cadastro/-Ndrx-B1hedr3zVETivZ/.json', data=json.dumps(dados))
#print(requisicao)
#print(requisicao.text)

#get
# Pegar uma venda específico ou todas as vendas (GET)
#requisicao = requests.get(f'{link}/Cadastro/.json')
#print(requisicao)
#requisicao = requisicao.json()
#id_alon = None
#tt = 'usuario'
#for idvenda in requisicao:
#    usuario = requisicao[idvenda]['usuario']
#    if usuario == "alon":
#        print(idvenda)
#        id_alon = idvenda

#delete
#requisicao = requests.delete(f'{link}/Cadastro/{id_alon}/.json')
#print(requisicao)
#print(requisicao.text)

import flet as ft

def main(page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#ffc800"

    def btn_click(e):
        input_email.border_color = "transparent"
        input_usuario.border_color = "transparent"
        input_senha.border_color = "transparent"
        input_confirmar_senha.border_color = "transparent"

        if not input_email.value:
            input_email.border_color = cor_botoes
            input_email.hint_style=TextStyle(color=cor_botoes)
            page.show_snack_bar(
            SnackBar(Text("Digite o email!", size=13, color="white"), open=True,
            action="Ok", action_color="white", bgcolor="#FA2100")
            )
            page.update()
        elif not input_usuario.value:
            input_usuario.border_color = cor_botoes
            input_usuario.hint_style=TextStyle(color=cor_botoes)
            page.show_snack_bar(
            SnackBar(Text("Digite o usuário!", size=13, color="white"), open=True,
            action="Ok", action_color="white", bgcolor="#FA2100")
            )
            page.update()
        elif not input_senha.value:
            input_senha.border_color = cor_botoes
            input_senha.hint_style=TextStyle(color=cor_botoes)
            page.show_snack_bar(
            SnackBar(Text("Digite a senha!", size=13, color="white"), open=True,
            action="Ok", action_color="white", bgcolor="#FA2100")
            )
            page.update()
        elif not input_confirmar_senha.value:
            input_confirmar_senha.border_color = cor_botoes
            input_confirmar_senha.hint_style=TextStyle(color=cor_botoes)
            page.show_snack_bar(
            SnackBar(Text("Digite a confirmação de senha!", size=13, color="white"), open=True,
            action="Ok", action_color="white", bgcolor="#FA2100")
            )
            page.update()
        elif input_senha.value != input_confirmar_senha.value:
            input_senha.border_color = cor_botoes
            input_confirmar_senha.border_color = cor_botoes
            page.show_snack_bar(
            SnackBar(Text("As senhas digitadas não são identicas!", size=13, color="white"), open=True,
            action="Ok", action_color="white", bgcolor="#FA2100")
            )
            page.update()
        else:
            link = "https://bddhlsystem-default-rtdb.firebaseio.com/"
            email = input_email.value
            usuario = input_usuario.value
            senha = input_senha.value
            dados = {f'usuario': f'{usuario}', 'senha': f'{senha}', 'email': f'{email}'}
            requests.post(f'{link}/Cadastro/.json', data=json.dumps(dados))
            print(f"oi: {email},{usuario},{senha}")
            page.show_snack_bar(
                SnackBar(Text("Usuário criado com sucesso!", size=13, color="white"), open=True, action="Ir para login", action_color="white", bgcolor="#35C300")
            )




    input_email = TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color="white",
                        focused_color="white",
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color="White",
                        hint_text="E-mail",
                        hint_style=TextStyle(size=11, color="white"),
                        password=False,
    )

    input_usuario = TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color="white",
                        focused_color="white",
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color="White",
                        hint_text="Usuário",
                        hint_style=TextStyle(size=11, color="white"),
                        password=False,
    )

    input_senha = TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color="white",
                        focused_color="white",
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color="White",
                        hint_text="Senha",
                        hint_style=TextStyle(size=11, color="white"),
                        password=True,
    )

    input_confirmar_senha = TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color="white",
                        focused_color="white",
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color="White",
                        hint_text="Confirme a senha",
                        hint_style=TextStyle(size=11, color="white"),
                        password=True,
    )


    Icon_input_email=Container(
            width=320,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, "White54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.EMAIL_ROUNDED,
                        size=14,
                        opacity=0.85,
                        color="white",
                    ),input_email
    ]))

    Icon_input_usuario=Container(
            width=320,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, "White54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.PERSON_ROUNDED,
                        size=14,
                        opacity=0.85,
                        color="white",
                   ),input_usuario
    ]))

    Icon_input_senha=Container(
            width=320,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, "White54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.LOCK_OUTLINE,
                        size=14,
                        opacity=0.85,
                        color="white",
                    ),input_senha
    ]))

    Icon_input_confirmar_senha=Container(
            width=320,
            height=40,
            border=border.only(bottom=border.BorderSide(0.5, "White54")),
            content=Row(
                spacing=20,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.LOCK_OUTLINE,
                        size=14,
                        opacity=0.85,
                        color="white",
                    ),input_confirmar_senha
    ]))












    page.add(Card(
                width=408,
                height=612,
                elevation=15,
                content=Container(
                        bgcolor='#23262a',
                        border_radius=6,
                        content=Column(
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Divider(height=10, color='transparent'),
                                Row(
                                    width=320,
                                    alignment=MainAxisAlignment.START,
                                    controls=[
                                        Icon(name=ft.icons.ARROW_BACK, color=cor_botoes)]),
                                        Icon(name=icons.SUPERVISED_USER_CIRCLE, color=cor_botoes, size=80),
                                Divider(height=10, color='transparent'),
                                Text("Cadastre-se", size=22, weight='bold', color="white"),
                                Text("Insira as informações para se cadastrar", size=13, color="white"),
                                Divider(height=10, color='transparent'),
                                Icon_input_email,
                                Divider(height=2, color='transparent'),
                                Icon_input_usuario,
                                Divider(height=2, color='transparent'),
                                Icon_input_senha,
                                Divider(height=2, color='transparent'),
                                Icon_input_confirmar_senha,
                                Divider(height=10, color='transparent'),
                                ElevatedButton(content=Text("Cadastre-se", size=13, weight='bold'),
                                                    style=ButtonStyle(
                                                        shape={
                                                            "": RoundedRectangleBorder(radius=8),
                                                        },
                                                        color={
                                                            "": "black",
                                                        },
                                                        bgcolor={"": cor_botoes},
                                                    ),
                                                    height=42,
                                                    width=160,
                                                    on_click=btn_click)]
                        ))))

ft.app(target=main, view=WEB_BROWSER)
