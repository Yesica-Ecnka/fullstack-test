---

### 1. ¿Qué framework/librería elegiste y por qué?

**Backend:** FastAPI  
Lo elegí porque es moderno, rápido y fácil de desarrollar APIs REST. Además, incluye documentación automática con Swagger, lo que facilita pruebas.

**Base de datos:** SQLite  
La elegí por su simplicidad y facilidad de integración en proyectos pequeños o pruebas técnicas, ya que no requiere instalación adicional.

**Frontend:** React con Vite  
React es muy usado en la industria y Vite permite crear proyectos rápidos y ligeros, ideal para pruebas técnicas con tiempo limitado.

---

### 2. ¿Qué arquitectura usaste en el backend y por qué?

Usé una arquitectura por capas (tipo modular):

- routes → endpoints
- schemas → validaciones (Pydantic)
- models → base de datos
- core → seguridad y utilidades
- db → configuración de la base de datos

La elegí porque facilita el mantenimiento, separa responsabilidades y sigue buenas prácticas usadas en proyectos reales.

---

### 3. ¿Qué fue lo más complicado de implementar?

Lo más complejo fue:

- Configurar la autenticación con JWT
- Integrar correctamente la base de datos con SQLAlchemy
- Resolver problemas de configuración del entorno (dependencias, rutas, imports)

Especialmente la conexión entre frontend y backend con CORS y tokens.

---

### 4. ¿Qué mejorarías con más tiempo?

Con más tiempo mejoraría:

- Validaciones más robustas en frontend
- Manejo global de errores
- Sistema de roles (admin/user)
- Tests unitarios
- Dockerización del proyecto
- Mejor UI/UX en el frontend

También implementaría refresh tokens y despliegue en la nube.

---

## Funcionalidades adicionales

Durante el desarrollo agregué:

- Autenticación con JWT
- Protección de rutas
- Arquitectura modular en backend
