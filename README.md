# Mi Blog - Django

Proyecto de blog desarrollado con Django. Incluye plantillas con herencia, rutas organizadas por app, estilos con archivos estáticos, publicaciones con imágenes (CRUD completo), y un sistema de autenticación con registro, login, logout y perfiles de usuario.

## Funcionalidades

- Página de **Inicio** con portada de bienvenida y las últimas 3 publicaciones.
- Página de **Publicaciones** con el listado dinámico de los posts publicados, del más reciente al más antiguo.
- Página **Acerca de** con la reseña del autor y el propósito del sitio.
- Menú de navegación compartido mediante `base.html`, con la página actual resaltada y opciones distintas según el usuario esté autenticado o no.
- **CRUD de posts** con imágenes (crear, editar y eliminar solo para usuarios autenticados).
- **Registro, inicio y cierre de sesión** de usuarios.
- **Perfil de usuario** con biografía, sitio web y avatar.
- **Panel de administración** para crear, editar, filtrar y buscar publicaciones y perfiles.
- Estilos CSS cargados desde la carpeta `static`.

## Cambios recientes

### Modelo `Post` y base de datos
- Nuevo modelo `Post` en `posts/models.py` con los campos `titulo`, `contenido`, `autor`, `fecha_creacion` (`auto_now_add=True`) y `estado`.
- El campo `estado` usa `choices`: **Borrador**, **Publicado** y **Archivado**.
- El método `__str__` devuelve el título del post.
- Migración inicial `0001_initial` generada y aplicada.

### Panel de administración
- Modelo `Post` registrado con una clase `PostAdmin`.
- Columnas visibles: título, autor, estado y fecha de creación.
- Filtros por estado y fecha, búsqueda por título, contenido y autor, y edición rápida del estado desde el listado.

### Vistas y plantillas
- La view `lista_posts` consulta los posts con el ORM:
  `Post.objects.filter(estado="publicado").order_by("-fecha_creacion")`.
- La view `inicio` envía al template las últimas 3 publicaciones.
- Las plantillas recorren los posts con `{% for post in posts %}` y muestran título, autor, fecha y contenido.
- Mensaje de aviso cuando todavía no hay publicaciones (`{% empty %}`).

### Rediseño visual
- Nueva portada con título destacado y botón de acción.
- Publicaciones presentadas con la fecha destacada.
- Paleta de colores definida con variables CSS en `:root` para cambiarla fácilmente.
- Tipografías de Google Fonts: Bricolage Grotesque (títulos) y Source Serif 4 (texto), con fuentes de respaldo.
- Diseño responsive, enlace para saltar al contenido y foco visible para navegación con teclado.

## Tecnologías

- Python
- Django 6.1
- SQLite
- Pillow (manejo de imágenes)
- HTML5 y CSS3

## Estructura principal

```
blog_django2/
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
├── blog_project2/            # Configuración del proyecto
│   ├── settings.py
│   └── urls.py
├── media/                    # Archivos subidos por los usuarios
│   ├── posts/
