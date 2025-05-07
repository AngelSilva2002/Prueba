import os
from datetime import datetime

#Crear la carpeta reportes si no existe
report_folder = 'reportes'
os.makedirs(report_folder, exist_ok=True)


#variables para crear el archivo de reporte
fecha_actual = datetime.now().strftime('%Y%m%d')
report_filename = f'reporte_{fecha_actual}.txt'
report_path = os.path.join(report_folder, report_filename)

#Se crea un arreglo para guardar los archivos .txt que se encuentren en la carpeta del script 
txt_files = []
for f in os.listdir('.'):
    if f.endswith('.txt'):
        txt_files.append(f)

#Se crea el report_file en la dirección dentro de /reportes
with open(report_path, 'w', encoding='utf-8') as report_file:

    #si txt_files existe
    if txt_files:
        total = 0

        #Encabezado
        report_file.write('===============================\n')
        report_file.write('  REPORTE DE ARCHIVOS DE TEXTO\n')
        report_file.write(f'  Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        report_file.write('===============================\n\n')

        #Columnas
        report_file.write(f'{"Nombre del archivo":<30} {"Líneas":>10}\n')
        report_file.write('-' * 42 + '\n')

        #se recorre cada archivo para extraer su nombre y la cantidad de lineas
        for txt in txt_files:
            try:
                with open(txt, 'r', encoding='utf-8') as f:
                    line_count = len(f.readlines())
                
                #escribe el nombre del archivo y las lineas que tiene
                report_file.write(f'{txt:<30} {line_count:>10}\n')
                total += 1
            except Exception as e:
                report_file.write(f'{txt:<30} Error al leer archivo\n')

        report_file.write('\n' + '-' * 42 + '\n')
        report_file.write(f'{"Total de archivos procesados:":<30} {total:>10}\n')
    else:
        report_file.write('No se encontraron archivos de texto.\n')

print(f'Reporte generado en: {report_path}')
