# Сборка сайта: содержимое каждой страницы из папки pages
# вставляется в общий шаблон templates/base.html,
# готовые страницы записываются в папку _site
import os
import shutil

PAGES = [
    ("index.html", "Главная"),
    ("games.html", "Игры"),
    ("prices.html", "Тарифы"),
    ("contacts.html", "Контакты"),
]


def build_menu(current):
    items = []
    for file_name, title in PAGES:
        if file_name == current:
            items.append(f'<a href="{file_name}" class="active">{title}</a>')
        else:
            items.append(f'<a href="{file_name}">{title}</a>')
    return "\n      ".join(items)


def main():
    with open("templates/base.html", encoding="utf-8") as f:
        template = f.read()
    os.makedirs("_site", exist_ok=True)
    for file_name, title in PAGES:
        with open(os.path.join("pages", file_name), encoding="utf-8") as f:
            content = f.read().rstrip("\n")
        page = template.replace("{{ title }}", title)
        page = page.replace("{{ menu }}", build_menu(file_name))
        page = page.replace("{{ content }}", content)
        with open(os.path.join("_site", file_name), "w", encoding="utf-8") as f:
            f.write(page)
        print("Собрана страница", file_name)
    shutil.copy("style.css", os.path.join("_site", "style.css"))


if __name__ == "__main__":
    main()
