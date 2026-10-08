# Despiece de cocinas y muebles

App web (un solo archivo, `index.html`) para diseñar cocinas y muebles de melamina por módulos y obtener:

- Lista de piezas (despiece) con medidas exactas según el grosor de melamina.
- Distribución de las piezas en láminas de corte, con merma y veta.
- Tapacanto necesario, herrajes, correderas, vidrio y perfiles.
- Vista 3D realista (arrastrar para girar, tocar para editar, abrir y cerrar puertas y cajones).
- Varios proyectos, hasta 3 lugares por proyecto, medidas de la habitación y elementos (ventana, refrigerador, estufa, etc.).

Los datos se guardan en el navegador (localStorage), por dispositivo.

## Correrla en tu computadora

Abre `index.html` en el navegador. Necesita internet solo para cargar three.js desde cdnjs.

Si prefieres un servidor local: `python3 -m http.server 8000` y abre http://localhost:8000

## Publicarla con GitHub Pages

1. Crea un repositorio en github.com y sube estos archivos (Add file > Upload files).
2. En el repositorio: Settings > Pages > Source: "Deploy from a branch" > rama `main`, carpeta `/ (root)` > Save.
3. Después de uno o dos minutos tendrás el enlace: `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`

## Limitación: propuestas con foto

La sección "Propuestas con foto" usa Claude desde dentro de claude.ai (función solo disponible cuando la página se abre como artefacto). Fuera de Claude, esa sección muestra un aviso y el resto de la app funciona igual.

## Modificarla con Claude

Lee `CLAUDE.md`: explica cómo está organizado el código y qué revisar después de cada cambio.

- **Claude Code en la web** (claude.ai/code): conecta tu cuenta de GitHub, elige este repositorio y pide los cambios; Claude propone los cambios en una rama para que los revises.
- **Claude Code en tu computadora:** clona el repositorio, abre la carpeta en la terminal y ejecuta `claude`.

Después de cada cambio ejecuta `python3 check.py` (necesita Node.js) para detectar errores de sintaxis o identificadores repetidos.
