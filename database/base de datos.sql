CREATE DATABASE sara;
USE sara;

CREATE TABLE usuarios(
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100),
correo VARCHAR(100),
password VARCHAR(255),
rol ENUM('Administrador','Docente')
);

CREATE TABLE carreras(
id_carrera INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100)
);

CREATE TABLE grupos(
id_grupo INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(20),
id_carrera INT,
FOREIGN KEY(id_carrera)
REFERENCES carreras(id_carrera)
);

CREATE TABLE alumnos(
id_alumno INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100),
apellido VARCHAR(100),
matricula VARCHAR(20),
correo VARCHAR(100),
id_grupo INT,
FOREIGN KEY(id_grupo)
REFERENCES grupos(id_grupo)
);

CREATE TABLE materias(
id_materia INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100)
);

CREATE TABLE calificaciones(
id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
id_alumno INT,
id_materia INT,
calificacion DECIMAL(4,2),
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno),
FOREIGN KEY(id_materia)
REFERENCES materias(id_materia)
);

CREATE TABLE asistencia(
id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
id_alumno INT,
porcentaje DECIMAL(5,2),
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno)
);

CREATE TABLE alertas(
id_alerta INT AUTO_INCREMENT PRIMARY KEY,
id_alumno INT,
nivel VARCHAR(20),
probabilidad DECIMAL(5,2),
fecha DATE,
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno)
);

CREATE TABLE comentarios(
id_comentario INT AUTO_INCREMENT PRIMARY KEY,
id_alumno INT,
comentario TEXT,
fecha DATE,
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno)
);

CREATE TABLE intervenciones(
id_intervencion INT AUTO_INCREMENT PRIMARY KEY,
id_alumno INT,
accion TEXT,
estatus VARCHAR(30),
fecha DATE,
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno)
);
