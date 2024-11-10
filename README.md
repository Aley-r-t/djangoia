# Proyecto Django con Pipeline CI/CD de Jenkins

## Descripción
Este es un proyecto de aplicación web Django en desarrollo, configurado para la integración CI/CD con Jenkins. El objetivo de este proyecto es crear un flujo de trabajo de integración continua y despliegue continuo (CI/CD) que automatice las pruebas y el despliegue de la aplicación Django. Este proyecto se encuentra actualmente en fase de desarrollo, y se está mejorando continuamente para implementar nuevas características y optimizar su funcionalidad.

## Requisitos
- **Python 3.x**: El proyecto está desarrollado usando Python 3. Asegúrese de que esté instalado en su máquina local.
- **Entorno Virtual**: `.venv` o **Conda** (recomendado para usuarios de Windows).
- **Jenkins**: Jenkins se utiliza para crear un pipeline de CI/CD para el proyecto. Asegúrese de que Jenkins esté instalado y configurado correctamente.
- **Git**: El proyecto requiere Git para el control de versiones.
- **Dependencias**: Todas las dependencias del proyecto se encuentran en `requirements.txt`.

## Configuración del Proyecto
### Clonar el Repositorio
Clone el repositorio desde GitHub usando el siguiente comando:
```sh
$ git clone <repository_url>
```

### Configuración del Entorno Virtual
Se recomienda usar `.venv` o `conda` para crear un entorno aislado para el proyecto:

#### Opción 1: Usando `.venv`
```sh
$ python -m venv .venv
$ .venv\Scripts\activate  # Para Windows
$ source .venv/bin/activate  # Para Linux/Mac
```

#### Opción 2: Usando Conda (Recomendado para Windows)
```sh
$ conda create --name django_env python=3.x
$ conda activate django_env
```

### Instalar Dependencias
Después de activar el entorno, instale las dependencias necesarias:
```sh
$ pip install -r requirements.txt
```

### Migración de Base de Datos
Ejecute el siguiente comando para migrar la base de datos:
```sh
$ python manage.py migrate
```

### Ejecutar el Servidor de Desarrollo
Para iniciar el servidor de desarrollo, ejecute:
```sh
$ python manage.py runserver
```

## Configuración del Pipeline de Jenkins
### Jenkinsfile
El proyecto incluye un `Jenkinsfile` que define un pipeline de CI/CD para probar y desplegar la aplicación Django. Este archivo incluye las siguientes etapas:
1. **Clonar el Repositorio**: Clonar el repositorio del proyecto desde GitHub.
2. **Instalar Dependencias**: Instalar las dependencias necesarias en un entorno virtual.
3. **Migrar la Base de Datos**: Ejecutar las migraciones para configurar el esquema de la base de datos.
4. **Ejecutar Pruebas**: Ejecutar pruebas unitarias para asegurar que todo funcione correctamente.

### Configuración de Jenkins para CI/CD
- **Crear un Trabajo de Jenkins**: Cree un trabajo de pipeline en Jenkins y apunte al repositorio de este proyecto.
- **Configuración del Pipeline**: Use el `Jenkinsfile` ubicado en la raíz de este proyecto para definir el pipeline de construcción.
- **Entorno de Jenkins**: Asegúrese de que Python y cualquier otra dependencia estén disponibles en el entorno de Jenkins.

## Ejecución del Pipeline
El pipeline de Jenkins definido en este proyecto incluye varias etapas automatizadas que se ejecutarán cada vez que se realicen cambios en el repositorio. Después de configurar el trabajo, cada commit o pull request desencadenará:
- Pruebas automatizadas
- Despliegue (si está configurado)

## Solución de Problemas
- **Problemas con la versión de Python**: Asegúrese de que la versión correcta de Python esté instalada y que el entorno virtual esté activado correctamente.
- **Fallos en el pipeline de Jenkins**: Revise los registros de Jenkins para obtener detalles. Las dependencias faltantes o rutas incorrectas pueden causar problemas.
- **Versión de Java para Jenkins**: Asegúrese de que Jenkins esté utilizando Java 17 si hay plugins relacionados con Android en la construcción.

## Notas
- Este proyecto está configurado para un flujo de trabajo CI/CD en un entorno **AC/DC** (Despliegue Continuo Automático e Integración Continua) utilizando Jenkins.
- Dado que el proyecto está en desarrollo, es posible que se realicen cambios frecuentes en la configuración del pipeline y en la estructura del proyecto.
- Si desea agregar etapas adicionales para el despliegue, siéntase libre de expandir el `Jenkinsfile` según sea necesario.

## Licencia
Este proyecto es de código abierto bajo la licencia MIT.

## Autor
- **Rodrigo** - Configuración inicial y configuración para Django con Jenkins.
