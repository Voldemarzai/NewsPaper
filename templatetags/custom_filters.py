from django import template

register = template.Library()

# Список запрещённых слов
BAD_WORDS = ['редиска', 'нехороший', 'плохой']


@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError(f"Фильтр 'censor' можно применять только к строкам, получен: {type(value)}")

    # Обрабатывать все формы запрета: целиком и в составе слов
    for bad_word in BAD_WORDS:
        lower_bad_word = bad_word.lower()
        value = value.lower().replace(lower_bad_word, '*' * len(lower_bad_word))

    return value