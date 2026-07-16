# SARA: Sistema de Alerta para el Rendimiento Académico

<div align="center">
  <i>Proyecto desarrollado por el equipo de SparkData</i>
</div>

## 📌 Descripción del Proyecto
SARA es una herramienta de análisis académico y modelado predictivo diseñada para procesar información educativa y monitorear el desempeño estudiantil. El sistema permite identificar patrones asociados a dificultades de aprendizaje, detectando oportunamente el riesgo de bajo rendimiento o abandono escolar. Mediante la generación de reportes y visualizaciones, SARA proporciona a los docentes la información necesaria para aplicar estrategias de intervención efectivas y fomentar la retención académica.

## ⚙️ Metodología
El desarrollo de este sistema se basa en la metodología CRISP-DM (Cross Industry Standard Process for Data Mining). Este estándar estructurado abarca las siguientes fases para asegurar la confiabilidad del modelo predictivo:
*   Comprensión del problema.
*   Comprensión de los datos.
*   Preparación de los datos.
*   Modelado.
*   Evaluación.
*   Implementación.

## 🏗️ Arquitectura del Sistema
SARA opera a través de múltiples módulos integrados:
*   **Módulo de integración de datos:** Obtiene información sobre actividades, tareas y calificaciones mediante conexión con Google Classroom, además de integrar el control de asistencia institucional.
*   **Gestión de base de datos:** Administra de forma estructurada en SQL el historial académico de los estudiantes, clases y entregas.
*   **Análisis Predictivo:** Utiliza un modelo de clasificación binaria mediante una función sigmoide para evaluar el promedio, la asistencia y las tareas entregadas, calculando probabilísticamente el nivel de riesgo de cada estudiante.
*   **Módulo de visualización:** Proporciona un Dashboard interactivo que muestra alumnos en riesgo, promedios generales e historiales académicos.
*   **Módulo de intervención:** Genera sugerencias de apoyo y registra una bitácora del cumplimiento de las acciones por parte del docente.

## 💻 Tecnologías y Herramientas
*   **Lenguajes:** Python, SQL, HTML, CSS, JavaScript.
*   **Bases de Datos:** MySQL (MySQL Workbench).
*   **Análisis de Datos y Machine Learning:** Pandas, NumPy, Matplotlib, Scikit-Learn.
*   **Entornos de Desarrollo:** Visual Studio Code, Jupyter Notebook.

## 🗄️ Estructura de la Base de Datos Relacional
El sistema se sostiene en un diagrama Entidad-Relación que conecta de manera eficiente las interacciones académicas. Las entidades principales incluyen:
*   `DOCENTE` y `ALUMNO`.
*   `CLASE`, `TAREA`, `ENTREGA` e `INSCRIPCION`.
*   `ALERTA_RIESGO` e `INTERVENCION`.

## 👥 Equipo SparkData
*   Avila Martinez Thelma Getzemani
*   Coronel Olvera Frida Sofia
*   Loredo Villanueva Paola Jocelyn
*   Olalde Campos Schoenstatt
*   Perez Mendoza Roxana