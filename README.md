# SARA: Sistema de Alerta para el Rendimiento Académico[cite: 1]

<div align="center">
  <i>Proyecto desarrollado por el equipo de SparkData</i>[cite: 1]
</div>

## 📌 Descripción del Proyecto[cite: 1]
SARA es una herramienta de análisis académico y modelado predictivo diseñada para procesar información educativa y monitorear el desempeño estudiantil[cite: 1]. El sistema permite identificar patrones asociados a dificultades de aprendizaje, detectando oportunamente el riesgo de bajo rendimiento o abandono escolar[cite: 1]. Mediante la generación de reportes y visualizaciones, SARA proporciona a los docentes la información necesaria para aplicar estrategias de intervención efectivas y fomentar la retención académica[cite: 1].

## ⚙️ Metodología[cite: 1]
El desarrollo de este sistema se basa en la metodología CRISP-DM (Cross Industry Standard Process for Data Mining)[cite: 1]. Este estándar estructurado abarca las siguientes fases para asegurar la confiabilidad del modelo predictivo[cite: 1]:
*   Comprensión del problema[cite: 1].
*   Comprensión de los datos[cite: 1].
*   Preparación de los datos[cite: 1].
*   Modelado[cite: 1].
*   Evaluación[cite: 1].
*   Implementación[cite: 1].

## 🏗️ Arquitectura del Sistema[cite: 1]
SARA opera a través de múltiples módulos integrados[cite: 1]:
*   **Módulo de integración de datos:** Obtiene información sobre actividades, tareas y calificaciones mediante conexión con Google Classroom, además de integrar el control de asistencia institucional[cite: 1].
*   **Gestión de base de datos:** Administra de forma estructurada en SQL el historial académico de los estudiantes, clases y entregas[cite: 1].
*   **Análisis Predictivo:** Utiliza un modelo de clasificación binaria mediante una función sigmoide para evaluar el promedio, la asistencia y las tareas entregadas, calculando probabilísticamente el nivel de riesgo de cada estudiante[cite: 1].
*   **Módulo de visualización:** Proporciona un Dashboard interactivo que muestra alumnos en riesgo, promedios generales e historiales académicos[cite: 1].
*   **Módulo de intervención:** Genera sugerencias de apoyo y registra una bitácora del cumplimiento de las acciones por parte del docente[cite: 1].

## 💻 Tecnologías y Herramientas[cite: 1]
*   **Lenguajes:** Python, SQL, HTML, CSS, JavaScript[cite: 1].
*   **Bases de Datos:** MySQL (MySQL Workbench)[cite: 1].
*   **Análisis de Datos y Machine Learning:** Pandas, NumPy, Matplotlib, Scikit-Learn[cite: 1].
*   **Entornos de Desarrollo:** Visual Studio Code, Jupyter Notebook[cite: 1].

## 🗄️ Estructura de la Base de Datos Relacional[cite: 1]
El sistema se sostiene en un diagrama Entidad-Relación que conecta de manera eficiente las interacciones académicas[cite: 1]. Las entidades principales incluyen[cite: 1]:
*   `DOCENTE` y `ALUMNO`[cite: 1].
*   `CLASE`, `TAREA`, `ENTREGA` e `INSCRIPCION`[cite: 1].
*   `ALERTA_RIESGO` e `INTERVENCION`[cite: 1].

## 👥 Equipo SparkData[cite: 1]
*   Avila Martinez Thelma Getzemani[cite: 1]
*   Coronel Olvera Frida Sofia[cite: 1]
*   Loredo Villanueva Paola Jocelyn[cite: 1]
*   Olalde Campos Schoenstatt[cite: 1]
*   Perez Mendoza Roxana[cite: 1]