quot = 'Летим и замираем перед краем – У пропасти, где не нащупать дна. Нет на земле ни ада и ни рая –  Поэзия и музыка одна.Как жаль, что мы судьбу не выбираем. Как жаль, что выбирает нас она. (Дарья Ильгова)'

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