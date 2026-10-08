# Guía para Claude: despiece de cocinas y muebles

Idioma de la interfaz y de los textos: español. Unidades: centímetros (los grosores del usuario van en mm).

## Estructura

Todo está en `index.html` (HTML + CSS + un `<script>` al final). three.js r128 se carga desde cdnjs. No hay build.

## Modelo de datos

- `S`: ajustes del proyecto activo: `t` grosor (cm), `sh` lámina "ancho x largo", `k` corte, `rot` permitir girar piezas, `ce` techo, `rl` largo de pared del fondo, `ra` ancho de paredes laterales, `gp` luz entre frentes, `sc` espacio de corredera por lado.
- `projects[]` -> cada uno `{name,S,places[3],cur}`; `places[i]` -> `{name,mods[],els[]}`.
- `mods` es el arreglo del lugar activo. Un módulo: `{ty,w,h,d,n,dr,doors,wl,up,dy,gl,go,led,lo,ov,mw,ac}`.
  - `ty`: base, wall, tall, libre, gav, vit, desp, horno, sobre, flot (catálogo `DEF`, nombres `NM`).
  - `wl`: pared f (fondo), l (izquierda), r (derecha). `up`: 0 abajo, 1 arriba, 2 tercer nivel. `dy`: ajuste de altura en cm.
  - `ac`: accesorios (`ACC`). Elementos del espacio: `ELD` y `EL()`.
- Persistencia: `localStorage['despiece']` con `{projects,pj}` (`save()`, `load()`, `stash()`, `openP()`).

## Funciones clave

- `parts(m)`: piezas de un módulo (`n,q,l,a,g,c`). `g` es grosor (número), `'v'` vidrio; `c` es canto en cm por pieza. Devuelve el arreglo con extras (`bis,alu,doors,sop,sl`).
- `pack()`: acomodo en láminas por filas. `calc()`: recalcula todo (tabla, láminas, tapacanto, herrajes, avisos) y redibuja el 3D.
- `layout()`: cajas en el espacio (posición de cada módulo por pared y nivel).
- 3D: `initGL`, `drawGL`, `viewGL`, `buildMod`, `buildEl`. Hay un dibujo 2D de respaldo (`draw3dCore`) si no hay WebGL.
- Abrir y cerrar: `OP`, `unit`, `toggleUnit`, `toggleKind`, `toggleOpen`, `setOp`, `tick`. Cada puerta (`pv`) y cada cajón (`dw`) tiene su estado.
- Propuestas con foto: usan `claude.use('sample')`, que solo existe dentro de claude.ai. Debe fallar con elegancia fuera de Claude.

## Reglas al modificar

1. Antes de agregar algo, busca con grep si ya existe (funciones, ids, estilos). Evita duplicar ids de HTML.
2. Mantén un solo `<script src>` de three.js y con versión fija.
3. Cualquier valor que cambie el despiece debe reflejarse también en el 3D (usa `S.gp`, `S.sc`, `S.t`, no constantes).
4. Después de cada cambio ejecuta `python3 check.py`.
5. Textos de interfaz en español, sin jerga técnica.
