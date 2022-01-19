from flask import Flask, request, jsonify
import random

app = Flask(__name__)


quot_list = [
"Летим и замираем перед краем – У пропасти, где не нащупать дна. Нет на земле ни ада и ни рая –  Поэзия и музыка одна. Как жаль, что мы судьбу не выбираем. Как жаль, что выбирает нас она. (Дарья Ильгова)",
"Люблю, отвергнув крик вокзальный, Забыв о бреднях рядовых, Блуждать по городу печально Маршрутом старых мостовых: Россия в них, как боль, упряма. И я, пройдя свою черту, В брусчатку, лёгшую у храма,  Немым булыжником врасту. (Д.Ханин)",
"Когда заката пролегла черта, И лес вдали был сумрачным и чёрным, Мы хоронили местноого кота, В саду у школы, за цветущим тёрном (Анастасия Кинаш)",
"и дело не в экономии, хоть это огромный плюс - цыгания и бездомия и хочется, и боюсь (Елена Жамбалова)",
"Я о прошлом тоскую нередко, А мечты о грядущем скупы — Мне бы стать плодоносною веткой У изгиба тернистой тропы (Дмитрий Ханин «Жердёлы») ",
"Эта птица пока не поёт И ещё не привыкла ко мне, Но упрям молчаливый полёт И глаза так знакомы в окне (Александр Рухлов «Птица»)",
"обратно поеду поездом. мне кажется, так честней. я в поезде встречусь с совестью и даже полажу с ней (Е.Жамбалова)",
"из тонкой прорези шестиугольной крыши. читает мальчик, и закат над нами, и мы молчим своими головами. мы наконец-то ничего не слышим (Е.Жамбалова)",
"Остаётся так мало… Небо смотрит в окно. Оно тоже устало, Ему тоже темно. (А.Кинаш)",
"И огибая прохожих, не оставляя тени, Вслух ничего особо не выражая, Жёлтые листья по жёлтому городу разлетелись На осколки разбитыми жёлтыми витражами.(А.Рухлов)"
]

@app.route('/', methods=['POST'])
@app.route('/alice/', methods=['POST'])
def respond():
    data = request.json
    command = data.get('request', {}).get('command', '')

    end_session = False

    shuffle_quotes = random.choice(quot_list)
    inp_text = f'Вы сказали {command}'

    if 'выход' in command:
        response_text = 'До свидания!'
        end_session = True
    elif command:
        response_text = inp_text + ' И вот вам цитата от современных классиков ' + shuffle_quotes
    else:
        response_text = 'Привет! Вы ничего не сказали.'

    response = {
        'response': {
            'text': response_text,
            'end_session ': end_session
        },
        'version': '1.0'
    }
    return response

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from url parameter
#     name = request.args.get("name", None)
#
#     # For debugging
#     print(f"got name {name}")
#
#     response = {}
#
#     # Check if user sent a name at all
#     if not name:
#         response["ERROR"] = "no name found, please send a name."
#     # Check if the user entered a number not a name
#     elif str(name).isdigit():
#         response["ERROR"] = "name can't be numeric."
#     # Now the user entered a valid name
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"
#
#     # Return the response in json format
#     return jsonify(response)
#
# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {name} to our awesome platform!!",
#             # Add this option to distinct the POST request
#             "METHOD" : "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "no name found, please send a name."
#         })
#
# # A welcome message to test our server
# @app.route('/')
# def index():
#     return "Welcome to our server !!"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)