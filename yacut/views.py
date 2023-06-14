import random

from flask import flash, redirect, render_template

from . import app, db
from .constants import S_LENGTH, SYMBOLS
from .forms import URLMap_Form
from .models import URLMap


def get_db_object(column, query):
    """Фильтрация и получение ответа из БД."""
    return URLMap.query.filter(column == query)


def check_short_id(short_id):
    """Проверка уникальности нового адреса."""
    if get_db_object(URLMap.short, short_id).first() is None:
        return True
    return False


def get_unique_short_id():
    """Генерация случайной уникальной последовательности из 6 символов."""
    short_id = ''.join(random.choice(SYMBOLS) for i in range(S_LENGTH))
    if check_short_id(short_id):
        return short_id
    return get_unique_short_id()


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMap_Form()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif not check_short_id(custom_id):
        flash(f'Имя {custom_id} уже занято!', 'link-taken')
        return render_template('index.html', form=form)
    new_url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(new_url)
    db.session.commit()
    return render_template('index.html', url=new_url, form=form)


@app.route('/<short_id>')
def follow_link(short_id):
    db_object = get_db_object(URLMap.short, short_id).first_or_404()
    original_link = db_object.original
    return redirect(original_link)
