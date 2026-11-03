
import flet as ft

def main(page: ft.Page):
    page.title = "Vehicle Service Management System"
    page.window.width = 400
    page.window.height = 700

    page.add(
        ft.Text(
            "Welcome!",
            size=30,
            weight=ft.FontWeight.BOLD
        ),
        ft.Text(
            "Vehicle Service & Maintenance Management System"
        ),
        ft.Button(
            "Get Started"
        )
    )

ft.run(main)
