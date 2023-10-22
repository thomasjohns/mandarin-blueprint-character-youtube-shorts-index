import json


with open('char_to_blueprint_shorts.json', 'r') as fp:
    char_to_blueprint_shorts = json.load(fp)


for char, shorts in char_to_blueprint_shorts.items():
    print(f'- {char}')
    for short in shorts:
        print(f'    - [{short["title"]}]({short["url"]})')
