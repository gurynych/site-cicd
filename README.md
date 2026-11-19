# site-cicd

![Deploy static site](https://github.com/gurynych/site-cicd/actions/workflows/deploy.yml/badge.svg)

Многостраничный сайт антикафе «Ход конём» с автоматическим развёртыванием через GitHub Actions.

Структура проекта:

- templates/base.html – общий шаблон страницы с меню и футером;
- pages – содержимое страниц: главная, игры, тарифы, контакты;
- build.py – скрипт, который собирает готовые страницы в папку _site;
- style.css – стили сайта.

При каждом push в main workflow собирает сайт, проверяет разметку утилитой html-validate и публикует папку _site на GitHub Pages.

Сайт на GitHub Pages: https://gurynych.github.io/site-cicd/

Сайт на Vercel: https://site-cicd-plum.vercel.app/
