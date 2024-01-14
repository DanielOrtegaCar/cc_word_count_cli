# WORD COUNT CLI

Este repositorio contiene el código del desafío de programación [building-wc](https://codingchallenges.fyi/challenges/challenge-wc/#the-challenge---building-wc).
 Mi idea es tomar pequeños desafíos e implementarlos con buenas prácticas, practicando el desarrollo de código y probando nuevas herramientas.

En este repositorio apliqué las librerías/ideas:
* Poetry (para la gestión de paquetes)
* Click (para crear CLI)
* Pytest (para gestionar las pruebas unitarias)
* Coverage (para revisar la cobertura de las pruebas de Pytest)
* Flake8, Black (como linters y para mantener una misma estructura de código en los diferentes archivos)
* Nox (para automatizar parte de la ejecución de los linters y las pruebas)
* Pre-commit (para realizar validaciones sobre archivos antes de realizar un nuevo commit)
* GIT (donde cada nuevo paso en el desarrollo del código se tomó como una rama distinta)


## Para ejecutarlo
1. git clone git@github.com:DanielOrtegaCar/cc_word_count_cli.git
2.``` cd cc_word_count_cli```
3. ```poetry install```
4. ```poetry run wc_cli --help:``` para ver los parámetros que se pueden entregar a la función
5. ```poetry run wc_cli <archivo>:``` para aplicar la funcion sobre el <archivo>


Para validar realizar validaciones antes de hacer un nuevo commit use:


    ```poetry run pre-commit run --all-files```
