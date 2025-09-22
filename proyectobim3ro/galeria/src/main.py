import flet as ft


def main(page: ft.Page):
    page.title = "Anime"
    page.bgcolor = ft.Colors.GREEN_800

    animes = [
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año":  1997,
            "descripcion": "One Piece es un manga y anime sobre Monkey D. Luffy, un joven que, tras comer una fruta que le dio el poder de un cuerpo de goma, sueña con convertirse en el Rey de los Piratas",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/One_Piece_Logo.png",

        }, 
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año": 1997,
            "descripcion": "Inicio de las aventuras de los sombrero de paja como Monkey D. luffy como su capitan y los primeros compañeros que tendra",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/One-Piece2.jpg",
        },
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año": 1997,
            "descripcion": "Este es un gran capitulo emotivo donde un gran miembro de la tripulacion muere el barco de la tripulacion Going Merry, despues de llevarlos tan lejos en las aventuras no puede seguir mas lejos por falta de arreglos teniendo que deshacerse de el de la mejor manera",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/onepiece4.jpg",
        },
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año": 1997,
            "descripcion": "Despues de vivir un suceso traumatico para los sombrero de paja teniendo que separarse en distintas ilas y su capitan luffy  sufriendo lo peor, deicido decirle a sus compañeros que despues de 2 años estar entrenando vuelvan a reencontrarse en la isla donde ocurrio todo",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/one%20piece3.jpg",
        },
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año": 1997,
            "descripcion": "Despues de distintas aventuras llegan a poder ayudar a su nuevo compañero Jimbe que esta bajo el mando de un yonkou( son los cuatro capitanes piratas más poderosos y temidos del mundo de One Piece), ayudanlo haciendo que deje de estar en la tripulacion de uno y asi poder unirse oficialmente con los sombrero de paja",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/ONE_PIECE_5.jpg",
        },
        {
            "titulo": "One Piece",
            "autor": "Eiichiro Oda",
            "año": 1997,
            "descripcion": "Tras viajar por distintas islas llegan a una donde esta el mayor genio del mundo EL DOCTOR VEGAPUNK en la isl EGG HEAD donde tendra mas sucesos importantes",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/onepiece.jpg",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012, 
            "descripcion": "es un anime sobre Shigeo Kageyama, un adolescente con inmensos poderes psíquicos al que apodan Mob por su personalidad discreta y falta de presencia",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/mob%20psycho%206.png",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012,
            "descripcion": "Se nos muestra a nuestro protagonista Shigeo Kageyama(Mob), un niño de secundaria que intenta controlar sus emociones para que sus poderes psiquicos no se lleguen a descontrolar, para esto trabaja con un psiquico al que le dice Maestro el cual Mob no sabe que es un estafador que en realidad no tiene poderes utilizando a Mob",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/mosaico3.jpg",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012,
            "descripcion": "En este episodio se muestra el origen de como conocio Mob a su Maestro diciendo cuanto a crecido como persona sabiendo que a aprendido a controlar sus emociones llegando a no deprimirlas como antes",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/mosaico.jpg",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012,
            "descripcion": "Mob despues de no derrotar a un jefe de una gran empresa que crea psiquicos artificiales destruye toda la zona donde vive Mob, el cual este va a enfrentrarlo pero al no poder y provocar una gran explosion junto al jefe se queda con el dandole la mejor reflexion de su vida'Cada uno es el protagonista de su propia vida'",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/Mob-Psycho-5.jpg",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012,
            "descripcion": "Mob logra controlar sus poderes llendo a por fin declararse a la chica que le a gustado desde pequeño llevandole un ramo de flores sin saber el problema que tendra por un hacer un buen acto",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/mob-psycho-4.jpg",
        },
        {
            "titulo": "Mob Psycho 100",
            "autor": "Tomohiro O mejor conocido por su alias ONE",
            "año": 2012,
            "descripcion": "Al final cuando Mob logra controlar sus emociones sin necesidad de comprimirlas o esconderlas logra controlar sus poderes y poder conseguir personas que en realidad lo apoyen y ayuden en su vida",
            "imagen": "https://raw.githubusercontent.com/Leonex657/proyectobimestral1periodo/refs/heads/main/mob-psycho2.jpg",
        },
    ]

    indice_actual=[0]

    contenedor = ft.Container(
        content=ft.Column([]),
        width=500,
        height=600,
        bgcolor=ft.Colors.BLUE_200,
        alignment=ft.alignment.center,
        padding=40
    )

    boton_siguiente=ft.ElevatedButton(text="siguiente pintura")

    def mostrar_anime():
        anime=animes[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=anime["imagen"], width=400, height=300, fit=ft.ImageFit.CONTAIN),
            ft.Text(anime["titulo"], size=20, weight=ft.FontWeight.BOLD, bgcolor=ft.Colors.BLACK),
            ft.Text(f"Autor: {anime['titulo']}", size=16, weight=ft.FontWeight.BOLD,bgcolor=ft.Colors.BLUE_600),
            ft.Text(f"Año: {anime['año']}",size=16, weight=ft.FontWeight.BOLD,bgcolor=ft.Colors.BLUE_600),
            ft.Text(anime["descripcion"], size=14, weight=ft.FontWeight.BOLD,bgcolor=ft.Colors.BLUE_600)
        ], alignment=ft.MainAxisAlignment.CENTER)

        if indice_actual[0]==len(animes)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="siguiente pintura"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(animes)
        mostrar_anime()
    boton_siguiente.on_click=siguiente_click


    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
        ], alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),  
            alignment=ft.alignment.center,
            expand=True
        )
    )
    mostrar_anime()


ft.app(main)