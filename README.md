# WORD COUNT CLI

Este repositorio contiene el codigo del desafio de programacion de [building-wc](https://codingchallenges.fyi/challenges/challenge-wc/#the-challenge---building-wc).
Mi idea es tomar pequeños desafios e implementarlos con buenas practicas. Y asi poder practicar como desarollar codigo probando nuevas herramientas.

En este repositorio aplique las librerias/ideas:
    - Poetry (para la gestion de paquetes)
    - click (para hacer CLI)
    - pytest (para gestionar las pruebas unitarias)
    - coverage (para revisar la cobertura de los pytest)
    - flake8, black (como linters y mantener una misma estructura del codigo en los diferentes archivos)
    - nox (para automatizar parte de la ejeuccion de los linters las pruebas)
    - pre-commit (para realizar validaciones sobre archivos antes de realizar un nuevo commit)
    - GIT (donde cada paso nuevo en el desarrollo del codigo se tomo como un branch distinta)


## Para ejecutarlo
1. git clone git@github.com:DanielOrtegaCar/cc_word_count_cli.git
2.``` cd cc_word_count_cli```
3. ```poetry install```
4. ```poetry run wc_cli --help: para ver los parametros que se pueden entregar a la funcion```
5. ```poetry run wc_cli <archivo>: para aplicar la funcion sobre el <archivo>```


Para validar realizar validaciones antes de hacer un nuevo commit use:


    ```poetry run pre-commit run --all-files```