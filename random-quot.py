import random

quot_list = [ 
"Летим и замираем перед краем – У пропасти, где не нащупать дна. Нет на земле ни ада и ни рая –  Поэзия и музыка одна. Как жаль, что мы судьбу не выбираем. Как жаль, что выбирает нас она. (Дарья Ильгова)", 
"Люблю, отвергнув крик вокзальный, Забыв о бреднях рядовых, Блуждать по городу печально Маршрутом старых мостовых: Россия в них, как боль, упряма. И я, пройдя свою черту, В брусчатку, лёгшую у храма,  Немым булыжником врасту. (Д.Ханин)", 
"Когда заката пролегла черта, И лес вдали был сумрачным и чёрным, Мы хоронили местноого кота В саду у школы, за цветущим тёрном (Анастасия Кинаш)", 
"и дело не в экономии, хоть это огромный плюс - цыгания и бездомия и хочется, и боюсь (Елена Жамбалова)", 
"Я о прошлом тоскую нередко, А мечты о грядущем скупы — Мне бы стать плодоносною веткой У изгиба тернистой тропы (Дмитрий Ханин «Жердёлы») ", 
"Эта птица пока не поёт И ещё не привыкла ко мне, Но упрям молчаливый полёт И глаза так знакомы в окне (Александр Рухлов «Птица»)", 
"обратно поеду поездом. мне кажется, так честней. я в поезде встречусь с совестью и даже полажу с ней (Е.Жамбалова)", 
"из тонкой прорези шестиугольной крыши. читает мальчик, и закат над нами, и мы молчим своими головами. мы наконец-то ничего не слышим (Е.Жамбалова)", 
"Остаётся так мало… Небо смотрит в окно. Оно тоже устало, Ему тоже темно. (А.Кинаш)", 
"И огибая прохожих, не оставляя тени, Вслух ничего особо не выражая, Жёлтые листья по жёлтому городу разлетелись На осколки разбитыми жёлтыми витражами.(А.Рухлов)"
]

quot = random.choice(quot_list)


def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    text = 'Привет, это навык Цитатник Совета молодых литераторов'
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = quot
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text,
            # Don't finish the session after this response.
            'end_session': 'false'
        },
    }