# Documentación del Módulo de Estudiantes

## Objetivo del módulo
El módulo de estudiantes tiene como propósito principal gestionar toda la información relacionada con los alumnos de la institución. Este módulo permite registrar, consultar, modificar y eliminar datos de los estudiantes, así como administrar su inscripción en cursos, asignaturas o programas académicos. Además, facilita el seguimiento del rendimiento académico y la generación de reportes.

## Datos que maneja
El módulo gestiona los siguientes datos de cada estudiante:

- **Identificación personal**: Nombres, apellidos, número de documento de identidad, fecha de nacimiento, género, nacionalidad.
- **Información de contacto**: Dirección, teléfono, correo electrónico, contacto de emergencia.
- **Datos académicos**: Matrícula (número de registro), fecha de ingreso, carrera o programa, año y semestre actual, estado (activo, egresado, retirado, etc.).
- **Historial académico**: Asignaturas cursadas, calificaciones, promedio acumulado, créditos aprobados, situación académica (regular, condicional, etc.).
- **Inscripciones**: Cursos o asignaturas en las que está inscrito en el período vigente, fechas de inscripción.
- **Documentación adicional**: Certificados, constancias, fotografía, documentos legales (si aplica).

## Funciones principales

### 1. Registro de estudiantes
Permite dar de alta a un nuevo estudiante en el sistema. Se ingresan todos los datos personales y académicos iniciales. El sistema genera un número de matrícula único y asigna el estado "activo" por defecto.

### 2. Consulta de estudiantes
Proporciona diferentes criterios de búsqueda para localizar a uno o varios estudiantes:
- Por número de matrícula.
- Por nombre y apellidos.
- Por documento de identidad.
- Por programa o carrera.
- Por estado académico.
- Por rango de fechas de ingreso.

Los resultados se muestran en una lista resumida, y al seleccionar un estudiante se puede ver su ficha completa con todos sus datos.

### 3. Actualización de datos
Permite modificar la información de un estudiante existente, ya sea datos personales (dirección, teléfono, correo), datos académicos (cambio de carrera, estado) o información de contacto de emergencia. También permite actualizar la situación académica al finalizar cada período.

### 4. Eliminación (baja) de estudiantes
Ofrece la opción de dar de baja a un estudiante (por ejemplo, por retiro voluntario, expulsión o egreso). Esta acción puede ser lógica (cambiar el estado a "inactivo" o "egresado") o física (eliminar el registro de la base de datos), según la política de la institución. Generalmente se prefiere la baja lógica para conservar el historial.

### 5. Gestión de inscripciones a cursos
Permite inscribir a un estudiante en una o varias asignaturas para un período académico determinado. Verifica que cumpla con los requisitos previos (correquisitos, prerrequisitos, cupos disponibles) y actualiza su carga académica.

### 6. Cálculo y actualización de promedio
Con base en las calificaciones ingresadas, el módulo calcula automáticamente el promedio acumulado del estudiante y actualiza su situación académica (por ejemplo, si está en riesgo académico).

### 7. Generación de reportes
Permite generar distintos tipos de reportes:
- Listado de estudiantes por programa, estado o período.
- Historial académico completo de un estudiante.
- Constancias de estudio.
- Reporte de rendimiento académico (promedios, aprobados/reprobados).
- Estadísticas generales (cantidad de estudiantes por carrera, por género, etc.).

### 8. Exportación de datos
Permite exportar la información de estudiantes (total o filtrada) a formatos como Excel, CSV o PDF para su uso externo o para impresión.

## Consideraciones técnicas
- El módulo debe garantizar la integridad de los datos, validando campos obligatorios, formatos de correo y teléfono, y evitando duplicados de documento de identidad.
- Debe contar con control de acceso (permisos) para que solo usuarios autorizados puedan realizar operaciones de escritura (registro, modificación, eliminación).
- Se recomienda mantener un historial de cambios (auditoría) para rastrear quién y cuándo modificó los datos de un estudiante.

---
