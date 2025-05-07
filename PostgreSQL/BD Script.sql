CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT NOW()
);

-- Insertar datos
INSERT INTO usuarios (nombre, correo) VALUES
('Angel Peñarredonda', 'angel.pena@gmail.com'),
('Camilo Romero', 'camilo.romero@gmail.com'),
('Julian Roso', 'julian.roso@gmail.com');

-- Consultar usuarios registrados 
SELECT * FROM usuarios
WHERE fecha_registro >= NOW() - INTERVAL '7 days';