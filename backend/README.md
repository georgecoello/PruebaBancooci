Pasos para la ejecución del backend 
===

1. Ejecutar el entorno virtual
    * source myenv/bin/activate
2. Realizar la migración de la Base de Datos 
    * python manage.py makemigrations 
    * python manage.py migrate
3. Realizar el llenado de la Base de Datos, ejecutando el archivo population.py 
    * python population.py
4. Crear un super usuario en Django para poder visualizar la información llenada en la Base de Datos 
    * python manage.py createsuperuser