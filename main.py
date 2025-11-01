import flet as ft

def main(page: ft.Page):
    page.title = "Interface Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt = ft.TextField(label="Digite algo")
    result = ft.Text("")

    def send(e):
        result.value = f"Você digitou: {txt.value}"
        page.update()

    btn = ft.ElevatedButton("Enviar", on_click=send)
    page.add(txt, btn, result)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
